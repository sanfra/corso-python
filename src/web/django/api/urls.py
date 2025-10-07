from django.urls import path  # Funzione per definire pattern URL
from . import views  # Importiamo le view dallo stesso package

# urlpatterns: lista che contiene tutti i pattern URL dell'app
# Django controlla questa lista dall'alto verso il basso per trovare la corrispondenza
urlpatterns = [
    # --- ENDPOINT ESISTENTI ---
    
    # path(): definisce un pattern URL
    # 'hello/': l'URL relativo (sarà /api/hello/ nel browser)
    # views.hello_world: la funzione view da chiamare quando l'URL corrisponde
    # name='hello': nome simbolico per riferirsi a questo URL nel codice
    path('hello/', views.hello_world, name='hello'),
    
    # POST /api/helloPost/
    path('helloPost/', views.hello_post, name='hello_post'),
    
    
    # --- CRUD COMPLETO PER SOFTWARE ---
    # C = Create, R = Read, U = Update, D = Delete
    
    # READ: lista tutti i software
    # GET /api/software/
    path('software/', views.lista_software, name='lista_software'),
    
    # CREATE: crea nuovo software
    # POST /api/software/create/
    # Nota: URL diverso da lista per chiarezza didattica
    # Django REST Framework gestisce automaticamente i metodi diversi
    path('software/create/', views.crea_software, name='crea_software'),
    
    
    # --- QUERY SPECIALI ---
    # IMPORTANTE: questi devono stare PRIMA degli URL con parametri dinamici
    # Altrimenti Django interpreterebbe 'gratuiti' come un ID numerico
    
    # GET /api/software/gratuiti/ - filtra software gratuiti
    path('software/gratuiti/', views.software_gratuiti, name='software_gratuiti'),
    
    # GET /api/software/produttore/Adobe/ - filtra per produttore
    # <str:produttore>: cattura una stringa dall'URL e la passa alla view
    # come parametro "produttore"
    path('software/produttore/<str:produttore>/', views.software_per_produttore, name='software_per_produttore'),
    
    
    # --- URL CON PARAMETRI DINAMICI ---
    # IMPORTANTE: questi devono stare DOPO le query speciali
    
    # READ: dettaglio singolo software
    # GET /api/software/1/
    # <int:software_id>: cattura un numero intero dall'URL e lo passa alla view
    # come parametro "software_id"
    path('software/<int:software_id>/', views.dettaglio_software, name='dettaglio_software'),
    
    # UPDATE: aggiorna tutto il software (PUT)
    # PUT /api/software/1/update/
    path('software/<int:software_id>/update/', views.aggiorna_software, name='aggiorna_software'),
    
    # UPDATE: aggiorna parzialmente (PATCH)
    # PATCH /api/software/1/patch/
    path('software/<int:software_id>/patch/', views.aggiorna_parziale_software, name='aggiorna_parziale_software'),
    
    # DELETE: elimina software
    # DELETE /api/software/1/delete/
    path('software/<int:software_id>/delete/', views.elimina_software, name='elimina_software'),
]