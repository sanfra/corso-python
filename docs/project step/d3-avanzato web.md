# 🐍 Corso Python – Giorno 3

## Lezione 3: Programmazione Avanzata e Introduzione al Web

### 🎯 Obiettivi della lezione

* Comprendere e gestire le eccezioni in modo efficace
* Utilizzare la programmazione orientata agli oggetti (classi, ereditarietà, polimorfismo)
* Esplorare librerie esterne fondamentali (requests, pandas, matplotlib)
* Comprendere i concetti base del web (HTTP, API REST)
* Creare un web server con Flask
* Sviluppare API REST semplici

---

## 1. Eccezioni e Gestione Errori

Le **eccezioni** sono eventi che interrompono il normale flusso di esecuzione del programma. Python fornisce meccanismi per gestirle elegantemente.

### 1.1 Try-Except base

```python
# Senza gestione errori (programma si interrompe)
# numero = int("abc")  # ValueError: invalid literal for int()

# Con gestione errori
try:
    # Blocco di codice che potrebbe generare errori
    numero = int(input("Inserisci un numero: "))
    risultato = 10 / numero
    print(f"Risultato: {risultato}")
except ValueError:
    # Gestisce errori di conversione
    print("Errore: devi inserire un numero valido.")
except ZeroDivisionError:
    # Gestisce divisione per zero
    print("Errore: divisione per zero non consentita.")
```

### 1.2 Try-Except-Else-Finally

```python
try:
    # Codice che potrebbe generare errori
    file = open("dati.txt", "r")
    contenuto = file.read()
    numero = int(contenuto)
except FileNotFoundError:
    # Eseguito se il file non esiste
    print("File non trovato!")
except ValueError:
    # Eseguito se la conversione fallisce
    print("Il contenuto del file non è un numero valido!")
else:
    # Eseguito SOLO se non ci sono eccezioni
    print(f"Numero letto correttamente: {numero}")
finally:
    # Eseguito SEMPRE, con o senza eccezioni
    # Utile per pulizia (chiudere file, connessioni, ecc.)
    try:
        file.close()
        print("File chiuso")
    except:
        pass
```

### 1.3 Catturare eccezioni multiple

```python
# Catturare eccezioni diverse con lo stesso handler
try:
    valore = int(input("Numero: "))
    risultato = 100 / valore
except (ValueError, ZeroDivisionError) as e:
    # 'as e' cattura l'oggetto eccezione
    print(f"Errore: {e}")
    print(f"Tipo errore: {type(e).__name__}")

# Catturare qualsiasi eccezione (sconsigliato in produzione)
try:
    # codice pericoloso
    pass
except Exception as e:
    # Exception è la classe base di quasi tutte le eccezioni
    print(f"Errore generico: {e}")
```

### 1.4 Sollevare eccezioni (raise)

```python
def calcola_sconto(prezzo, percentuale):
    """Calcola il prezzo scontato"""
    # Validazione input
    if prezzo < 0:
        # raise solleva un'eccezione
        raise ValueError("Il prezzo non può essere negativo")
    if percentuale < 0 or percentuale > 100:
        raise ValueError("La percentuale deve essere tra 0 e 100")
  
    # Calcolo
    sconto = prezzo * (percentuale / 100)
    return prezzo - sconto

# Uso della funzione
try:
    prezzo_finale = calcola_sconto(100, 150)  # percentuale non valida
except ValueError as e:
    print(f"Errore: {e}")
```

### 1.5 Creare eccezioni personalizzate

```python
# Definire una classe di eccezione personalizzata
class SaldoInsufficienteError(Exception):
    """Eccezione sollevata quando il saldo è insufficiente"""
    pass

class ContoBancario:
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale
  
    def preleva(self, importo):
        """Preleva denaro dal conto"""
        if importo > self.saldo:
            # Solleva eccezione personalizzata
            raise SaldoInsufficienteError(
                f"Saldo insufficiente. Disponibile: €{self.saldo}, Richiesto: €{importo}"
            )
        self.saldo -= importo
        return self.saldo

# Uso
conto = ContoBancario(100)

try:
    conto.preleva(150)
except SaldoInsufficienteError as e:
    print(f"Operazione negata: {e}")
```

### 1.6 Gerarchia delle eccezioni

```python
"""
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError
      └── ...
"""

# Catturare dall'eccezione più specifica alla più generica
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    # Più specifica: gestisce solo IndexError
    print("Indice fuori range")
except LookupError:
    # Meno specifica: gestisce IndexError, KeyError, ecc.
    print("Errore di ricerca")
except Exception:
    # Generale: cattura quasi tutto
    print("Errore generico")
```

### 1.7 Context manager e with statement

```python
# Il 'with' gestisce automaticamente le eccezioni e la pulizia
with open("file.txt", "r") as f:
    contenuto = f.read()
# Il file viene chiuso automaticamente, anche se ci sono errori

# Equivalente senza 'with' (più verboso)
f = None
try:
    f = open("file.txt", "r")
    contenuto = f.read()
except Exception as e:
    print(f"Errore: {e}")
finally:
    if f:
        f.close()
```

### 1.8 Best practices gestione errori

```python
# ✅ BUONA PRATICA: essere specifici
try:
    numero = int(input("Numero: "))
except ValueError:
    print("Input non valido")

# ❌ CATTIVA PRATICA: catturare tutto
try:
    numero = int(input("Numero: "))
except:  # troppo generico!
    print("Errore")

# ✅ BUONA PRATICA: gestire errori previsti
def dividi(a, b):
    """Divide due numeri"""
    if b == 0:
        raise ValueError("Divisione per zero")
    return a / b

# ❌ CATTIVA PRATICA: usare eccezioni per controllo flusso
def trova_elemento(lista, valore):
    try:
        return lista.index(valore)
    except ValueError:
        return -1

# ✅ MEGLIO: controllo esplicito
def trova_elemento(lista, valore):
    if valore in lista:
        return lista.index(valore)
    return -1
```

---

## 2. Programmazione Orientata agli Oggetti (OOP)

La **OOP** organizza il codice in **classi** (blueprint) e **oggetti** (istanze).

### 2.1 Classi base

```python
# Definizione di una classe
class Persona:
    """Rappresenta una persona con nome ed età"""
  
    # Costruttore: chiamato quando si crea un oggetto
    def __init__(self, nome, eta):
        # self rappresenta l'istanza corrente
        # Attributi di istanza
        self.nome = nome
        self.eta = eta
  
    # Metodo di istanza
    def saluta(self):
        """Stampa un saluto"""
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")
  
    def compleanno(self):
        """Incrementa l'età di 1"""
        self.eta += 1
        print(f"Buon compleanno! Ora hai {self.eta} anni.")

# Creare oggetti (istanze)
persona1 = Persona("Luca", 25)
persona2 = Persona("Anna", 30)

# Chiamare metodi
persona1.saluta()  # Ciao, mi chiamo Luca e ho 25 anni.
persona2.saluta()  # Ciao, mi chiamo Anna e ho 30 anni.

# Accedere e modificare attributi
print(persona1.nome)  # Luca
persona1.nome = "Luca Rossi"
print(persona1.nome)  # Luca Rossi

# Chiamare metodo che modifica lo stato
persona1.compleanno()  # Buon compleanno! Ora hai 26 anni.
```

