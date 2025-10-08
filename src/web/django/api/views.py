# --- IMPORTAZIONI ---
from rest_framework.decorators import api_view  # Trasforma funzioni in API endpoints
from rest_framework.response import Response    # Risposta API (auto-converte in JSON)
from rest_framework import status              # Codici HTTP (200, 404, 201, ecc.)
from rest_framework import serializers         # Per convertire Model ↔ JSON
from datetime import datetime

from .models.software import Software  # Modello database


# --- SERIALIZER ---
# Serializer = "Traduttore" bidirezionale tra Python objects ↔ JSON
class SoftwareSerializer(serializers.ModelSerializer):
    """
    Converte automaticamente oggetti Software in JSON e viceversa.
    
    ModelSerializer: genera automaticamente i campi dal modello,
    risparmiando codice ripetitivo.
    """
    
    class Meta:
        model = Software  # Modello da serializzare
        fields = '__all__'  # Includi tutti i campi
        # Alternative:
        # fields = ['id', 'nome', 'versione']  # Solo campi specifici
        # exclude = ['data_creazione']          # Tutti tranne questi


# --- ENDPOINTS DI TEST ---

@api_view(['GET'])  # ⚠️ IMPORTANTE: limita ai metodi HTTP specificati
def hello_world(request):
    """GET /api/hello/ - Endpoint di test"""
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,  # 'GET', 'POST', ecc.
        'path': request.path,      # '/api/hello/'
    }
    # Response converte automaticamente dict → JSON
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def hello_post(request):
    """POST /api/helloPost/ - Test endpoint POST"""
    data = {
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat(),  # '2024-10-08T14:30:00'
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)


# --- CRUD: READ (GET) ---

@api_view(['GET'])
def lista_software(request):
    """
    GET /api/software/
    Restituisce TUTTI i software nel database.
    
    Risposta: [{"id": 1, "nome": "VS Code", ...}, {...}]
    """
    # ORM query: SELECT * FROM software
    software_list = Software.objects.all()
    
    # ⚠️ many=True: obbligatorio quando serializzi LISTE/QuerySet
    # Senza many=True → errore!
    serializer = SoftwareSerializer(software_list, many=True)
    
    # serializer.data = dizionario Python, Response → JSON automaticamente
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def dettaglio_software(request, software_id):
    """
    GET /api/software/5/
    Restituisce UN SOLO software.
    
    Args:
        software_id: catturato da <int:software_id> nell'URL
    """
    try:
        # .get(): restituisce 1 oggetto o solleva DoesNotExist
        # SELECT * FROM software WHERE id = software_id LIMIT 1
        software = Software.objects.get(id=software_id)
        
        # ⚠️ NO many=True per singoli oggetti
        serializer = SoftwareSerializer(software)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Software.DoesNotExist:
        # ⚠️ Gestisci sempre DoesNotExist per evitare crash
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


# --- CRUD: CREATE (POST) ---

@api_view(['POST'])
def crea_software(request):
    """
    POST /api/software/create/
    Crea nuovo software nel database.
    
    Body JSON richiesto:
    {
        "nome": "Photoshop",
        "versione": "25.0",
        "produttore": "Adobe",
        "prezzo": "239.88",
        "gratuito": false,
        "data_rilascio": "2024-10-01"
    }
    
    Risposta 201: {"id": 3, "nome": "Photoshop", ...}
    Risposta 400: {"nome": ["Questo campo è obbligatorio"]}
    """
    # ⚠️ request.data (DRF) ≠ request.body (Django puro)
    # request.data è già parsato (JSON → dict Python)
    
    # data=request.data: modalità "scrittura" del serializer
    serializer = SoftwareSerializer(data=request.data)
    
    # .is_valid(): valida secondo le regole del modello
    # - Campi obbligatori presenti?
    # - Tipi corretti? (int, str, bool, date)
    # - Validatori custom soddisfatti?
    # raise_exception=True: se fallisce → 400 automatico con errori
    if serializer.is_valid(raise_exception=True):
        # .save(): INSERT INTO software (...) VALUES (...)
        serializer.save()
        
        # ⚠️ 201 CREATED (non 200) per nuove risorse
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # ⚠️ Questo codice non viene mai eseguito (raise_exception=True)
    # Lo lasciamo solo per chiarezza didattica
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- CRUD: UPDATE (PUT) ---

