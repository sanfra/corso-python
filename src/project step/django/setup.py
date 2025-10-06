#!/usr/bin/env python3
"""
Script di Setup Automatico per Progetto PWW (Python Web Workshop)

Questo script automatizza:
1. Creazione del virtual environment
2. Installazione delle dipendenze da requirements.txt
3. Creazione del progetto Django (se non esiste)
4. Creazione dell'app API (se non esiste)
5. Configurazione del progetto
6. Applicazione delle migrazioni Django
7. Avvio del server di sviluppo

Uso:
    python setup.py
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


class Colors:
    """Colori ANSI per output colorato nel terminale"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_step(message):
    """Stampa un messaggio di step con formattazione"""
    print(f"\n{Colors.OKBLUE}{Colors.BOLD}>>> {message}{Colors.ENDC}")


def print_success(message):
    """Stampa un messaggio di successo"""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    """Stampa un messaggio di errore"""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_warning(message):
    """Stampa un messaggio di warning"""
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")


def get_python_command():
    """Determina il comando Python corretto per il sistema"""
    if platform.system() == "Windows":
        return "python"
    else:
        # Su macOS/Linux prova prima python3, poi python
        try:
            subprocess.run(["python3", "--version"], 
                         capture_output=True, check=True)
            return "python3"
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "python"