### 2.2 Attributi di classe vs attributi di istanza

```python
class Studente:
    """Rappresenta uno studente"""
  
    # Attributo di classe: condiviso da tutte le istanze
    numero_studenti = 0
  
    def __init__(self, nome, matricola):
        # Attributi di istanza: specifici per ogni oggetto
        self.nome = nome
        self.matricola = matricola
      
        # Incrementa il contatore di classe
        Studente.numero_studenti += 1
  
    @classmethod
    def conta_studenti(cls):
        """Metodo di classe: opera sulla classe, non sull'istanza"""
        # 'cls' rappresenta la classe
        return cls.numero_studenti

# Creare studenti
s1 = Studente("Mario", "12345")
s2 = Studente("Laura", "67890")
s3 = Studente("Giovanni", "11111")

# Attributo di classe condiviso
print(Studente.numero_studenti)  # 3
print(s1.numero_studenti)        # 3 (accessibile anche dalle istanze)

# Chiamare metodo di classe
print(Studente.conta_studenti())  # 3
```

### 2.3 Metodi speciali (magic methods)

```python
class Punto:
    """Rappresenta un punto nel piano cartesiano"""
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    # __str__: rappresentazione "user-friendly" (usata da print)
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
  
    # __repr__: rappresentazione "tecnica" (usata nella console)
    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"
  
    # __add__: sovraccarico operatore +
    def __add__(self, altro):
        return Punto(self.x + altro.x, self.y + altro.y)
  
    # __eq__: sovraccarico operatore ==
    def __eq__(self, altro):
        return self.x == altro.x and self.y == altro.y
  
    # __len__: definisce len()
    def __len__(self):
        return 2  # un punto ha 2 coordinate
  
    # __getitem__: permette accesso con []
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Indice non valido")

# Uso dei magic methods
p1 = Punto(1, 2)
p2 = Punto(3, 4)

# __str__ chiamato da print()
print(p1)  # Punto(1, 2)

# __add__ per sommare punti
p3 = p1 + p2
print(p3)  # Punto(4, 6)

# __eq__ per confrontare
print(p1 == p2)  # False
print(p1 == Punto(1, 2))  # True

# __len__
print(len(p1))  # 2

# __getitem__
print(p1[0])  # 1
print(p1[1])  # 2
```

### 2.4 Ereditarietà

```python
# Classe base (padre)
class Animale:
    """Classe base per animali"""
  
    def __init__(self, nome):
        self.nome = nome
  
    def mangia(self):
        print(f"{self.nome} sta mangiando")
  
    def dormi(self):
        print(f"{self.nome} sta dormendo")
  
    def verso(self):
        # Metodo generico da sovrascrivere nelle sottoclassi
        print("L'animale fa un verso")

# Classe derivata (figlia)
class Cane(Animale):
    """Cane eredita da Animale"""
  
    def __init__(self, nome, razza):
        # Chiama il costruttore della classe padre
        super().__init__(nome)
        # Aggiunge attributi specifici
        self.razza = razza
  
    # Override: sovrascrive il metodo della classe padre
    def verso(self):
        print(f"{self.nome} fa: Bau Bau!")
  
    # Metodo specifico della classe Cane
    def porta_giornale(self):
        print(f"{self.nome} porta il giornale")

class Gatto(Animale):
    """Gatto eredita da Animale"""
  
    def verso(self):
        print(f"{self.nome} fa: Miao!")
  
    def graffia(self):
        print(f"{self.nome} sta graffiando")

# Creare istanze
cane = Cane("Rex", "Labrador")
gatto = Gatto("Whiskers")

# Metodi ereditati
cane.mangia()   # Rex sta mangiando
gatto.dormi()   # Whiskers sta dormendo

# Metodi sovrascritti (override)
cane.verso()    # Rex fa: Bau Bau!
gatto.verso()   # Whiskers fa: Miao!

# Metodi specifici
cane.porta_giornale()  # Rex porta il giornale
gatto.graffia()        # Whiskers sta graffiando

# Attributi specifici
print(cane.razza)  # Labrador
```

### 2.5 Polimorfismo

```python
# Polimorfismo: oggetti di classi diverse rispondono allo stesso metodo
def fai_parlare(animale):
    """Funzione che accetta qualsiasi animale"""
    # Non importa il tipo: basta che abbia il metodo verso()
    animale.verso()

# Lista di animali diversi
animali = [
    Cane("Fido", "Pastore"),
    Gatto("Micio"),
    Cane("Pluto", "Bulldog"),
    Gatto("Felix")
]

# Polimorfismo in azione
for animale in animali:
    fai_parlare(animale)
# Output:
# Fido fa: Bau Bau!
# Micio fa: Miao!
# Pluto fa: Bau Bau!
# Felix fa: Miao!
```

### 2.6 Incapsulamento e proprietà

```python
class ContoBancario:
    """Conto bancario con incapsulamento"""
  
    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        # Attributo privato (convenzione: prefisso __)
        self.__saldo = saldo_iniziale
  
    # Property: permette accesso controllato all'attributo
    @property
    def saldo(self):
        """Getter: legge il saldo"""
        return self.__saldo
  
    # Setter: permette modifica controllata
    @saldo.setter
    def saldo(self, valore):
        """Setter: imposta il saldo con validazione"""
        if valore < 0:
            raise ValueError("Il saldo non può essere negativo")
        self.__saldo = valore
  
    def deposita(self, importo):
        """Deposita denaro"""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self.__saldo += importo
  
    def preleva(self, importo):
        """Preleva denaro"""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        if importo > self.__saldo:
            raise ValueError("Saldo insufficiente")
        self.__saldo -= importo

# Uso
conto = ContoBancario("Mario Rossi", 1000)

# Accesso tramite property (sembra un attributo normale)
print(conto.saldo)  # 1000

# Non possiamo accedere direttamente a __saldo
# print(conto.__saldo)  # AttributeError

# Modifica tramite metodi
conto.deposita(500)
print(conto.saldo)  # 1500

conto.preleva(200)
print(conto.saldo)  # 1300

# Tentativo di impostare saldo negativo
try:
    conto.saldo = -100
except ValueError as e:
    print(f"Errore: {e}")
```

### 2.7 Ereditarietà multipla

```python
# Classe base 1
class Volante:
    def vola(self):
        return "Sto volando!"

# Classe base 2
class Nuotante:
    def nuota(self):
        return "Sto nuotando!"

# Classe che eredita da entrambe
class Anatra(Volante, Nuotante):
    def __init__(self, nome):
        self.nome = nome
  
    def quack(self):
        return f"{self.nome} fa: Quack!"

# Uso
paperino = Anatra("Paperino")
print(paperino.vola())   # Sto volando!
print(paperino.nuota())  # Sto nuotando!
print(paperino.quack())  # Paperino fa: Quack!
```

---

## 3. Librerie Esterne Fondamentali

Python ha un ecosistema ricchissimo di librerie. Vediamo le più importanti.

### 3.1 requests - HTTP per umani

**Installazione:**

```bash
pip install requests
```

**Uso base:**

