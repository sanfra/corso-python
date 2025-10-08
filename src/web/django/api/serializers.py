from rest_framework import serializers
from .models import Software, Azienda



# ============================================
# SERIALIZER AZIENDA
# ============================================

class AziendaSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Azienda.
    
    Converte automaticamente oggetti Azienda in JSON e viceversa.
    Include campo calcolato per numero di software.
    """
    
    # Campo read-only calcolato (non nel database)
    num_software = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Azienda
        fields = [
            'id',
            'nome',
            'partita_iva',
            'sede',
            'email',
            'telefono',
            'sito_web',
            'descrizione',
            'data_fondazione',
            'creata_il',
            'modificata_il',
            'num_software'  # Campo calcolato
        ]
        
        # Campi read-only (non modificabili via API)
        read_only_fields = ['id', 'creata_il', 'modificata_il']


class AziendaMinimalSerializer(serializers.ModelSerializer):
    """
    Versione minimal di AziendaSerializer.
    Usata quando serve solo info base (es: nested in Software).
    """
    
    class Meta:
        model = Azienda
        fields = ['id', 'nome', 'sede', 'email']


# ============================================
# SERIALIZER SOFTWARE
# ============================================

class SoftwareSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Software.
    
    Include informazioni complete dell'azienda produttrice (nested).
    """
    
    # ✅ Nested serializer: include dati completi azienda
    # read_only=True: solo in lettura (per GET)
    azienda_dettagli = AziendaMinimalSerializer(source='azienda', read_only=True)
    
    # Campo per scrittura (POST/PUT/PATCH): accetta solo ID azienda
    azienda = serializers.PrimaryKeyRelatedField(
        queryset=Azienda.objects.all(),
        write_only=True
    )
    
    # Campo calcolato: prezzo formattato
    prezzo_formattato = serializers.SerializerMethodField()
    
    class Meta:
        model = Software
        fields = [
            'id',
            'nome',
            'versione',
            'descrizione',
            'azienda',            # Per scrittura (ID)
            'azienda_dettagli',   # Per lettura (oggetto completo)
            'prezzo',
            'prezzo_formattato',  # Campo calcolato
            'gratuito',
            'attivo',
            'data_rilascio',
            'creato_il',
            'modificato_il'
        ]
        
        read_only_fields = ['id', 'creato_il', 'modificato_il']
    
    def get_prezzo_formattato(self, obj):
        """
        Metodo per campo calcolato prezzo_formattato.
        
        Args:
            obj: istanza Software
        
        Returns:
            str: prezzo formattato (es: "€239.88" o "Gratuito")
        """
        if obj.gratuito:
            return "Gratuito"
        return f"€{obj.prezzo}"


class SoftwareMinimalSerializer(serializers.ModelSerializer):
    """
    Versione minimal di SoftwareSerializer.
    Usata per liste o quando servono pochi dati.
    """
    
    # Solo nome azienda (non oggetto completo)
    azienda_nome = serializers.CharField(source='azienda.nome', read_only=True)
    
    class Meta:
        model = Software
        fields = ['id', 'nome', 'versione', 'azienda_nome', 'prezzo', 'gratuito']


# ============================================
# SERIALIZER ALTERNATIVO: Software semplice
# ============================================

class SoftwareSimpleSerializer(serializers.ModelSerializer):
    """
    Versione semplice senza nested serializer.
    Restituisce solo ID azienda + nome separato.
    """
    
    azienda_nome = serializers.CharField(source='azienda.nome', read_only=True)
    
    class Meta:
        model = Software
        fields = '__all__'
        read_only_fields = ['id', 'creato_il', 'modificato_il']


# ============================================
# SERIALIZER CON VALIDAZIONI CUSTOM
# ============================================

class SoftwareConValidazioneSerializer(serializers.ModelSerializer):
    """
    Serializer con validazioni custom aggiuntive.
    """
    
    azienda_dettagli = AziendaMinimalSerializer(source='azienda', read_only=True)
    azienda = serializers.PrimaryKeyRelatedField(
        queryset=Azienda.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Software
        fields = '__all__'
        read_only_fields = ['id', 'creato_il', 'modificato_il']
    
    def validate_prezzo(self, value):
        """
        Validazione custom per campo prezzo.
        
        Args:
            value: valore da validare
        
        Returns:
            value validato
        
        Raises:
            ValidationError se prezzo negativo
        """
        if value < 0:
            raise serializers.ValidationError(
                "Il prezzo non può essere negativo"
            )
        return value
    
    def validate(self, data):
        """
        Validazione a livello oggetto (più campi insieme).
        
        Args:
            data: dizionario con tutti i dati
        
        Returns:
            data validati
        
        Raises:
            ValidationError se validazione fallisce
        """
        # Se gratuito, prezzo deve essere 0
        if data.get('gratuito') and data.get('prezzo', 0) > 0:
            raise serializers.ValidationError(
                "Un software gratuito deve avere prezzo = 0"
            )
        
        # Se non gratuito, prezzo deve essere > 0
        if not data.get('gratuito') and data.get('prezzo', 0) == 0:
            raise serializers.ValidationError(
                "Un software a pagamento deve avere prezzo > 0"
            )
        
        return data


# ============================================
# SERIALIZER PER STATISTICHE
# ============================================

class StatisticheSerializer(serializers.Serializer):
    """
    Serializer per dati statistici (non collegato a un modello).
    """
    
    totale = serializers.IntegerField()
    gratuiti = serializers.IntegerField()
    a_pagamento = serializers.IntegerField()
    prezzo_medio = serializers.FloatField()
    prezzo_max = serializers.FloatField()
    prezzo_min = serializers.FloatField()


# ============================================
# NOTE IMPORTANTI
# ============================================

# 1. ModelSerializer vs Serializer:
#    - ModelSerializer: basato su un modello Django (genera campi auto)
#    - Serializer: generico, per dati non collegati a modelli

# 2. read_only=True:
#    Campo visibile in GET, ma non richiesto/accettato in POST/PUT/PATCH

# 3. write_only=True:
#    Campo accettato in POST/PUT/PATCH, ma non visibile in GET

# 4. source='campo':
#    Specifica da quale campo del modello prendere il valore
#    source='azienda.nome' → attraversa la ForeignKey

# 5. SerializerMethodField():
#    Campo calcolato con metodo custom get_<nome_campo>()

# 6. PrimaryKeyRelatedField:
#    Per ForeignKey: accetta/restituisce solo l'ID (non oggetto completo)
#    queryset= specifica oggetti validi
#    write_only=True → solo per scrittura

# 7. Nested Serializers:
#    Includere un serializer dentro un altro per oggetti completi
#    Utile per GET, ma complesso per POST (meglio usare ID)