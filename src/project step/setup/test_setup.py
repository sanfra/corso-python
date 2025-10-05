# test_setup.py - Verifica installazione Python

import sys
import platform

print("=" * 50)
print("VERIFICA AMBIENTE PYTHON")
print("=" * 50)

# Versione Python
print(f"\nVersione Python: {sys.version}")
print(f"Versione breve: {platform.python_version()}")

# Percorso eseguibile
print(f"\nPercorso Python: {sys.executable}")

# Sistema operativo
print(f"\nSistema: {platform.system()} {platform.release()}")
print(f"Architettura: {platform.machine()}")

# Moduli importanti
try:
    import pip
    print(f"\nPip versione: {pip.__version__}")
except ImportError:
    print("\n⚠️  Pip non trovato!")

# Test import moduli standard
modules_to_test = ['os', 'sys', 'json', 'datetime', 'random', 'math']
print(f"\nTest import moduli standard:")
for module in modules_to_test:
    try:
        __import__(module)
        print(f"  ✓ {module}")
    except ImportError:
        print(f"  ✗ {module} - ERRORE")

print("\n" + "=" * 50)
print("Test completato!")
print("=" * 50)