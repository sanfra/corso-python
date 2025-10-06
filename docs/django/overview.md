# Guida Python: Virtual Environment, Requirements e Django (Windows)

## 1. Virtual Environment (venv)

### A cosa serve

Un **virtual environment** è un ambiente Python isolato che permette di:

* Installare pacchetti specifici per un progetto senza interferire con altri progetti
* Avere versioni diverse dello stesso pacchetto in progetti diversi
* Evitare conflitti tra dipendenze
* Mantenere pulito il sistema Python globale

### Come si configura su Windows

#### Creazione del virtual environment

```cmd
python -m venv venv
```

Il comando crea una cartella `venv` contenente:

* Una copia dell'interprete Python
* Le librerie standard
* Gli strumenti pip e setuptools

#### Attivazione

```cmd
# CMD (Prompt dei comandi)
venv\Scripts\activate

# PowerShell
venv\Scripts\Activate.ps1
```

 **Nota PowerShell** : Se ricevi un errore di policy, esegui:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Quando attivo, vedrai il nome dell'ambiente nel prompt:

```
(venv) C:\progetti\mio_progetto>
```

#### Disattivazione

```cmd
deactivate
```

#### Esempio pratico

```cmd
# 1. Creare il virtual environment
python -m venv venv

# 2. Attivarlo
venv\Scripts\activate

# 3. Ora puoi installare pacchetti
pip install django

# 4. Quando hai finito
deactivate
```

---

## 2. File requirements.txt

### A cosa serve

Il file `requirements.txt` contiene l'elenco di tutti i pacchetti Python necessari per il tuo progetto, con le loro versioni specifiche. Serve per:

* Documentare le dipendenze del progetto
* Replicare l'ambiente su altre macchine
* Condividere il progetto con altri sviluppatori
* Deployare l'applicazione su server

### Il tuo file requirements.txt

Crea un file chiamato `requirements.txt` nella root del progetto con questo contenuto:

```txt
Django==5.0.1
djangorestframework==3.14.0
```

### Come si usa

#### Installare le dipendenze dal file

```cmd
# 1. Assicurati che il venv sia attivo
venv\Scripts\activate

# 2. Installa tutte le dipendenze
pip install -r requirements.txt
```

Questo comando installerà:

* Django versione 5.0.1
* Django REST Framework versione 3.14.0
* Tutte le dipendenze richieste da questi pacchetti

#### Verificare l'installazione

```cmd
pip list
```

Output atteso:

```
Package              Version
-------------------- -------
Django               5.0.1
djangorestframework  3.14.0
pip                  24.0
pytz                 2024.1
sqlparse             0.4.4
```

#### Aggiungere nuove dipendenze

Se installi un nuovo pacchetto:

```cmd
# Installare il nuovo pacchetto
pip install nome_pacchetto

# Aggiornare requirements.txt manualmente
# oppure rigenerarlo completamente
pip freeze > requirements.txt
```

---

## 3. Django Framework

### A cosa serve

**Django** è un framework web Python di alto livello che permette di:

* Sviluppare applicazioni web rapidamente
* Gestire database con l'ORM (Object-Relational Mapping)
* Creare API REST
* Implementare autenticazione e autorizzazione
* Gestire form, template e routing
* Avere un'interfaccia admin automatica

### Caratteristiche principali

* **MTV Pattern** : Model-Template-View (simile a MVC)
* **ORM integrato** : gestione database senza SQL diretto
* **Admin panel** : interfaccia di amministrazione automatica
* **Sicurezza** : protezione CSRF, SQL injection, XSS
* **Scalabilità** : usato da Instagram, Pinterest, Mozilla

### Come si installa

```cmd
# 1. Creare e attivare virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Installare Django e DRF dal requirements.txt
pip install -r requirements.txt

# 3. Verificare l'installazione
python -m django --version
```

Output atteso: `5.0.1`

### Creare un progetto Django

