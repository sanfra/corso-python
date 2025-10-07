# Importazioni da Django REST Framework
from rest_framework.decorators import api_view  # Decorator per creare API views
from rest_framework.response import Response  # Classe per restituire risposte API
from rest_framework import status  # Contiene i codici di stato HTTP (200, 404, ecc.)
from rest_framework import serializers  # Per creare serializers
from datetime import datetime  # Per gestire date e orari

# Importiamo il modello Software
from .models import Software


# --- SERIALIZER PER SOFTWARE ---
# Un Serializer è come un "traduttore" tra oggetti Python e JSON
class SoftwareSerializer(serializers.ModelSerializer):
    """
    Serializer per il modello Software.
    Converte automaticamente gli oggetti Software in JSON e viceversa.
    
    ModelSerializer: crea automaticamente i campi basandosi sul modello.
    """
    
    class Meta:
        # model: specifica quale modello questo serializer rappresenta
        model = Software
        
        # fields: quali campi del modello includere nel JSON
        # '__all__': include TUTTI i campi del modello
        # Alternativa: fields = ['id', 'nome', 'versione'] per campi specifici
        fields = '__all__'


# --- VIEW ESISTENTI ---

@api_view(['GET'])  # Decorator: questa view accetta solo richieste GET
def hello_world(request):
    """
    Endpoint GET /api/hello/
    
    Restituisce un messaggio di benvenuto con informazioni sulla richiesta.
    
    @api_view(['GET']): limita questa view solo a richieste GET
    Se arriva un POST/PUT/DELETE, DRF restituisce automaticamente errore 405
    """
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,  # Tipo di richiesta HTTP (GET, POST, ecc.)
        'path': request.path,  # URL richiesto (es: /api/hello/)
    }
    # Response: oggetto DRF che gestisce automaticamente la serializzazione JSON
    # status.HTTP_200_OK: codice 200 (successo)
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])  # Questa view accetta solo richieste POST
def hello_post(request):
    """
    Endpoint POST /api/helloPost/
    
    Restituisce un messaggio con timestamp della richiesta.
    """
    data = {
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat(),  # Data/ora attuale in formato ISO
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)


# --- NUOVE VIEW PER SOFTWARE ---

