#!/usr/bin/env python3
"""
Script di Setup Automatico per Progetto PWW (Python Web Workshop)

Setup essenziale di un progetto Django con API REST:
1. Verifica Python 3.8+
2. Crea virtual environment
3. Installa dipendenze
4. Crea progetto Django
5. Crea app API
6. Configura settings e URLs
7. Applica migrazioni

Uso:
    python setup.py
"""

import sys
import subprocess
import platform
from pathlib import Path


class Colors:
    """Colori ANSI per output formattato"""
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_step(message):
    print(f"\n{Colors.OKBLUE}{Colors.BOLD}>>> {message}{Colors.ENDC}")


def print_success(message):
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_warning(message):
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")


def get_python_command():
    """Determina il comando Python corretto"""
    if platform.system() == "Windows":
        return "python"
    else:
        try:
            subprocess.run(["python3", "--version"], capture_output=True, check=True)
            return "python3"
        except:
            return "python"


def check_python_version():
    """Verifica Python 3.8+"""
    print_step("Verifica Python")
    python_cmd = get_python_command()
    
    try:
        result = subprocess.run([python_cmd, "--version"], capture_output=True, text=True, check=True)
        version_string = result.stdout.strip()
        print_success(f"Python: {version_string}")
        
        version = version_string.split()[1]
        major, minor = map(int, version.split('.')[:2])
        
        if major < 3 or (major == 3 and minor < 8):
            print_error(f"Serve Python 3.8+, trovato {major}.{minor}")
            return False
        return True
    except:
        print_error("Python non trovato")
        return False


def create_requirements():
    """Crea requirements.txt"""
    print_step("File requirements.txt")
    
    if Path("requirements.txt").exists():
        print_success("requirements.txt già esistente")
        return True
    
    with open("requirements.txt", "w") as f:
        f.write("Django==5.0.1\ndjangorestframework==3.14.0\n")
    
    print_success("requirements.txt creato")
    return True


def create_venv():
    """Crea virtual environment"""
    print_step("Virtual environment")
    
    if Path("venv_pww").exists():
        print_success("venv_pww già esistente")
        return True
    
    python_cmd = get_python_command()
    
    try:
        subprocess.run([python_cmd, "-m", "venv", "venv_pww"], check=True)
        print_success("venv_pww creato")
        return True
    except:
        print_error("Errore creazione venv")
        return False


def get_venv_pip():
    """Path pip nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "pip.exe")
    return str(Path("venv_pww") / "bin" / "pip")


def get_venv_python():
    """Path python nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "python.exe")
    return str(Path("venv_pww") / "bin" / "python")


def get_django_admin():
    """Path django-admin nel venv"""
    if platform.system() == "Windows":
        return str(Path("venv_pww") / "Scripts" / "django-admin.exe")
    return str(Path("venv_pww") / "bin" / "django-admin")


def install_requirements():
    """Installa dipendenze"""
    print_step("Installazione dipendenze")
    
    pip_cmd = get_venv_pip()
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print_success("Dipendenze installate")
        return True
    except:
        print_error("Errore installazione")
        return False


def create_django_project():
    """Crea progetto Django"""
    print_step("Progetto Django")
    
    if Path("manage.py").exists():
        print_success("Progetto già esistente")
        # Verifica che la cartella del progetto esista
        project_folder = find_project_folder()
        if project_folder:
            print_success(f"Trovata cartella progetto: {project_folder}")
            return True
        else:
            print_warning("manage.py esiste ma cartella progetto non trovata")
            print_warning("Ricreo il progetto...")
    
    django_admin_cmd = get_django_admin()
    
    try:
        # Crea il progetto nella cartella corrente
        subprocess.run([django_admin_cmd, "startproject", "pww", "."], check=True, capture_output=True)
        print_success("Progetto 'pww' creato")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Errore creazione progetto: {e.stderr.decode() if e.stderr else str(e)}")
        return False
    except Exception as e:
        print_error(f"Errore: {e}")
        return False


def create_api_app():
    """Crea app API"""
    print_step("App API")
    
    if Path("api").exists():
        print_success("App API già esistente")
        # Verifica che i file base esistano
        if (Path("api") / "__init__.py").exists():
            return True
        else:
            print_warning("Cartella api/ esiste ma è incompleta")
            print_warning("Ricreo l'app...")
            import shutil
            shutil.rmtree(Path("api"))
    
    python_cmd = get_venv_python()
    
    try:
        subprocess.run([python_cmd, "manage.py", "startapp", "api"], check=True, capture_output=True)
        print_success("App API creata")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Errore creazione app: {e.stderr.decode() if e.stderr else str(e)}")
        return False
    except Exception as e:
        print_error(f"Errore: {e}")
        return False