```bash
# Creare un nuovo progetto
django-admin startproject nome_progetto

# Struttura creata:
# nome_progetto/
#     manage.py
#     nome_progetto/
#         __init__.py
#         settings.py
#         urls.py
#         asgi.py
#         wsgi.py
```

### Creare un'app Django

```bash
# Entrare nella cartella del progetto
cd nome_progetto

# Creare una nuova app
python manage.py startapp nome_app
```

### Avviare il server di sviluppo

```cmd
# Avviare il server (porta 8000 di default)
python manage.py runserver

# Avviare su porta specifica
python manage.py runserver 8080

# Avviare su IP e porta specifici
python manage.py runserver 0.0.0.0:8000
```

Output tipico:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 06, 2025 - 21:30:00
Django version 5.0.1, using settings 'nome_progetto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

 **Per fermare il server** : premi `CTRL + C` o `CTRL + BREAK`

### Comandi Django essenziali

```cmd
# Creare le migrazioni del database
python manage.py makemigrations

# Applicare le migrazioni
python manage.py migrate

# Creare superuser per admin
python manage.py createsuperuser

# Aprire shell Python con context Django
python manage.py shell

# Raccogliere file statici
python manage.py collectstatic

# Eseguire test
python manage.py test
```

### Workflow completo su Windows

```cmd
# 1. Setup iniziale
python -m venv venv
venv\Scripts\activate

# 2. Creare il file requirements.txt
# Crea manualmente il file con:
# Django==5.0.1
# djangorestframework==3.14.0

# 3. Installare dipendenze
pip install -r requirements.txt

# 4. Creare progetto
django-admin startproject mio_sito
cd mio_sito

# 5. Creare app
python manage.py startapp api

# 6. Configurare database
python manage.py migrate

# 7. Creare admin user
python manage.py createsuperuser

# 8. Avviare server
python manage.py runserver
```

### Accedere all'applicazione

* **Homepage** : http://127.0.0.1:8000/
* **Admin panel** : http://127.0.0.1:8000/admin/

---

## Best Practices

### Virtual Environment

* ✅ Crea sempre un venv per ogni progetto
* ✅ Aggiungi `venv/` o `.venv/` al `.gitignore`
* ✅ Usa nomi standard come `venv`, `.venv` o `env`
* ❌ Non committare mai il virtual environment su Git

### Requirements

* ✅ Mantieni `requirements.txt` aggiornato
* ✅ Specifica versioni esatte per produzione (`==`)
* ✅ Considera file separati: `requirements-dev.txt`, `requirements-prod.txt`
* ✅ Documenta dipendenze con commenti

### Django

* ✅ Usa sempre il server di sviluppo solo per sviluppo
* ✅ Cambia `SECRET_KEY` in produzione
* ✅ Imposta `DEBUG = False` in produzione
* ✅ Usa database robusti (PostgreSQL, MySQL) in produzione
* ❌ Non usare SQLite in produzione per progetti grandi

---

## Esempio completo

```cmd
# Setup progetto Django completo su Windows
mkdir mio_progetto
cd mio_progetto

# Virtual environment
python -m venv venv
venv\Scripts\activate

# Creare requirements.txt con:
# Django==5.0.1
# djangorestframework==3.14.0

# Installare dipendenze
pip install -r requirements.txt

# Creare progetto
django-admin startproject config .

# Creare app
python manage.py startapp api

# Setup database
python manage.py migrate

# Creare superuser
python manage.py createsuperuser

# Avviare server
python manage.py runserver
```

## File .gitignore consigliato

Crea un file `.gitignore` nella root del progetto:

```
# Virtual Environment
venv/
env/
.venv/

# Database
*.sqlite3
db.sqlite3

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Django
*.log
media/
staticfiles/

# IDE
.vscode/
.idea/
*.swp
*.swo
```

## Risorse utili

* **Documentazione Django** : https://docs.djangoproject.com/
* **Django Tutorial ufficiale** : https://docs.djangoproject.com/en/stable/intro/tutorial01/
* **Virtual Environment docs** : https://docs.python.org/3/library/venv.html
