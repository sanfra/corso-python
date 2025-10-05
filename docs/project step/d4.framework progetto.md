# 🐍 Corso Python – Giorno 4

## Lezione 4: Framework Web e Progetto Finale

### 🎯 Obiettivi della lezione

- Capire differenze e casi d’uso tra Django, Flask e FastAPI
- Sviluppare una semplice applicazione web full stack
- Collegare un database (SQLite o PostgreSQL)
- Effettuare test e debugging di base

---

## 1. Panoramica Framework Web

| Framework         | Tipo               | Caratteristiche principali                     |
| ----------------- | ------------------ | ---------------------------------------------- |
| **Flask**   | Microframework     | Leggero, flessibile, adatto a progetti piccoli |
| **Django**  | Framework completo | Include ORM, autenticazione, admin panel       |
| **FastAPI** | Moderno e veloce   | Ideale per API REST e microservizi             |

---

## 2. Setup app Flask o FastAPI

### Flask

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []  # lista per memorizzare i task

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    task = request.json.get("task")
    todos.append(task)
    return jsonify({"message": "Task aggiunto!"})

if __name__ == "__main__":
    app.run(debug=True)
```

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Benvenuto in FastAPI"}
```

Avvio:

```bash
uvicorn app:app --reload
```

---

## 3. Connessione a un Database (SQLite)

```python
import sqlite3

conn = sqlite3.connect("database.db")     # crea/connette il db
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT)")
cur.execute("INSERT INTO todo (task) VALUES (?)", ("Studiare Python",))
conn.commit()

for row in cur.execute("SELECT * FROM todo"):
    print(row)

conn.close()
```

---

## 4. Progetto finale: App ToDo

**Obiettivo:** creare una piccola app con Flask che permetta di aggiungere, visualizzare e cancellare attività.

Funzionalità:

1. Pagina HTML per visualizzare i task
2. Endpoint Flask per gestire CRUD
3. Salvataggio su SQLite
4. Test con Postman o browser

---

## 5. Test e Debugging

```python
import unittest

class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(2 + 3, 5)

if __name__ == "__main__":
    unittest.main()
```

Debugging:

```python
import pdb; pdb.set_trace()  # ferma l'esecuzione per analizzare variabili
```

---

## 6. Conclusione e approfondimenti

- Approfondire OOP e design pattern
- Imparare a usare Git e GitHub
- Studiare framework Django e FastAPI in modo completo
- Esplorare database relazionali con SQLAlchemy

---

**Fine Lezione 4 – Framework web e progetto finale**