def configure_api():
    """Configura views e URLs dell'API"""
    print_step("Configurazione API")
    
    # Views con GET e POST
    views_content = """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def hello_world(request):
    \"\"\"Endpoint GET /api/hello/\"\"\"
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def hello_post(request):
    \"\"\"Endpoint POST /api/helloPost/\"\"\"
    data = {
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)
"""
    with open(Path("api") / "views.py", "w") as f:
        f.write(views_content)
    
    # URLs con entrambi gli endpoint
    urls_content = """from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('helloPost/', views.hello_post, name='hello_post'),
]
"""
    with open(Path("api") / "urls.py", "w") as f:
        f.write(urls_content)
    
    print_success("API configurata (GET /api/hello/, POST /api/helloPost/)")
    return True


def find_project_folder():
    """Trova la cartella del progetto Django"""
    # Cerca la cartella che contiene settings.py
    for item in Path(".").iterdir():
        if item.is_dir() and (item / "settings.py").exists():
            return item.name
    return None


def update_settings():
    """Aggiorna settings.py"""
    print_step("Aggiornamento settings")
    
    # Trova la cartella del progetto
    project_folder = find_project_folder()
    if not project_folder:
        print_error("Cartella progetto non trovata")
        return False
    
    settings_path = Path(project_folder) / "settings.py"
    
    with open(settings_path, "r") as f:
        content = f.read()
    
    # Aggiungi apps se non presenti
    if "'rest_framework'" not in content:
        content = content.replace(
            "'django.contrib.staticfiles',",
            "'django.contrib.staticfiles',\n    'rest_framework',\n    'api',"
        )
        print_success("Apps aggiunte a INSTALLED_APPS")
    
    # Disabilita CSRF per API (solo per sviluppo)
    if "REST_FRAMEWORK" not in content:
        content += """\n
# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
"""
        print_success("Configurazione DRF aggiunta")
    
    with open(settings_path, "w") as f:
        f.write(content)
    
    return True


def update_urls():
    """Aggiorna urls.py principale"""
    print_step("Aggiornamento URLs")
    
    # Trova la cartella del progetto
    project_folder = find_project_folder()
    if not project_folder:
        print_error("Cartella progetto non trovata")
        return False
    
    urls_path = Path(project_folder) / "urls.py"
    
    urls_content = """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
"""
    
    with open(urls_path, "w") as f:
        f.write(urls_content)
    
    print_success("URLs configurati")
    return True


def apply_migrations():
    """Applica migrazioni"""
    print_step("Migrazioni database")
    
    python_cmd = get_venv_python()
    
    try:
        subprocess.run([python_cmd, "manage.py", "migrate"], check=True, capture_output=True)
        print_success("Migrazioni applicate")
        return True
    except:
        print_error("Errore migrazioni")
        return False


def start_server():
    """Avvia server Django"""
    print_step("Avvio server")
    
    python_cmd = get_venv_python()
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}Server disponibile su: http://127.0.0.1:8000/{Colors.ENDC}")
    print(f"{Colors.OKGREEN}API GET:  http://127.0.0.1:8000/api/hello/{Colors.ENDC}")
    print(f"{Colors.OKGREEN}API POST: http://127.0.0.1:8000/api/helloPost/{Colors.ENDC}")
    print(f"{Colors.WARNING}Per fermare: CTRL+C{Colors.ENDC}\n")
    
    try:
        subprocess.run([python_cmd, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print(f"\n{Colors.OKGREEN}Server fermato{Colors.ENDC}")


def main():
    """Funzione principale"""
    print(f"\n{Colors.BOLD}=== SETUP PWW ==={Colors.ENDC}\n")
    
    # Verifica Python
    if not check_python_version():
        sys.exit(1)
    
    # Crea requirements.txt
    if not create_requirements():
        sys.exit(1)
    
    # Crea venv
    if not create_venv():
        sys.exit(1)
    
    # Installa dipendenze
    if not install_requirements():
        sys.exit(1)
    
    # Crea progetto
    if not create_django_project():
        sys.exit(1)
    
    # Crea app
    if not create_api_app():
        sys.exit(1)
    
    # Configura API
    configure_api()
    update_settings()
    update_urls()
    
    # Applica migrazioni
    apply_migrations()
    
    # Riepilogo
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}✓ Setup completato!{Colors.ENDC}\n")
    print("Struttura:")
    print("  📁 venv_pww/  - Virtual environment")
    print("  📁 pww/       - Progetto Django")
    print("  📁 api/       - App API")
    print("  📄 manage.py")
    print("  📄 db.sqlite3")
    
    # Chiedi se avviare
    response = input(f"\n{Colors.BOLD}Avviare server? (s/n): {Colors.ENDC}").lower()
    
    if response == 's':
        start_server()
    else:
        print(f"\n{Colors.OKGREEN}Per avviare:{Colors.ENDC}")
        if platform.system() == "Windows":
            print("  venv_pww\\Scripts\\activate")
        else:
            print("  source venv_pww/bin/activate")
        print("  python manage.py runserver\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Setup interrotto{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Errore: {e}")
        sys.exit(1)