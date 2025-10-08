from django.db import models


class Software(models.Model):
    """
    Modello Software: rappresenta un software nel catalogo.
    
    Relazione: Ogni Software appartiene a una Azienda (Many-to-One)
    """
    
    # --- CAMPI TESTO ---
    nome = models.CharField(
        max_length=100,
        help_text="Nome del software"
    )
    
    versione = models.CharField(
        max_length=20,
        help_text="Versione del software (es: 1.0, 2.5.3)"
    )
    
    descrizione = models.TextField(
        blank=True,
        help_text="Descrizione del software (opzionale)"
    )
    
    # --- RELAZIONE CON AZIENDA (FOREIGN KEY - JOIN) ---
    # ⚠️ IMPORTANTE: usa solo 'Azienda' (non 'azienda.Azienda')
    # perché sono nello stesso app (api)
    azienda = models.ForeignKey(
        'Azienda',  # ✅ CORRETTO - stesso app
        on_delete=models.CASCADE,
        related_name='software',
        help_text="Azienda produttrice del software"
    )
    
    # --- CAMPI NUMERICI ---
    prezzo = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Prezzo in euro (es: 239.88)"
    )
    
    # --- CAMPI BOOLEANI ---
    gratuito = models.BooleanField(
        default=False,
        help_text="True se il software è gratuito"
    )
    
    attivo = models.BooleanField(
        default=True,
        help_text="True se il software è ancora disponibile"
    )
    
    # --- CAMPI DATA/ORA ---
    data_rilascio = models.DateField(
        help_text="Data di rilascio della versione"
    )
    
    creato_il = models.DateTimeField(
        auto_now_add=True,
        help_text="Data creazione record"
    )
    
    modificato_il = models.DateTimeField(
        auto_now=True,
        help_text="Data ultima modifica"
    )
    
    # --- METODI ---
    def __str__(self):
        return f"{self.nome} v{self.versione} - {self.azienda.nome}"
    
    def prezzo_formattato(self):
        if self.gratuito:
            return "Gratuito"
        return f"€{self.prezzo}"
    
    # --- META OPTIONS ---
    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Software"
        ordering = ['-data_rilascio']
        unique_together = [['nome', 'versione', 'azienda']]
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['azienda', 'data_rilascio']),
        ]