def check_python_version():
    """Verifica che Python sia installato e sia versione 3.8+"""
    print_step("Verifica versione Python")
    
    python_cmd = get_python_command()
    
    try:
        result = subprocess.run(
            [python_cmd, "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        version_string = result.stdout.strip()
        print_success(f"Python trovato: {version_string}")
        
        # Estrai versione
        version = version_string.split()[1]
        major, minor = map(int, version.split('.')[:2])
        
        if major < 3 or (major == 3 and minor < 8):
            print_error(f"Python {major}.{minor} trovato, ma serve Python 3.8+")
            return False
        
        return True
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Python non trovato! Installa Python 3.8+ prima di continuare")
        return False


def create_requirements_if_missing():
    """Crea requirements.txt se non esiste"""
    print_step("Verifica file requirements.txt")
    
    if not Path("requirements.txt").exists():
        print_warning("File requirements.txt non trovato, lo creo...")
        
        requirements_content = """Django==5.0.1
djangorestframework==3.14.0
"""
        
        with open("requirements.txt", "w") as f:
            f.write(requirements_content)
        
        print_success("File requirements.txt creato")
    else:
        print_success("File requirements.txt trovato")
    
    return True


def create_virtual_environment():
    """Crea il virtual environment"""
    print_step("Creazione virtual environment 'venv_pww'")
    
    venv_path = Path("venv_pww")
    
    # Controlla se esiste già
    if venv_path.exists():
        print_warning("Virtual environment 'venv_pww' già esistente")
        response = input("Vuoi ricrearlo? (s/n): ").lower()
        
        if response == 's':
            print("Eliminazione vecchio virtual environment...")
            import shutil
            shutil.rmtree(venv_path)
        else:
            print_success("Uso virtual environment esistente")
            return True
    
    # Crea il virtual environment
    python_cmd = get_python_command()
    
    try:
        subprocess.run(
            [python_cmd, "-m", "venv", "venv_pww"],
            check=True
        )
        print_success("Virtual environment creato con successo")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Errore nella creazione del virtual environment: {e}")
        return False


def get_pip_command():
    """Restituisce il path completo del comando pip nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "pip.exe")
    else:
        return str(Path("venv_pww") / "bin" / "pip")


def get_python_venv_command():
    """Restituisce il path completo del comando python nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "python.exe")
    else:
        return str(Path("venv_pww") / "bin" / "python")


def get_django_admin_command():
    """Restituisce il path completo del comando django-admin nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "django-admin.exe")
    else:
        return str(Path("venv_pww") / "bin" / "django-admin")


def upgrade_pip():
    """Aggiorna pip all'ultima versione"""
    print_step("Aggiornamento pip")
    
    pip_cmd = get_pip_command()
    
    try:
        subprocess.run(
            [pip_cmd, "install", "--upgrade", "pip"],
            check=True,
            capture_output=True
        )
        print_success("pip aggiornato con successo")
        return True
        
    except subprocess.CalledProcessError as e:
        print_warning(f"Impossibile aggiornare pip: {e}")
        print_warning("Continuo comunque...")
        return True


def install_requirements():
    """Installa le dipendenze da requirements.txt"""
    print_step("Installazione dipendenze da requirements.txt")
    
    pip_cmd = get_pip_command()
    
    try:
        # Esegui pip install mostrando l'output in tempo reale
        process = subprocess.Popen(
            [pip_cmd, "install", "-r", "requirements.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        # Mostra output in tempo reale
        for line in process.stdout:
            print(f"  {line.strip()}")
        
        process.wait()
        
        if process.returncode == 0:
            print_success("Dipendenze installate con successo")
            return True
        else:
            print_error("Errore nell'installazione delle dipendenze")
            return False
            
    except Exception as e:
        print_error(f"Errore: {e}")
        return False


def create_django_project():
    """Crea il progetto Django se non esiste"""
    print_step("Verifica/Creazione progetto Django")
    
    if Path("manage.py").exists():
        print_success("Progetto Django già esistente")
        return True
    
    print_warning("Progetto Django non trovato, lo creo...")
    
    django_admin_cmd = get_django_admin_command()
    
    try:
        subprocess.run(
            [django_admin_cmd, "startproject", "pww", "."],
            check=True
        )
        print_success("Progetto Django 'pww' creato con successo")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Errore nella creazione del progetto: {e}")
        return False


def create_api_app():
    """Crea l'app API se non esiste"""
    print_step("Verifica/Creazione app API")
    
    if Path("api").exists():
        print_success("App API già esistente")
        return True
    
    print_warning("App API non trovata, la creo...")
    
    python_cmd = get_python_venv_command()
    
    try:
        subprocess.run(
            [python_cmd, "manage.py", "startapp", "api"],
            check=True
        )
        print_success("App API creata con successo")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Errore nella creazione dell'app: {e}")
        return False


def create_api_views():
    """Crea il file views.py per l'API"""
    print_step("Configurazione views API")
    
    views_content = """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def hello_world(request):
    \"\"\"
    API endpoint semplice che risponde con un messaggio
    \"\"\"
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)
"""
    
    views_path = Path("api") / "views.py"
    
    with open(views_path, "w") as f:
        f.write(views_content)
    
    print_success("File views.py configurato")
    return True


def create_api_urls():
    """Crea il file urls.py per l'API"""
    print_step("Configurazione URLs API")
    
    urls_content = """from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]
"""
    
    urls_path = Path("api") / "urls.py"
    
    with open(urls_path, "w") as f:
        f.write(urls_content)
    
    print_success("File urls.py configurato")
    return True


def create_middleware():
    """Crea il middleware per il logging"""
    print_step("Configurazione middleware per logging")
    
    middleware_content = """import logging

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:
    \"\"\"
    Middleware che logga ogni request in arrivo
    \"\"\"
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
"""
    
    middleware_path = Path("api") / "middleware.py"
    
    with open(middleware_path, "w") as f:
        f.write(middleware_content)
    
    print_success("Middleware creato")
    return True


def update_settings():
    """Aggiorna il file settings.py"""
    print_step("Configurazione settings.py")
    
    settings_path = Path("pww") / "settings.py"
    
    if not settings_path.exists():
        print_error("File settings.py non trovato!")
        return False
    
    with open(settings_path, "r") as f:
        settings_content = f.read()
    
    # Aggiungi le app se non ci sono già
    if "'rest_framework'" not in settings_content:
        settings_content = settings_content.replace(
            "'django.contrib.staticfiles',",
            "'django.contrib.staticfiles',\n    'rest_framework',\n    'api',"
        )
        print_success("App 'rest_framework' e 'api' aggiunte a INSTALLED_APPS")
    
    # Aggiungi il middleware se non c'è già
    if "'api.middleware.RequestLoggerMiddleware'" not in settings_content:
        settings_content = settings_content.replace(
            "'django.middleware.clickjacking.XFrameOptionsMiddleware',",
            "'django.middleware.clickjacking.XFrameOptionsMiddleware',\n    'api.middleware.RequestLoggerMiddleware',"
        )
        print_success("Middleware aggiunto a MIDDLEWARE")
    
    # Salva il file modificato
    with open(settings_path, "w") as f:
        f.write(settings_content)
    
    return True


def update_main_urls():
    """Aggiorna il file urls.py principale"""
    print_step("Configurazione URLs principale")
    
    urls_path = Path("pww") / "urls.py"
    
    if not urls_path.exists():
        print_error("File urls.py non trovato!")
        return False
    
    urls_content = """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
"""
    
    with open(urls_path, "w") as f:
        f.write(urls_content)
    
    print_success("URLs principale configurato")
    return True


def create_gitignore():
    """Crea il file .gitignore"""
    print_step("Creazione file .gitignore")
    
    if Path(".gitignore").exists():
        print_success("File .gitignore già esistente")
        return True
    
    gitignore_content = """# Virtual Environment
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
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print_success("File .gitignore creato")
    return True


def apply_migrations():
    """Applica le migrazioni Django"""
    print_step("Applicazione migrazioni Django")
    
    python_cmd = get_python_venv_command()
    
    try:
        result = subprocess.run(
            [python_cmd, "manage.py", "migrate"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Mostra output
        print(result.stdout)
        
        print_success("Migrazioni applicate con successo")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Errore nell'applicazione delle migrazioni: {e}")
        print(e.stdout)
        print(e.stderr)
        return False


def start_server():
    """Avvia il server Django"""
    print_step("Avvio server Django")
    
    python_cmd = get_python_venv_command()
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}")
    print("=" * 60)
    print("  SERVER DJANGO AVVIATO CON SUCCESSO!")
    print("=" * 60)
    print(f"{Colors.ENDC}")
    print(f"\n{Colors.OKCYAN}🌐 Server disponibile su: http://127.0.0.1:8000/{Colors.ENDC}")
    print(f"{Colors.OKCYAN}🔗 API endpoint: http://127.0.0.1:8000/api/hello/{Colors.ENDC}")
    print(f"\n{Colors.WARNING}⚠  Per fermare il server premi CTRL+C{Colors.ENDC}\n")
    
    try:
        # Avvia il server (questo blocca l'esecuzione)
        subprocess.run(
            [python_cmd, "manage.py", "runserver"],
            check=True
        )
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.OKGREEN}Server fermato correttamente{Colors.ENDC}")
        
    except subprocess.CalledProcessError as e:
        print_error(f"Errore nell'avvio del server: {e}")


def get_venv_activation_command():
    """Restituisce il comando per attivare il virtual environment"""
    if platform.system() == "Windows":
        return "venv_pww\\Scripts\\activate"
    else:
        return "source venv_pww/bin/activate"


def print_manual_activation():
    """Stampa le istruzioni per attivare manualmente il venv"""
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}Per attivare manualmente il virtual environment:{Colors.ENDC}")
    activation_cmd = get_venv_activation_command()
    print(f"{Colors.BOLD}{activation_cmd}{Colors.ENDC}\n")


def main():
    """Funzione principale"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("=" * 60)
    print("  SETUP AUTOMATICO PROGETTO PWW")
    print("  Python Web Workshop")
    print("=" * 60)
    print(f"{Colors.ENDC}\n")
    
    # Step 1: Verifica Python
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Crea requirements.txt se manca
    if not create_requirements_if_missing():
        sys.exit(1)
    
    # Step 3: Crea virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Step 4: Aggiorna pip
    if not upgrade_pip():
        print_warning("Continuo senza aggiornare pip...")
    
    # Step 5: Installa dipendenze
    if not install_requirements():
        sys.exit(1)
    
    # Step 6: Crea progetto Django
    if not create_django_project():
        sys.exit(1)
    
    # Step 7: Crea app API
    if not create_api_app():
        sys.exit(1)
    
    # Step 8: Configura i file dell'API
    create_api_views()
    create_api_urls()
    create_middleware()
    
    # Step 9: Aggiorna settings e urls
    update_settings()
    update_main_urls()
    
    # Step 10: Crea .gitignore
    create_gitignore()
    
    # Step 11: Applica migrazioni
    if not apply_migrations():
        print_warning("Migrazioni non applicate, ma continuo...")
    
    # Step 12: Mostra info su attivazione manuale
    print_manual_activation()
    
    # Step 13: Riepilogo
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}✓ Setup completato con successo!{Colors.ENDC}\n")
    print("Struttura progetto creata:")
    print("  📁 pww/          - Configurazione Django")
    print("  📁 api/          - App API REST")
    print("  📄 manage.py     - Script di gestione")
    print("  📄 requirements.txt")
    print("  📄 .gitignore")
    
    # Step 14: Chiedi se avviare il server
    print(f"\n{Colors.BOLD}Vuoi avviare il server Django ora? (s/n): {Colors.ENDC}", end="")
    response = input().lower()
    
    if response == 's':
        start_server()
    else:
        print(f"\n{Colors.OKGREEN}Setup completato!{Colors.ENDC}")
        print(f"\nPer avviare il server manualmente:")
        print(f"1. Attiva il virtual environment: {Colors.BOLD}{get_venv_activation_command()}{Colors.ENDC}")
        print(f"2. Avvia il server: {Colors.BOLD}python manage.py runserver{Colors.ENDC}")
        print(f"3. Visita: {Colors.BOLD}http://127.0.0.1:8000/api/hello/{Colors.ENDC}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Setup interrotto dall'utente{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Errore inaspettato: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)s