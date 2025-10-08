#!/usr/bin/env python3
"""
Script di setup per inizializzare un progetto Flask completo
con virtual environment, dipendenze e struttura base funzionale.
"""

import os
import sys
import subprocess
import venv
from pathlib import Path


class FlaskSetup:
    def __init__(self, project_name="flask_app"):
        self.project_name = project_name
        self.project_dir = Path.cwd() / project_name
        self.venv_dir = self.project_dir / "venv"
        
    def create_project_structure(self):
        """Crea la struttura delle directory del progetto"""
        print(f"📁 Creazione struttura progetto '{self.project_name}'...")
        
        directories = [
            self.project_dir,
            self.project_dir / "app",
            self.project_dir / "app" / "templates",
            self.project_dir / "app" / "static",
            self.project_dir / "app" / "static" / "css",
            self.project_dir / "app" / "static" / "js",
            self.project_dir / "tests",
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            
        print("✅ Struttura creata con successo")
        
    def create_venv(self):
        """Crea il virtual environment"""
        print(f"🐍 Creazione virtual environment in {self.venv_dir}...")
        venv.create(self.venv_dir, with_pip=True)
        print("✅ Virtual environment creato")
        
    def get_pip_executable(self):
        """Ottiene il path dell'eseguibile pip nel venv"""
        if sys.platform == "win32":
            return self.venv_dir / "Scripts" / "pip.exe"
        return self.venv_dir / "bin" / "pip"
    
    def get_python_executable(self):
        """Ottiene il path dell'eseguibile python nel venv"""
        if sys.platform == "win32":
            return self.venv_dir / "Scripts" / "python.exe"
        return self.venv_dir / "bin" / "python"
        
    def install_dependencies(self):
        """Installa le dipendenze Flask"""
        print("📦 Installazione dipendenze...")
        
        pip_exe = self.get_pip_executable()
        
        dependencies = [
            "flask",
            "python-dotenv",
            "flask-sqlalchemy",
            "flask-migrate",
            "flask-wtf",
            "pytest",
            "pytest-flask",
        ]
        
        subprocess.run(
            [str(pip_exe), "install", "--upgrade", "pip"],
            check=True
        )
        
        subprocess.run(
            [str(pip_exe), "install"] + dependencies,
            check=True
        )
        
        # Crea requirements.txt
        subprocess.run(
            [str(pip_exe), "freeze"],
            stdout=open(self.project_dir / "requirements.txt", "w"),
            check=True
        )
        
        print("✅ Dipendenze installate")
        
    def create_app_files(self):
        """Crea i file base dell'applicazione Flask"""
        print("📝 Creazione file applicazione...")
        
        # __init__.py dell'app
        init_content = '''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app import routes, models
    app.register_blueprint(routes.bp)
    
    return app
'''
        
        # routes.py
        routes_content = '''from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models import Item

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html', title='Home')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')


@bp.route('/api/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        data = request.get_json()
        item = Item(name=data.get('name'), description=data.get('description'))
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201
    
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


@bp.route('/api/items/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(id):
    item = Item.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        return jsonify(item.to_dict())
    
    return jsonify(item.to_dict())
'''
        
        # models.py
        models_content = '''from datetime import datetime
from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Item {self.name}>'
'''
        
        # config.py
        config_content = '''import os
from pathlib import Path

basedir = Path(__file__).parent


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{basedir / "app.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
        
        # run.py (entry point)
        run_content = '''from app import create_app, db
from app.models import Item

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Item': Item}


if __name__ == '__main__':
    app.run(debug=True)
'''
        
        # .env
        env_content = '''FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
'''
        
        # .gitignore
        gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/
dist/
build/

# Flask
instance/
.webassets-cache
*.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local

# Testing
.pytest_cache/
.coverage
htmlcov/
'''
        
        # Template base
        base_template = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('main.index') }}">Home</a></li>
            <li><a href="{{ url_for('main.about') }}">About</a></li>
        </ul>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 Flask App</p>
    </footer>
    
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
'''
        
        # Template index
        index_template = '''{% extends "base.html" %}

{% block content %}
<h1>Benvenuto in Flask!</h1>
<p>Questa è la pagina principale della tua applicazione Flask.</p>

<h2>Items</h2>
<div id="items-list"></div>

<h3>Aggiungi nuovo item</h3>
<form id="add-item-form">
    <input type="text" id="item-name" placeholder="Nome" required>
    <input type="text" id="item-description" placeholder="Descrizione">
    <button type="submit">Aggiungi</button>
</form>
{% endblock %}
'''
        
        # Template about
        about_template = '''{% extends "base.html" %}

{% block content %}
<h1>About</h1>
<p>Questa è un'applicazione Flask di esempio con:</p>
<ul>
    <li>Routing</li>
    <li>Templates Jinja2</li>
    <li>SQLAlchemy ORM</li>
    <li>REST API</li>
    <li>Static files</li>
