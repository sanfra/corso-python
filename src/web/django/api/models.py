from django.db import models

# Definiamo una classe che eredita da models.Model
# Ogni classe che eredita da Model diventa una tabella nel database
class Software(models.Model):
    # CharField: campo di testo con lunghezza massima
    # max_length=100: il nome può avere massimo 100 caratteri
    # Questo diventerà una colonna VARCHAR(100) nel database
    nome = models.CharField(max_length=100)
    
    # CharField per la versione (es: "1.0", "2.5.3", ecc.)
    versione = models.CharField(max_length=20)
    
    # CharField per il nome del produttore
    produttore = models.CharField(max_length=100)
    
    # DecimalField: campo numerico decimale per valori monetari
    # max_digits=8: numero totale di cifre (es: 999999.99)
    # decimal_places=2: numero di cifre decimali (i centesimi)
    # Meglio di FloatField per i soldi perché più preciso
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    
    # BooleanField: campo booleano (True/False)
    # default=False: se non specificato, il valore di default è False
    gratuito = models.BooleanField(default=False)
    
    # DateField: campo per memorizzare solo la data (senza ora)
    # Per data e ora insieme useremmo DateTimeField
    data_rilascio = models.DateField()
    
    # Metodo speciale __str__: definisce come l'oggetto viene rappresentato come stringa
    # Viene usato nell'admin di Django e quando facciamo print(software)
    def __str__(self):
        return f"{self.nome} v{self.versione}"
    
    # class Meta: classe interna che contiene metadati (informazioni aggiuntive)
    # sul modello, NON sono campi del database
    class Meta:
        # verbose_name_plural: come Django chiama questo modello al plurale
        # nell'interfaccia admin. Senza questo, Django userebbe "Softwares"
        # che è grammaticalmente sbagliato
        verbose_name_plural = "Software"
        
        # Altri esempi di opzioni Meta che si possono usare:
        # ordering = ['nome']  # ordina automaticamente per nome
        # db_table = 'miei_software'  # nome personalizzato della tabella nel DB
        # verbose_name = 'Programma Software'  # nome al singolarefrom django.db import models

# Definiamo una classe che eredita da models.Model
# Ogni classe che eredita da Model diventa una tabella nel database
class Software(models.Model):
    # CharField: campo di testo con lunghezza massima
    # max_length=100: il nome può avere massimo 100 caratteri
    # Questo diventerà una colonna VARCHAR(100) nel database
    nome = models.CharField(max_length=100)
    
    # CharField per la versione (es: "1.0", "2.5.3", ecc.)
    versione = models.CharField(max_length=20)
    
    # CharField per il nome del produttore
    produttore = models.CharField(max_length=100)
    
    # DecimalField: campo numerico decimale per valori monetari
    # max_digits=8: numero totale di cifre (es: 999999.99)
    # decimal_places=2: numero di cifre decimali (i centesimi)
    # Meglio di FloatField per i soldi perché più preciso
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    
    # BooleanField: campo booleano (True/False)
    # default=False: se non specificato, il valore di default è False
    gratuito = models.BooleanField(default=False)
    
    # DateField: campo per memorizzare solo la data (senza ora)
    # Per data e ora insieme useremmo DateTimeField
    data_rilascio = models.DateField()
    
    # Metodo speciale __str__: definisce come l'oggetto viene rappresentato come stringa
    # Viene usato nell'admin di Django e quando facciamo print(software)
    def __str__(self):
        return f"{self.nome} v{self.versione}"
    
    # class Meta: classe interna che contiene metadati (informazioni aggiuntive)
    # sul modello, NON sono campi del database
    class Meta:
        # verbose_name_plural: come Django chiama questo modello al plurale
        # nell'interfaccia admin. Senza questo, Django userebbe "Softwares"
        # che è grammaticalmente sbagliato
        verbose_name_plural = "Software"
        
        # Altri esempi di opzioni Meta che si possono usare:
        # ordering = ['nome']  # ordina automaticamente per nome
        # db_table = 'miei_software'  # nome personalizzato della tabella nel DB
        # verbose_name = 'Programma Software'  # nome al singolare