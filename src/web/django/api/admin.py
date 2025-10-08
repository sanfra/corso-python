from django.contrib import admin
from .models.software import Software


# @admin.register(): decorator per registrare il modello nell'admin Django
# ⚠️ IMPORTANTE: Senza questa registrazione, il modello NON appare nell'admin!
#
# Metodo 1 (con decorator): @admin.register(Software)
# Metodo 2 (tradizionale): admin.site.register(Software, SoftwareAdmin)
# Sono equivalenti, usa quello che preferisci
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    """
    Personalizzazione dell'interfaccia admin per il modello Software.
    
    ⚠️ Senza questa classe: Django mostra interfaccia base (funzionale ma minimale)
    ⚠️ Con questa classe: interfaccia personalizzata (ricerca, filtri, ordinamento, ecc.)
    """
    
    # --- VISTA LISTA (tabella dei record) ---
    
    # list_display: colonne da mostrare nella tabella
    # Default: solo __str__() del modello
    # Con list_display: vedi tutti i campi specificati come colonne
    # 
    # ⚠️ Puoi anche usare metodi custom:
    # list_display = ['nome', 'versione', 'prezzo_formattato']
    # def prezzo_formattato(self, obj):
    #     return f"€{obj.prezzo}"
    list_display = ['nome', 'versione', 'produttore', 'prezzo', 'gratuito', 'data_rilascio']
    
    # list_filter: filtri nella sidebar destra
    # Crea automaticamente filtri interattivi per questi campi
    # - BooleanField: mostra "Sì/No/Tutti"
    # - CharField: mostra tutte le opzioni uniche
    # - DateField: mostra "Oggi/Ultimi 7 giorni/Questo mese/Quest'anno"
    list_filter = ['gratuito', 'produttore']
    
    # search_fields: campi ricercabili con la barra di ricerca
    # Django cerca usando LIKE %testo% (case-insensitive di default)
    # Esempio: cercare "adobe" trova "Adobe", "ADOBE", "adobe photoshop"
    # 
    # ⚠️ Puoi specificare il tipo di ricerca:
    # search_fields = ['=nome']        # Corrispondenza esatta
    # search_fields = ['^nome']        # Inizia con
    # search_fields = ['@nome']        # Full-text search (solo PostgreSQL)
    search_fields = ['nome', 'produttore']
    
    # ordering: ordinamento di default nella lista
    # '-' = ordine DECRESCENTE (Z-A, 9-0, più recente→vecchio)
    # Senza '-' = CRESCENTE (A-Z, 0-9, vecchio→recente)
    # 
    # Esempi:
    # ordering = ['nome']                    # A-Z
    # ordering = ['-prezzo']                 # Dal più costoso
    # ordering = ['produttore', 'nome']      # Per produttore, poi nome
    ordering = ['-data_rilascio']  # Più recenti prima
    
    
    # --- ALTRE OPZIONI UTILI ---
    
    # list_per_page: quanti record mostrare per pagina
    # list_per_page = 25  # Default: 100
    
    # date_hierarchy: navigazione gerarchica per data (anno > mese > giorno)
    # date_hierarchy = 'data_rilascio'  # Aggiunge menu in alto
    
    # readonly_fields: campi in sola lettura (visualizzabili ma non modificabili)
    # readonly_fields = ['id', 'data_creazione']
    
    # fields: ordine e raggruppamento campi nel form di modifica
    # fields = ['nome', 'versione', ('produttore', 'prezzo')]  # tuple = stessa riga
    
    # fieldsets: raggruppa campi in sezioni con titoli
    # fieldsets = [
    #     ('Informazioni Base', {
    #         'fields': ['nome', 'versione', 'produttore']
    #     }),
    #     ('Dettagli Commerciali', {
    #         'fields': ['prezzo', 'gratuito']
    #     }),
    # ]
    
    # list_editable: campi modificabili direttamente dalla lista (senza aprire il form)
    # list_editable = ['prezzo', 'gratuito']  # ⚠️ Non includere il primo campo di list_display!
    
    # list_display_links: quali campi sono link alla pagina di modifica
    # list_display_links = ['nome', 'versione']  # Default: primo campo
    
    # actions: azioni custom sulla lista (oltre a "Elimina selezionati")
    # def rendi_gratuito(self, request, queryset):
    #     queryset.update(gratuito=True, prezzo=0)
    # rendi_gratuito.short_description = "Rendi gratuito il software selezionato"
    # actions = [rendi_gratuito]
    
    # autocomplete_fields: autocompletamento per ForeignKey/ManyToMany
    # autocomplete_fields = ['categoria']  # Richiede search_fields nel modello correlato
    
    # prepopulated_fields: auto-riempie campi (utile per slug)
    # prepopulated_fields = {'slug': ('nome',)}  # Genera slug da nome
    
    # save_on_top: pulsanti Salva anche in cima (oltre che in fondo)
    # save_on_top = True
    
    # list_select_related: ottimizza query per ForeignKey (evita N+1 queries)
    # list_select_related = ['categoria', 'produttore']


# --- METODI CUSTOM PER list_display ---

# Puoi aggiungere metodi custom per mostrare dati calcolati:
#
# @admin.register(Software)
# class SoftwareAdmin(admin.ModelAdmin):
#     list_display = ['nome', 'prezzo_formattato', 'e_gratuito']
#     
#     def prezzo_formattato(self, obj):
#         """Mostra prezzo con valuta"""
#         return f"€{obj.prezzo}"
#     prezzo_formattato.short_description = 'Prezzo'  # Nome colonna
#     
#     def e_gratuito(self, obj):
#         """Icona verde/rossa per gratuito"""
#         return obj.gratuito
#     e_gratuito.boolean = True  # Mostra icona ✓/✗
#     e_gratuito.short_description = 'Gratis?'


# --- REGISTRAZIONE ALTERNATIVA (senza decorator) ---

# Se preferisci non usare @admin.register(), puoi fare:
#
# class SoftwareAdmin(admin.ModelAdmin):
#     list_display = [...]
#     # ... altre opzioni
#
# admin.site.register(Software, SoftwareAdmin)
#
# Oppure registrazione base senza personalizzazioni:
# admin.site.register(Software)  # Interfaccia admin di default


# --- INLINE ADMIN (per relazioni) ---

# Se hai modelli con ForeignKey, puoi modificarli inline:
#
# class RecensioneInline(admin.TabularInline):
#     model = Recensione
#     extra = 1  # Numero di form vuoti da mostrare
#
# @admin.register(Software)
# class SoftwareAdmin(admin.ModelAdmin):
#     inlines = [RecensioneInline]  # Mostra recensioni dentro il form Software


# --- NOTE FINALI ---

# 1. ACCESSO ADMIN:
#    URL: http://localhost:8000/admin/
#    Richiede superuser: python manage.py createsuperuser
#
# 2. PERSONALIZZAZIONE INTERFACCIA:
#    - list_display: cosa vedere nella lista
#    - list_filter: come filtrare
#    - search_fields: cosa cercare
#    - ordering: come ordinare
#
# 3. PERFORMANCE:
#    - list_select_related: per ForeignKey (evita query multiple)
#    - list_prefetch_related: per ManyToMany (evita query multiple)
#    - list_per_page: limita record per pagina
#
# 4. DOCUMENTAZIONE:
#    https://docs.djangoproject.com/en/stable/ref/contrib/admin/