```python
import requests

# GET request semplice
response = requests.get("https://api.github.com")

# Verificare il codice di stato HTTP
print(response.status_code)  # 200 = OK, 404 = Not Found, ecc.

# Contenuto della risposta
print(response.text)  # testo grezzo
print(response.json())  # parsing automatico JSON

# Headers della risposta
print(response.headers)
print(response.headers['Content-Type'])

# Controllo errori
if response.status_code == 200:
    print("Richiesta riuscita!")
else:
    print(f"Errore: {response.status_code}")
```

**GET con parametri:**

```python
# API con parametri query string
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc'
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

# URL generato: https://api.github.com/search/repositories?q=python&sort=stars&order=desc

data = response.json()
print(f"Totale repository: {data['total_count']}")
```

**POST request:**

```python
# Inviare dati JSON
data = {
    'nome': 'Mario',
    'email': 'mario@example.com'
}

response = requests.post(
    "https://httpbin.org/post",
    json=data  # converte automaticamente in JSON
)

print(response.json())
```

**Gestione errori:**

```python
try:
    response = requests.get("https://api.example.com/data", timeout=5)
    # raise_for_status() solleva eccezione per codici 4xx/5xx
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Timeout: il server non risponde")
except requests.exceptions.ConnectionError:
    print("Errore di connessione")
except requests.exceptions.HTTPError as e:
    print(f"Errore HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Errore generico: {e}")
```

**Headers personalizzati:**

```python
headers = {
    'User-Agent': 'MiaApp/1.0',
    'Authorization': 'Bearer TOKEN_QUI'
}

response = requests.get(
    "https://api.example.com/protected",
    headers=headers
)
```

### 3.2 pandas - Analisi dati

**Installazione:**

```bash
pip install pandas
```

**Creare DataFrame:**

```python
import pandas as pd

# Da dizionario
dati = {
    'Nome': ['Anna', 'Luca', 'Mario', 'Laura'],
    'Età': [30, 25, 35, 28],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino']
}

df = pd.DataFrame(dati)
print(df)
#     Nome  Età    Città
# 0   Anna   30     Roma
# 1   Luca   25   Milano
# 2  Mario   35   Napoli
# 3  Laura   28   Torino
```

**Operazioni base:**

```python
# Prime/ultime righe
print(df.head(2))  # prime 2 righe
print(df.tail(2))  # ultime 2 righe

# Informazioni sul DataFrame
print(df.info())
print(df.describe())  # statistiche numeriche

# Selezionare colonne
print(df['Nome'])  # singola colonna (Series)
print(df[['Nome', 'Età']])  # multiple colonne (DataFrame)

# Selezionare righe per indice
print(df.loc[0])  # prima riga
print(df.loc[0:2])  # righe 0-2

# Filtrare righe
over_30 = df[df['Età'] > 30]
print(over_30)

roma_milano = df[df['Città'].isin(['Roma', 'Milano'])]
print(roma_milano)

# Aggiungere colonne
df['Adulto'] = df['Età'] >= 18
print(df)

# Ordinare
df_sorted = df.sort_values('Età', ascending=False)
print(df_sorted)
```

**Leggere/scrivere file:**

```python
# Leggere CSV
df = pd.read_csv('dati.csv')

# Leggere Excel
df = pd.read_excel('dati.xlsx')

# Leggere JSON
df = pd.read_json('dati.json')

# Scrivere CSV
df.to_csv('output.csv', index=False)

# Scrivere Excel
df.to_excel('output.xlsx', index=False)
```

**Operazioni aggregate:**

```python
# Raggruppare e aggregare
grouped = df.groupby('Città')['Età'].mean()
print(grouped)

# Multiple aggregazioni
stats = df.groupby('Città').agg({
    'Età': ['mean', 'min', 'max'],
    'Nome': 'count'
})
print(stats)
```

### 3.3 matplotlib - Visualizzazione dati

**Installazione:**

```bash
pip install matplotlib
```

**Grafico lineare:**

```python
import matplotlib.pyplot as plt

# Dati
numeri = [1, 2, 3, 4, 5]
quadrati = [n ** 2 for n in numeri]

# Creare il grafico
plt.plot(numeri, quadrati, marker='o', linestyle='-', color='blue')

# Personalizzazione
plt.title("Numeri e loro quadrati")
plt.xlabel("Numero")
plt.ylabel("Quadrato")
plt.grid(True)

# Mostrare il grafico
plt.show()

# Salvare invece di mostrare
# plt.savefig('grafico.png')
```

**Grafico a barre:**

```python
# Dati
categorie = ['A', 'B', 'C', 'D']
valori = [23, 45, 56, 78]

# Grafico a barre
plt.bar(categorie, valori, color='green')
plt.title("Vendite per categoria")
plt.xlabel("Categoria")
plt.ylabel("Vendite")
plt.show()
```

**Multiple subplot:**

```python
# Creare una griglia 2x2 di grafici
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Grafico 1: linea
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title('Linea')

# Grafico 2: barre
axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15])
axes[0, 1].set_title('Barre')

# Grafico 3: scatter
axes[1, 0].scatter([1, 2, 3, 4], [2, 4, 6, 8])
axes[1, 0].set_title('Scatter')

# Grafico 4: torta
axes[1, 1].pie([30, 20, 50], labels=['X', 'Y', 'Z'], autopct='%1.1f%%')
axes[1, 1].set_title('Torta')

plt.tight_layout()
plt.show()
```

### 3.4 Altre librerie utili

```python
# numpy: calcolo numerico
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array.mean())  # media
print(array.std())   # deviazione standard

# datetime: già visto, ma molto usato
from datetime import datetime, timedelta
ora = datetime.now()
domani = ora + timedelta(days=1)

# collections: strutture dati avanzate
from collections import Counter, defaultdict
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})

# itertools: iteratori avanzati
from itertools import combinations, permutations
print(list(combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]
```

---

## 4. Introduzione a Flask e Web Development

**Flask** è un micro-framework per creare applicazioni web in Python.

### 4.1 Installazione

```bash
pip install flask
```

### 4.2 Hello World con Flask

**File: `app.py`**

```python
# Importare Flask
from flask import Flask

# Creare l'applicazione Flask
# __name__ indica il modulo corrente
app = Flask(__name__)

# Definire una rotta (route)
# @app.route è un decoratore che associa un URL a una funzione
@app.route("/")
def home():
    """Funzione view per la homepage"""
    # La funzione restituisce il contenuto HTML
    return "Benvenuto nel mio server Flask!"

# Punto di ingresso dell'applicazione
if __name__ == "__main__":
    # Avvia il server di sviluppo
    # debug=True ricarica automaticamente il server quando modifichi il codice
    app.run(debug=True)
```

**Eseguire:**

```bash
python app.py
```

**Visitare:** http://127.0.0.1:5000

### 4.3 Route multiple e parametri

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Homepage</h1><p>Benvenuto!</p>"

# Rotta semplice
@app.route("/about")
def about():
    return "<h1>Chi siamo</h1><p>Informazioni sul sito</p>"

# Rotta con parametro
@app.route("/user/<username>")
def show_user(username):
    """Mostra il profilo di un utente"""
    # username viene estratto dall'URL
    return f"<h1>Profilo di {username}</h1>"

# Parametro con tipo
@app.route("/post/<int:post_id>")
def show_post(post_id):
    """Mostra un post specifico"""
    # post_id viene convertito automaticamente in intero
    return f"<h1>Post #{post_id}</h1>"

