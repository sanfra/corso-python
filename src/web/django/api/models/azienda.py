from django.db import models


class Azienda(models.Model):
    """
    Modello Azienda: rappresenta un'azienda produttrice di software.
    
    Relazione: Un'Azienda può produrre molti Software (One-to-Many)
    """
    
    # --- CAMPI IDENTIFICATIVI ---
    nome = models.CharField(
        max_length=200,
        unique=True,
        help_text="Nome dell'azienda"
    )
    
    partita_iva = models.CharField(
        max_length=20,
        unique=True,
        help_text="Partita IVA (univoca)"
    )
    
    # --- CAMPI CONTATTO ---
    sede = models.CharField(
        max_length=200,
        help_text="Indirizzo sede principale"
    )
    
    email = models.EmailField(
        help_text="Email di contatto aziendale"
    )
    
    telefono = models.CharField(
        max_length=20,
        blank=True,
        help_text="Numero di telefono (opzionale)"
    )
    
    sito_web = models.URLField(
        blank=True,
        help_text="Sito web aziendale (opzionale)"
    )
    
    # --- CAMPI DESCRITTIVI ---
    descrizione = models.TextField(
        blank=True,
        help_text="Descrizione dell'azienda"
    )
    
    # --- CAMPI DATA ---
    data_fondazione = models.DateField(
        null=True,
        blank=True,
        help_text="Data di fondazione dell'azienda"
    )
    
    # --- TIMESTAMP AUTOMATICI ---
    creata_il = models.DateTimeField(
        auto_now_add=True,
        help_text="Data creazione record"
    )
    
    modificata_il = models.DateTimeField(
        auto_now=True,
        help_text="Data ultima modifica"
    )
    
    # --- METODI ---
    def __str__(self):
        """Rappresentazione testuale dell'oggetto"""
        return f"{self.nome} (P.IVA: {self.partita_iva})"
    
    def numero_software(self):
        """Conta il numero di software prodotti da questa azienda"""
        return self.software.count()  # usa related_name='software'
    
    # --- META OPTIONS ---
    class Meta:
        verbose_name = "Azienda"
        verbose_name_plural = "Aziende"
        ordering = ['nome']  # Ordina alfabeticamente per nome
        
        # Indici per performance
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['partita_iva']),
        ]