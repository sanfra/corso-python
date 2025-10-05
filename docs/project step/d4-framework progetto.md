# 🐍 Corso Python – Giorno 4

## Lezione 4: Framework Web e Progetto Finale

### 🎯 Obiettivi della lezione

* Comprendere differenze e casi d'uso tra Django, Flask e FastAPI
* Sviluppare un'applicazione web full-stack completa
* Integrare database (SQLite e PostgreSQL) con ORM
* Implementare autenticazione e autorizzazione
* Effettuare test e debugging professionali
* Deployare l'applicazione (cenni)
* Completare un progetto finale funzionante

---

## 1. Panoramica Framework Web Python

Python offre diversi framework web, ognuno con caratteristiche specifiche.

### 1.1 Confronto Framework

| Framework         | Tipo           | Curva Apprendimento | Performance           | Caso d'uso ideale                |
| ----------------- | -------------- | ------------------- | --------------------- | -------------------------------- |
| **Flask**   | Microframework | ⭐⭐ Facile         | ⭐⭐⭐ Buona          | Piccoli progetti, prototipi, API |
| **Django**  | Full-stack     | ⭐⭐⭐⭐ Complessa  | ⭐⭐⭐ Buona          | Applicazioni enterprise, CMS     |
| **FastAPI** | Moderno/Async  | ⭐⭐⭐ Media        | ⭐⭐⭐⭐⭐ Eccellente | API moderne, microservizi        |

### 1.2 Flask - Microframework

**Vantaggi:**

* ✅ Semplice e minimalista
* ✅ Flessibile (aggiungi solo ciò che serve)
* ✅ Eccellente documentazione
* ✅ Grande ecosistema di estensioni
* ✅ Ideale per imparare i concetti web

**Svantaggi:**

* ❌ Devi configurare tutto manualmente
* ❌ No ORM integrato (usa SQLAlchemy)
* ❌ No admin panel built-in

**Quando usare Flask:**

* Progetti piccoli/medi
* API REST semplici
* Prototipi rapidi
* Quando vuoi controllo totale

### 1.3 Django - Framework Full-Stack

**Vantaggi:**

* ✅ "Batteries included" (tutto incluso)
* ✅ ORM potente integrato
* ✅ Admin panel automatico
* ✅ Sistema di autenticazione robusto
* ✅ Sicurezza integrata (CSRF, XSS, SQL Injection)
* ✅ Ottimo per progetti grandi

**Svantaggi:**

* ❌ Curva di apprendimento ripida
* ❌ Più "opinionated" (meno flessibile)
* ❌ Overhead per progetti piccoli

**Quando usare Django:**

* Applicazioni enterprise
* CMS, e-commerce
* Progetti con database complessi
* Team grandi

**Esempio base Django:**

```python
# views.py
from django.http import JsonResponse
from django.views import View

class TodoView(View):
    def get(self, request):
        # Logica per ottenere todos
        return JsonResponse({'todos': []})
  
    def post(self, request):
        # Logica per creare todo
        return JsonResponse({'message': 'Todo creato'})

# urls.py
from django.urls import path
from .views import TodoView

urlpatterns = [
    path('api/todos/', TodoView.as_view()),
]
```

### 1.4 FastAPI - Framework Moderno

**Vantaggi:**

* ✅ Molto veloce (basato su Starlette e Pydantic)
* ✅ Validazione automatica con type hints
* ✅ Documentazione automatica (Swagger/OpenAPI)
* ✅ Supporto async/await nativo
* ✅ Moderno e intuitivo

**Svantaggi:**

* ❌ Relativamente nuovo (meno librerie)
* ❌ No template engine integrato
* ❌ Richiede conoscenza async

**Quando usare FastAPI:**

* API REST moderne
* Microservizi
* Applicazioni ad alte prestazioni
* Progetti data-intensive

**Esempio base FastAPI:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    """Modello con validazione automatica"""
    title: str
    completed: bool = False

todos = []

@app.get("/")
async def root():
    """Documentazione automatica generata"""
    return {"message": "Benvenuto in FastAPI"}

@app.post("/todos")
async def create_todo(todo: Todo):
    """Validazione automatica del body"""
    todos.append(todo.dict())
    return {"message": "Todo creato", "todo": todo}

@app.get("/todos")
async def get_todos():
    return {"todos": todos}
```

**Avvio FastAPI:**

```bash
# Installazione
pip install fastapi uvicorn

# Avvio server
uvicorn app:app --reload