# Multiple parametri
@app.route("/user/<username>/post/<int:post_id>")
def user_post(username, post_id):
    return f"Post #{post_id} di {username}"

if __name__ == "__main__":
    app.run(debug=True)
```

### 4.4 Metodi HTTP

```python
from flask import Flask, request

app = Flask(__name__)

# GET (default)
@app.route("/search")
def search():
    # Accedere ai parametri query string (?q=python&lang=it)
    query = request.args.get('q', '')  # default ''
    lang = request.args.get('lang', 'en')
    return f"Cerchi: {query} in {lang}"

# POST
@app.route("/login", methods=['POST'])
def login():
    # Accedere ai dati del form
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Login: {username}"

# GET e POST sulla stessa rotta
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Gestire invio form
        name = request.form.get('name')
        message = request.form.get('message')
        return f"Grazie {name}! Messaggio ricevuto: {message}"
    else:
        # Mostrare il form
        return '''
            <form method="post">
                <input type="text" name="name" placeholder="Nome">
                <textarea name="message" placeholder="Messaggio"></textarea>
                <button type="submit">Invia</button>
            </form>
        '''

if __name__ == "__main__":
    app.run(debug=True)
```

### 4.5 Template con Jinja2

Flask include **Jinja2** per creare template HTML dinamici.

**Struttura directory:**

```
progetto/
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    └── user.html
```

**File: `templates/base.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Il mio sito{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">Chi siamo</a>
    </nav>
  
    <main>
        {% block content %}{% endblock %}
    </main>
  
    <footer>
        <p>© 2025 Il mio sito</p>
    </footer>
</body>
</html>
```

**File: `templates/index.html`**

```html
{% extends "base.html" %}

{% block title %}Homepage{% endblock %}

{% block content %}
    <h1>Benvenuto!</h1>
    <p>Questo è il mio sito Flask.</p>
  
    {% if user %}
        <p>Ciao {{ user }}!</p>
    {% else %}
        <p>Benvenuto visitatore!</p>
    {% endif %}
  
    <h2>Lista utenti:</h2>
    <ul>
    {% for nome in utenti %}
        <li>{{ nome }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

**File: `app.py`**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # render_template cerca il file in templates/
    # Passa variabili al template
    return render_template(
        'index.html',
        user='Mario',
        utenti=['Anna', 'Luca', 'Giovanni']
    )

@app.route("/user/<username>")
def user_profile(username):
    # Dizionario con dati utente
    user_data = {
        'username': username,
        'email': f'{username}@example.com',
        'posts': 42
    }
    return render_template('user.html', user=user_data)

if __name__ == "__main__":
    app.run(debug=True)
```

### 4.6 API REST con Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database simulato (in memoria)
tasks = [
    {'id': 1, 'title': 'Studiare Python', 'done': False},
    {'id': 2, 'title': 'Fare esercizi', 'done': True}
]

# GET: ottenere tutte le tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    # jsonify converte Python in JSON
    return jsonify({'tasks': tasks})

# GET: ottenere una task specifica
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Cercare la task per id
    task = next((t for t in tasks if t['id'] == task_id), None)
  
    if task is None:
        # Restituire errore 404
        return jsonify({'error': 'Task non trovata'}), 404
  
    return jsonify({'task': task})

# POST: creare una nuova task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    # Ottenere dati JSON dalla richiesta
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Dati non validi'}), 400
  
    # Creare nuova task
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'done': request.json.get('done', False)
    }
  
    tasks.append(new_task)
  
    # Restituire la task creata con status 201 (Created)
    return jsonify({'task': new_task}), 201

# PUT: aggiornare una task esistente
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
  
    if task is None:
        return jsonify({'error': 'Task non trovata'}), 404
  
    if not request.json:
        return jsonify({'error': 'Dati non validi'}), 400
  
    # Aggiornare campi
    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
  
    return jsonify({'task': task})

# DELETE: eliminare una task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
  
    if task is None:
        return jsonify({'error': 'Task non trovata'}), 404
  
    tasks.remove(task)
  
    # Restituire 204 (No Content)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
```

**Testare l'API con requests:**

```python
import requests

# GET tutte le tasks
response = requests.get('http://localhost:5000/api/tasks')
print(response.json())

# POST: creare nuova task
new_task = {'title': 'Imparare Flask', 'done': False}
response = requests.post('http://localhost:5000/api/tasks', json=new_task)
print(response.json())

# PUT: aggiornare task
updated = {'title': 'Imparare Flask avanzato', 'done': True}
response = requests.put('http://localhost:5000/api/tasks/3', json=updated)
print(response.json())

# DELETE: eliminare task
response = requests.delete('http://localhost:5000/api/tasks/1')
print(response.status_code)  # 204
```

### 4.7 File statici e CSS

**Struttura directory:**

```
progetto/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

**File: `static/css/style.css`**

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
```

**File: `templates/index.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Il mio sito</title>
    <!-- url_for genera l'URL corretto per i file statici -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Benvenuto!</h1>
        <p>Questo è un sito Flask con CSS.</p>
    </div>
  
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

### 4.8 Gestione errori

```python
from flask import Flask, render_template

app = Flask(__name__)

# Handler per errore 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handler per errore 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Esempio di rotta che genera errore
@app.route('/error')
def trigger_error():
    # Questo genererà un errore 500
    1 / 0

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 5. Mini-Esercizi Pratici

### Esercizio 1: Classe Studente completa

```python
"""
Crea una classe Studente con:
- Attributi: nome, corso, lista di voti
- Metodi: aggiungi_voto(), calcola_media(), promosso()
"""

class Studente:
    """Rappresenta uno studente universitario"""
  
    def __init__(self, nome, corso):
        """Inizializza studente con nome e corso"""
        self.nome = nome
        self.corso = corso
        self.voti = []  # lista vuota per i voti
  
    def aggiungi_voto(self, voto):
        """Aggiunge un voto alla lista"""
        # Validazione: voto deve essere tra 18 e 30
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(f"Voto {voto} aggiunto per {self.nome}")
        else:
            raise ValueError("Il voto deve essere tra 18 e 30")
  
    def calcola_media(self):
        """Calcola la media dei voti"""
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)
  
    def promosso(self):
        """Verifica se lo studente è promosso (media >= 18)"""
        return self.calcola_media() >= 18
  
    def __str__(self):
        """Rappresentazione string dello studente"""
        media = self.calcola_media()
        return f"Studente: {self.nome}, Corso: {self.corso}, Media: {media:.2f}"

# Test della classe
studente1 = Studente("Mario Rossi", "Informatica")
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(25)
studente1.aggiungi_voto(30)

print(studente1)
print(f"Promosso: {studente1.promosso()}")

# Test con gestione errori
try:
    studente1.aggiungi_voto(35)  # Voto non valido
except ValueError as e:
    print(f"Errore: {e}")
```

### Esercizio 2: Divisione sicura con gestione errori

```python
"""
Funzione che gestisce la divisione con try/except.
Gestisce: ValueError (input non numerico), ZeroDivisionError
"""

def divisione_sicura():
    """Esegue una divisione gestendo possibili errori"""
    while True:
        try:
            # Input utente
            dividendo = float(input("Inserisci il dividendo: "))
            divisore = float(input("Inserisci il divisore: "))
          
            # Tentativo di divisione
            risultato = dividendo / divisore
          
            # Se arriviamo qui, tutto ok
            print(f"Risultato: {dividendo} / {divisore} = {risultato}")
            break  # Esci dal loop
          
        except ValueError:
            print("Errore: devi inserire un numero valido!")
            print("Riprova...\n")
      
        except ZeroDivisionError:
            print("Errore: impossibile dividere per zero!")
            print("Riprova...\n")
      
        except Exception as e:
            print(f"Errore imprevisto: {e}")
            break

# Esegui la funzione
divisione_sicura()
```

### Esercizio 3: Chiamata a API pubblica

```python
"""
Usa l'API di JSONPlaceholder per ottenere dati.
JSONPlaceholder è un'API fake gratuita per test.
"""

import requests

def ottieni_posts():
    """Recupera posts da JSONPlaceholder"""
    try:
        # API endpoint
        url = "https://jsonplaceholder.typicode.com/posts"
      
        # GET request
        response = requests.get(url, timeout=10)
      
        # Verifica successo
        response.raise_for_status()
      
        # Parsing JSON
        posts = response.json()
      
        # Mostra i primi 5 posts
        print("=== PRIMI 5 POSTS ===")
        for post in posts[:5]:
            print(f"\nID: {post['id']}")
            print(f"Titolo: {post['title']}")
            print(f"Corpo: {post['body'][:50]}...")  # primi 50 caratteri
      
        print(f"\n\nTotale posts: {len(posts)}")
      
    except requests.exceptions.Timeout:
        print("Errore: timeout della richiesta")
    except requests.exceptions.HTTPError as e:
        print(f"Errore HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
    except Exception as e:
        print(f"Errore imprevisto: {e}")

def cerca_post_per_id(post_id):
    """Cerca un post specifico per ID"""
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        response.raise_for_status()
      
        post = response.json()
        print(f"\n=== POST #{post_id} ===")
        print(f"Titolo: {post['title']}")
        print(f"Corpo: {post['body']}")
      
    except Exception as e:
        print(f"Errore: {e}")

# Esegui
ottieni_posts()
cerca_post_per_id(1)
```

### Esercizio 4: Server Flask completo

```python
"""
Crea un server Flask con:
- Homepage
- About page
- API endpoint che restituisce JSON
- Gestione errori 404
"""

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Template HTML semplice
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Il mio sito Flask</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 { color: #2c3e50; }
        nav a {
            margin-right: 15px;
            text-decoration: none;
            color: #3498db;
        }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">Chi siamo</a>
        <a href="/api/info">API Info</a>
    </nav>
  
    <h1>Benvenuto!</h1>
    <p>Questo è un semplice server Flask.</p>
    <p>Visita le altre pagine usando il menu sopra.</p>
</body>
</html>
"""

ABOUT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Chi siamo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <h1>Chi siamo</h1>
    <p>Siamo un team di sviluppatori Python appassionati.</p>
    <a href="/">← Torna alla home</a>
</body>
</html>
"""

@app.route("/")
def home():
    """Homepage"""
    return render_template_string(HOME_TEMPLATE)

@app.route("/about")
def about():
    """Pagina chi siamo"""
    return render_template_string(ABOUT_TEMPLATE)

@app.route("/api/info")
def api_info():
    """Endpoint API che restituisce informazioni in JSON"""
    info = {
        'nome': 'Il mio sito Flask',
        'versione': '1.0.0',
        'autore': 'Mario Rossi',
        'endpoints': [
            {'path': '/', 'descrizione': 'Homepage'},
            {'path': '/about', 'descrizione': 'Chi siamo'},
            {'path': '/api/info', 'descrizione': 'Informazioni API'}
        ]
    }
    return jsonify(info)

@app.route("/api/saluta/<nome>")
def saluta_api(nome):
    """API che saluta un utente"""
    return jsonify({
        'messaggio': f'Ciao {nome}!',
        'timestamp': '2025-10-05T14:30:00'
    })

@app.errorhandler(404)
def page_not_found(e):
    """Gestione errore 404"""
    return """
        <h1>404 - Pagina non trovata</h1>
        <p>La pagina che cerchi non esiste.</p>
        <a href="/">Torna alla home</a>
    """, 404

if __name__ == "__main__":
    print("Server avviato su http://127.0.0.1:5000")
    print("Premi CTRL+C per fermare il server")
    app.run(debug=True)
```

### Esercizio 5: To-Do List API completa

```python
"""
API REST completa per gestire una to-do list.
Include: GET, POST, PUT, DELETE
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Database in memoria
todos = []
next_id = 1

@app.route('/api/todos', methods=['GET'])
def get_all_todos():
    """Ottieni tutte le todo"""
    return jsonify({'todos': todos, 'count': len(todos)})

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Ottieni una todo specifica"""
    todo = next((t for t in todos if t['id'] == todo_id), None)
  
    if todo is None:
        return jsonify({'error': 'Todo non trovata'}), 404
  
    return jsonify({'todo': todo})

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Crea nuova todo"""
    global next_id
  
    # Validazione
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Campo title obbligatorio'}), 400
  
    # Crea todo
    todo = {
        'id': next_id,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
  
    todos.append(todo)
    next_id += 1
  
    return jsonify({'todo': todo, 'message': 'Todo creata'}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Aggiorna una todo"""
    todo = next((t for t in todos if t['id'] == todo_id), None)
  
    if todo is None:
        return jsonify({'error': 'Todo non trovata'}), 404
  
    if not request.json:
        return jsonify({'error': 'Dati non validi'}), 400
  
    # Aggiorna campi
    todo['title'] = request.json.get('title', todo['title'])
    todo['description'] = request.json.get('description', todo['description'])
    todo['completed'] = request.json.get('completed', todo['completed'])
  
    return jsonify({'todo': todo, 'message': 'Todo aggiornata'})

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Elimina una todo"""
    global todos
  
    todo = next((t for t in todos if t['id'] == todo_id), None)
  
    if todo is None:
        return jsonify({'error': 'Todo non trovata'}), 404
  
    todos = [t for t in todos if t['id'] != todo_id]
  
    return jsonify({'message': 'Todo eliminata'}), 200

# Rotta di utilità per resettare
@app.route('/api/todos/reset', methods=['POST'])
def reset_todos():
    """Resetta tutte le todo"""
    global todos, next_id
    todos = []
    next_id = 1
    return jsonify({'message': 'Todo list resettata'})

if __name__ == "__main__":
    print("API Todo List avviata su http://127.0.0.1:5000")
    print("\nEndpoint disponibili:")
    print("  GET    /api/todos           - Lista tutte le todo")
    print("  GET    /api/todos/<id>      - Ottieni todo specifica")
    print("  POST   /api/todos           - Crea nuova todo")
    print("  PUT    /api/todos/<id>      - Aggiorna todo")
    print("  DELETE /api/todos/<id>      - Elimina todo")
    print("  POST   /api/todos/reset     - Resetta lista\n")
  
    app.run(debug=True)
```

**Client per testare l'API:**

```python
import requests

BASE_URL = "http://127.0.0.1:5000/api/todos"

# Creare todo
new_todo = {
    'title': 'Studiare Flask',
    'description': 'Completare il corso Python'
}
response = requests.post(BASE_URL, json=new_todo)
print("Creata:", response.json())

# Ottenere tutte le todo
response = requests.get(BASE_URL)
print("\nTutte le todo:", response.json())

# Aggiornare todo
update_data = {'completed': True}
response = requests.put(f"{BASE_URL}/1", json=update_data)
print("\nAggiornata:", response.json())

# Eliminare todo
response = requests.delete(f"{BASE_URL}/1")
print("\nEliminata:", response.json())
```

---

## 6. Concetti Web Fondamentali

### 6.1 HTTP - HyperText Transfer Protocol

**Metodi HTTP principali:**

* **GET** : Recupera dati (non modifica il server)
* **POST** : Invia dati (crea nuove risorse)
* **PUT** : Aggiorna risorsa esistente
* **DELETE** : Elimina risorsa
* **PATCH** : Aggiorna parzialmente risorsa

**Codici di stato HTTP:**

```python
# 2xx - Successo
200  # OK
201  # Created
204  # No Content

# 3xx - Redirect
301  # Moved Permanently
302  # Found (redirect temporaneo)

# 4xx - Errori client
400  # Bad Request
401  # Unauthorized
403  # Forbidden
404  # Not Found

# 5xx - Errori server
500  # Internal Server Error
503  # Service Unavailable
```

### 6.2 REST API - Principi

**REST** (Representational State Transfer) è uno stile architetturale per API.

**Principi REST:**

1. **Stateless** : ogni richiesta è indipendente
2. **Client-Server** : separazione responsabilità
3. **Uniform Interface** : interfaccia coerente
4. **Risorse** : tutto è una risorsa con URI univoco

**Convenzioni REST:**

```
GET    /api/users          # Lista tutti gli utenti
GET    /api/users/123      # Ottieni utente 123
POST   /api/users          # Crea nuovo utente
PUT    /api/users/123      # Aggiorna utente 123
DELETE /api/users/123      # Elimina utente 123
```

### 6.3 JSON - JavaScript Object Notation

```python
import json

# Python → JSON
dati_python = {
    'nome': 'Mario',
    'eta': 30,
    'attivo': True,
    'skills': ['Python', 'Flask', 'SQL']
}

json_string = json.dumps(dati_python, indent=2)
print(json_string)

# JSON → Python
json_data = '{"nome": "Laura", "eta": 25}'
dati = json.loads(json_data)
print(dati['nome'])  # Laura
```

---

## 7. Riepilogo Giorno 3

### Concetti chiave appresi

✅ **Gestione Eccezioni:**

* try-except-else-finally
* Sollevare eccezioni con raise
* Creare eccezioni personalizzate
* Best practices

✅ **OOP Avanzato:**

* Classi e oggetti
* Ereditarietà e polimorfismo
* Metodi speciali (magic methods)
* Properties e incapsulamento
* Ereditarietà multipla

✅ **Librerie Esterne:**

* **requests** : HTTP per umani
* **pandas** : analisi dati
* **matplotlib** : visualizzazione

✅ **Flask Web Framework:**

* Routing e parametri
* Template Jinja2
* API REST complete
* Gestione errori
* File statici

✅ **Concetti Web:**

* HTTP methods e status codes
* REST API principles
* JSON

---

## 8. Preparazione per il Giorno 4

Nel **Giorno 4** approfondiremo:

* **Framework web avanzati** : Django, FastAPI
* **Database** : SQLite, PostgreSQL, ORM
* **Progetto finale** : app full-stack completa
* **Testing** e **debugging**
* **Deployment** basics

### Compiti per casa (opzionali)

1. Creare una classe complessa con ereditarietà (es. sistema bancario)
2. Sviluppare un'API REST completa per un blog (posts, commenti)
3. Creare un'applicazione Flask con template e CSS
4. Esplorare un'API pubblica e creare un dashboard dei dati
5. Leggere la documentazione Flask: https://flask.palletsprojects.com/

---

## 9. Esercizi Avanzati Bonus

### Bonus 1: Sistema di autenticazione base

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'chiave-segreta-cambiarla-in-produzione'

# Database utenti (in memoria)
users = {}

@app.route('/api/register', methods=['POST'])
def register():
    """Registra nuovo utente"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
  
    if not username or not password:
        return jsonify({'error': 'Username e password obbligatori'}), 400
  
    if username in users:
        return jsonify({'error': 'Username già esistente'}), 400
  
    # Hash della password
    users[username] = generate_password_hash(password)
  
    return jsonify({'message': 'Utente registrato'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    """Login utente"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
  
    if username not in users:
        return jsonify({'error': 'Credenziali non valide'}), 401
  
    # Verifica password
    if not check_password_hash(users[username], password):
        return jsonify({'error': 'Credenziali non valide'}), 401
  
    # Salva nella session
    session['username'] = username
  
    return jsonify({'message': 'Login effettuato', 'username': username})

@app.route('/api/logout', methods=['POST'])
def logout():
    """Logout utente"""
    session.pop('username', None)
    return jsonify({'message': 'Logout effettuato'})

@app.route('/api/profile')
def profile():
    """Profilo utente (richiede login)"""
    if 'username' not in session:
        return jsonify({'error': 'Non autenticato'}), 401
  
    return jsonify({'username': session['username']})

if __name__ == "__main__":
    app.run(debug=True)
```

### Bonus 2: Web scraping con BeautifulSoup

```python
"""
NOTA: Rispettare sempre i robots.txt e i termini di servizio!
"""

import requests
from bs4 import BeautifulSoup

def scrape_example():
    """Esempio di web scraping"""
    try:
        # Richiesta
        url = "https://example.com"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
      
        # Parsing HTML
        soup = BeautifulSoup(response.text, 'html.parser')
      
        # Estrarre titolo
        title = soup.find('title').text
        print(f"Titolo: {title}")
      
        # Estrarre tutti i link
        links = soup.find_all('a')
        print(f"\nTrovati {len(links)} link:")
        for link in links[:5]:  # primi 5
            href = link.get('href')
            text = link.text.strip()
            print(f"  {text}: {href}")
      
        # Estrarre paragrafi
        paragraphs = soup.find_all('p')
        print(f"\nPrimi 3 paragrafi:")
        for p in paragraphs[:3]:
            print(f"  {p.text.strip()[:100]}...")
      
    except Exception as e:
        print(f"Errore: {e}")

# Installare prima: pip install beautifulsoup4
# scrape_example()
```

---

## 10. Progetti Completi Guidati

### Progetto 1: Blog API completa

```python
"""
API REST completa per un blog con posts e commenti.
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Database in memoria
posts = []
comments = []
next_post_id = 1
next_comment_id = 1

# ============ POSTS ============

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Ottieni tutti i posts"""
    return jsonify({
        'posts': posts,
        'count': len(posts)
    })

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Ottieni un post specifico con i suoi commenti"""
    post = next((p for p in posts if p['id'] == post_id), None)
  
    if not post:
        return jsonify({'error': 'Post non trovato'}), 404
  
    # Trova commenti del post
    post_comments = [c for c in comments if c['post_id'] == post_id]
  
    return jsonify({
        'post': post,
        'comments': post_comments
    })

@app.route('/api/posts', methods=['POST'])
def create_post():
    """Crea nuovo post"""
    global next_post_id
  
    data = request.json
  
    # Validazione
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title e content obbligatori'}), 400
  
    # Crea post
    post = {
        'id': next_post_id,
        'title': data['title'],
        'content': data['content'],
        'author': data.get('author', 'Anonimo'),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
  
    posts.append(post)
    next_post_id += 1
  
    return jsonify({
        'post': post,
        'message': 'Post creato'
    }), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Aggiorna un post"""
    post = next((p for p in posts if p['id'] == post_id), None)
  
    if not post:
        return jsonify({'error': 'Post non trovato'}), 404
  
    data = request.json
  
    # Aggiorna campi
    if 'title' in data:
        post['title'] = data['title']
    if 'content' in data:
        post['content'] = data['content']
  
    post['updated_at'] = datetime.now().isoformat()
  
    return jsonify({
        'post': post,
        'message': 'Post aggiornato'
    })

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Elimina un post e i suoi commenti"""
    global posts, comments
  
    post = next((p for p in posts if p['id'] == post_id), None)
  
    if not post:
        return jsonify({'error': 'Post non trovato'}), 404
  
    # Elimina post
    posts = [p for p in posts if p['id'] != post_id]
  
    # Elimina commenti associati
    comments = [c for c in comments if c['post_id'] != post_id]
  
    return jsonify({'message': 'Post e commenti eliminati'})

# ============ COMMENTS ============

@app.route('/api/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    """Crea commento per un post"""
    global next_comment_id
  
    # Verifica che il post esista
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post non trovato'}), 404
  
    data = request.json
  
    # Validazione
    if not data or 'content' not in data:
        return jsonify({'error': 'Content obbligatorio'}), 400
  
    # Crea commento
    comment = {
        'id': next_comment_id,
        'post_id': post_id,
        'content': data['content'],
        'author': data.get('author', 'Anonimo'),
        'created_at': datetime.now().isoformat()
    }
  
    comments.append(comment)
    next_comment_id += 1
  
    return jsonify({
        'comment': comment,
        'message': 'Commento creato'
    }), 201

@app.route('/api/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """Elimina un commento"""
    global comments
  
    comment = next((c for c in comments if c['id'] == comment_id), None)
  
    if not comment:
        return jsonify({'error': 'Commento non trovato'}), 404
  
    comments = [c for c in comments if c['id'] != comment_id]
  
    return jsonify({'message': 'Commento eliminato'})

# ============ UTILITÀ ============

@app.route('/api/stats')
def stats():
    """Statistiche del blog"""
    return jsonify({
        'total_posts': len(posts),
        'total_comments': len(comments),
        'posts_with_comments': len(set(c['post_id'] for c in comments))
    })

if __name__ == "__main__":
    # Dati di esempio
    posts.append({
        'id': 1,
        'title': 'Primo post',
        'content': 'Benvenuti nel mio blog!',
        'author': 'Admin',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    })
    next_post_id = 2
  
    print("Blog API avviata su http://127.0.0.1:5000")
    print("\nEndpoint disponibili:")
    print("  GET    /api/posts")
    print("  GET    /api/posts/<id>")
    print("  POST   /api/posts")
    print("  PUT    /api/posts/<id>")
    print("  DELETE /api/posts/<id>")
    print("  POST   /api/posts/<id>/comments")
    print("  DELETE /api/comments/<id>")
    print("  GET    /api/stats\n")
  
    app.run(debug=True)
```

### Progetto 2: Applicazione meteo con API esterna

```python
"""
App che usa l'API OpenWeatherMap per ottenere dati meteo.
Registrati su openweathermap.org per ottenere API key gratuita.
"""

from flask import Flask, render_template_string, request, jsonify
import requests

app = Flask(__name__)

# SOSTITUISCI CON LA TUA API KEY
API_KEY = 'TUA_API_KEY_QUI'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>App Meteo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        input {
            width: 70%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background: #4CAF50;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #45a049;
        }
        .weather-info {
            margin-top: 30px;
        }
        .temp {
            font-size: 48px;
            font-weight: bold;
        }
        .error {
            color: #ff6b6b;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌤️ App Meteo</h1>
      
        <form id="weatherForm">
            <input type="text" id="city" placeholder="Inserisci città..." required>
            <button type="submit">Cerca</button>
        </form>
      
        <div id="weatherInfo" class="weather-info" style="display: none;">
            <h2 id="cityName"></h2>
            <div class="temp" id="temperature"></div>
            <p id="description"></p>
            <p>💨 Vento: <span id="wind"></span> m/s</p>
            <p>💧 Umidità: <span id="humidity"></span>%</p>
        </div>
      
        <div id="error" class="error" style="display: none;"></div>
    </div>
  
    <script>
        document.getElementById('weatherForm').addEventListener('submit', async (e) => {
            e.preventDefault();
          
            const city = document.getElementById('city').value;
            const weatherInfo = document.getElementById('weatherInfo');
            const errorDiv = document.getElementById('error');
          
            weatherInfo.style.display = 'none';
            errorDiv.style.display = 'none';
          
            try {
                const response = await fetch(`/api/weather?city=${city}`);
                const data = await response.json();
              
                if (response.ok) {
                    document.getElementById('cityName').textContent = data.city;
                    document.getElementById('temperature').textContent = data.temperature + '°C';
                    document.getElementById('description').textContent = data.description;
                    document.getElementById('wind').textContent = data.wind;
                    document.getElementById('humidity').textContent = data.humidity;
                    weatherInfo.style.display = 'block';
                } else {
                    errorDiv.textContent = data.error;
                    errorDiv.style.display = 'block';
                }
            } catch (error) {
                errorDiv.textContent = 'Errore di connessione';
                errorDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Homepage con form di ricerca"""
    return render_template_string(TEMPLATE)

@app.route('/api/weather')
def get_weather():
    """API endpoint per ottenere dati meteo"""
    city = request.args.get('city')
  
    if not city:
        return jsonify({'error': 'Città non specificata'}), 400
  
    try:
        # Chiamata all'API OpenWeatherMap
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',  # temperatura in Celsius
            'lang': 'it'        # descrizioni in italiano
        }
      
        response = requests.get(BASE_URL, params=params, timeout=10)
      
        if response.status_code == 404:
            return jsonify({'error': 'Città non trovata'}), 404
      
        response.raise_for_status()
        data = response.json()
      
        # Estrae dati rilevanti
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'description': data['weather'][0]['description'].capitalize(),
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed']
        }
      
        return jsonify(weather_data)
      
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout richiesta'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Errore API: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': 'Errore interno'}), 500

