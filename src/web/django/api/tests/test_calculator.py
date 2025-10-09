import pytest
from api.calculator import Calculator

#è un decorator di pytest che permette di creare oggetti riutilizzabili per i test. È come un "preparatore" che crea qualcosa prima di ogni test e lo passa come argomento.
@pytest.fixture
def calc():
    """Fixture per creare una calcolatrice"""
    return Calculator()

#@pytest.mark.parametrize è un decorator di pytest che permette di eseguire lo stesso test con input diversi senza scrivere codice ripetuto.
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (100, 200, 300),
    (0, 5, 5),
])
def test_add_positive(calc, a, b, expected):
    """Test addizione con pytest"""
    result = calc.add(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b", [
    (None, 5),
    (5, None),
    (None, None),
])

#"Verifica che calc.add(a, b) sollevi un errore TypeError che contenga la parola 'None' nel messaggio"
def test_add_with_none(calc, a, b):
    """Test addizione con None"""
    with pytest.raises(TypeError, match="None"):
        calc.add(a, b)


# Esegui con:
# pytest api/tests.py -v