# Documentazione automatica disponibile su:
# http://127.0.0.1:8000/docs (Swagger)
# http://127.0.0.1:8000/redoc (ReDoc)
```

### 1.5 Tabella Riepilogativa Dettagliata

| Caratteristica            | Flask                    | Django              | FastAPI             |
| ------------------------- | ------------------------ | ------------------- | ------------------- |
| **Anno rilascio**   | 2010                     | 2005                | 2018                |
| **Tipo**            | Micro                    | Full-stack          | Async Modern        |
| **ORM**             | ❌ (usa SQLAlchemy)      | ✅ Django ORM       | ❌ (usa SQLAlchemy) |
| **Admin Panel**     | ❌                       | ✅                  | ❌                  |
| **Template Engine** | ✅ Jinja2                | ✅ Django Templates | ❌                  |
| **Async**           | ❌ (solo con estensioni) | ✅ (da v3.0)        | ✅ Nativo           |
| **Validazione**     | ❌ Manuale               | ✅ Forms            | ✅ Pydantic         |
| **API Docs**        | ❌                       | ❌                  | ✅ Automatica       |
| **Learning Curve**  | Facile                   | Difficile           | Media               |
| **Performance**     | Buona                    | Buona               | Eccellente          |

---

## 2. Database e ORM

### 2.1 SQLite - Database File-Based

SQLite è perfetto per sviluppo e piccole applicazioni.

**Operazioni base con sqlite3:**

```python
import sqlite3
from datetime import datetime

# Connessione (crea il file se non esiste)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Creare tabella
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Inserire dati
cursor.execute("""
    INSERT INTO todos (title, description)
    VALUES (?, ?)
""", ("Studiare Python", "Completare corso Python"))

# Inserimenti multipli
todos_data = [
    ("Fare esercizi", "Esercizi giorno 4"),
    ("Progetto finale", "Completare app todo"),
]
cursor.executemany("""
    INSERT INTO todos (title, description)
    VALUES (?, ?)
""", todos_data)

# Commit per salvare
conn.commit()

# Query SELECT
cursor.execute("SELECT * FROM todos")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Query con WHERE
cursor.execute("""
    SELECT * FROM todos
    WHERE completed = 0
""")
pending = cursor.fetchall()

# UPDATE
cursor.execute("""
    UPDATE todos
    SET completed = 1
    WHERE id = ?
""", (1,))
conn.commit()

# DELETE
cursor.execute("""
    DELETE FROM todos
    WHERE id = ?
""", (2,))
conn.commit()

# Chiudere connessione
conn.close()
```

**Context manager per gestione automatica:**

```python
import sqlite3

def init_db():
    """Inizializza il database"""
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def add_todo(title, description=""):
    """Aggiunge un todo"""
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)",
            (title, description)
        )
        conn.commit()
        return cursor.lastrowid

def get_all_todos():
    """Ottiene tutti i todos"""
    with sqlite3.connect("database.db") as conn:
        # Row factory per avere risultati come dizionari
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
        return [dict(row) for row in cursor.fetchall()]

def update_todo(todo_id, completed):
    """Aggiorna stato todo"""
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET completed = ? WHERE id = ?",
            (completed, todo_id)
        )
        conn.commit()

def delete_todo(todo_id):
    """Elimina un todo"""
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
```

### 2.2 SQLAlchemy - ORM Potente

**SQLAlchemy** è l'ORM più popolare per Python. Permette di lavorare con database usando classi Python invece di SQL.

**Installazione:**

```bash
pip install sqlalchemy
```

**Modelli con SQLAlchemy:**

```python
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Base per i modelli
Base = declarative_base()

# Definizione modello
class Todo(Base):
    """Modello Todo"""
    __tablename__ = 'todos'
  
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
  
    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}', completed={self.completed})>"
  
    def to_dict(self):
        """Converte in dizionario"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Creare engine (connessione database)
engine = create_engine('sqlite:///todos.db')

# Creare tabelle
Base.metadata.create_all(engine)

# Creare session factory
Session = sessionmaker(bind=engine)
```

**CRUD con SQLAlchemy:**

```python
# CREATE
def create_todo(title, description=""):
    """Crea nuovo todo"""
    session = Session()
    try:
        todo = Todo(title=title, description=description)
        session.add(todo)
        session.commit()
        return todo.to_dict()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# READ
def get_all_todos():
    """Ottieni tutti i todos"""
    session = Session()
    try:
        todos = session.query(Todo).order_by(Todo.created_at.desc()).all()
        return [todo.to_dict() for todo in todos]
    finally:
        session.close()

def get_todo_by_id(todo_id):
    """Ottieni todo specifico"""
    session = Session()
    try:
        todo = session.query(Todo).filter_by(id=todo_id).first()
        return todo.to_dict() if todo else None
    finally:
        session.close()

# UPDATE
def update_todo(todo_id, **kwargs):
    """Aggiorna todo"""
    session = Session()
    try:
        todo = session.query(Todo).filter_by(id=todo_id).first()
        if not todo:
            return None
      
        for key, value in kwargs.items():
            if hasattr(todo, key):
                setattr(todo, key, value)
      
        session.commit()
        return todo.to_dict()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# DELETE
def delete_todo(todo_id):
    """Elimina todo"""
    session = Session()
    try:
        todo = session.query(Todo).filter_by(id=todo_id).first()
        if not todo:
            return False
      
        session.delete(todo)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# QUERY avanzate
def get_completed_todos():
    """Ottieni solo todos completati"""
    session = Session()
    try:
        todos = session.query(Todo).filter_by(completed=True).all()
        return [todo.to_dict() for todo in todos]
    finally:
        session.close()

def search_todos(keyword):
    """Cerca todos per keyword"""
    session = Session()
    try:
        todos = session.query(Todo).filter(
            Todo.title.like(f'%{keyword}%')
        ).all()
        return [todo.to_dict() for todo in todos]
    finally:
        session.close()
```

### 2.3 Flask-SQLAlchemy

**Flask-SQLAlchemy** integra SQLAlchemy con Flask in modo più semplice.

**Installazione:**

```bash
pip install flask-sqlalchemy
```

**Setup:**

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configurazione database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db = SQLAlchemy(app)

# Modello
class Todo(db.Model):
    """Modello Todo"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
  
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