if __name__ == "__main__":
    if API_KEY == 'TUA_API_KEY_QUI':
        print("⚠️  ATTENZIONE: Inserisci la tua API key di OpenWeatherMap!")
        print("Registrati su: https://openweathermap.org/api")
    else:
        print("App Meteo avviata su http://127.0.0.1:5000")
  
    app.run(debug=True)
```

### Progetto 3: Sistema di votazioni con persistenza

```python
"""
Sistema di votazioni con salvataggio su file JSON.
"""

from flask import Flask, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path('polls.json')

# ============ GESTIONE DATI ============

def load_polls():
    """Carica polls da file"""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_polls(polls):
    """Salva polls su file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(polls, f, indent=2, ensure_ascii=False)

# ============ API ============

@app.route('/api/polls', methods=['GET'])
def get_polls():
    """Ottieni tutti i sondaggi"""
    polls = load_polls()
    return jsonify({
        'polls': list(polls.values()),
        'count': len(polls)
    })

@app.route('/api/polls/<poll_id>', methods=['GET'])
def get_poll(poll_id):
    """Ottieni sondaggio specifico"""
    polls = load_polls()
  
    if poll_id not in polls:
        return jsonify({'error': 'Sondaggio non trovato'}), 404
  
    return jsonify({'poll': polls[poll_id]})

@app.route('/api/polls', methods=['POST'])
def create_poll():
    """Crea nuovo sondaggio"""
    data = request.json
  
    # Validazione
    if not data or 'question' not in data or 'options' not in data:
        return jsonify({'error': 'Question e options obbligatori'}), 400
  
    if len(data['options']) < 2:
        return jsonify({'error': 'Servono almeno 2 opzioni'}), 400
  
    polls = load_polls()
  
    # Genera ID
    poll_id = str(len(polls) + 1)
  
    # Crea poll
    poll = {
        'id': poll_id,
        'question': data['question'],
        'options': {opt: 0 for opt in data['options']}
    }
  
    polls[poll_id] = poll
    save_polls(polls)
  
    return jsonify({
        'poll': poll,
        'message': 'Sondaggio creato'
    }), 201

@app.route('/api/polls/<poll_id>/vote', methods=['POST'])
def vote(poll_id):
    """Vota in un sondaggio"""
    data = request.json
  
    if not data or 'option' not in data:
        return jsonify({'error': 'Option obbligatoria'}), 400
  
    polls = load_polls()
  
    if poll_id not in polls:
        return jsonify({'error': 'Sondaggio non trovato'}), 404
  
    option = data['option']
  
    if option not in polls[poll_id]['options']:
        return jsonify({'error': 'Opzione non valida'}), 400
  
    # Incrementa voto
    polls[poll_id]['options'][option] += 1
    save_polls(polls)
  
    return jsonify({
        'poll': polls[poll_id],
        'message': 'Voto registrato'
    })

@app.route('/api/polls/<poll_id>/results')
def get_results(poll_id):
    """Ottieni risultati sondaggio"""
    polls = load_polls()
  
    if poll_id not in polls:
        return jsonify({'error': 'Sondaggio non trovato'}), 404
  
    poll = polls[poll_id]
    total_votes = sum(poll['options'].values())
  
    # Calcola percentuali
    results = {
        'question': poll['question'],
        'total_votes': total_votes,
        'results': []
    }
  
    for option, votes in poll['options'].items():
        percentage = (votes / total_votes * 100) if total_votes > 0 else 0
        results['results'].append({
            'option': option,
            'votes': votes,
            'percentage': round(percentage, 1)
        })
  
    return jsonify(results)

if __name__ == "__main__":
    print("Sistema Votazioni avviato su http://127.0.0.1:5000")
    print("\nEndpoint disponibili:")
    print("  GET  /api/polls")
    print("  GET  /api/polls/<id>")
    print("  POST /api/polls")
    print("  POST /api/polls/<id>/vote")
    print("  GET  /api/polls/<id>/results\n")
  
    app.run(debug=True)
```

---

## 11. Testing Base

### Test con pytest

```bash
pip install pytest
```

**File: `test_app.py`**

```python
"""
Test per l'applicazione Flask.
Esegui con: pytest test_app.py
"""

import pytest
from app import app  # importa la tua app Flask

@pytest.fixture
def client():
    """Crea un client di test"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test homepage"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Benvenuto' in response.data

