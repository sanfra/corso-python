"""
Modulo calcolatrice per testing unitario con pytest.
"""


class Calculator:
    """Calcolatrice con operazioni base e validazione input"""
    
    def _validate_numbers(self, *args):
        """Valida che tutti gli argomenti siano numeri (non None)"""
        for arg in args:
            if arg is None:
                raise TypeError("Gli argomenti non possono essere None")
            if not isinstance(arg, (int, float)):
                raise TypeError(
                    f"Tipo non valido: {type(arg).__name__}. "
                    f"Atteso int o float"
                )
    
    def add(self, a, b):
        """Somma due numeri"""
        self._validate_numbers(a, b)
        return a + b
    
    def subtract(self, a, b):
        """Sottrae b da a"""
        self._validate_numbers(a, b)
        return a - b
    
    def multiply(self, a, b):
        """Moltiplica due numeri"""
        self._validate_numbers(a, b)
        return a * b
    
    def divide(self, a, b):
        """Divide a per b"""
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Divisione per zero non permessa")
        return a / b
    
    def power(self, base, exponent):
        """Calcola base^exponent"""
        self._validate_numbers(base, exponent)
        return base ** exponent
    
    def modulo(self, a, b):
        """Calcola il resto della divisione a % b"""
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Modulo per zero non permesso")
        return a % b
    
    def is_even(self, n):
        """Verifica se un numero è pari"""
        self._validate_numbers(n)
        return n % 2 == 0
    
    def is_positive(self, n):
        """Verifica se un numero è positivo"""
        self._validate_numbers(n)
        return n > 0
    
    def absolute(self, n):
        """Restituisce il valore assoluto"""
        self._validate_numbers(n)
        return abs(n)
    
    def max_of_two(self, a, b):
        """Restituisce il massimo tra due numeri"""
        self._validate_numbers(a, b)
        return max(a, b)
    
    def min_of_two(self, a, b):
        """Restituisce il minimo tra due numeri"""
        self._validate_numbers(a, b)
        return min(a, b)