@api_view(['PUT'])
def aggiorna_software(request, software_id):
    """
    PUT /api/software/5/update/
    Aggiornamento COMPLETO: richiede TUTTI i campi.
    
    ⚠️ PUT vs PATCH:
    - PUT: sostituisce completamente (tutti i campi obbligatori)
    - PATCH: modifica parziale (solo campi specificati)
    
    Body JSON: TUTTI i campi richiesti!
    {
        "nome": "VS Code",
        "versione": "1.86",
        "produttore": "Microsoft",
        "prezzo": "0.00",
        "gratuito": true,
        "data_rilascio": "2024-01-15"
    }
    """
    try:
        software = Software.objects.get(id=software_id)
        
        # SoftwareSerializer(istanza, data=nuovi_dati):
        # - 1° param: oggetto da aggiornare
        # - data=: nuovi valori
        # ⚠️ Senza partial=True → tutti i campi obbligatori!
        serializer = SoftwareSerializer(software, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            # UPDATE software SET ... WHERE id = software_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


# --- CRUD: UPDATE (PATCH) ---

@api_view(['PATCH'])
def aggiorna_parziale_software(request, software_id):
    """
    PATCH /api/software/5/patch/
    Aggiornamento PARZIALE: solo campi specificati.
    
    Body JSON: solo campi da modificare
    {
        "versione": "1.87"
    }
    
    ⚠️ partial=True è CRITICO per PATCH!
    Senza di esso → errore se mancano campi obbligatori
    """
    try:
        software = Software.objects.get(id=software_id)
        
        # ⚠️ partial=True: permette aggiornamenti parziali
        # Campi non specificati nel body → rimangono invariati
        serializer = SoftwareSerializer(
            software, 
            data=request.data, 
            partial=True  # 🔑 CHIAVE per PATCH!
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


# --- CRUD: DELETE ---

@api_view(['DELETE'])
def elimina_software(request, software_id):
    """
    DELETE /api/software/5/delete/
    Elimina software dal database.
    
    ⚠️ ATTENZIONE: operazione IRREVERSIBILE!
    
    Risposta tipica:
    - 200 OK con messaggio di conferma
    - 204 NO CONTENT (nessun body, solo status code)
    """
    try:
        software = Software.objects.get(id=software_id)
        
        nome_software = software.nome  # Salva prima di eliminare
        
        # ⚠️ .delete(): IRREVERSIBILE!
        # DELETE FROM software WHERE id = software_id
        software.delete()
        
        # Alternative:
        # return Response(status=status.HTTP_204_NO_CONTENT)  # Nessun body
        return Response(
            {'messaggio': f'Software "{nome_software}" eliminato con successo'}, 
            status=status.HTTP_200_OK
        )
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'}, 
            status=status.HTTP_404_NOT_FOUND
        )


# --- QUERY AVANZATE: FILTRI ---

@api_view(['GET'])
def software_gratuiti(request):
    """
    GET /api/software/gratuiti/
    Restituisce solo software gratuiti.
    
    Esempio di filtering con Django ORM.
    """
    # .filter(): filtra risultati (può restituire 0+ oggetti)
    # SQL: SELECT * FROM software WHERE gratuito = TRUE
    software_list = Software.objects.filter(gratuito=True)
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    # Risposta con metadati aggiuntivi
    return Response({
        'count': len(serializer.data),  # Numero risultati
        'software': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def software_per_produttore(request, produttore):
    """
    GET /api/software/produttore/Adobe/
    Filtra per produttore (case-insensitive).
    
    Args:
        produttore: catturato da <str:produttore> nell'URL
    
    ⚠️ Field Lookups: produttore__iexact
    Django ORM usa __ (doppio underscore) per lookup avanzati:
    - __iexact: uguale (case-insensitive) → Adobe = adobe = ADOBE
    - __contains: contiene → "Microsoft" contiene "soft"
    - __startswith: inizia con
    - __endswith: finisce con
    - __gt / __gte: maggiore / maggiore-uguale
    - __lt / __lte: minore / minore-uguale
    - __in: in lista → produttore__in=['Adobe', 'Microsoft']
    """
    # SQL: SELECT * FROM software WHERE LOWER(produttore) = LOWER('Adobe')
    software_list = Software.objects.filter(produttore__iexact=produttore)
    
    # ⚠️ .exists(): più efficiente di len() o .count() per check booleani
    # Ferma la query appena trova 1 match
    if not software_list.exists():
        return Response(
            {'messaggio': f'Nessun software trovato per il produttore "{produttore}"'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'produttore': produttore,
        'count': software_list.count(),  # Conta risultati (query COUNT(*))
        'software': serializer.data
    }, status=status.HTTP_200_OK)


# --- NOTE FINALI ---

# 1. SERIALIZER:
#    - Lettura: SoftwareSerializer(oggetto/queryset, many=True/False)
#    - Scrittura: SoftwareSerializer(data=request.data, partial=True/False)
#    - Update: SoftwareSerializer(oggetto, data=request.data, partial=True/False)

# 2. STATUS CODES:
#    - 200 OK: successo generico (GET, PUT, PATCH, DELETE)
#    - 201 CREATED: risorsa creata (POST)
#    - 204 NO CONTENT: successo senza body (DELETE alternativo)
#    - 400 BAD REQUEST: validazione fallita
#    - 404 NOT FOUND: risorsa non trovata
#    - 405 METHOD NOT ALLOWED: metodo HTTP non permesso (@api_view)

# 3. DJANGO ORM:
#    - .all(): tutti i record
#    - .get(): 1 record (solleva DoesNotExist se non trovato)
#    - .filter(): 0+ record (mai solleva eccezioni)
#    - .exists(): controlla esistenza (più veloce di count() > 0)
#    - .count(): numero di record (query COUNT(*))

# 4. REQUEST.DATA vs REQUEST.BODY:
#    - request.data: DRF, già parsato (dict Python) ✅
#    - request.body: Django puro, bytes raw (serve json.loads()) ❌

# 5. PARTIAL=TRUE:
#    - PUT: partial=False (default) → tutti i campi obbligatori
#    - PATCH: partial=True → solo campi specificati