# Setup Ambiente di Sviluppo - PWW

## 1. Clonare il Repository

```bash
git clone <url-del-repository>
cd pww
```

---

## 2. Creare il Virtual Environment

### Windows

```bash
python -m venv venv_pww
```

### macOS/Linux

```bash
python3 -m venv venv_pww
```

**Cosa succede:**

* Python crea una cartella `venv_pww` con l'ambiente virtuale isolato
* Questa cartella contiene Python, pip e tutte le librerie che installeremo

---

## 3. Attivare il Virtual Environment

### Windows (Command Prompt)

```bash
venv_pww\Scripts\activate
```

### Windows (PowerShell)

```powershell
venv_pww\Scripts\Activate.ps1
```

### macOS/Linux

```bash
source venv_pww/bin/activate
```

**Verifica che sia attivo:**

* Dovresti vedere `(venv_pww)` all'inizio della riga del terminale
* Esempio: `(venv_pww) C:\progetti\pww>`

---

## 4. File requirements.txt

Il file `requirements.txt` contiene tutte le dipendenze del progetto:

```txt
Django==5.0.1
djangorestframework==3.14.0
```

**Cosa contiene:**

* `Django==5.0.1` - Il framework web Django versione 5.0.1
* `djangorestframework==3.14.0` - Libreria per creare API REST

---

## 5. Installare le Dipendenze

```bash
pip install -r requirements.txt
```

**Cosa succede:**

* pip legge il file `requirements.txt` riga per riga
* Scarica e installa Django 5.0.1
* Scarica e installa Django REST Framework 3.14.0
* Installa anche tutte le dipendenze di queste librerie

**Output atteso:**

```
Collecting Django==5.0.1 (from -r requirements.txt (line 1))
  Downloading Django-5.0.1-py3-none-any.whl (8.1 MB)
Collecting djangorestframework==3.14.0 (from -r requirements.txt (line 2))
  Downloading djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
Collecting asgiref<4,>=3.7.0
  Downloading asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.4.4-py3-none-any.whl (41 kB)
Installing collected packages: sqlparse, asgiref, pytz, Django, djangorestframework
Successfully installed Django-5.0.1 asgiref-3.7.2 djangorestframework-3.14.0 pytz-2023.3 sqlparse-0.4.4
```

---

## 6. Verificare l'Installazione

```bash
pip list
```

**Output atteso:**

```
Package              Version
-------------------- -------
asgiref              3.7.2
Django               5.0.1
djangorestframework  3.14.0
pip                  24.0
pytz                 2023.3
sqlparse             0.4.4
```

---

## 7. Comandi di Riepilogo

```bash
# 1. Clonare il progetto
git clone <url-del-repository>
cd pww

# 2. Creare virtual environment
python -m venv venv_pww

# 3. Attivare virtual environment
# Windows:
venv_pww\Scripts\activate
# macOS/Linux:
source venv_pww/bin/activate

# 4. Installare dipendenze
pip install -r requirements.txt

# 5. Verificare installazione
pip list
```

---

## 8. Disattivare il Virtual Environment

Quando hai finito di lavorare:

```bash
deactivate
```

**Cosa succede:**

* Il prefisso `(venv_pww)` scompare dal terminale
* Torni a usare Python e pip di sistema
* Le librerie del progetto non sono più disponibili

---

## 9. Troubleshooting

### Problema: "python: command not found" (macOS/Linux)

**Soluzione:**

```bash
python3 -m venv venv_pww
source venv_pww/bin/activate
pip3 install -r requirements.txt
```

### Problema: Errore PowerShell su Windows

**Errore:**

```
venv_pww\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled
```

**Soluzione:**

```powershell
# Apri PowerShell come Amministratore
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Chiudi e riapri PowerShell normale
venv_pww\Scripts\Activate.ps1
```

### Problema: pip install fallisce

**Soluzione:**

```bash
# Aggiorna pip
python -m pip install --upgrade pip

# Riprova l'installazione
pip install -r requirements.txt
```

---

## 10. Note Importanti

⚠️ **SEMPRE attivare il virtual environment prima di lavorare!**

✅ Ogni volta che apri un nuovo terminale:

```bash
cd pww
venv_pww\Scripts\activate  # Windows
# oppure
source venv_pww/bin/activate  # macOS/Linux
```

❌ La cartella `venv_pww/` NON è su Git:

* Non preoccuparti se non la vedi nel repository
* Ogni sviluppatore crea il proprio virtual environment
* Serve solo il file `requirements.txt` per ricreare l'ambiente

---

## Prossimo Step

Una volta completato il setup, puoi passare a:

* Avviare il server Django
* Testare l'API
* Iniziare a sviluppare

📘 Vai al file `02-avvio-server.md` per continuare.
