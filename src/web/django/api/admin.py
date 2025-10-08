from django.contrib import admin
from .models import Software, Azienda


@admin.register(Azienda)
class AziendaAdmin(admin.ModelAdmin):
    """Configurazione admin per Azienda"""
    
    list_display = ['nome', 'partita_iva', 'sede', 'email', 'telefono']
    search_fields = ['nome', 'partita_iva', 'sede']
    list_filter = ['data_fondazione']
    ordering = ['nome']


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    """Configurazione admin per Software"""
    
    # ✅ CORRETTO: usa 'azienda' invece di 'produttore'
    list_display = ['nome', 'versione', 'azienda', 'prezzo', 'gratuito', 'attivo', 'data_rilascio']
    
    # ✅ CORRETTO: filtra per 'azienda' e 'gratuito'
    list_filter = ['gratuito', 'attivo', 'azienda']
    
    # ✅ Cerca anche nel nome dell'azienda con __
    search_fields = ['nome', 'azienda__nome', 'versione']
    
    ordering = ['-data_rilascio']
    
    # Campo readonly
    readonly_fields = ['creato_il', 'modificato_il']
    
    # Organizza campi nel form
    fieldsets = [
        ('Informazioni Base', {
            'fields': ['nome', 'versione', 'descrizione']
        }),
        ('Azienda', {
            'fields': ['azienda']
        }),
        ('Prezzo', {
            'fields': ['prezzo', 'gratuito']
        }),
        ('Dettagli', {
            'fields': ['attivo', 'data_rilascio']
        }),
        ('Metadata', {
            'fields': ['creato_il', 'modificato_il'],
            'classes': ['collapse']
        }),
    ]