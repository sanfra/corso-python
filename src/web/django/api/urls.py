from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views


# ============================================
# ROUTER per ViewSet
# ============================================

# Il router genera automaticamente gli URL per i ViewSet
router = DefaultRouter()

# Registra i ViewSet
# - basename: nome base per gli URL (usato per reverse())
# - ViewSet gestisce automaticamente: list, create, retrieve, update, partial_update, destroy
router.register(r'aziende', views.AziendaViewSet, basename='azienda')
router.register(r'software', views.SoftwareViewSet, basename='software')


# ============================================
# URL PATTERNS
# ============================================

urlpatterns = [
    # ============================================
    # JWT AUTHENTICATION
    # ============================================
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    # ============================================
    # HELLO ENDPOINT (TEST)
    # ============================================
    path('hello/', views.hello_world, name='hello'),
    
    
    # ============================================
    # STATISTICHE (endpoint separato)
    # ============================================
    path('statistiche/', views.statistiche_generali, name='statistiche_generali'),
    
    
    # ============================================
    # INCLUDE ROUTER URLs
    # ============================================
    # Questo include tutti gli URL generati automaticamente dal router
    path('', include(router.urls)),
]


# ============================================
# URL GENERATI AUTOMATICAMENTE DAL ROUTER
# ============================================

# AZIENDE:
# GET    /aziende/                    → list (lista tutte le aziende)
# POST   /aziende/                    → create (crea nuova azienda)
# GET    /aziende/{id}/               → retrieve (dettaglio azienda)
# PUT    /aziende/{id}/               → update (aggiorna azienda completa)
# PATCH  /aziende/{id}/               → partial_update (aggiorna parziale)
# DELETE /aziende/{id}/               → destroy (elimina azienda)
# GET    /aziende/{id}/software/      → custom action (software dell'azienda)
# GET    /aziende/{id}/statistiche/   → custom action (statistiche azienda)

# SOFTWARE:
# GET    /software/                   → list (lista tutti i software)
# POST   /software/                   → create (crea nuovo software)
# GET    /software/{id}/              → retrieve (dettaglio software)
# PUT    /software/{id}/              → update (aggiorna software completo)
# PATCH  /software/{id}/              → partial_update (aggiorna parziale)
# DELETE /software/{id}/              → destroy (elimina software)
# GET    /software/gratuiti/          → custom action (software gratuiti)
# GET    /software/pagamento/         → custom action (software a pagamento)
# GET    /software/cerca/?q=query     → custom action (cerca software)
# GET    /software/filtra/?min=&max=  → custom action (filtra per prezzo)


# ============================================
# VANTAGGI DEL ROUTER
# ============================================

# 1. AUTOMATICO: Genera tutti gli URL CRUD standard
# 2. CONSISTENTE: Struttura URL uniforme per tutti i ViewSet
# 3. MENO CODICE: Non serve scrivere manualmente ogni path()
# 4. CUSTOM ACTIONS: @action() crea automaticamente URL custom
# 5. BROWSABLE API: Supporto completo per la UI di DRF


# ============================================
# REVERSE URL (come usarli nel codice)
# ============================================

# Da codice Python:
# reverse('azienda-list')              → /aziende/
# reverse('azienda-detail', args=[1])  → /aziende/1/
# reverse('azienda-software', args=[1]) → /aziende/1/software/
# reverse('software-list')             → /software/
# reverse('software-gratuiti')         → /software/gratuiti/