def test_api_endpoint(client):
    """Test API endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
  
    data = response.get_json()
    assert 'nome' in data
    assert data['versione'] == '1.0.0'

def test_create_resource(client):
    """Test creazione risorsa"""
    new_data = {'title': 'Test', 'content': 'Contenuto'}
    response = client.post('/api/posts', json=new_data)
  
    assert response.status_code == 201
  
    data = response.get_json()
    assert data['post']['title'] == 'Test'

def test_not_found(client):
    """Test pagina non esistente"""
    response = client.get('/pagina-inesistente')
    assert response.status_code == 404
```

---

## 12. Risorse e Best Practices

### 12.1 Struttura progetto Flask consigliata

```
mio_progetto/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       ├── css/
│       └── js/
├── tests/
│   └── test_app.py
├── venv/
├── requirements.txt
├── config.py
└── run.py
```

### 12.2 Best practices Flask

```python
# ✅ Usare variabili d'ambiente per configurazione
import os

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

# ✅ Validare sempre l'input utente
if not request.json or 'title' not in request.json:
    return jsonify({'error': 'Dati non validi'}), 400

# ✅ Gestire errori esplicitamente
@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Errore interno'}), 500

# ✅ Usare blueprint per organizzare route
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users')
def users():
    return jsonify({'users': []})

app.register_blueprint(api)

# ✅ Logging
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/process')
def process():
    logger.info('Processing started')
    # ...
    logger.info('Processing completed')
```

---

## 13. Riepilogo Finale

Complimenti! Hai completato il **Giorno 3** del corso Python.

### Competenze acquisite

✅ **Gestione errori professionale**

* Exception handling completo
* Creazione eccezioni custom
* Best practices

✅ **OOP avanzato**

* Ereditarietà multipla
* Magic methods
* Properties
* Polimorfismo

✅ **Librerie esterne**

* requests per HTTP
* pandas per dati
* matplotlib per grafici

✅ **Web development**

* Flask completo
* Template Jinja2
* API REST
* JSON

✅ **Progetti reali**

* Blog API
* App meteo
* Sistema votazioni

### Prossimi passi

1. **Pratica** : Implementa i progetti proposti
2. **Esplora** : Prova altre librerie (FastAPI, Django)
3. **Approfondisci** : Database, autenticazione, deployment
4. **Costruisci** : Crea il tuo progetto personale

---

## 🔗 Riferimenti Utili

### Documentazione ufficiale

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Requests Documentation](https://requests.readthedocs.io/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

### Tutorial e guide

* [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Real Python - Flask](https://realpython.com/tutorials/flask/)
* [Python Exception Handling](https://realpython.com/python-exceptions/)

### API pubbliche per praticare

* [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake API per test
* [OpenWeatherMap](https://openweathermap.org/api) - Dati meteo
* [GitHub API](https://docs.github.com/en/rest) - Dati repository
* [NewsAPI](https://newsapi.org/) - Notizie
* [TheCatAPI](https://thecatapi.com/) - Immagini gatti

### Tools

* [Postman](https://www.postman.com/) - Test API
* [HTTPie](https://httpie.io/) - Client HTTP da terminale
* [curl](https://curl.se/) - Trasferimento dati

---

## 📝 Note Finali

Eccellente lavoro! Hai ora le competenze per:

* Gestire errori in modo professionale
* Creare applicazioni OOP complesse
* Lavorare con API esterne
* Sviluppare web server e API REST

**Ricorda:**

* La pratica è fondamentale
* Leggi codice di altri sviluppatori
* Contribuisci a progetti open source
* Continua a sperimentare

Ci vediamo al **Giorno 4** per il progetto finale! 🚀
