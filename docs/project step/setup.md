# 🐍 Setup Ambiente Python su Windows con VS Code

## Guida Completa per il Corso Python

---

## 📋 Prerequisiti

**Sistema Operativo:** Windows 10/11 (64-bit)

**Spazio disco:** Almeno 5GB liberi

**RAM:** Minimo 4GB (consigliato 8GB)

**Connessione:** Internet attiva per download

---

## 1️⃣ Installazione Visual Studio Code

### Download e Installazione

1. Vai su [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Clicca su **Download for Windows** (scaricherà automaticamente la versione corretta)
3. Esegui il file scaricato: `VSCodeUserSetup-x64-*.exe`

### Opzioni di Installazione (IMPORTANTE)

Durante l'installazione, **seleziona queste opzioni:**

* ✅ **Add "Open with Code" action to Windows Explorer file context menu**
* ✅ **Add "Open with Code" action to Windows Explorer directory context menu**
* ✅ **Register Code as an editor for supported file types**
* ✅ **Add to PATH** (fondamentale!)

### Verifica Installazione

1. Premi `Win + R`
2. Digita `cmd` e premi Invio
3. Nel prompt dei comandi digita:
   ```bash
   code --version
   ```
4. Dovresti vedere qualcosa come:
   ```
   1.85.08b3775030ed1a69b13e4f4c628c612102e30a681x64
   ```

---

## 2️⃣ Installazione Python

### Download Python

1. Vai su [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clicca su **Download Python 3.13.7** (o versione più recente 3.11+)
   * Link diretto: [https://www.python.org/downloads/release/python-3137/](https://www.python.org/downloads/release/python-3137/)
3. Scorri in basso fino a **Files**
4. Scarica: **Windows installer (64-bit)**

### Installazione Python (CRITICO)

1. **Esegui** il file scaricato (`python-3.13.7-amd64.exe`)
2. **⚠️ PRIMA DI CLICCARE "Install Now":**
   * ✅ **Seleziona "Add Python 3.13 to PATH"** (in basso, fondamentale!)
   * ✅ **Seleziona "Install launcher for all users (recommended)"**
3. Clicca **Install Now**
4. Attendi il completamento
5. Clicca **Close**

### Verifica Installazione Python

1. **Chiudi** eventuali finestre del Prompt dei comandi aperte prima
2. Apri un **nuovo** Prompt dei comandi (`Win + R` → `cmd`)
3. Digita:

   ```bash
   python --version
   ```

   Output atteso:

   ```
   Python 3.13.7
   ```
4. Digita:

   ```bash
   pip --version
   ```

   Output atteso:

   ```
   pip 24.0 from C:\Users\...\Python313\lib\site-packages\pip (python 3.13)
   ```

### ⚠️ Troubleshooting Python

**Se il comando `python` non viene riconosciuto:**

1. Cerca "Variabili d'ambiente" nel menu Start
2. Clicca su "Modifica le variabili d'ambiente del sistema"
3. Clicca su "Variabili d'ambiente"
4. In "Variabili utente", seleziona "Path" e clicca "Modifica"
5. Verifica che ci siano questi percorsi (modifica secondo la tua installazione):
   * `C:\Users\TuoNome\AppData\Local\Programs\Python\Python313\`
   * `C:\Users\TuoNome\AppData\Local\Programs\Python\Python313\Scripts\`
6. Se mancano, clicca "Nuovo" e aggiungili
7. Clicca OK su tutte le finestre
8. **Riavvia** il Prompt dei comandi

---

## 3️⃣ Installazione Git

### Download Git

1. Vai su [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Il download dovrebbe partire automaticamente (64-bit Git for Windows Setup)
3. Se non parte, clicca su "Click here to download manually"

### Installazione Git

1. Esegui il file scaricato (`Git-*-64-bit.exe`)
2. **Usa le impostazioni predefinite** , clicca sempre "Next"
3. Opzioni raccomandate:
   * Editor: "Use Visual Studio Code as Git's default editor"
   * PATH: "Git from the command line and also from 3rd-party software"
   * HTTPS: "Use bundled OpenSSL library"
   * Line endings: "Checkout Windows-style, commit Unix-style"
4. Clicca "Install"
5. Deseleziona "View Release Notes" e clicca "Finish"

### Verifica Installazione Git

Apri un nuovo Prompt dei comandi e digita:

```bash
git --version
```

Output atteso:

```
git version 2.43.0.windows.1
```

### Configurazione Iniziale Git (Opzionale ma consigliata)

```bash
git config --global user.name "Tuo Nome"
git config --global user.email "tua.email@example.com"
```

---

## 4️⃣ Configurazione VS Code per Python

### Installazione Estensioni

1. Apri VS Code
2. Clicca sull'icona **Extensions** (quadrato con 4 quadratini) nella barra laterale sinistra
   * Oppure premi `Ctrl+Shift+X`

### Estensioni Obbligatorie

Cerca e installa  **nell'ordine** :

#### 1. Python (ms-python.python)

* Cerca: `Python`
* Publisher: Microsoft
* Descrizione: IntelliSense, linting, debugging, formatting
* Clicca **Install**

#### 2. Pylance (ms-python.vscode-pylance)

* Cerca: `Pylance`
* Publisher: Microsoft
* Descrizione: Fast, feature-rich language support
* Clicca **Install**

### Estensioni Raccomandate

#### 3. GitLens (eamodio.gitlens)

* Cerca: `GitLens`
* Publisher: GitKraken
* Descrizione: Git supercharged
* Clicca **Install**

#### 4. Markdown All in One (yzhang.markdown-all-in-one)

* Cerca: `Markdown All in One`
* Publisher: Yu Zhang
* Descrizione: Supporto completo per Markdown
* Clicca **Install**

#### 5. Python Indent (KevinRose.vsc-python-indent)

* Cerca: `Python Indent`
* Publisher: Kevin Rose
* Descrizione: Auto-indentazione corretta
* Clicca **Install**

#### 6. autoDocstring (njpwerner.autodocstring)

* Cerca: `autoDocstring`
* Publisher: Nils Werner
* Descrizione: Genera docstring automaticamente
* Clicca **Install**

### Estensioni Opzionali (Utili)

* **Python Test Explorer** - Testing integrato
* **Better Comments** - Commenti colorati
* **Bracket Pair Colorizer 2** - Parentesi colorate (VS Code 2021+ lo ha integrato)
* **Error Lens** - Mostra errori inline
* **Code Runner** - Esegui codice rapidamente

---

## 5️⃣ Configurazione Workspace Python

### Creare Cartella di Lavoro

1. Crea una cartella per il corso, es: `C:\Users\TuoNome\Documents\corso-python`
2. Apri VS Code
3. File → Open Folder → Seleziona `corso-python`

### Selezionare Interprete Python

1. Premi `Ctrl+Shift+P` per aprire il Command Palette
2. Digita: `Python: Select Interpreter`
3. Seleziona la versione Python installata (es. `Python 3.13.7 64-bit`)

### Creare File di Test

1. Nel file explorer di VS Code (barra sinistra), clicca sull'icona "New File"
2. Nomina il file: `test_setup.py`
3. Scrivi questo codice:

```python
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
```

### Eseguire il File di Test

**Metodo 1 - Pulsante Run:**

* Clicca sul pulsante ▶️ **Run Python File** in alto a destra
* Oppure premi `Ctrl+F5`

**Metodo 2 - Terminale integrato:**

* Apri il terminale in VS Code: `Ctrl+ù` (o View → Terminal)
* Digita:
  ```bash
  python test_setup.py
  ```

### Output Atteso

```
==================================================
VERIFICA AMBIENTE PYTHON
==================================================

Versione Python: 3.13.7 (tags/v3.13.7:...) [MSC v.1936 64 bit (AMD64)]
Versione breve: 3.13.7

Percorso Python: C:\Users\...\Python313\python.exe

Sistema: Windows 10
Architettura: AMD64

Pip versione: 24.0

Test import moduli standard:
  ✓ os
  ✓ sys
  ✓ json
  ✓ datetime
  ✓ random
  ✓ math

==================================================
Test completato!
==================================================
```

---

## 6️⃣ Configurazione Terminale in VS Code

### Impostare PowerShell o Command Prompt

1. Apri VS Code
2. Premi `Ctrl+Shift+P`
3. Digita: `Terminal: Select Default Profile`
4. Seleziona **Command Prompt** o **PowerShell** (raccomandato Command Prompt per il corso)

### Test Terminale

1. Apri terminale: `Ctrl+ù`
2. Dovresti vedere il prompt tipo:
   ```
   C:\Users\TuoNome\Documents\corso-python>
   ```
3. Verifica comandi:
   ```bash
   python --versionpip --versiongit --versioncode --version
   ```

---

## 7️⃣ Configurazioni Consigliate VS Code

### Settings JSON

1. Premi `Ctrl+,` per aprire Settings
2. Cerca: `Python formatting provider`
3. Imposta: `autopep8` (o `black`)
4. Cerca: `Python linting enabled`
5. Assicurati sia ✅ abilitato
6. Cerca: `Files: Auto Save`
7. Imposta: `afterDelay` (salvataggio automatico)

### Formattazione Automatica

1. Premi `Ctrl+Shift+P`
2. Digita: `Format Document With...`
3. Seleziona: `Python`

### Shortcut Utili da Ricordare

| Azione              | Shortcut          |
| ------------------- | ----------------- |
| Command Palette     | `Ctrl+Shift+P`  |
| Terminale integrato | `Ctrl+ù`       |
| File Explorer       | `Ctrl+Shift+E`  |
| Cerca file          | `Ctrl+P`        |
| Cerca in file       | `Ctrl+Shift+F`  |
| Commenta riga       | `Ctrl+K Ctrl+C` |
| Decommenta riga     | `Ctrl+K Ctrl+U` |
| Formatta documento  | `Shift+Alt+F`   |
| Esegui file Python  | `Ctrl+F5`       |
| Salva tutto         | `Ctrl+K S`      |

---

## 8️⃣ Test Completo dell'Ambiente

### Script di Verifica Avanzato

Crea un file `verifica_completa.py`:

```python
#!/usr/bin/env python3
# verifica_completa.py - Test completo ambiente Python

import sys
import subprocess
import importlib.util

def check_command(command, name):
    """Verifica se un comando è disponibile"""
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

# Verifica comandi di sistema
print("\n1. COMANDI DI SISTEMA:")
check_command('python', 'Python')
check_command('pip', 'Pip')
check_command('git', 'Git')
check_command('code', 'VS Code')

# Verifica versione Python
print(f"\n2. VERSIONE PYTHON:")
print(f"   {sys.version}")

# Verifica moduli standard
print("\n3. MODULI STANDARD:")
standard_modules = [
    'os', 'sys', 'json', 'csv', 'datetime',
    'random', 'math', 'sqlite3', 're'
]
for module in standard_modules:
    check_module(module)

# Verifica capacità pip
print("\n4. TEST PIP:")
try:
    result = subprocess.run(
        ['pip', 'list'],
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

print("\n" + "=" * 60)
print("VERIFICA COMPLETATA!")
print("=" * 60)
```

Esegui con:

```bash
python verifica_completa.py
```

---

## 9️⃣ Checklist Finale

### Verifica Installazioni

* [ ] **VS Code installato**
  * Test: `code --version` nel cmd
  * Versione attesa: 1.85+
* [ ] **Python installato**
  * Test: `python --version`
  * Versione attesa: 3.13.7 (o 3.11+)
* [ ] **Pip funzionante**
  * Test: `pip --version`
  * Versione attesa: 24.0+
* [ ] **Git installato**
  * Test: `git --version`
  * Versione attesa: 2.43+

### Verifica Estensioni VS Code

* [ ] **Python** (ms-python.python)
* [ ] **Pylance** (ms-python.vscode-pylance)
* [ ] **GitLens** (eamodio.gitlens)
* [ ] **Markdown All in One** (yzhang.markdown-all-in-one)

### Verifica Funzionalità

* [ ] **File Python eseguito** (`test_setup.py`)
* [ ] **Terminale integrato** funziona (`Ctrl+ù`)
* [ ] **Interprete Python** selezionato in VS Code
* [ ] **Formattazione codice** funziona (`Shift+Alt+F`)
* [ ] **IntelliSense** (suggerimenti automatici) funziona

---

## 🔧 Troubleshooting Comune

### Problema: "python non è riconosciuto come comando"

**Soluzione:**

1. Reinstalla Python con "Add to PATH" selezionato
2. Oppure aggiungi manualmente il PATH (vedi sezione 2)
3. Riavvia VS Code e terminale

### Problema: VS Code non trova Python

**Soluzione:**

1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Se non appare: "Enter interpreter path" → Sfoglia → Trova `python.exe`
3. Path tipico: `C:\Users\TuoNome\AppData\Local\Programs\Python\Python313\python.exe`

### Problema: Estensioni non si installano

**Soluzione:**

1. Verifica connessione internet
2. Disabilita antivirus temporaneamente
3. Riavvia VS Code
4. Prova manualmente: scarica `.vsix` e installa offline

### Problema: Terminale non si apre

**Soluzione:**

1. View → Terminal (o `Ctrl+ù`)
2. Se non funziona: `Ctrl+Shift+P` → "Terminal: Create New Terminal"
3. Verifica impostazioni: Settings → Terminal → Integrated

---

## 📚 Risorse Aggiuntive

* [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
* [Python Official Docs](https://docs.python.org/3/)
* [Git Documentation](https://git-scm.com/doc)
* [VS Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

---

## ✅ Pronto per il Corso!

Se tutte le checklist sono completate, sei pronto per iniziare il corso Python! 🎉

**Prossimi passi:**

1. Familiarizza con VS Code
2. Prova a scrivere qualche riga di Python
3. Esplora le estensioni installate
4. Rivedi gli shortcut principali

**Ci vediamo alla prima lezione!** 🚀