</ul>
{% endblock %}
'''
        
        # CSS
        css_content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

nav {
    background: #333;
    color: white;
    padding: 1rem;
    margin-bottom: 2rem;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
}

nav a {
    color: white;
    text-decoration: none;
}

nav a:hover {
    text-decoration: underline;
}

main {
    min-height: 400px;
}

footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #ccc;
    text-align: center;
}

form {
    margin: 1rem 0;
}

input, button {
    margin: 0.5rem;
    padding: 0.5rem;
}

button {
    background: #333;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #555;
}

#items-list {
    margin: 1rem 0;
}

.item {
    padding: 1rem;
    margin: 0.5rem 0;
    border: 1px solid #ddd;
    border-radius: 4px;
}
'''
        
        # JavaScript
        js_content = '''document.addEventListener('DOMContentLoaded', function() {
    loadItems();
    
    const form = document.getElementById('add-item-form');
    if (form) {
        form.addEventListener('submit', addItem);
    }
});

async function loadItems() {
    const itemsList = document.getElementById('items-list');
    if (!itemsList) return;
    
    try {
        const response = await fetch('/api/items');
        const items = await response.json();
        
        itemsList.innerHTML = items.map(item => `
            <div class="item">
                <h3>${item.name}</h3>
                <p>${item.description || 'Nessuna descrizione'}</p>
                <small>Creato: ${new Date(item.created_at).toLocaleString()}</small>
            </div>
        `).join('');
    } catch (error) {
        console.error('Errore nel caricamento degli items:', error);
    }
}

async function addItem(e) {
    e.preventDefault();
    
    const name = document.getElementById('item-name').value;
    const description = document.getElementById('item-description').value;
    
    try {
        const response = await fetch('/api/items', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description })
        });
        
        if (response.ok) {
            document.getElementById('add-item-form').reset();
            loadItems();
        }
    } catch (error) {
        console.error('Errore nell\'aggiunta dell\'item:', error);
    }
}
'''
        
        # Test
        test_content = '''import pytest
from app import create_app, db
from app.models import Item


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_create_item(client):
    response = client.post('/api/items',
                          json={'name': 'Test Item', 'description': 'Test'})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Item'
'''
        
        # README
        readme_content = f'''# {self.project_name}

Progetto Flask generato automaticamente con setup completo.

## Struttura del Progetto

```
{self.project_name}/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── about.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── tests/
│   └── test_app.py
├── venv/
├── config.py
├── run.py
├── .env
├── .gitignore
└── requirements.txt
```

## Setup

Il progetto è già configurato! Per avviare:

### Su Linux/Mac:
```bash
source venv/bin/activate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python run.py
```

### Su Windows:
```cmd
venv\\Scripts\\activate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python run.py
```

## Funzionalità Incluse

- ✅ Routing con Blueprint
- ✅ Template Jinja2
- ✅ SQLAlchemy ORM
- ✅ Flask-Migrate per database migrations
- ✅ REST API completa (CRUD)
- ✅ Static files (CSS/JS)
- ✅ Testing con pytest
- ✅ Environment variables (.env)

## API Endpoints

- `GET /` - Homepage
- `GET /about` - About page
- `GET /api/items` - Lista tutti gli items
- `POST /api/items` - Crea nuovo item
- `GET /api/items/<id>` - Dettaglio item
- `PUT /api/items/<id>` - Aggiorna item
- `DELETE /api/items/<id>` - Elimina item

## Testing

```bash
pytest
```

## Note

L'applicazione usa SQLite per default. Per usare un altro database, 
modifica la variabile DATABASE_URL nel file .env.
'''
        
        # Scrivi tutti i file
        files = {
            self.project_dir / "app" / "__init__.py": init_content,
            self.project_dir / "app" / "routes.py": routes_content,
            self.project_dir / "app" / "models.py": models_content,
            self.project_dir / "config.py": config_content,
            self.project_dir / "run.py": run_content,
            self.project_dir / ".env": env_content,
            self.project_dir / ".gitignore": gitignore_content,
            self.project_dir / "app" / "templates" / "base.html": base_template,
            self.project_dir / "app" / "templates" / "index.html": index_template,
            self.project_dir / "app" / "templates" / "about.html": about_template,
            self.project_dir / "app" / "static" / "css" / "style.css": css_content,
            self.project_dir / "app" / "static" / "js" / "main.js": js_content,
            self.project_dir / "tests" / "test_app.py": test_content,
            self.project_dir / "README.md": readme_content,
        }
        
        for filepath, content in files.items():
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
        print("✅ File applicazione creati")
        
    def run(self):
        """Esegue l'intero processo di setup"""
        print(f"\n🚀 Inizializzazione progetto Flask: {self.project_name}\n")
        
        try:
            self.create_project_structure()
            self.create_venv()
            self.install_dependencies()
            self.create_app_files()
            
            print(f"\n✨ Setup completato con successo! ✨\n")
            print(f"Per iniziare:")
            print(f"  cd {self.project_name}")
            
            if sys.platform == "win32":
                print(f"  venv\\Scripts\\activate")
            else:
                print(f"  source venv/bin/activate")
                
            print(f"  flask db init")
            print(f"  flask db migrate -m 'Initial migration'")
            print(f"  flask db upgrade")
            print(f"  python run.py")
            print(f"\nApri il browser su: http://127.0.0.1:5000\n")
            
        except Exception as e:
            print(f"\n❌ Errore durante il setup: {e}")
            sys.exit(1)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Inizializza un nuovo progetto Flask con venv e dipendenze'
    )
    parser.add_argument(
        'project_name',
        nargs='?',
        default='flask_app',
        help='Nome del progetto (default: flask_app)'
    )
    
    args = parser.parse_args()
    
    setup = FlaskSetup(args.project_name)
    setup.run()


if __name__ == '__main__':
    main()