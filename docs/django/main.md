# Setup Progetto PWW - Python Web Workshop

**Acronimo progetto:** PWW (Python Web Workshop)

---

## 1. Setup Iniziale per lo Studente

### Prerequisiti

* Python 3.10 o superiore installato
* Git installato
* Editor di codice (VS Code, PyCharm, etc.)

---

## 2. Clone del Progetto

```bash
# Clonare il repository
git clone <url-del-repository>

# Entrare nella cartella del progetto
cd pww
```

---

## 3. Creazione Virtual Environment

```bash
# Creare il virtual environment
python -m venv venv_pww
```

**Spiegazione:**

* `python -m venv` = comando per creare un ambiente virtuale
* `venv_pww` = nome dell'ambiente virtuale (PWW = Python Web Workshop)

---

## 4. Attivazione Virtual Environment

### Su Windows:

```bash
venv_pww\Scripts\activate
```

### Su macOS/Linux:

```bash
source venv_pww/bin/activate
```

**Verifica:** Dovresti vedere `(venv_pww)` all'inizio del prompt del terminale.

---

## 5. Installazione Dipendenze

```bash
# Installare tutte le librerie necessarie
pip install -r requirements.txt
```

**Cosa fa:**

* Legge il file `requirements.txt`
* Installa Django e Django REST Framework
* Installa tutte le dipendenze necessarie

---

## 6. Avvio del Server

```bash
# Avviare il server di sviluppo
python manage.py runserver
```

**Server attivo su:** `http://127.0.0.1:8000/`

**Per fermare il server:** Premi `CTRL + C`

---

## 7. Testare l'API

### Endpoint disponibile:

```
GET http://127.0.0.1:8000/api/hello/
```

### Test con browser:

* Apri il browser
* Vai su `http://127.0.0.1:8000/api/hello/`
* Dovresti vedere una risposta JSON

### Test con curl:

```bash
curl http://127.0.0.1:8000/api/hello/
```

---

## 8. Struttura del Progetto

```
pww/
├── venv_pww/              # Virtual environment (NON presente su Git)
├── pww/                   # Configurazione Django
│   ├── settings.py        # Impostazioni del progetto
│   ├── urls.py            # URL routing principale
│   └── wsgi.py
├── api/                   # App per l'API REST
│   ├── views.py           # Logica delle API
│   ├── urls.py            # URL dell'API
│   └── middleware.py      # Middleware per logging request
├── manage.py              # Script di gestione Django
├── requirements.txt       # Lista dipendenze
├── .gitignore            # File da ignorare su Git
└── README.md             # Questa guida
```

---

## 9. File requirements.txt

```txt
Django==5.0.1
djangorestframework==3.14.0
```

---

## 10. Comandi Utili

```bash
# Attivare virtual environment
venv_pww\Scripts\activate          # Windows
source venv_pww/bin/activate       # macOS/Linux

# Disattivare virtual environment
deactivate

# Avviare server
python manage.py runserver

# Avviare su porta diversa
python manage.py runserver 8080

# Vedere pacchetti installati
pip list
```

---

## 11. Troubleshooting

### Problema: "django: command not found"

**Soluzione:** Assicurati che il virtual environment sia attivo (vedi `(venv_pww)` nel prompt)

### Problema: "Port already in use"

**Soluzione:**

```bash
# Usa una porta diversa
python manage.py runserver 8080
```

### Problema: Errore durante pip install

**Soluzione:**

```bash
# Aggiorna pip
python -m pip install --upgrade pip
# Riprova
pip install -r requirements.txt
```

---

## 12. Note per lo Sviluppo

* **NON committare** la cartella `venv_pww/` su Git
* **NON committare** il file `db.sqlite3` su Git
* Tutte le request vengono loggate automaticamente nella console
* L'API è accessibile anche da Postman o altri tool REST

---

## Setup per il Docente (Creazione Progetto)

### Comandi eseguiti per creare il progetto:

```bash
# 1. Creare virtual environment
python -m venv venv_pww

# 2. Attivare venv
venv_pww\Scripts\activate  # Windows
source venv_pww/bin/activate  # macOS/Linux

# 3. Installare Django e DRF
pip install django==5.0.1
pip install djangorestframework==3.14.0

# 4. Creare progetto
django-admin startproject pww .

# 5. Creare app API
python manage.py startapp api

# 6. Creare requirements.txt
pip freeze > requirements.txt

# 7. Applicare migrazioni
python manage.py migrate

# 8. Creare .gitignore
# (vedere sezione successiva)

# 9. Commit iniziale
git init
git add .
git commit -m "Initial commit: PWW project setup"
git remote add origin <url-repository>
git push -u origin main
```

### File .gitignore

```gitignore
# Virtual Environment
venv_pww/
venv/
env/
ENV/

# Database
*.sqlite3
db.sqlite3

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Django
*.log
local_settings.py
/static/
/media/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
```

---

## Configurazione Base del Progetto

### pww/settings.py (aggiunte necessarie)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # ← Aggiungere
    'api',             # ← Aggiungere
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.RequestLoggerMiddleware',  # ← Aggiungere
]
```

### pww/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ← Aggiungere
]
```

### api/urls.py (file da creare)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]
```

### api/views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def hello_world(request):
    """
    API endpoint semplice che risponde con un messaggio
    """
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)
```

### api/middleware.py (file da creare)

```python
import logging

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:
    """
    Middleware che logga ogni request in arrivo
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logga la request prima di processarla
        logger.info(f"REQUEST: {request.method} {request.path}")
      
        # Processa la request
        response = self.get_response(request)
      
        # Logga la response
        logger.info(f"RESPONSE: {response.status_code} for {request.path}")
      
        return response
```

---

## Test dell'API

### Test 1: Browser

1. Avvia il server: `python manage.py runserver`
2. Apri: `http://127.0.0.1:8000/api/hello/`
3. Dovresti vedere JSON con il messaggio

### Test 2: curl

```bash
curl http://127.0.0.1:8000/api/hello/
```

### Test 3: Python requests

```python
import requests

response = requests.get('http://127.0.0.1:8000/api/hello/')
print(response.json())
```

### Output atteso:

```json
{
    "message": "Hello from PWW API!",
    "method": "GET",
    "path": "/api/hello/"
}
```

### Log nella console:

```
INFO: REQUEST: GET /api/hello/
INFO: RESPONSE: 200 for /api/hello/
```
