from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# urlpatterns: lista che contiene tutti i pattern URL dell'app
# Django controlla questa lista dall'alto verso il basso per trovare la corrispondenza
urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    


    # ============================================
    # HELLO ENDPOINTS (TEST)
    # ============================================
    path('hello/', views.hello_world, name='hello'),
    path('helloPost/', views.hello_post, name='hello_post'),
    
    
    # ============================================
    # AZIENDE - CRUD
    # ============================================
    
    # Lista e creazione
    path('aziende/', views.lista_aziende, name='lista_aziende'),
    path('aziende/create/', views.crea_azienda, name='crea_azienda'),
    
    # ⚠️ IMPORTANTE: URL specifici PRIMA di quelli con parametri dinamici
    
    # Dettaglio, update, delete (con ID dinamico)
    path('aziende/<int:azienda_id>/', views.dettaglio_azienda, name='dettaglio_azienda'),
    path('aziende/<int:azienda_id>/update/', views.aggiorna_azienda, name='aggiorna_azienda'),
    path('aziende/<int:azienda_id>/patch/', views.aggiorna_parziale_azienda, name='aggiorna_parziale_azienda'),
    path('aziende/<int:azienda_id>/delete/', views.elimina_azienda, name='elimina_azienda'),
    
    # Relazioni e statistiche
    path('aziende/<int:azienda_id>/software/', views.software_per_azienda, name='software_per_azienda'),
    path('aziende/<int:azienda_id>/statistiche/', views.statistiche_azienda, name='statistiche_azienda'),
    
    
    # ============================================
    # SOFTWARE - CRUD
    # ============================================
    
    # Lista e creazione
    path('software/', views.lista_software, name='lista_software'),
    path('software/create/', views.crea_software, name='crea_software'),
    
    # ⚠️ FILTRI E RICERCHE - Devono stare PRIMA degli URL con <int:software_id>
    path('software/gratuiti/', views.software_gratuiti, name='software_gratuiti'),
    path('software/pagamento/', views.software_a_pagamento, name='software_a_pagamento'),
    path('software/cerca/', views.cerca_software, name='cerca_software'),
    path('software/filtra/', views.filtra_per_prezzo, name='filtra_per_prezzo'),
    
    # Dettaglio, update, delete (con ID dinamico)
    # ⚠️ Questi vanno DOPO i filtri sopra!
    path('software/<int:software_id>/', views.dettaglio_software, name='dettaglio_software'),
    path('software/<int:software_id>/update/', views.aggiorna_software, name='aggiorna_software'),
    path('software/<int:software_id>/patch/', views.aggiorna_parziale_software, name='aggiorna_parziale_software'),
    path('software/<int:software_id>/delete/', views.elimina_software, name='elimina_software'),
    
    
    # ============================================
    # STATISTICHE
    # ============================================
    path('statistiche/', views.statistiche_generali, name='statistiche_generali'),
]


# ============================================
# NOTE IMPORTANTI
# ============================================

# 1. ORDINE URL:
#    ✅ URL fissi PRIMA (es: 'software/gratuiti/')
#    ✅ URL dinamici DOPO (es: 'software/<int:id>/')
#    Motivo: Django si ferma al primo match

# 2. PARAMETRI DINAMICI:
#    <int:nome>    → cattura numero intero
#    <str:nome>    → cattura stringa
#    <slug:nome>   → cattura slug (lettere, numeri, -, _)
#    <path:nome>   → cattura tutto, anche con /

# 3. NAME:
#    Usato per reverse URL: reverse('lista_software') → '/api/software/'
#    Utile nei template e redirect

# 4. TRAILING SLASH:
#    Django preferisce URL con / finale
#    /api/software/ ✅ (con slash)
#    /api/software  → redirect automatico