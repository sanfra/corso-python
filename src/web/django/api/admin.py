from django.contrib import admin  # Modulo per l'interfaccia admin di Django
from .models import Software  # Importiamo il modello

# @admin.register(Software): decorator che registra il modello nell'admin
# È equivalente a scrivere: admin.site.register(Software, SoftwareAdmin)
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    """
    Configurazione personalizzata per il modello Software nell'admin.
    ModelAdmin permette di personalizzare come il modello appare nell'interfaccia admin.
    """
    
    # list_display: quali campi mostrare nella lista (tabella) nell'admin
    # Questi campi appaiono come colonne nella vista lista
    list_display = ['nome', 'versione', 'produttore', 'prezzo', 'gratuito', 'data_rilascio']
    
    # list_filter: aggiunge filtri nella sidebar destra dell'admin
    # Permette di filtrare i record per questi campi
    list_filter = ['gratuito', 'produttore']
    
    # search_fields: campi in cui cercare con la barra di ricerca dell'admin
    # Django cerca il testo in questi campi usando LIKE %text%
    search_fields = ['nome', 'produttore']
    
    # ordering: ordine di default nella lista
    # '-data_rilascio' = ordina per data decrescente (più recenti prima)
    # 'nome' = ordinerebbe alfabeticamente per nome
    ordering = ['-data_rilascio']
    
    # Altri esempi di opzioni utili:
    # readonly_fields = ['id']  # campi in sola lettura
    # fields = ['nome', 'versione']  # campi da mostrare nel form di modifica
    # list_per_page = 50  # numero di record per pagina (default 100)
    # date_hierarchy = 'data_rilascio'  # aggiunge navigazione per data in alto