from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configurazione dell'app 'api'.
    
    ⚠️ IMPORTANTE: Questo file viene creato automaticamente da Django quando
    esegui 'python manage.py startapp api' e raramente necessita modifiche.
    
    Viene utilizzato per:
    - Configurare il nome dell'app
    - Definire il tipo di campo auto-generato per le primary key
    - Registrare signal handlers (avanzato)
    - Eseguire codice all'avvio dell'app (metodo ready())
    """
    
    # default_auto_field: tipo di campo usato per le primary key auto-generate
    # 
    # BigAutoField: numeri interi grandi (1 a 9,223,372,036,854,775,807)
    # SQL: BIGINT AUTO_INCREMENT
    # 
    # ⚠️ Perché BigAutoField e non AutoField?
    # - AutoField: max 2,147,483,647 record (circa 2 miliardi)
    # - BigAutoField: max 9 quintilioni di record (praticamente infinito)
    # Django usa BigAutoField di default da versione 3.2+
    #
    # Alternative:
    # - 'django.db.models.AutoField'      # Numeri più piccoli (max 2 miliardi)
    # - 'django.db.models.SmallAutoField' # Ancora più piccoli (max 32,767)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # name: nome dell'app (deve corrispondere al nome della cartella)
    # ⚠️ CRITICO: deve essere esattamente il nome della cartella dell'app
    # Usato da Django per:
    # - Importare i modelli (api.models.Software)
    # - Trovare templates (api/templates/)
    # - Identificare l'app in INSTALLED_APPS
    name = 'api'
    
    # --- ALTRE OPZIONI UTILI (opzionali) ---
    
    # verbose_name: nome leggibile dell'app nel Django Admin
    # verbose_name = 'API Software'
    
    # default: se True, questa è l'app di default del progetto
    # default = False
    
    
    # --- METODO READY (avanzato) ---
    
    # ready(): eseguito quando Django inizializza l'app
    # Usato per registrare signal handlers o eseguire codice di setup
    #
    # def ready(self):
    #     """Eseguito all'avvio dell'app"""
    #     # Importa e registra signals
    #     import api.signals
    #     
    #     # Oppure registra checks custom
    #     from django.core.checks import register, Tags
    #     
    #     print(f"App {self.name} caricata!")


# --- DOVE VIENE USATO? ---

# Questo file viene referenziato in settings.py → INSTALLED_APPS:
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     ...
#     'rest_framework',
#     'api',              # ← Usa ApiConfig automaticamente
#     # oppure esplicitamente:
#     # 'api.apps.ApiConfig',
# ]


# --- QUANDO MODIFICARLO? ---

# Raramente! Le modifiche più comuni sono:
#
# 1. Aggiungere verbose_name per l'admin:
#    verbose_name = 'Gestione Software'
#
# 2. Registrare signals nel metodo ready():
#    def ready(self):
#        import api.signals  # Connette signal handlers
#
# 3. Cambiare default_auto_field (sconsigliato dopo il primo migrate):
#    default_auto_field = 'django.db.models.AutoField'


# --- NOTE FINALI ---

# 1. NON cambiare 'name' dopo aver fatto migrate
#    Motivo: rompe le referenze nel database
#
# 2. BigAutoField vs AutoField:
#    - Per app piccole: AutoField va bene
#    - Per app che potrebbero crescere: BigAutoField (default Django 3.2+)
#    - Una volta scelto e migrato: difficile cambiare
#
# 3. Se NON hai questo file:
#    Django usa una configurazione di default, ma è meglio averlo
#
# 4. Path completo in INSTALLED_APPS:
#    'api' → Django cerca automaticamente api.apps.ApiConfig
#    'api.apps.ApiConfig' → Specificato esplicitamente (equivalente)