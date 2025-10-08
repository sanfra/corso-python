# Setup base

python setup.py

# Con nome personalizzato

python setup.py my_flask_app

# Poi per avviare:

cd flask_app
source venv/bin/activate  # su Linux/Mac

# oppure venv\Scripts\activate  # su Windows

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python run.py



# 📚 Documentazione Flask Setup

Guida completa per l'utilizzo dello script di setup Flask e della struttura del progetto generato.

---

## 📋 Indice

1. [Installazione e Setup](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#installazione-e-setup)
2. [Struttura del Progetto](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#struttura-del-progetto)
3. [Configurazione](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#configurazione)
4. [Database e Modelli](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#database-e-modelli)
5. [Routing e Views](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#routing-e-views)
6. [Template](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#template)
7. [API REST](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#api-rest)
8. [Static Files](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#static-files)
9. [Testing](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#testing)
10. [Deployment](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#deployment)
11. [Troubleshooting](https://claude.ai/chat/43b8f302-67da-4cef-ab7e-c3fead4bcf53#troubleshooting)

---

## 🚀 Installazione e Setup

### Requisiti

* Python 3.8 o superiore
* pip (package installer per Python)

### Installazione Base

```bash
# Esegui lo script di setup
python setup.py

# Oppure con nome personalizzato
python setup.py nome_progetto
```

### Primo Avvio

**Su Linux/MacOS:**

```bash
cd flask_app
source venv/bin/activate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python run.py
```

**Su Windows:**

```cmd
cd flask_app
venv\Scripts\activate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python run.py
```

L'applicazione sarà disponibile su: `http://127.0.0.1:5000`

---

## 📁 Struttura del Progetto

```
flask_app/
│
├── app/                          # Package principale dell'applicazione
│   ├── __init__.py              # Factory function e inizializzazione estensioni
│   ├── routes.py                # Route e views (Blueprint)
│   ├── models.py                # Modelli database SQLAlchemy
│   │
│   ├── templates/               # Template Jinja2
│   │   ├── base.html           # Template base
│   │   ├── index.html          # Homepage
│   │   └── about.html          # Pagina about
│   │
│   └── static/                  # File statici
│       ├── css/
│       │   └── style.css       # Stili CSS
│       └── js/
│           └── main.js         # JavaScript
│
├── tests/                       # Test suite
│   └── test_app.py             # Test dell'applicazione
│
├── venv/                        # Virtual environment (non committare)
│
├── migrations/                  # Migrazioni database (generato da Flask-Migrate)
│
├── config.py                    # Configurazione dell'applicazione
├── run.py                       # Entry point dell'applicazione
├── .env                         # Variables d'ambiente (non committare)
├── .gitignore                   # File da ignorare in Git
├── requirements.txt             # Dipendenze Python
└── README.md                    # Readme del progetto
```

---

## ⚙️ Configurazione

### File config.py

Il file `config.py` contiene la configurazione dell'applicazione:

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### File .env

Variabili d'ambiente per lo sviluppo:

```bash
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

**⚠️ IMPORTANTE:** Il file `.env` contiene dati sensibili e NON deve essere committato su Git!

### Variabili d'Ambiente

| Variabile        | Descrizione                       | Default              |
| ---------------- | --------------------------------- | -------------------- |
| `FLASK_APP`    | Entry point dell'app              | `run.py`           |
| `FLASK_ENV`    | Ambiente (development/production) | `development`      |
| `SECRET_KEY`   | Chiave segreta per sessioni       | `dev-secret-key`   |
| `DATABASE_URL` | URL del database                  | `sqlite:///app.db` |

---

## 🗄️ Database e Modelli

### SQLAlchemy ORM

Il progetto usa SQLAlchemy come ORM (Object-Relational Mapping).

### Modello di Esempio: Item

```python
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### Creare un Nuovo Modello

1. Aggiungi il modello in `app/models.py`
2. Esegui le migrazioni:

```bash
flask db migrate -m "Descrizione della modifica"
flask db upgrade
```

### Comandi Database Utili

```bash
# Inizializza il sistema di migrazioni (solo la prima volta)
flask db init

# Crea una nuova migrazione
flask db migrate -m "messaggio"

# Applica le migrazioni
flask db upgrade

# Torna indietro di una migrazione
flask db downgrade

# Mostra la cronologia delle migrazioni
flask db history
```

### Shell Interattiva

Per interagire con il database:

```bash
flask shell
```

```python
>>> from app.models import Item
>>> item = Item(name='Test', description='Descrizione test')
>>> db.session.add(item)
>>> db.session.commit()
>>> Item.query.all()
```

---

## 🛣️ Routing e Views

### Blueprint

Il progetto usa i Blueprint per organizzare le route:

```python
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')
```

### Aggiungere Nuove Route

In `app/routes.py`:

```python
@bp.route('/nuova-pagina')
def nuova_pagina():
    return render_template('nuova_pagina.html')
```

### Route con Parametri

```python
@bp.route('/user/<username>')
def user_profile(username):
    return render_template('profile.html', username=username)

@bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)
```

### Metodi HTTP

```python
@bp.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Gestisci POST
        data = request.form['field']
        return redirect(url_for('main.index'))
    # Gestisci GET
    return render_template('form.html')
```

---

## 🎨 Template

### Sistema di Template: Jinja2

### Template Base

Tutti i template ereditano da `base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }} - Flask App</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### Estendere il Template Base

```html
{% extends "base.html" %}

{% block content %}
<h1>Mia Pagina</h1>
<p>Contenuto della pagina</p>
{% endblock %}
```

### Sintassi Jinja2 Comune

**Variabili:**

```html
<h1>{{ titolo }}</h1>
<p>{{ descrizione|safe }}</p>
```

**Cicli:**

```html
{% for item in items %}
    <div>{{ item.name }}</div>
{% endfor %}
```

**Condizioni:**

```html
{% if user.is_authenticated %}
    <p>Benvenuto, {{ user.name }}!</p>
{% else %}
    <p>Per favore, effettua il login.</p>
{% endif %}
```

**Link:**

```html
<a href="{{ url_for('main.index') }}">Home</a>
<a href="{{ url_for('main.user_profile', username='john') }}">Profilo</a>
```

**Static Files:**

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}">
```

---

## 🔌 API REST

### Endpoint Disponibili

| Metodo     | Endpoint            | Descrizione           |
| ---------- | ------------------- | --------------------- |
| `GET`    | `/api/items`      | Lista tutti gli items |
| `POST`   | `/api/items`      | Crea nuovo item       |
| `GET`    | `/api/items/<id>` | Dettaglio item        |
| `PUT`    | `/api/items/<id>` | Aggiorna item         |
| `DELETE` | `/api/items/<id>` | Elimina item          |

### Esempi di Utilizzo

**GET - Lista items:**

```bash
curl http://localhost:5000/api/items
```

**POST - Crea item:**

```bash
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Nuovo Item","description":"Descrizione"}'
```

**PUT - Aggiorna item:**

```bash
curl -X PUT http://localhost:5000/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Item Modificato"}'
```

**DELETE - Elimina item:**

```bash
curl -X DELETE http://localhost:5000/api/items/1
```

### Creare Nuovi Endpoint API

```python
@bp.route('/api/utenti', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/api/utenti/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())
```

### Gestione Errori API

```python
from flask import jsonify

@bp.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@bp.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400
```

---

## 🎨 Static Files

### Organizzazione

```
static/
├── css/
│   └── style.css
├── js/
│   └── main.js
├── images/
└── fonts/
```

### Aggiungere CSS

1. Crea il file in `app/static/css/`
2. Collegalo nel template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">
```

### Aggiungere JavaScript

1. Crea il file in `app/static/js/`
2. Collegalo nel template:

```html
<script src="{{ url_for('static', filename='js/custom.js') }}"></script>
```

### JavaScript per API

Il file `main.js` include esempi di chiamate AJAX:

```javascript
async function loadItems() {
    const response = await fetch('/api/items');
    const items = await response.json();
    // Elabora i dati
}

async function addItem(name, description) {
    const response = await fetch('/api/items', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, description})
    });
    return await response.json();
}
```

---

## 🧪 Testing

### Eseguire i Test

```bash
# Esegui tutti i test
pytest

# Esegui con output dettagliato
pytest -v

# Esegui test specifici
pytest tests/test_app.py::test_index

# Esegui con coverage
pytest --cov=app
```

### Scrivere Nuovi Test

In `tests/test_app.py`:

```python
def test_nuova_funzionalita(client):
    response = client.get('/nuova-route')
    assert response.status_code == 200
    assert b'testo atteso' in response.data

def test_api_create_item(client):
    response = client.post('/api/items',
                          json={'name': 'Test'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test'
```

### Test del Database

```python
def test_item_creation():
    item = Item(name='Test', description='Desc')
    db.session.add(item)
    db.session.commit()
  
    assert item.id is not None
    assert Item.query.count() == 1
```

---

## 🚀 Deployment

### Preparazione per Produzione

1. **Cambia SECRET_KEY:**

```python
# Genera una chiave sicura
import secrets
secrets.token_hex(32)
```

2. **Aggiorna .env per produzione:**

```bash
FLASK_ENV=production
SECRET_KEY=chiave-generata-sicura
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

3. **Disabilita Debug:**

```python
# In run.py
if __name__ == '__main__':
    app.run(debug=False)
```

### Deploy con Gunicorn

1. **Installa Gunicorn:**

```bash
pip install gunicorn
pip freeze > requirements.txt
```

2. **Esegui con Gunicorn:**

```bash
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

### Deploy su Heroku

```bash
# Crea Procfile
echo "web: gunicorn 'app:create_app()'" > Procfile

# Deploy
heroku create nome-app
git push heroku main
heroku run flask db upgrade
```

### Deploy su PythonAnywhere

1. Upload del codice
2. Crea virtual environment
3. Installa dipendenze: `pip install -r requirements.txt`
4. Configura WSGI file
5. Esegui migrazioni: `flask db upgrade`

### Database in Produzione

**PostgreSQL (consigliato):**

```bash
DATABASE_URL=postgresql://user:password@host:5432/database
```

**MySQL:**

```bash
DATABASE_URL=mysql://user:password@host:3306/database
```

---

## 🔧 Troubleshooting

### Problemi Comuni

**1. Errore: ModuleNotFoundError**

```bash
# Soluzione: attiva il virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**2. Errore: No module named 'flask'**

```bash
# Soluzione: installa le dipendenze
pip install -r requirements.txt
```

**3. Database locked (SQLite)**

```bash
# Soluzione: chiudi altre connessioni o usa PostgreSQL in produzione
```

**4. CSRF token missing**

```python
# Soluzione: aggiungi CSRF token nei form
{{ form.csrf_token }}
```

**5. Template not found**

```python
# Verifica che il template sia in app/templates/
# E che usi render_template('nome_file.html')
```

### Debug

**Attiva modalità debug:**

```python
app.run(debug=True)
```

**Log degli errori:**

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Flask Shell per debug:**

```bash
flask shell
>>> app.config
>>> db
>>> Item.query.all()
```

### Performance

**1. Usa un database reale (PostgreSQL) invece di SQLite**

**2. Configura caching:**

```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=60)
def get_expensive_data():
    ...
```

**3. Ottimizza query database:**

```python
# Evita N+1 queries
items = Item.query.options(joinedload(Item.category)).all()
```

---

## 📚 Risorse Aggiuntive

### Documentazione Ufficiale

* [Flask Documentation](https://flask.palletsprojects.com/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
* [Jinja2 Template Designer](https://jinja.palletsprojects.com/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/)

### Tutorial e Guide

* [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)
* [Flask by Example](https://www.flaskapi.org/)

### Estensioni Utili

* **Flask-Login** : Gestione autenticazione utenti
* **Flask-WTF** : Form validation
* **Flask-Mail** : Invio email
* **Flask-Admin** : Admin panel
* **Flask-CORS** : CORS support per API
* **Flask-JWT-Extended** : JWT authentication

---

## 📝 Best Practices

1. **Usa virtual environment** per ogni progetto
2. **Non committare** `.env`, `venv/`, `*.pyc`, `__pycache__/`
3. **Usa migrazioni** per modifiche al database
4. **Scrivi test** per funzionalità critiche
5. **Usa Blueprint** per organizzare route complesse
6. **Valida input utente** sempre
7. **Gestisci errori** con error handler appropriati
8. **Usa HTTPS** in produzione
9. **Log errori** in produzione
10. **Backup database** regolarmente

---

## 🆘 Supporto

Per problemi o domande:

1. Consulta la [documentazione ufficiale Flask](https://flask.palletsprojects.com/)
2. Cerca su [Stack Overflow](https://stackoverflow.com/questions/tagged/flask)
3. Visita il [GitHub di Flask](https://github.com/pallets/flask)

---

**Versione:** 1.0

**Ultimo aggiornamento:** Ottobre 2025

**Autore:** Flask Setup