# Creare tabelle
with app.app_context():
    db.create_all()

# Route con database
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return {'todos': [todo.to_dict() for todo in todos]}

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    todo = Todo(
        title=data['title'],
        description=data.get('description', '')
    )
    db.session.add(todo)
    db.session.commit()
    return {'todo': todo.to_dict()}, 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.json
  
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
  
    db.session.commit()
    return {'todo': todo.to_dict()}

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return {'message': 'Todo eliminato'}, 200

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 3. Progetto Finale: Todo App Full-Stack

### 3.1 File: `requirements.txt`

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Werkzeug==3.0.1
python-dotenv==1.0.0
pytest==7.4.3
pytest-flask==1.3.0
```

### 3.2 Installazione e Avvio

```bash
# Creare ambiente virtuale
python -m venv venv

# Attivare ambiente
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Installare dipendenze
pip install -r requirements.txt

# Avviare applicazione
python run.py

# Visitare: http://127.0.0.1:5000
```

---

## 4. Testing e Debugging

### 4.1 Testing con pytest

**Eseguire i test:**

```bash
# Esegui tutti i test
pytest

# Con output verbose
pytest -v

# Con copertura
pip install pytest-cov
pytest --cov=app tests/

# Test specifico
pytest tests/test_app.py::test_create_todo
```

### 4.2 Debugging

**Usando pdb (Python Debugger):**

```python
def problematic_function(data):
    # Inserisci breakpoint
    import pdb; pdb.set_trace()
  
    # Il codice si fermerà qui
    result = process_data(data)
    return result

# Comandi pdb:
# n (next): prossima riga
# s (step): entra nella funzione
# c (continue): continua esecuzione
# p variabile: stampa variabile
# l (list): mostra codice
# q (quit): esci
```

---

## 5. Deployment (Cenni)

### 5.1 WSGI Server con Gunicorn

**Installazione:**

```bash
pip install gunicorn
```

**Avvio con Gunicorn:**

```bash
# Avvio base
gunicorn wsgi:app

# Con workers multipli
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

# Con reload automatico (development)
gunicorn --reload wsgi:app
```

---

## 6. Conclusioni e Prossimi Passi

### 6.1 Riepilogo Corso Completo

**Giorno 1:**

* ✅ Fondamenti Python
* ✅ Variabili, tipi, operatori
* ✅ Strutture di controllo
* ✅ Funzioni

**Giorno 2:**

* ✅ Strutture dati avanzate
* ✅ Manipolazione stringhe
* ✅ File I/O
* ✅ Moduli e pacchetti
* ✅ Virtual environments

**Giorno 3:**

* ✅ Gestione eccezioni
* ✅ OOP avanzato
* ✅ Librerie esterne
* ✅ Flask e API REST

**Giorno 4:**

* ✅ Confronto framework
* ✅ Database e ORM
* ✅ Progetto full-stack
* ✅ Testing e debugging

### 6.2 Cosa Studiare Dopo

**Backend Avanzato:**

* Django completo
* FastAPI async avanzato
* GraphQL con Graphene
* Celery per task asincroni

**Database:**

* PostgreSQL avanzato
* MongoDB (NoSQL)
* SQLAlchemy ORM avanzato

**DevOps:**

* Docker e Docker Compose
* Kubernetes basics
* CI/CD (GitHub Actions)

### 6.3 Risorse Consigliate

**Documentazione:**

* [Flask](https://flask.palletsprojects.com/)
* [Django](https://docs.djangoproject.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://docs.sqlalchemy.org/)

**Tutorial:**

* [Real Python](https://realpython.com/)
* [Full Stack Python](https://www.fullstackpython.com/)

**Community:**

* [r/Python](https://reddit.com/r/Python)
* [r/learnpython](https://reddit.com/r/learnpython)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

## 📝 Note Finali

Eccezionale! Hai completato l'intero corso Python! 🎉

**Hai ora le competenze per:**

* ✅ Sviluppare applicazioni web complete
* ✅ Creare API REST professionali
* ✅ Gestire database relazionali
* ✅ Implementare autenticazione
* ✅ Scrivere test automatizzati

**Buon coding! 🚀**
