from django.urls import path  # Funzione per definire pattern URL
from . import views  # Importa le view dalla cartella corrente (api/)

# urlpatterns: lista degli URL dell'app
# ⚠️ IMPORTANTE: Django controlla dall'ALTO verso il BASSO e si ferma al PRIMO match
urlpatterns = [
    # --- ENDPOINT DI TEST ---
    
    # GET /api/hello/
    # path(URL_pattern, funzione_view, nome_simbolico)
    path('hello/', views.hello_world, name='hello'),
    
    # POST /api/helloPost/
    path('helloPost/', views.hello_post, name='hello_post'),
    
    
    # --- CRUD SOFTWARE ---
    
    # READ ALL: Ottieni lista completa
    # GET /api/software/
    path('software/', views.lista_software, name='lista_software'),
    
    # CREATE: Crea nuovo record
    # POST /api/software/create/
    # Body JSON richiesto con tutti i campi del modello
    path('software/create/', views.crea_software, name='crea_software'),
    
    
    # --- FILTRI SPECIALI (URL FISSI) ---
    # ⚠️ CRITICO: Questi DEVONO stare PRIMA degli URL con parametri dinamici!
    # Motivo: se 'gratuiti' venisse dopo <int:software_id>, Django proverebbe
    # a convertire "gratuiti" in un numero intero → Errore 404
    
    # GET /api/software/gratuiti/ - Solo software con gratuito=True
    path('software/gratuiti/', views.software_gratuiti, name='software_gratuiti'),
    
    # GET /api/software/produttore/Microsoft/
    # <str:produttore>: cattura qualsiasi testo dall'URL e lo passa come parametro
    # Esempio: "Adobe" viene passato a views.software_per_produttore(request, produttore="Adobe")
    path('software/produttore/<str:produttore>/', 
         views.software_per_produttore, 
         name='software_per_produttore'),
    
    
    # --- URL DINAMICI (CON PARAMETRI) ---
    # ⚠️ REGOLA: Questi vanno ALLA FINE, dal più specifico al più generico
    # Motivo: <int:software_id> cattura QUALSIASI numero, quindi è molto "generico"
    
    # READ ONE: Dettaglio di un singolo software
    # GET /api/software/5/
    # <int:software_id>: cattura SOLO numeri interi (es: 1, 42, 999)
    # Django passa automaticamente software_id alla view come parametro
    path('software/<int:software_id>/', 
         views.dettaglio_software, 
         name='dettaglio_software'),
    
    # UPDATE COMPLETO: Sostituisce tutti i campi (richiede TUTTI i campi nel body)
    # PUT /api/software/5/update/
    # Body JSON: deve contenere TUTTI i campi (nome, versione, produttore, ecc.)
    path('software/<int:software_id>/update/', 
         views.aggiorna_software, 
         name='aggiorna_software'),
    
    # UPDATE PARZIALE: Modifica solo alcuni campi
    # PATCH /api/software/5/patch/
    # Body JSON: solo i campi da modificare (es: {"versione": "2.0"})
    # Django REST Framework usa partial=True nel serializer
    path('software/<int:software_id>/patch/', 
         views.aggiorna_parziale_software, 
         name='aggiorna_parziale_software'),
    
    # DELETE: Elimina record dal database (IRREVERSIBILE!)
    # DELETE /api/software/5/delete/
    # Nessun body richiesto, solo l'ID nell'URL
    path('software/<int:software_id>/delete/', 
         views.elimina_software, 
         name='elimina_software'),
]


# --- NOTE IMPORTANTI ---

# 1. ORDINE URL: Sempre dal PIÙ SPECIFICO al PIÙ GENERICO
#    ✅ Corretto: 'software/gratuiti/' PRIMA di 'software/<int:id>/'
#    ❌ Sbagliato: 'software/<int:id>/' PRIMA di 'software/gratuiti/' → 404 error!

# 2. PARAMETRI URL:
#    - <int:nome>: solo numeri interi (1, 42, 999)
#    - <str:nome>: qualsiasi testo (Adobe, Microsoft, "hello world")
#    - <slug:nome>: solo lettere, numeri, trattini, underscore
#    - <path:nome>: qualsiasi cosa, anche con / (percorsi completi)

# 3. NAME: Utile per reverse() e {% url %} nei template
#    Esempio: reverse('dettaglio_software', args=[5]) → '/api/software/5/'

# 4. TRAILING SLASH: Django preferisce URL con / finale
#    - /api/software/ ✅ (con slash)
#    - /api/software  ❌ (senza slash → redirect automatico a versione con /)