@api_view(['GET'])  # Solo richieste GET
def lista_software(request):
    """
    Restituisce la lista di tutti i software.
    
    GET /api/software/
    
    Risposta JSON:
    [
        {"id": 1, "nome": "VS Code", "versione": "1.85", ...},
        {"id": 2, "nome": "PyCharm", "versione": "2024.1", ...}
    ]
    """
    # Software.objects.all(): recupera TUTTI i record dal database
    # Restituisce un QuerySet (lista di oggetti Software)
    software_list = Software.objects.all()
    
    # SoftwareSerializer(software_list, many=True):
    # - software_list: i dati da serializzare
    # - many=True: indica che stiamo serializzando MULTIPLI oggetti (una lista)
    #   Senza many=True, il serializer si aspetta un singolo oggetto
    serializer = SoftwareSerializer(software_list, many=True)
    
    # serializer.data: contiene i dati serializzati (dizionario Python)
    # Response li converte automaticamente in JSON
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def dettaglio_software(request, software_id):
    """
    Restituisce i dettagli di un singolo software.
    
    GET /api/software/<id>/
    
    Args:
        software_id (int): ID del software (catturato dall'URL)
    
    Risposta JSON:
    {"id": 1, "nome": "VS Code", "versione": "1.85", ...}
    
    Se non trovato: errore 404
    """
    try:
        # .get(id=software_id): cerca UN SOLO record con quell'ID
        # Se non esiste, solleva l'eccezione Software.DoesNotExist
        software = Software.objects.get(id=software_id)
        
        # Serializziamo il singolo oggetto (senza many=True)
        serializer = SoftwareSerializer(software)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Software.DoesNotExist:
        # Software non trovato: restituiamo errore 404
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])  # Solo richieste POST
def crea_software(request):
    """
    Crea un nuovo software nel database.
    
    POST /api/software/create/
    
    Body JSON richiesto:
    {
        "nome": "Photoshop",
        "versione": "25.0",
        "produttore": "Adobe",
        "prezzo": "239.88",
        "gratuito": false,
        "data_rilascio": "2024-10-01"
    }
    
    Risposta JSON (successo - 201):
    {"id": 3, "nome": "Photoshop", "versione": "25.0", ...}
    
    Risposta JSON (errore - 400):
    {"nome": ["Questo campo è obbligatorio."]}
    """
    # request.data: contiene i dati inviati nel body della richiesta POST
    # DRF li ha già parsati automaticamente (da JSON a dizionario Python)
    
    # SoftwareSerializer(data=request.data):
    # - data=request.data: passiamo i dati da validare e salvare
    # Questo crea un serializer in "modalità scrittura"
    serializer = SoftwareSerializer(data=request.data)
    
    # .is_valid(): valida i dati secondo le regole del modello
    # - Controlla che i campi obbligatori ci siano
    # - Verifica che i tipi di dato siano corretti
    # - Applica eventuali validatori custom
    # raise_exception=True: se non valido, solleva automaticamente
    # un'eccezione e restituisce errore 400 con i dettagli
    if serializer.is_valid(raise_exception=True):
        # .save(): salva l'oggetto nel database
        # Crea un nuovo record nella tabella software
        serializer.save()
        
        # status.HTTP_201_CREATED: codice 201 (risorsa creata con successo)
        # serializer.data: contiene i dati del software appena creato (con ID)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Nota: il codice sotto non viene mai raggiunto perché raise_exception=True
    # solleva un'eccezione se la validazione fallisce
    # Ma lo lasciamo per chiarezza didattica
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])  # Solo richieste PUT (aggiornamento completo)
def aggiorna_software(request, software_id):
    """
    Aggiorna un software esistente (tutti i campi).
    
    PUT /api/software/<id>/update/
    
    Body JSON richiesto (TUTTI i campi):
    {
        "nome": "VS Code",
        "versione": "1.86",
        "produttore": "Microsoft",
        "prezzo": "0.00",
        "gratuito": true,
        "data_rilascio": "2024-01-15"
    }
    
    Risposta: dati aggiornati del software
    """
    try:
        # Recuperiamo il software da aggiornare
        software = Software.objects.get(id=software_id)
        
        # SoftwareSerializer(software, data=request.data):
        # - software: l'oggetto esistente da aggiornare
        # - data=request.data: i nuovi dati
        # Questo crea un serializer in "modalità aggiornamento"
        serializer = SoftwareSerializer(software, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            # .save(): salva le modifiche nel database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['PATCH'])  # Solo richieste PATCH (aggiornamento parziale)
def aggiorna_parziale_software(request, software_id):
    """
    Aggiorna parzialmente un software (solo alcuni campi).
    
    PATCH /api/software/<id>/patch/
    
    Body JSON (solo i campi da modificare):
    {
        "versione": "1.87",
        "prezzo": "0.00"
    }
    
    Risposta: dati aggiornati del software
    """
    try:
        software = Software.objects.get(id=software_id)
        
        # partial=True: permette aggiornamenti parziali
        # Non è necessario inviare TUTTI i campi, solo quelli da modificare
        serializer = SoftwareSerializer(
            software, 
            data=request.data, 
            partial=True  # IMPORTANTE per PATCH
        )
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])  # Solo richieste DELETE
def elimina_software(request, software_id):
    """
    Elimina un software dal database.
    
    DELETE /api/software/<id>/delete/
    
    Risposta: messaggio di conferma
    """
    try:
        software = Software.objects.get(id=software_id)
        
        # Salviamo il nome prima di eliminarlo per il messaggio
        nome_software = software.nome
        
        # .delete(): elimina il record dal database
        # Questa operazione è IRREVERSIBILE!
        software.delete()
        
        # status.HTTP_200_OK: codice 200 con messaggio di conferma
        # Alternativamente si può usare status.HTTP_204_NO_CONTENT (senza messaggio)
        return Response(
            {'messaggio': f'Software "{nome_software}" eliminato con successo'}, 
            status=status.HTTP_200_OK
        )
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def software_gratuiti(request):
    """
    Restituisce solo i software gratuiti.
    
    GET /api/software/gratuiti/
    
    Esempio di query filtering con Django ORM.
    """
    # .filter(gratuito=True): restituisce solo i record dove gratuito=True
    # È l'equivalente SQL di: SELECT * FROM software WHERE gratuito = TRUE
    software_list = Software.objects.filter(gratuito=True)
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'count': len(serializer.data),  # Numero di software gratuiti
        'software': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def software_per_produttore(request, produttore):
    """
    Restituisce i software di un produttore specifico.
    
    GET /api/software/produttore/<nome>/
    
    Args:
        produttore (str): Nome del produttore (catturato dall'URL)
    
    Esempio di query filtering con parametri URL.
    """
    # .filter(produttore__iexact=produttore):
    # - produttore__iexact: confronto case-insensitive (Adobe = adobe = ADOBE)
    # - __iexact è un "field lookup" di Django ORM
    # Altri esempi: __contains, __startswith, __gt (greater than), ecc.
    software_list = Software.objects.filter(produttore__iexact=produttore)
    
    if not software_list.exists():
        # .exists(): controlla se il QuerySet ha almeno un elemento
        # È più efficiente di len(software_list) > 0
        return Response(
            {'messaggio': f'Nessun software trovato per il produttore "{produttore}"'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'produttore': produttore,
        'count': software_list.count(),  # Numero di software trovati
        'software': serializer.data
    }, status=status.HTTP_200_OK)