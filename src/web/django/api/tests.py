# api/tests.py

from django.test import TestCase
from datetime import date

# Import assoluti (NON relativi)
from api.models import Azienda, Software


class AziendaModelTest(TestCase):
    """Test per il modello Azienda"""
    
    def test_azienda_creation(self):
        """Test creazione azienda su DB temporaneo"""
        
        # Crea un'azienda con TUTTI i campi obbligatori del TUO modello
        azienda = Azienda.objects.create(
            nome="Microsoft",
            partita_iva="12345678901",
            sede="Redmond, WA",
            email="info@microsoft.com"
        )
        
        # Verifica che sia stata creata correttamente
        self.assertEqual(azienda.nome, "Microsoft")
        self.assertEqual(azienda.sede, "Redmond, WA")
        self.assertEqual(Azienda.objects.count(), 1)
        
        print(f"✅ Test passato! Azienda creata: {azienda}")