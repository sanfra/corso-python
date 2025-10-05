#!/usr/bin/env python3
# verifica_completa.py - Test completo ambiente Python (macOS/Linux compatible)

import sys
import subprocess
import importlib.util
import platform

def check_command(commands, name):
    """Verifica se un comando è disponibile (prova varianti)"""
    if isinstance(commands, str):
        commands = [commands]
    
    for command in commands:
        try:
            result = subprocess.run(
                [command, '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip() or result.stderr.strip()
                print(f"✓ {name}: {version.split()[0] if version else 'OK'}")
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            continue
    
    print(f"✗ {name}: NON TROVATO")
    return False

def check_module(module_name):
    """Verifica se un modulo Python è disponibile"""
    spec = importlib.util.find_spec(module_name)
    if spec is not None:
        print(f"  ✓ {module_name}")
        return True
    else:
        print(f"  ✗ {module_name}")
        return False

print("=" * 60)
print("VERIFICA COMPLETA AMBIENTE PYTHON")
print("=" * 60)

# Rileva sistema operativo
is_mac = platform.system() == 'Darwin'
is_windows = platform.system() == 'Windows'

# Verifica comandi di sistema (con varianti per macOS)
print("\n1. COMANDI DI SISTEMA:")
if is_mac:
    check_command(['python3', 'python'], 'Python')
    check_command(['pip3', 'pip'], 'Pip')
else:
    check_command('python', 'Python')
    check_command('pip', 'Pip')

check_command('git', 'Git')
check_command('code', 'VS Code')

# Verifica versione Python
print(f"\n2. VERSIONE PYTHON:")
print(f"   {sys.version}")
print(f"   Sistema: {platform.system()} {platform.release()}")

# Verifica moduli standard
print("\n3. MODULI STANDARD:")
standard_modules = [
    'os', 'sys', 'json', 'csv', 'datetime',
    'random', 'math', 'sqlite3', 're'
]
for module in standard_modules:
    check_module(module)

# Verifica capacità pip (con varianti)
print("\n4. TEST PIP:")
pip_command = 'pip3' if is_mac else 'pip'
try:
    result = subprocess.run(
        [pip_command, 'list'],
        capture_output=True,
        text=True,
        timeout=10
    )
    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        print(f"  ✓ Pip funziona ({len(lines)-2} pacchetti installati)")
    else:
        print(f"  ✗ Errore pip")
except Exception as e:
    print(f"  ✗ Pip non disponibile: {e}")

# Test scrittura file
print("\n5. TEST SCRITTURA FILE:")
try:
    with open('test_write.txt', 'w') as f:
        f.write('Test scrittura file')
    print("  ✓ Scrittura file OK")
    
    import os
    os.remove('test_write.txt')
    print("  ✓ Eliminazione file OK")
except Exception as e:
    print(f"  ✗ Errore: {e}")

# Info aggiuntive macOS
if is_mac:
    print("\n6. INFO macOS:")
    print(f"  Percorso Python: {sys.executable}")
    try:
        # Verifica se è installato via Homebrew
        result = subprocess.run(['which', 'python3'], capture_output=True, text=True)
        print(f"  Which python3: {result.stdout.strip()}")
        
        result = subprocess.run(['which', 'pip3'], capture_output=True, text=True)
        print(f"  Which pip3: {result.stdout.strip()}")
    except:
        pass

print("\n" + "=" * 60)
print("VERIFICA COMPLETATA!")
print("=" * 60)

if is_mac:
    print("\nNOTA macOS: Usa 'python3' e 'pip3' invece di 'python' e 'pip'")