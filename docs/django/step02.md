# Avvio Server Django - PWW

## Prerequisiti

Prima di avviare il server, assicurati di aver completato:

* ✅ Clonato il repository
* ✅ Creato il virtual environment `venv_pww`
* ✅ Attivato il virtual environment (vedi `(venv_pww)` nel terminale)
* ✅ Installato le dipendenze con `pip install -r requirements.txt`

---

## 1. Verifica di Essere nella Cartella Corretta

```bash
# Controlla di essere nella cartella pww
pwd  # macOS/Linux
cd   # Windows

# Dovresti vedere il percorso che finisce con /pww o \pww
```

**Verifica che esista il file `manage.py`:**

```bash
# Windows
dir manage.py

# macOS/Linux
ls manage.py
```

---

## 2. Verifica Virtual Environment Attivo

**Controlla che il terminale mostri:**

```bash
(venv_pww) C:\progetti\pww>  # Windows
# oppure
(venv_pww) ~/progetti/pww$   # macOS/Linux
```

**Se NON vedi `(venv_pww)`, attivalo:**

```bash
# Windows
venv_pww\Scripts\activate

# macOS/Linux
source venv_pww/bin/activate
```

---

## 3. Avviare il Server di Sviluppo

```bash
python manage.py runserver
```

**Output atteso:**

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 06, 2025 - 14:30:00
Django version 5.0.1, using settings 'pww.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Cosa significa:**

* `Watching for file changes` = Django monitora i file e si ricarica automaticamente quando modifichi il codice
* `System check identified no issues` = Nessun errore nella configurazione
* `Starting development server at http://127.0.0.1:8000/` = Server attivo su questa porta
* `Quit the server with CTRL-BREAK` = Premi CTRL+C per fermare il server

---

## 4. Verificare che il Server Funzioni

### Metodo 1: Browser

1. Apri il browser
2. Vai all'indirizzo: `http://127.0.0.1:8000/api/hello/`
3. Dovresti vedere una risposta JSON

**Risposta attesa:**

```json
{
    "message": "Hello from PWW API!",
    "method": "GET",
    "path": "/api/hello/"
}
```

### Metodo 2: curl (da un altro terminale)

```bash
curl http://127.0.0.1:8000/api/hello/
```

### Metodo 3: Python requests

Apri un altro terminale, attiva venv e:

```bash
pip install requests
python
```

```python
import requests
response = requests.get('http://127.0.0.1:8000/api/hello/')
print(response.json())
```

---

## 5. Vedere i Log delle Request

Nel terminale dove hai avviato il server, vedrai i log di ogni request:

```
INFO: REQUEST: GET /api/hello/
INFO: RESPONSE: 200 for /api/hello/
[06/Oct/2025 14:30:15] "GET /api/hello/ HTTP/1.1" 200 98
```

**Cosa significa:**

* `REQUEST: GET /api/hello/` = Request ricevuta
* `RESPONSE: 200` = Risposta con codice 200 (OK)
* `"GET /api/hello/ HTTP/1.1" 200 98` = Log standard Django

---

## 6. Fermare il Server

Nel terminale dove il server è in esecuzione:

```bash
# Premi CTRL + C
```

**Output:**

```
^C
Quit the server with CTRL-BREAK.
```

Il server si fermerà e potrai eseguire altri comandi.

---

## 7. Avviare su Porta Diversa

Se la porta 8000 è occupata:

```bash
python manage.py runserver 8080
```

Poi accedi a: `http://127.0.0.1:8080/api/hello/`

---

## 8. Avviare per Test da Altri Dispositivi

Per testare da smartphone o altro computer nella stessa rete:

```bash
python manage.py runserver 0.0.0.0:8000
```

**Trova il tuo IP:**

```bash
# Windows
ipconfig

# macOS/Linux
ifconfig  # oppure
ip addr show
```

Poi da altro dispositivo vai a: `http://TUO_IP:8000/api/hello/`

Esempio: `http://192.168.1.100:8000/api/hello/`

---

## 9. Comandi Utili Durante lo Sviluppo

```bash
# Avviare il server
python manage.py runserver

# Avviare su porta specifica
python manage.py runserver 8080

# Avviare per accesso da rete
python manage.py runserver 0.0.0.0:8000

# Fermare il server
# Premi CTRL + C

# Vedere tutti i comandi disponibili
python manage.py help
```

---

## 10. Troubleshooting

### Problema: "No module named 'django'"

**Causa:** Virtual environment non attivo o Django non installato

**Soluzione:**

```bash
# 1. Attiva venv
venv_pww\Scripts\activate  # Windows
source venv_pww/bin/activate  # macOS/Linux

# 2. Verifica installazione
pip list | grep Django  # macOS/Linux
pip list | findstr Django  # Windows

# 3. Se manca, installa
pip install -r requirements.txt
```

### Problema: "That port is already in use"

**Causa:** Hai già un server Django in esecuzione

**Soluzione 1:** Chiudi l'altro server (trova la finestra terminale e premi CTRL+C)

**Soluzione 2:** Usa porta diversa

```bash
python manage.py runserver 8080
```

### Problema: "Error: [Errno 98] Address already in use"

**Causa:** La porta è occupata da altro processo

**Soluzione Windows:**

```bash
# Trova il processo sulla porta 8000
netstat -ano | findstr :8000

# Killa il processo (PID è l'ultimo numero)
taskkill /PID <numero_pid> /F
```

**Soluzione macOS/Linux:**

```bash
# Trova il processo
lsof -ti:8000

# Killa il processo
kill -9 $(lsof -ti:8000)
```

### Problema: Pagina non si carica nel browser

**Verifiche:**

1. Server è in esecuzione? (controlla il terminale)
2. URL corretto? `http://127.0.0.1:8000/api/hello/`
3. Virtual environment attivo?
4. Firewall blocca la porta?

---

## 11. Workflow Completo

```bash
# 1. Apri terminale
cd pww

# 2. Attiva virtual environment
venv_pww\Scripts\activate  # Windows
source venv_pww/bin/activate  # macOS/Linux

# 3. Avvia server
python manage.py runserver

# 4. Apri browser
# http://127.0.0.1:8000/api/hello/

# 5. Quando finisci, ferma server
# CTRL + C

# 6. Disattiva venv (opzionale)
deactivate
```

---

## 12. Note Importanti

⚠️ **Il server di sviluppo NON è per produzione!**

* Va bene per sviluppo e test
* NON usarlo in produzione
* Per produzione serve Gunicorn/uWSGI + Nginx

✅ **Auto-reload:**

* Django ricarica automaticamente quando modifichi file .py
* Non serve riavviare il server dopo ogni modifica
* Se modifichi `settings.py` a volte serve riavvio manuale

📝 **Tutti i log nel terminale:**

* Ogni request viene loggata
* Ottimo per debugging
* Vedi errori in tempo reale

---

## Prossimo Step

Ora che il server funziona, puoi:

* Testare l'API con diversi tool (Postman, curl, browser)
* Modificare il codice e vedere i cambiamenti
* Aggiungere nuovi endpoint API

📘 Vai al file `03-testing-api.md` per continuare.
