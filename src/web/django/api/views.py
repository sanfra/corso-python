# --- IMPORTAZIONI DJANGO REST FRAMEWORK ---
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response

# --- IMPORTAZIONI DJANGO ORM ---
from django.db.models import Count, Avg, Sum, Q, Max, Min

# --- IMPORTAZIONI LOCALI ---
from .models import Software, Azienda
from .serializers import SoftwareSerializer, AziendaSerializer

# --- UTILITY ---
from datetime import datetime


# ============================================
# CUSTOM PERMISSION - STRICT
# ============================================

class StrictDjangoModelPermissions(DjangoModelPermissions):
    """
    Estende DjangoModelPermissions richiedendo permessi anche per le operazioni GET.
    
    Permessi richiesti:
    - GET: view_<model>
    - POST: add_<model>
    - PUT/PATCH: change_<model>
    - DELETE: delete_<model>
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],      # ✅ AGGIUNTO controllo per GET
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


# ============================================
# AZIENDE - VIEWSET CON PERMESSI STRICT
# ============================================

class AziendaViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo per Aziende con controllo permessi su TUTTE le operazioni.
    
    Permessi richiesti (gestiti dal pannello admin):
    - view_azienda: GET (lista e dettaglio) ✅
    - add_azienda: POST
    - change_azienda: PUT, PATCH
    - delete_azienda: DELETE
    """
    queryset = Azienda.objects.annotate(num_software=Count('software')).all()
    serializer_class = AziendaSerializer
    permission_classes = [StrictDjangoModelPermissions]  # ✅ CORRETTO
    
    def list(self, request):
        """GET /api/aziende/"""
        aziende = self.get_queryset()
        serializer = self.get_serializer(aziende, many=True)
        
        return Response({
            'count': aziende.count(),
            'aziende': serializer.data
        })
    
    def retrieve(self, request, pk=None):
        """GET /api/aziende/{id}/"""
        try:
            azienda = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(azienda)
            return Response(serializer.data)
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def create(self, request):
        """POST /api/aziende/"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """PUT /api/aziende/{id}/"""
        try:
            azienda = Azienda.objects.get(id=pk)
            serializer = self.get_serializer(azienda, data=request.data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request, pk=None):
        """PATCH /api/aziende/{id}/"""
        try:
            azienda = Azienda.objects.get(id=pk)
            serializer = self.get_serializer(azienda, data=request.data, partial=True)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, pk=None):
        """DELETE /api/aziende/{id}/"""
        try:
            azienda = Azienda.objects.get(id=pk)
            nome_azienda = azienda.nome
            num_software = azienda.software.count()
            
            azienda.delete()
            
            return Response({
                'messaggio': f'Azienda "{nome_azienda}" eliminata con successo',
                'software_eliminati': num_software
            })
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['get'], url_path='software')
    def software(self, request, pk=None):
        """GET /api/aziende/{id}/software/"""
        try:
            azienda = Azienda.objects.get(id=pk)
            software_list = azienda.software.all()
            
            serializer = SoftwareSerializer(software_list, many=True)
            
            return Response({
                'azienda': {
                    'id': azienda.id,
                    'nome': azienda.nome
                },
                'count': software_list.count(),
                'software': serializer.data
            })
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['get'], url_path='statistiche')
    def statistiche(self, request, pk=None):
        """GET /api/aziende/{id}/statistiche/"""
        try:
            azienda = Azienda.objects.get(id=pk)
            
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
            })
        except Azienda.DoesNotExist:
            return Response(
                {'errore': 'Azienda non trovata'},
                status=status.HTTP_404_NOT_FOUND
            )


# ============================================
# SOFTWARE - VIEWSET CON PERMESSI STRICT
# ============================================

class SoftwareViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo per Software con controllo permessi su TUTTE le operazioni.
    
    Permessi richiesti (gestiti dal pannello admin):
    - view_software: GET (lista e dettaglio) ✅
    - add_software: POST
    - change_software: PUT, PATCH
    - delete_software: DELETE
    """
    queryset = Software.objects.select_related('azienda').all()
    serializer_class = SoftwareSerializer
    permission_classes = [StrictDjangoModelPermissions]  # ✅ CORRETTO
    
    def list(self, request):
        """GET /api/software/"""
        software_list = self.get_queryset()
        serializer = self.get_serializer(software_list, many=True)
        
        return Response({
            'count': software_list.count(),
            'software': serializer.data
        })
    
    def retrieve(self, request, pk=None):
        """GET /api/software/{id}/"""
        try:
            software = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(software)
            return Response(serializer.data)
        except Software.DoesNotExist:
            return Response(
                {'errore': 'Software non trovato'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def create(self, request):
        """POST /api/software/"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """PUT /api/software/{id}/"""
        try:
            software = Software.objects.get(id=pk)
            serializer = self.get_serializer(software, data=request.data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Software.DoesNotExist:
            return Response(
                {'errore': 'Software non trovato'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request, pk=None):
        """PATCH /api/software/{id}/"""
        try:
            software = Software.objects.get(id=pk)
            serializer = self.get_serializer(software, data=request.data, partial=True)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Software.DoesNotExist:
            return Response(
                {'errore': 'Software non trovato'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, pk=None):
        """DELETE /api/software/{id}/"""
        try:
            software = Software.objects.get(id=pk)
            nome_software = software.nome
            
            software.delete()
            
            return Response({
                'messaggio': f'Software "{nome_software}" eliminato con successo'
            })
        except Software.DoesNotExist:
            return Response(
                {'errore': 'Software non trovato'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'], url_path='gratuiti')
    def gratuiti(self, request):
        """GET /api/software/gratuiti/"""
        software_list = self.get_queryset().filter(gratuito=True)
        serializer = self.get_serializer(software_list, many=True)
        
        return Response({
            'count': software_list.count(),
            'software': serializer.data
        })
    
    @action(detail=False, methods=['get'], url_path='pagamento')
    def pagamento(self, request):
        """GET /api/software/pagamento/"""
        software_list = self.get_queryset().filter(gratuito=False)
        serializer = self.get_serializer(software_list, many=True)
        
        return Response({
            'count': software_list.count(),
            'software': serializer.data
        })
    
    @action(detail=False, methods=['get'], url_path='cerca')
    def cerca(self, request):
        """GET /api/software/cerca/?q=photoshop"""
        query = request.query_params.get('q', '')
        
        if not query:
            return Response({
                'errore': 'Parametro "q" mancante'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        software_list = self.get_queryset().filter(
            Q(nome__icontains=query) | Q(azienda__nome__icontains=query)
        )
        
        serializer = self.get_serializer(software_list, many=True)
        
        return Response({
            'query': query,
            'count': software_list.count(),
            'risultati': serializer.data
        })
    
    @action(detail=False, methods=['get'], url_path='filtra')
    def filtra(self, request):
        """GET /api/software/filtra/?min=0&max=100"""
        prezzo_min = float(request.query_params.get('min', 0))
        prezzo_max = request.query_params.get('max')
        
        software_list = self.get_queryset().filter(prezzo__gte=prezzo_min)
        
        if prezzo_max:
            software_list = software_list.filter(prezzo__lte=float(prezzo_max))
        
        serializer = self.get_serializer(software_list, many=True)
        
        return Response({
            'filtro': {
                'prezzo_min': prezzo_min,
                'prezzo_max': prezzo_max if prezzo_max else 'illimitato'
            },
            'count': software_list.count(),
            'software': serializer.data
        })


# ============================================
# STATISTICHE (endpoint separato, richiede autenticazione)
# ============================================

@api_view(['GET'])
def statistiche_generali(request):
    """
    GET /api/statistiche/
    
    Restituisce statistiche generali (richiede solo autenticazione).
    """
    if not request.user.is_authenticated:
        return Response(
            {'errore': 'Autenticazione richiesta'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    num_aziende = Azienda.objects.count()
    
    stats_software = Software.objects.aggregate(
        totale=Count('id'),
        prezzo_medio=Avg('prezzo'),
        prezzo_max=Max('prezzo'),
        prezzo_min=Min('prezzo'),
        gratuiti=Count('id', filter=Q(gratuito=True)),
        a_pagamento=Count('id', filter=Q(gratuito=False))
    )
    
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
    })


# ============================================
# HELLO ENDPOINT (pubblico per test)
# ============================================

@api_view(['GET', 'POST'])
def hello_world(request):
    """Endpoint di test pubblico (senza autenticazione)"""
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
        'timestamp': datetime.now().isoformat(),
        'authenticated': request.user.is_authenticated,
        'user': str(request.user) if request.user.is_authenticated else 'Anonymous'
    }
    
    if request.method == 'POST':
        data['received_data'] = request.data
    
    return Response(data)