# --- IMPORTAZIONI DJANGO REST FRAMEWORK ---
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- IMPORTAZIONI DJANGO ORM ---
from django.db.models import Count, Avg, Sum, Q
from django.shortcuts import get_object_or_404

# --- IMPORTAZIONI LOCALI ---
from .models import Software, Azienda
from .serializers import SoftwareSerializer, AziendaSerializer

# --- UTILITY ---
from datetime import datetime


# ============================================
# AZIENDE - CRUD COMPLETO
# ============================================

@api_view(['GET'])
def lista_aziende(request):
    """
    GET /api/aziende/
    
    Restituisce tutte le aziende con numero di software prodotti.
    """
    # Query con annotazione (conta software per azienda)
    aziende = Azienda.objects.annotate(
        num_software=Count('software')
    ).all()
    
    serializer = AziendaSerializer(aziende, many=True)
    
    return Response({
        'count': aziende.count(),
        'aziende': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def dettaglio_azienda(request, azienda_id):
    """
    GET /api/aziende/<id>/
    
    Restituisce dettagli di una singola azienda.
    """
    try:
        azienda = Azienda.objects.annotate(
            num_software=Count('software')
        ).get(id=azienda_id)
        
        serializer = AziendaSerializer(azienda)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
def crea_azienda(request):
    """
    POST /api/aziende/create/
    
    Crea una nuova azienda.
    
    Body JSON richiesto:
    {
        "nome": "Adobe Inc.",
        "partita_iva": "12345678901",
        "sede": "San Jose, California",
        "email": "info@adobe.com",
        "telefono": "+1-408-536-6000",
        "sito_web": "https://www.adobe.com",
        "descrizione": "Leader software creativo",
        "data_fondazione": "1982-12-01"
    }
    """
    serializer = AziendaSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def aggiorna_azienda(request, azienda_id):
    """
    PUT /api/aziende/<id>/update/
    
    Aggiorna completamente un'azienda (tutti i campi richiesti).
    """
    try:
        azienda = Azienda.objects.get(id=azienda_id)
        serializer = AziendaSerializer(azienda, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['PATCH'])
def aggiorna_parziale_azienda(request, azienda_id):
    """
    PATCH /api/aziende/<id>/patch/
    
    Aggiorna parzialmente un'azienda (solo campi specificati).
    
    Body JSON (esempio - solo campi da modificare):
    {
        "email": "nuovo@email.com",
        "telefono": "+39 06 1234567"
    }
    """
    try:
        azienda = Azienda.objects.get(id=azienda_id)
        serializer = AziendaSerializer(azienda, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
def elimina_azienda(request, azienda_id):
    """
    DELETE /api/aziende/<id>/delete/
    
    Elimina un'azienda e TUTTI i suoi software (CASCADE).
    """
    try:
        azienda = Azienda.objects.get(id=azienda_id)
        nome_azienda = azienda.nome
        num_software = azienda.software.count()
        
        # Elimina (CASCADE elimina anche i software)
        azienda.delete()
        
        return Response({
            'messaggio': f'Azienda "{nome_azienda}" eliminata con successo',
            'software_eliminati': num_software
        }, status=status.HTTP_200_OK)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def software_per_azienda(request, azienda_id):
    """
    GET /api/aziende/<id>/software/
    
    Restituisce tutti i software di una specifica azienda.
    """
    try:
        azienda = Azienda.objects.get(id=azienda_id)
        
        # ✅ Relazione inversa con related_name='software'
        software_list = azienda.software.all()
        
        serializer = SoftwareSerializer(software_list, many=True)
        
        return Response({
            'azienda': {
                'id': azienda.id,
                'nome': azienda.nome
            },
            'count': software_list.count(),
            'software': serializer.data
        }, status=status.HTTP_200_OK)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


# ============================================
# SOFTWARE - CRUD COMPLETO
# ============================================

@api_view(['GET'])
def lista_software(request):
    """
    GET /api/software/
    
    Restituisce tutti i software con informazioni azienda.
    
    ✅ Ottimizzato con select_related per JOIN efficiente.
    """
    # ✅ select_related('azienda') fa JOIN in una sola query
    software_list = Software.objects.select_related('azienda').all()
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'count': software_list.count(),
        'software': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def dettaglio_software(request, software_id):
    """
    GET /api/software/<id>/
    
    Restituisce dettagli di un singolo software con info azienda.
    """
    try:
        # ✅ select_related per includere dati azienda
        software = Software.objects.select_related('azienda').get(id=software_id)
        
        serializer = SoftwareSerializer(software)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
def crea_software(request):
    """
    POST /api/software/create/
    
    Crea un nuovo software.
    
    Body JSON richiesto:
    {
        "nome": "Photoshop",
        "versione": "25.0",
        "azienda": 1,  ← ID dell'azienda (obbligatorio)
        "prezzo": "239.88",
        "gratuito": false,
        "data_rilascio": "2024-10-01",
        "descrizione": "Software per editing foto"
    }
    """
    serializer = SoftwareSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def aggiorna_software(request, software_id):
    """
    PUT /api/software/<id>/update/
    
    Aggiorna completamente un software (tutti i campi).
    """
    try:
        software = Software.objects.get(id=software_id)
        serializer = SoftwareSerializer(software, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['PATCH'])
def aggiorna_parziale_software(request, software_id):
    """
    PATCH /api/software/<id>/patch/
    
    Aggiorna parzialmente un software (solo campi specificati).
    
    Body JSON (esempio):
    {
        "versione": "25.1",
        "prezzo": "199.99"
    }
    """
    try:
        software = Software.objects.get(id=software_id)
        serializer = SoftwareSerializer(software, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
def elimina_software(request, software_id):
    """
    DELETE /api/software/<id>/delete/
    
    Elimina un software dal database.
    """
    try:
        software = Software.objects.get(id=software_id)
        nome_software = software.nome
        
        software.delete()
        
        return Response({
            'messaggio': f'Software "{nome_software}" eliminato con successo'
        }, status=status.HTTP_200_OK)
    
    except Software.DoesNotExist:
        return Response(
            {'errore': 'Software non trovato'},
            status=status.HTTP_404_NOT_FOUND
        )


# ============================================
# FILTRI E RICERCHE
# ============================================

@api_view(['GET'])
def software_gratuiti(request):
    """
    GET /api/software/gratuiti/
    
    Restituisce solo i software gratuiti.
    """
    # ✅ select_related per JOIN ottimizzata
    software_list = Software.objects.select_related('azienda').filter(gratuito=True)
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'count': software_list.count(),
        'software': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def software_a_pagamento(request):
    """
    GET /api/software/pagamento/
    
    Restituisce solo i software a pagamento.
    """
    software_list = Software.objects.select_related('azienda').filter(gratuito=False)
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'count': software_list.count(),
        'software': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def cerca_software(request):
    """
    GET /api/software/cerca/?q=photoshop
    
    Cerca software per nome o nome azienda.
    
    Query params:
    - q: termine di ricerca
    """
    query = request.query_params.get('q', '')
    
    if not query:
        return Response({
            'errore': 'Parametro "q" mancante'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # ✅ Cerca in nome software O nome azienda (con JOIN)
    # Q() permette query OR complesse
    software_list = Software.objects.select_related('azienda').filter(
        Q(nome__icontains=query) | Q(azienda__nome__icontains=query)
    )
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'query': query,
        'count': software_list.count(),
        'risultati': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def filtra_per_prezzo(request):
    """
    GET /api/software/filtra/?min=0&max=100
    
    Filtra software per range di prezzo.
    
    Query params:
    - min: prezzo minimo (default: 0)
    - max: prezzo massimo (opzionale)
    """
    prezzo_min = float(request.query_params.get('min', 0))
    prezzo_max = request.query_params.get('max')
    
    software_list = Software.objects.select_related('azienda').filter(
        prezzo__gte=prezzo_min
    )
    
    if prezzo_max:
        software_list = software_list.filter(prezzo__lte=float(prezzo_max))
    
    serializer = SoftwareSerializer(software_list, many=True)
    
    return Response({
        'filtro': {
            'prezzo_min': prezzo_min,
            'prezzo_max': prezzo_max if prezzo_max else 'illimitato'
        },
        'count': software_list.count(),
        'software': serializer.data
    }, status=status.HTTP_200_OK)


# ============================================
# STATISTICHE E AGGREGAZIONI
# ============================================

@api_view(['GET'])
def statistiche_generali(request):
    """
    GET /api/statistiche/
    
    Restituisce statistiche generali su software e aziende.
    """
    from django.db.models import Avg, Max, Min
    
    # Statistiche aziende
    num_aziende = Azienda.objects.count()
    
    # Statistiche software
    stats_software = Software.objects.aggregate(
        totale=Count('id'),
        prezzo_medio=Avg('prezzo'),
        prezzo_max=Max('prezzo'),
        prezzo_min=Min('prezzo'),
        gratuiti=Count('id', filter=Q(gratuito=True)),
        a_pagamento=Count('id', filter=Q(gratuito=False))
    )
    
    # Azienda con più software
    azienda_top = Azienda.objects.annotate(
        num_software=Count('software')
    ).order_by('-num_software').first()
    
    return Response({
        'aziende': {
            'totale': num_aziende
        },
        'software': {
            'totale': stats_software['totale'],
            'gratuiti': stats_software['gratuiti'],
            'a_pagamento': stats_software['a_pagamento'],
            'prezzo_medio': float(stats_software['prezzo_medio'] or 0),
            'prezzo_max': float(stats_software['prezzo_max'] or 0),
            'prezzo_min': float(stats_software['prezzo_min'] or 0)
        },
        'top_azienda': {
            'nome': azienda_top.nome if azienda_top else None,
            'num_software': azienda_top.num_software if azienda_top else 0
        }
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def statistiche_azienda(request, azienda_id):
    """
    GET /api/aziende/<id>/statistiche/
    
    Statistiche dettagliate per una specifica azienda.
    """
    try:
        azienda = Azienda.objects.get(id=azienda_id)
        
        # Statistiche software dell'azienda
        stats = azienda.software.aggregate(
            totale=Count('id'),
            gratuiti=Count('id', filter=Q(gratuito=True)),
            a_pagamento=Count('id', filter=Q(gratuito=False)),
            prezzo_medio=Avg('prezzo'),
            prezzo_totale=Sum('prezzo')
        )
        
        return Response({
            'azienda': {
                'id': azienda.id,
                'nome': azienda.nome
            },
            'software': {
                'totale': stats['totale'],
                'gratuiti': stats['gratuiti'],
                'a_pagamento': stats['a_pagamento'],
                'prezzo_medio': float(stats['prezzo_medio'] or 0),
                'valore_catalogo': float(stats['prezzo_totale'] or 0)
            }
        }, status=status.HTTP_200_OK)
    
    except Azienda.DoesNotExist:
        return Response(
            {'errore': 'Azienda non trovata'},
            status=status.HTTP_404_NOT_FOUND
        )


# ============================================
# HELLO ENDPOINTS (TEST)
# ============================================

@api_view(['GET'])
def hello_world(request):
    """GET /api/hello/ - Endpoint di test"""
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
        'timestamp': datetime.now().isoformat()
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def hello_post(request):
    """POST /api/helloPost/ - Endpoint di test POST"""
    data = {
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)