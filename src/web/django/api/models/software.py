from django.db import models

# ⚠️ IMPORTANTE: Ogni classe che eredita da models.Model = 1 tabella nel database
# Django genera automaticamente SQL per creare/modificare tabelle (migrations)
class Software(models.Model):
    """
    Modello Software: rappresenta un software nel database.
    
    Django ORM traduce questa classe Python in tabella SQL:
    - Classe → Tabella
    - Attributi → Colonne
    - Istanza → Riga
    """
    
    # --- CAMPI TESTO ---
    
    # CharField: testo a lunghezza limitata
    # SQL: VARCHAR(100)
    # ⚠️ max_length è OBBLIGATORIO per CharField
    nome = models.CharField(max_length=100)
    
    # Versione come testo (non numero!) per gestire formati come "2.5.3-beta"
    versione = models.CharField(max_length=20)
    
    produttore = models.CharField(max_length=100)
    
    
    # --- CAMPI NUMERICI ---
    
    # DecimalField: numeri decimali precisi
    # ⚠️ Usa DecimalField (non FloatField!) per PREZZI/DENARO
    # Motivo: evita errori di arrotondamento float (0.1 + 0.2 ≠ 0.3)
    # 
    # max_digits=8: totale cifre (prima + dopo virgola)
    # decimal_places=2: cifre dopo la virgola
    # Esempio: 999999.99 è valido, 1000000.00 NO (troppo grande)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    
    
    # --- CAMPI BOOLEANI ---
    
    # BooleanField: True/False
    # SQL: BOOLEAN o TINYINT(1) a seconda del DB
    # default=False: valore predefinito se non specificato
    # ⚠️ Senza default, il campo è obbligatorio!
    gratuito = models.BooleanField(default=False)
    
    
    # --- CAMPI DATA/ORA ---
    
    # DateField: solo data (YYYY-MM-DD)
    # SQL: DATE
    # Alternative:
    # - DateTimeField: data + ora (YYYY-MM-DD HH:MM:SS)
    # - TimeField: solo ora (HH:MM:SS)
    data_rilascio = models.DateField()
    
    
    # --- METODI SPECIALI ---
    
    # __str__: rappresentazione testuale dell'oggetto
    # ⚠️ IMPORTANTE: usato in Django Admin, shell, debug, ecc.
    # Senza __str__: vedrai "Software object (1)" nell'admin
    # Con __str__: vedrai "Photoshop v25.0" (più utile!)
    def __str__(self):
        return f"{self.nome} v{self.versione}"
    
    
    # --- META OPTIONS ---
    
    # class Meta: configurazioni del modello (NON sono campi database!)
    class Meta:
        # verbose_name_plural: nome plurale per Django Admin
        # Senza: "Softwares" ❌ (grammaticamente sbagliato)
        # Con: "Software" ✅ (corretto in italiano)
        verbose_name_plural = "Software"
        
        # --- ALTRE OPZIONI META UTILI ---
        
        # ordering: ordine default delle query
        # ordering = ['nome']              # A-Z per nome
        # ordering = ['-data_rilascio']    # Dal più recente (- = DESC)
        # ordering = ['produttore', 'nome'] # Prima per produttore, poi nome
        
        # db_table: nome custom della tabella nel DB
        # db_table = 'catalogo_software'   # Default: api_software
        
        # verbose_name: nome singolare per Django Admin
        # verbose_name = 'Programma'
        
        # unique_together: vincoli di unicità multipli
        # unique_together = [['nome', 'versione']]  # stesso nome+versione = errore
        
        # indexes: indici per performance
        # indexes = [
        #     models.Index(fields=['produttore']),  # velocizza query per produttore
        # ]


# --- ALTRI TIPI DI CAMPO COMUNI ---

# class Esempio(models.Model):
#     # TextField: testo illimitato (descrizioni lunghe)
#     # SQL: TEXT
#     descrizione = models.TextField()
    
#     # IntegerField: numeri interi
#     downloads = models.IntegerField(default=0)
    
#     # EmailField: email con validazione automatica
#     contatto = models.EmailField()
    
#     # URLField: URL con validazione
#     sito_web = models.URLField(blank=True)  # blank=True → opzionale
    
#     # FileField / ImageField: upload di file/immagini
#     logo = models.ImageField(upload_to='loghi/')
    
#     # ForeignKey: relazione Many-to-One (chiave esterna)
#     # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
#     # ManyToManyField: relazione Many-to-Many
#     # tag = models.ManyToManyField(Tag)
    
#     # JSONField: dati JSON (disponibile da Django 3.1+)
#     metadati = models.JSONField(default=dict, blank=True)
    
#     # Auto fields (gestiti automaticamente da Django):
#     # id = models.AutoField(primary_key=True)  # Creato automaticamente!
#     # created_at = models.DateTimeField(auto_now_add=True)  # Settato alla creazione
#     # updated_at = models.DateTimeField(auto_now=True)      # Aggiornato a ogni save()


# --- OPZIONI CAMPO COMUNI ---

# Ogni campo può avere opzioni:
#
# blank=True          → Opzionale nei form (validazione Django)
# null=True           → Può essere NULL nel DB (validazione SQL)
# default=valore      → Valore predefinito
# unique=True         → Deve essere unico nel DB
# choices=CHOICES     → Limita a scelte predefinite
# help_text="..."     → Testo di aiuto nell'admin
# verbose_name="..."  → Nome leggibile del campo
# validators=[...]    → Validatori custom
#
# ⚠️ DIFFERENZA blank vs null:
# - blank: validazione a livello FORM (Django)
# - null: a livello DATABASE (SQL)
# Per CharField: usa blank=True (non null=True!)
# Per altri campi: usa entrambi se opzionali


# --- ESEMPIO CON CHOICES ---

# class Software(models.Model):
#     CATEGORIA_CHOICES = [
#         ('DEV', 'Sviluppo'),
#         ('DESIGN', 'Grafica'),
#         ('OFFICE', 'Ufficio'),
#     ]
#     
#     categoria = models.CharField(
#         max_length=10,
#         choices=CATEGORIA_CHOICES,
#         default='DEV'
#     )
#     
#     # Nel database: salva 'DEV'
#     # In Python: obj.get_categoria_display() → 'Sviluppo'


# --- NOTE FINALI ---

# 1. DOPO aver creato/modificato un modello:
#    python manage.py makemigrations  # Crea file migrazione
#    python manage.py migrate         # Applica al database

# 2. ID AUTO-GENERATO:
#    Django crea automaticamente un campo 'id' (primary key) se non specificato

# 3. NOMI TABELLE:
#    Default: app_nomemodello (es: api_software)
#    Custom: usa db_table in Meta

# 4. FIELD TYPES REFERENCE:
#    https://docs.djangoproject.com/en/stable/ref/models/fields/