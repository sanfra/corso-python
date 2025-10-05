
# 🐍 Corso Python – Giorno 2

## Lezione 2: Strutture Dati e Strumenti di Lavoro

### 🎯 Obiettivi della lezione

* Comprendere e utilizzare le principali strutture dati di Python (liste, tuple, set, dizionari)
* Manipolare stringhe con metodi avanzati
* Leggere e scrivere file di testo e CSV
* Comprendere il sistema di moduli e pacchetti
* Creare e gestire ambienti virtuali
* Usare pip per installare e gestire dipendenze
* Reimplementare problemi risolti in altri linguaggi

---

## 1. Strutture Dati Python

Le strutture dati permettono di organizzare e gestire collezioni di valori in modo efficiente. Python offre quattro strutture dati principali:  **liste** ,  **tuple** , **set** e  **dizionari** .

### 1.1 Liste (List)

Le **liste** sono collezioni **ordinate** e **modificabili** di elementi. Possono contenere elementi di tipi diversi.

```python
# Creazione di una lista
frutti = ["mela", "banana", "pera"]

# Stampa l'intera lista
print(frutti)  # ['mela', 'banana', 'pera']

# Accesso per indice (inizia da 0)
print(frutti[0])   # 'mela'
print(frutti[1])   # 'banana'
print(frutti[-1])  # 'pera' (ultimo elemento)

# Modifica di un elemento
frutti[1] = "arancia"
print(frutti)  # ['mela', 'arancia', 'pera']

# Aggiunge un elemento alla fine
frutti.append("kiwi")
print(frutti)  # ['mela', 'arancia', 'pera', 'kiwi']

# Inserisce un elemento in una posizione specifica
frutti.insert(1, "fragola")  # inserisce 'fragola' all'indice 1
print(frutti)  # ['mela', 'fragola', 'arancia', 'pera', 'kiwi']

# Rimuove un elemento per valore
frutti.remove("pera")
print(frutti)  # ['mela', 'fragola', 'arancia', 'kiwi']

# Rimuove un elemento per indice e lo restituisce
elemento = frutti.pop(0)  # rimuove il primo elemento
print(elemento)  # 'mela'
print(frutti)    # ['fragola', 'arancia', 'kiwi']

# Numero di elementi
print(len(frutti))  # 3

# Verifica presenza di un elemento
print("kiwi" in frutti)  # True
print("mela" in frutti)  # False
```

#### Slicing (affettare) le liste

Lo **slicing** permette di estrarre porzioni di una lista.

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sintassi: lista[inizio:fine:passo]
# 'inizio' è incluso, 'fine' è escluso

# Primi tre elementi
print(numeri[0:3])   # [0, 1, 2]
print(numeri[:3])    # [0, 1, 2] (stesso risultato)

# Dal quarto elemento in poi
print(numeri[3:])    # [3, 4, 5, 6, 7, 8, 9]

# Elementi dal terzo al settimo
print(numeri[2:7])   # [2, 3, 4, 5, 6]

# Elementi pari (passo 2)
print(numeri[::2])   # [0, 2, 4, 6, 8]

# Lista invertita
print(numeri[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Ultimi tre elementi
print(numeri[-3:])   # [7, 8, 9]
```

#### Metodi utili delle liste

```python
numeri = [3, 1, 4, 1, 5, 9, 2, 6]

# Ordina la lista (modifica l'originale)
numeri.sort()
print(numeri)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Ordina in ordine decrescente
numeri.sort(reverse=True)
print(numeri)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() restituisce una nuova lista ordinata (non modifica l'originale)
numeri = [3, 1, 4, 1, 5]
ordinati = sorted(numeri)
print(ordinati)  # [1, 1, 3, 4, 5]
print(numeri)    # [3, 1, 4, 1, 5] (originale invariato)

# Inverte l'ordine (modifica l'originale)
numeri.reverse()
print(numeri)  # [5, 1, 4, 1, 3]

# Conta occorrenze di un elemento
print(numeri.count(1))  # 2

# Trova l'indice della prima occorrenza
print(numeri.index(4))  # 2

# Estende una lista con un'altra
numeri.extend([7, 8])
print(numeri)  # [5, 1, 4, 1, 3, 7, 8]

# Svuota la lista
numeri.clear()
print(numeri)  # []
```

#### List Comprehension (revisione)

```python
# Crea una lista di quadrati
quadrati = [x**2 for x in range(10)]
print(quadrati)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lista di numeri pari
pari = [x for x in range(20) if x % 2 == 0]
print(pari)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Trasformazione condizionale
numeri = [1, 2, 3, 4, 5]
raddoppiati_o_zero = [x*2 if x % 2 == 0 else 0 for x in numeri]
print(raddoppiati_o_zero)  # [0, 4, 0, 8, 0]
```

---

### 1.2 Tuple

Le **tuple** sono collezioni **ordinate** ma **immutabili** (non modificabili dopo la creazione). Si usano per dati che non devono cambiare.

```python
# Creazione di una tupla
coordinate = (10, 20)
print(coordinate)  # (10, 20)

# Accesso per indice (come le liste)
print(coordinate[0])  # 10
print(coordinate[1])  # 20

# Le tuple non si possono modificare
# coordinate[0] = 5  # ❌ TypeError: 'tuple' object does not support item assignment

# Tupla con un solo elemento (nota la virgola!)
singola = (42,)  # ✅ tupla
# non_tupla = (42)  # ❌ questo è solo un numero tra parentesi

# Unpacking (spacchettamento)
x, y = coordinate
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# Tupla senza parentesi
punto = 5, 10, 15
print(punto)      # (5, 10, 15)
print(type(punto)) # <class 'tuple'>

# Scambio di variabili usando tuple
a = 1
b = 2
a, b = b, a  # scambia i valori
print(a, b)  # 2 1
```

#### Quando usare tuple invece di liste?

✅ **Usare tuple quando:**

* I dati non devono cambiare (coordinate, configurazioni, costanti)
* Serve una chiave per un dizionario (le liste non possono essere chiavi)
* Si vuole maggiore efficienza (le tuple sono più veloci)
* Si vuole proteggere i dati da modifiche accidentali

```python
# Esempio: funzione che restituisce più valori
def calcola_statistiche(numeri):
    """Restituisce minimo, massimo e media"""
    return min(numeri), max(numeri), sum(numeri) / len(numeri)

# La funzione restituisce una tupla
stats = calcola_statistiche([1, 2, 3, 4, 5])
print(stats)  # (1, 5, 3.0)

# Unpacking diretto
minimo, massimo, media = calcola_statistiche([1, 2, 3, 4, 5])
print(f"Min: {minimo}, Max: {massimo}, Media: {media}")
```

---

### 1.3 Set (Insiemi)

I **set** sono collezioni **non ordinate** di elementi **unici** (senza duplicati). Ottimi per eliminare duplicati e verificare appartenenza.

```python
# Creazione di un set
numeri = {1, 2, 3, 3, 4, 4, 5}
print(numeri)  # {1, 2, 3, 4, 5} (duplicati rimossi automaticamente)

# Set vuoto (attenzione: {} crea un dizionario!)
set_vuoto = set()  # ✅ set vuoto
# non_set = {}     # ❌ questo è un dizionario vuoto

# Aggiunge un elemento
numeri.add(6)
print(numeri)  # {1, 2, 3, 4, 5, 6}

# Rimuove un elemento (errore se non esiste)
numeri.remove(3)
print(numeri)  # {1, 2, 4, 5, 6}

# Rimuove un elemento (nessun errore se non esiste)
numeri.discard(10)  # non fa nulla, 10 non esiste

# Verifica presenza (molto veloce!)
print(2 in numeri)  # True
print(3 in numeri)  # False

# Numero di elementi
print(len(numeri))  # 5
```

#### Operazioni tra set

I set supportano operazioni matematiche come  **unione** ,  **intersezione** ,  **differenza** .

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unione: elementi presenti in a O in b
print(a | b)        # {1, 2, 3, 4, 5, 6}
print(a.union(b))   # {1, 2, 3, 4, 5, 6}

# Intersezione: elementi presenti in a E in b
print(a & b)              # {3, 4}
print(a.intersection(b))  # {3, 4}

# Differenza: elementi in a ma non in b
print(a - b)          # {1, 2}
print(a.difference(b)) # {1, 2}

# Differenza simmetrica: elementi in a O b ma non in entrambi
print(a ^ b)                      # {1, 2, 5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}

# Sottoinsieme: a è contenuto in b?
print({1, 2}.issubset({1, 2, 3}))  # True

# Sovrainsieme: a contiene b?
print({1, 2, 3}.issuperset({1, 2}))  # True
```

#### Caso d'uso pratico: eliminare duplicati

```python
# Lista con duplicati
numeri = [1, 2, 2, 3, 4, 4, 4, 5]

# Convertire in set per rimuovere duplicati
unici = list(set(numeri))
print(unici)  # [1, 2, 3, 4, 5]

# Contare elementi unici
parole = ["mela", "banana", "mela", "pera", "banana"]
print(f"Parole uniche: {len(set(parole))}")  # 3
```

---

### 1.4 Dizionari (Dictionary)

I **dizionari** sono collezioni **non ordinate** di coppie  **chiave-valore** . Le chiavi devono essere uniche e immutabili (stringhe, numeri, tuple).

```python
# Creazione di un dizionario
persona = {
    "nome": "Anna",
    "eta": 30,
    "citta": "Milano"
}

# Accesso per chiave
print(persona["nome"])  # 'Anna'
print(persona["eta"])   # 30

# Accesso sicuro con get() (non dà errore se la chiave non esiste)
print(persona.get("telefono"))        # None
print(persona.get("telefono", "N/A")) # 'N/A' (valore di default)

# Aggiungere o modificare una coppia chiave-valore
persona["citta"] = "Torino"      # modifica
persona["professione"] = "Medico" # aggiunge
print(persona)

# Rimuovere una chiave
del persona["eta"]
print(persona)

# Rimuovere e restituire il valore
professione = persona.pop("professione")
print(professione)  # 'Medico'
print(persona)

# Verificare se una chiave esiste
print("nome" in persona)  # True
print("eta" in persona)   # False
```

#### Metodi utili dei dizionari

```python
persona = {"nome": "Anna", "eta": 30, "citta": "Milano"}

# Ottiene tutte le chiavi
print(persona.keys())    # dict_keys(['nome', 'eta', 'citta'])

# Ottiene tutti i valori
print(persona.values())  # dict_values(['Anna', 30, 'Milano'])

# Ottiene tutte le coppie chiave-valore
print(persona.items())   # dict_items([('nome', 'Anna'), ('eta', 30), ('citta', 'Milano')])

# Iterare sul dizionario
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")

# Aggiornare con un altro dizionario
persona.update({"telefono": "1234567", "eta": 31})
print(persona)

# Svuotare il dizionario
persona.clear()
print(persona)  # {}
```

#### Dictionary Comprehension

```python
# Creare un dizionario con comprehension
quadrati = {x: x**2 for x in range(6)}
print(quadrati)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condizione
pari_quadrati = {x: x**2 for x in range(10) if x % 2 == 0}
print(pari_quadrati)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invertire chiavi e valori
originale = {"a": 1, "b": 2, "c": 3}
invertito = {valore: chiave for chiave, valore in originale.items()}
print(invertito)  # {1: 'a', 2: 'b', 3: 'c'}
```

#### Dizionari annidati

```python
# Dizionario di dizionari
studenti = {
    "001": {"nome": "Mario", "voto": 28},
    "002": {"nome": "Laura", "voto": 30},
    "003": {"nome": "Giovanni", "voto": 25}
}

# Accesso a valori annidati
print(studenti["001"]["nome"])  # 'Mario'
print(studenti["002"]["voto"])  # 30

# Iterare su dizionari annidati
for id_studente, dati in studenti.items():
    print(f"ID: {id_studente}, Nome: {dati['nome']}, Voto: {dati['voto']}")
```

---

### 1.5 Confronto Strutture Dati

| Struttura            | Ordinata | Modificabile | Duplicati   | Sintassi      | Caso d'uso                               |
| -------------------- | -------- | ------------ | ----------- | ------------- | ---------------------------------------- |
| **Lista**      | ✅       | ✅           | ✅          | `[1, 2, 3]` | Collezioni generiche, sequenze           |
| **Tupla**      | ✅       | ❌           | ✅          | `(1, 2, 3)` | Dati immutabili, coordinate              |
| **Set**        | ❌       | ✅           | ❌          | `{1, 2, 3}` | Elementi unici, operazioni insiemistiche |
| **Dizionario** | ❌*      | ✅           | ❌ (chiavi) | `{"a": 1}`  | Mappature chiave-valore                  |

*Da Python 3.7+ i dizionari mantengono l'ordine di inserimento

---

## 2. Gestione delle Stringhe

Le stringhe in Python sono  **immutabili** : ogni operazione crea una nuova stringa.

### 2.1 Creazione e operazioni base

```python
# Creazione di stringhe
testo1 = "Ciao"
testo2 = 'Mondo'
multilinea = """Questa è
una stringa
su più righe"""

# Concatenazione
saluto = testo1 + " " + testo2
print(saluto)  # 'Ciao Mondo'

# Ripetizione
print("Ha" * 3)  # 'HaHaHa'

# Lunghezza
print(len(saluto))  # 10

# Accesso per indice (come le liste)
print(saluto[0])   # 'C'
print(saluto[-1])  # 'o'

# Slicing
print(saluto[0:4])   # 'Ciao'
print(saluto[5:])    # 'Mondo'
print(saluto[::-1])  # 'odnuM oaiC' (invertita)
```

### 2.2 Metodi delle stringhe

```python
testo = "  Ciao Mondo Python  "

# Trasformazione maiuscole/minuscole
print(testo.lower())       # '  ciao mondo python  '
print(testo.upper())       # '  CIAO MONDO PYTHON  '
print(testo.capitalize())  # '  ciao mondo python  '
print(testo.title())       # '  Ciao Mondo Python  '

# Rimozione spazi
print(testo.strip())   # 'Ciao Mondo Python' (rimuove ai bordi)
print(testo.lstrip())  # 'Ciao Mondo Python  ' (rimuove a sinistra)
print(testo.rstrip())  # '  Ciao Mondo Python' (rimuove a destra)

# Sostituzione
print(testo.replace("Mondo", "World"))  # '  Ciao World Python  '
print(testo.replace(" ", ""))           # 'CiaoMondoPython'

# Verifica contenuto
print("Mondo" in testo)         # True
print("Java" in testo)          # False
print(testo.startswith("  C"))  # True
print(testo.endswith("on  "))   # True

# Divisione in lista
parole = "Ciao,Mondo,Python".split(",")
print(parole)  # ['Ciao', 'Mondo', 'Python']

frase = "Ciao Mondo Python"
parole = frase.split()  # split senza argomenti usa gli spazi
print(parole)  # ['Ciao', 'Mondo', 'Python']

# Unione da lista
lista_parole = ["Python", "è", "fantastico"]
frase = " ".join(lista_parole)
print(frase)  # 'Python è fantastico'

# Trova posizione
testo = "Python è un linguaggio Python"
print(testo.find("Python"))   # 0 (prima occorrenza)
print(testo.find("Java"))     # -1 (non trovato)
print(testo.index("Python"))  # 0 (come find, ma solleva errore se non trova)
print(testo.count("Python"))  # 2 (conta occorrenze)
```

### 2.3 Verifiche sul contenuto

```python
# Verifica tipi di caratteri
print("Python3".isalnum())    # True (alfanumerico)
print("Python".isalpha())     # True (solo lettere)
print("12345".isdigit())      # True (solo cifre)
print("   ".isspace())        # True (solo spazi)
print("Python".islower())     # False
print("PYTHON".isupper())     # True
print("Python 3".istitle())   # True (ogni parola inizia con maiuscola)
```

### 2.4 Formattazione stringhe

```python
nome = "Anna"
eta = 30

# f-string (metodo moderno, consigliato)
messaggio = f"Mi chiamo {nome} e ho {eta} anni"
print(messaggio)

# Espressioni nelle f-string
print(f"Tra 5 anni avrò {eta + 5} anni")
print(f"Il mio nome al contrario è {nome[::-1]}")

# Formattazione numeri
prezzo = 19.99
print(f"Prezzo: €{prezzo:.2f}")  # Prezzo: €19.99 (2 decimali)

pi_greco = 3.14159265359
print(f"Pi greco: {pi_greco:.3f}")  # Pi greco: 3.142 (3 decimali)

# Allineamento
print(f"{'Left':<10}|")    # 'Left      |' (sinistra, 10 caratteri)
print(f"{'Center':^10}|")  # '  Center  |' (centro)
print(f"{'Right':>10}|")   # '     Right|' (destra)

# Metodi più vecchi (ancora validi)
# format()
messaggio = "Mi chiamo {} e ho {} anni".format(nome, eta)
print(messaggio)

# % (stile C, obsoleto)
messaggio = "Mi chiamo %s e ho %d anni" % (nome, eta)
print(messaggio)
```

### 2.5 Caratteri speciali ed escape

```python
# \n: nuova riga
print("Prima riga\nSeconda riga")

# \t: tab
print("Colonna1\tColonna2")

# \\: backslash letterale
print("C:\\Users\\nome")

# \': apice singolo
print('L\'apostrofo')

# \": virgolette doppie
print("Ha detto: \"Ciao\"")

# Raw string (ignora escape)
path = r"C:\Users\nome\Documents"  # il carattere r prima della stringa
print(path)
```

---

## 3. File I/O (Input/Output)

Python rende semplice leggere e scrivere file.

### 3.1 Lettura di file di testo

```python
# Metodo consigliato: with statement
# 'with' chiude automaticamente il file alla fine del blocco
with open("testo.txt", "r", encoding="utf-8") as f:
    # 'r' = read (lettura)
    # encoding='utf-8' gestisce correttamente caratteri accentati
    contenuto = f.read()  # legge tutto il file come stringa
    print(contenuto)
# Il file viene chiuso automaticamente qui

# Leggere riga per riga
with open("testo.txt", "r", encoding="utf-8") as f:
    for riga in f:
        # ogni riga include il carattere \n alla fine
        print(riga.strip())  # strip() rimuove \n

# Leggere tutte le righe in una lista
with open("testo.txt", "r", encoding="utf-8") as f:
    righe = f.readlines()  # lista di stringhe
    print(righe)

# Leggere solo le prime N righe
with open("testo.txt", "r", encoding="utf-8") as f:
    prima_riga = f.readline()  # legge una singola riga
    seconda_riga = f.readline()
    print(prima_riga, seconda_riga)
```

### 3.2 Scrittura su file

```python
# Modalità 'w' (write): SOVRASCRIVE il file se esiste
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Prima riga\n")
    f.write("Seconda riga\n")

# Modalità 'a' (append): AGGIUNGE al file esistente
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Terza riga\n")

# Scrivere liste
righe = ["Riga 1\n", "Riga 2\n", "Riga 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(righe)
```

### 3.3 Modalità di apertura file

| Modalità | Descrizione                 | Crea file | Sovrascrive |
| --------- | --------------------------- | --------- | ----------- |
| `'r'`   | Lettura (default)           | ❌        | -           |
| `'w'`   | Scrittura                   | ✅        | ✅          |
| `'a'`   | Append (aggiunge alla fine) | ✅        | ❌          |
| `'r+'`  | Lettura e scrittura         | ❌        | ❌          |
| `'w+'`  | Scrittura e lettura         | ✅        | ✅          |
| `'rb'`  | Lettura binaria             | ❌        | -           |
| `'wb'`  | Scrittura binaria           | ✅        | ✅          |

### 3.4 Gestione errori con file

```python
# Gestire file inesistenti
try:
    with open("file_inesistente.txt", "r") as f:
        contenuto = f.read()
except FileNotFoundError:
    print("Errore: il file non esiste!")
except PermissionError:
    print("Errore: permessi insufficienti!")
except Exception as e:
    print(f"Errore generico: {e}")

# Verificare esistenza file
import os

if os.path.exists("testo.txt"):
    with open("testo.txt", "r") as f:
        print(f.read())
else:
    print("Il file non esiste")
```

### 3.5 Lavorare con file CSV

CSV (Comma-Separated Values) è un formato comune per dati tabulari.

```python
import csv

# Leggere un CSV
with open("dati.csv", "r", encoding="utf-8") as file:
    # csv.reader legge il file riga per riga
    lettore = csv.reader(file)
  
    # Prima riga spesso contiene intestazioni
    intestazioni = next(lettore)
    print(f"Intestazioni: {intestazioni}")
  
    # Legge le rimanenti righe
    for riga in lettore:
        print(riga)  # ogni riga è una lista

# Leggere CSV come dizionari (più comodo!)
with open("dati.csv", "r", encoding="utf-8") as file:
    # DictReader usa la prima riga come chiavi
    lettore = csv.DictReader(file)
  
    for riga in lettore:
        # ogni riga è un dizionario
        print(riga["nome"], riga["eta"])  # accesso per nome colonna

# Scrivere un CSV
dati = [
    ["Nome", "Età", "Città"],
    ["Mario", "25", "Roma"],
    ["Laura", "30", "Milano"],
    ["Giovanni", "28", "Napoli"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    # newline="" previene righe vuote su Windows
    scrittore = csv.writer(file)
  
    # Scrive tutte le righe
    scrittore.writerows(dati)

# Scrivere CSV da dizionari
dati = [
    {"nome": "Mario", "eta": 25, "citta": "Roma"},
    {"nome": "Laura", "eta": 30, "citta": "Milano"}
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    # Specifica i nomi delle colonne
    campi = ["nome", "eta", "citta"]
    scrittore = csv.DictWriter(file, fieldnames=campi)
  
    # Scrive le intestazioni
    scrittore.writeheader()
  
    # Scrive i dati
    scrittore.writerows(dati)
```

### 3.6 Lavorare con percorsi (pathlib)

```python
from pathlib import Path

# Creare percorsi in modo portabile
percorso = Path("dati") / "file.txt"  # funziona su Windows e Unix
print(percorso)

# Verificare esistenza
if percorso.exists():
    print("Il file esiste")

# Creare directory
Path("nuova_cartella").mkdir(exist_ok=True)  # exist_ok evita errore se esiste

# Leggere/scrivere con pathlib
percorso = Path("testo.txt")
contenuto = percorso.read_text(encoding="utf-8")
percorso.write_text("Nuovo contenuto", encoding="utf-8")

# Informazioni sul file
print(percorso.name)        # 'testo.txt'
print(percorso.stem)        # 'testo'
print(percorso.suffix)      # '.txt'
print(percorso.parent)      # directory contenitore
print(percorso.absolute())  # percorso assoluto

# Elencare file in una directory
for file in Path(".").glob("*.txt"):
    print(file)
```

---

## 4. Moduli e Pacchetti

I **moduli** permettono di organizzare il codice e riutilizzare funzionalità. Un modulo è semplicemente un file `.py` che contiene definizioni di funzioni, classi e variabili.

### 4.1 Import di moduli standard

Python include una ricca **libreria standard** con moduli per molte funzionalità comuni.

```python
# Import semplice
import math

# Uso delle funzioni del modulo
print(math.sqrt(16))      # 4.0 (radice quadrata)
print(math.pi)            # 3.141592653589793
print(math.ceil(4.3))     # 5 (arrotonda verso l'alto)
print(math.floor(4.7))    # 4 (arrotonda verso il basso)
print(math.pow(2, 3))     # 8.0 (2 elevato alla 3)

# Import con alias (rinominare per comodità)
import math as m
print(m.sqrt(25))  # 5.0

# Import di funzioni specifiche
from math import sqrt, pi, cos
print(sqrt(9))     # 3.0 (non serve math.sqrt)
print(pi)          # 3.141592653589793
print(cos(0))      # 1.0

# Import di tutto (sconsigliato!)
# from math import *  # ❌ può creare conflitti di nomi
```

### 4.2 Moduli utili della libreria standard

```python
# datetime: gestione date e orari
import datetime

# Data e ora correnti
ora = datetime.datetime.now()
print(ora)  # 2025-10-05 14:30:45.123456

# Solo data
oggi = datetime.date.today()
print(oggi)  # 2025-10-05

# Creare date specifiche
compleanno = datetime.date(1990, 5, 15)
print(compleanno)

# Differenza tra date
eta = oggi - compleanno
print(f"Giorni di vita: {eta.days}")

# Formattare date
print(ora.strftime("%d/%m/%Y %H:%M"))  # 05/10/2025 14:30

# ---

# random: numeri casuali
import random

# Numero casuale tra 0 e 1
print(random.random())  # es. 0.7432891234

# Numero intero casuale in un intervallo
dado = random.randint(1, 6)  # numero da 1 a 6
print(dado)

# Scegliere elemento casuale da lista
colori = ["rosso", "verde", "blu", "giallo"]
colore = random.choice(colori)
print(colore)

# Mescolare una lista
carte = [1, 2, 3, 4, 5]
random.shuffle(carte)  # modifica la lista originale
print(carte)

# ---

# os: interazione con sistema operativo
import os

# Directory corrente
print(os.getcwd())  # /path/to/current/directory

# Cambiare directory
# os.chdir("/path/to/directory")

# Elencare file in directory
file_list = os.listdir(".")
print(file_list)

# Creare directory
# os.mkdir("nuova_cartella")

# Verificare se esiste
print(os.path.exists("file.txt"))

# Percorso assoluto
print(os.path.abspath("file.txt"))

# ---

# json: lavorare con JSON
import json

# Convertire dizionario Python in stringa JSON
dati = {"nome": "Mario", "eta": 30, "citta": "Roma"}
json_string = json.dumps(dati, indent=2)  # indent=2 per formattazione
print(json_string)

# Convertire JSON in dizionario Python
json_data = '{"nome": "Laura", "eta": 25}'
dati_python = json.loads(json_data)
print(dati_python["nome"])  # 'Laura'

# Salvare JSON su file
with open("dati.json", "w") as f:
    json.dump(dati, f, indent=2)

# Leggere JSON da file
with open("dati.json", "r") as f:
    dati = json.load(f)
    print(dati)

# ---

# sys: informazioni sistema Python
import sys

# Versione Python
print(sys.version)

# Percorso eseguibile Python
print(sys.executable)

# Argomenti da linea di comando
print(sys.argv)  # lista degli argomenti

# Uscire dal programma
# sys.exit(0)
```

### 4.3 Creare moduli personalizzati

Un modulo è semplicemente un file `.py` con funzioni e variabili.

**File: `mio_modulo.py`**

```python
"""
Modulo di esempio con funzioni matematiche personalizzate.
"""

# Variabile del modulo
PI = 3.14159

def saluta(nome="utente"):
    """Stampa un saluto personalizzato"""
    print(f"Ciao {nome} da mio_modulo!")

def somma(a, b):
    """Restituisce la somma di due numeri"""
    return a + b

def calcola_area_cerchio(raggio):
    """Calcola l'area di un cerchio"""
    return PI * raggio ** 2

# Codice eseguito solo se il modulo viene eseguito direttamente
# (non quando viene importato)
if __name__ == "__main__":
    print("Test del modulo:")
    saluta()
    print(f"Somma 5 + 3 = {somma(5, 3)}")
```

**File: `main.py`** (usa il modulo)

```python
# Importare il modulo personalizzato
import mio_modulo

# Usare le funzioni del modulo
mio_modulo.saluta("Anna")
risultato = mio_modulo.somma(10, 20)
print(risultato)

area = mio_modulo.calcola_area_cerchio(5)
print(f"Area: {area}")

# Accedere alle variabili del modulo
print(f"Pi greco: {mio_modulo.PI}")

# Import specifico
from mio_modulo import saluta, somma
saluta("Marco")
print(somma(7, 8))
```

### 4.4 Pacchetti (packages)

Un **pacchetto** è una directory contenente moduli e un file speciale `__init__.py`.

**Struttura directory:**

```
mio_pacchetto/
    __init__.py
    matematica.py
    stringhe.py
```

**File: `mio_pacchetto/__init__.py`**

```python
"""Pacchetto di utilità varie"""
# Può essere vuoto o contenere codice di inizializzazione

# Rendere disponibili funzioni specifiche
from .matematica import somma, sottrazione
from .stringhe import maiuscola

__all__ = ['somma', 'sottrazione', 'maiuscola']
```

**File: `mio_pacchetto/matematica.py`**

```python
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b
```

**File: `mio_pacchetto/stringhe.py`**

```python
def maiuscola(testo):
    return testo.upper()

def conta_vocali(testo):
    vocali = "aeiouAEIOU"
    return sum(1 for char in testo if char in vocali)
```

**Uso del pacchetto:**

```python
# Import del pacchetto
import mio_pacchetto

# Usare le funzioni
print(mio_pacchetto.somma(5, 3))
print(mio_pacchetto.maiuscola("ciao"))

# Import specifico da sottomodi
from mio_pacchetto.matematica import somma
from mio_pacchetto.stringhe import conta_vocali

print(somma(10, 20))
print(conta_vocali("Python è fantastico"))
```

### 4.5 Dove Python cerca i moduli

```python
import sys

# Lista dei percorsi dove Python cerca moduli
for path in sys.path:
    print(path)

# Python cerca moduli in questo ordine:
# 1. Directory corrente
# 2. Variabile ambiente PYTHONPATH
# 3. Directory di installazione standard
```

---

## 5. Ambienti Virtuali e Gestione Pacchetti

Gli **ambienti virtuali** permettono di isolare le dipendenze di progetti diversi.

### 5.1 Perché usare ambienti virtuali?

**Problema senza ambienti virtuali:**

* Progetto A richiede Django 3.2
* Progetto B richiede Django 4.0
* Non puoi avere due versioni di Django installate globalmente!

**Soluzione: ambiente virtuale**

* Ogni progetto ha il suo ambiente isolato
* Dipendenze separate per ogni progetto
* Nessun conflitto tra versioni

### 5.2 Creare un ambiente virtuale

```bash
# Creare ambiente virtuale chiamato 'venv'
python -m venv venv

# Su Windows:
python -m venv venv

# Su macOS/Linux:
python3 -m venv venv

# Struttura creata:
# venv/
#   ├── Scripts/      (Windows) o bin/ (Unix)
#   ├── Lib/
#   └── Include/
```

### 5.3 Attivare l'ambiente virtuale

```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# Quando attivato, il prompt cambia:
# (venv) C:\Users\nome\progetto>

# Verificare che Python usi l'ambiente virtuale
which python  # Unix
where python  # Windows
```

### 5.4 Disattivare l'ambiente virtuale

```bash
# Basta digitare:
deactivate

# Il prompt torna normale
```

### 5.5 Usare pip (Package Installer for Python)

```bash
# Verificare versione pip
pip --version

# Aggiornare pip
python -m pip install --upgrade pip

# Installare un pacchetto
pip install requests

# Installare versione specifica
pip install requests==2.28.0

# Installare versione minima
pip install "requests>=2.25.0"

# Installare più pacchetti
pip install requests pandas numpy

# Elencare pacchetti installati
pip list

# Mostrare info su un pacchetto
pip show requests

# Cercare pacchetti
pip search flask  # (funzionalità disabilitata su PyPI)

# Disinstallare un pacchetto
pip uninstall requests

# Aggiornare un pacchetto
pip install --upgrade requests
```

### 5.6 Requirements.txt

Il file `requirements.txt` elenca tutte le dipendenze del progetto.

```bash
# Salvare pacchetti installati in requirements.txt
pip freeze > requirements.txt

# Contenuto esempio di requirements.txt:
# requests==2.28.1
# pandas==1.5.3
# numpy==1.24.2

# Installare tutti i pacchetti da requirements.txt
pip install -r requirements.txt

# Questo è utile per:
# - Condividere progetti
# - Deployare applicazioni
# - Replicare ambienti
```

**Creare requirements.txt manualmente:**

```txt
# requirements.txt
requests>=2.28.0
pandas>=1.5.0
numpy>=1.24.0
flask==2.3.0  # versione specifica
```

### 5.7 Best practices ambienti virtuali

```bash
# 1. Creare sempre un ambiente virtuale per ogni progetto
cd mio_progetto
python -m venv venv

# 2. Aggiungere venv/ al .gitignore
echo "venv/" >> .gitignore

# 3. Documentare dipendenze
pip freeze > requirements.txt

# 4. Struttura progetto consigliata:
# mio_progetto/
#   ├── venv/              (ignorato da git)
#   ├── src/
#   │   └── main.py
#   ├── tests/
#   ├── requirements.txt
#   ├── README.md
#   └── .gitignore
```

### 5.8 Pacchetti utili da conoscere

```bash
# Web scraping
pip install requests beautifulsoup4

# Data science
pip install pandas numpy matplotlib seaborn

# Machine Learning
pip install scikit-learn tensorflow

# Web development
pip install flask django fastapi

# Testing
pip install pytest

# Automazione
pip install selenium

# Excel
pip install openpyxl xlrd

# Database
pip install sqlalchemy psycopg2
```

---

## 6. Esercizi Pratici

### Esercizio 1: Conta righe in un file

```python
"""
Leggi un file di testo e conta:
- Numero di righe
- Numero di parole
- Numero di caratteri
"""

def analizza_file(nome_file):
    """Analizza un file di testo e restituisce statistiche"""
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            # Legge tutto il contenuto
            contenuto = f.read()
          
            # Conta caratteri
            num_caratteri = len(contenuto)
          
            # Conta righe
            righe = contenuto.split("\n")
            num_righe = len(righe)
          
            # Conta parole
            parole = contenuto.split()
            num_parole = len(parole)
          
            # Stampa risultati
            print(f"File: {nome_file}")
            print(f"Righe: {num_righe}")
            print(f"Parole: {num_parole}")
            print(f"Caratteri: {num_caratteri}")
          
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non esiste")
    except Exception as e:
        print(f"Errore: {e}")

# Test
analizza_file("testo.txt")
```

### Esercizio 2: Trova lo studente più giovane

```python
"""
Crea un dizionario con studenti e le loro età.
Trova e stampa lo studente più giovane.
"""

# Dizionario studenti
studenti = {
    "Mario": 22,
    "Laura": 19,
    "Giovanni": 25,
    "Anna": 20
}

# Metodo 1: usando min() con key
studente_giovane = min(studenti, key=studenti.get)
print(f"Studente più giovane: {studente_giovane} ({studenti[studente_giovane]} anni)")

# Metodo 2: iterazione manuale
eta_minima = float('inf')  # infinito
nome_giovane = None

for nome, eta in studenti.items():
    if eta < eta_minima:
        eta_minima = eta
        nome_giovane = nome

print(f"Studente più giovane: {nome_giovane} ({eta_minima} anni)")

# Metodo 3: sorted con lambda
studenti_ordinati = sorted(studenti.items(), key=lambda x: x[1])
print(f"Studente più giovane: {studenti_ordinati[0][0]} ({studenti_ordinati[0][1]} anni)")
```

### Esercizio 3: Leggi CSV e mostra prima colonna

```python
"""
Leggi un file CSV e mostra solo i valori della prima colonna.
"""
import csv

def mostra_prima_colonna(nome_file):
    """Legge un CSV e stampa la prima colonna"""
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            lettore = csv.reader(file)
          
            # Salta intestazioni (opzionale)
            intestazioni = next(lettore)
            print(f"Prima colonna: {intestazioni[0]}")
            print("-" * 30)
          
            # Stampa prima colonna di ogni riga
            for riga in lettore:
                if riga:  # ignora righe vuote
                    print(riga[0])
                  
    except FileNotFoundError:
        print(f"File '{nome_file}' non trovato")
    except Exception as e:
        print(f"Errore: {e}")

# Test (crea prima un file CSV di esempio)
with open("studenti.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Età", "Città"])
    writer.writerow(["Mario", "22", "Roma"])
    writer.writerow(["Laura", "19", "Milano"])
    writer.writerow(["Giovanni", "25", "Napoli"])

mostra_prima_colonna("studenti.csv")
```

### Esercizio 4: Usa modulo datetime

```python
"""
Calcola quanti giorni mancano al prossimo compleanno.
"""
import datetime

def giorni_a_compleanno(giorno, mese):
    """Calcola giorni mancanti al prossimo compleanno"""
    # Data corrente
    oggi = datetime.date.today()
  
    # Compleanno di quest'anno
    compleanno = datetime.date(oggi.year, mese, giorno)
  
    # Se il compleanno è già passato, considera l'anno prossimo
    if compleanno < oggi:
        compleanno = datetime.date(oggi.year + 1, mese, giorno)
  
    # Calcola differenza
    differenza = compleanno - oggi
  
    return differenza.days

# Test
giorno = int(input("Giorno di nascita: "))
mese = int(input("Mese di nascita (1-12): "))

giorni = giorni_a_compleanno(giorno, mese)
print(f"Mancano {giorni} giorni al tuo compleanno!")
```

### Esercizio 5: Gestione rubrica (completo)

```python
"""
Rubrica telefonica con salvataggio su file JSON.
Funzionalità: aggiungere, cercare, eliminare, elencare contatti.
"""
import json
from pathlib import Path

class Rubrica:
    """Gestisce una rubrica telefonica"""
  
    def __init__(self, file_path="rubrica.json"):
        """Inizializza la rubrica e carica i contatti dal file"""
        self.file_path = Path(file_path)
        self.contatti = self.carica_contatti()
  
    def carica_contatti(self):
        """Carica i contatti dal file JSON"""
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
  
    def salva_contatti(self):
        """Salva i contatti nel file JSON"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.contatti, f, indent=2, ensure_ascii=False)
  
    def aggiungi(self, nome, telefono):
        """Aggiunge un nuovo contatto"""
        self.contatti[nome] = telefono
        self.salva_contatti()
        print(f"Contatto '{nome}' aggiunto!")
  
    def cerca(self, nome):
        """Cerca un contatto per nome"""
        if nome in self.contatti:
            print(f"{nome}: {self.contatti[nome]}")
        else:
            print(f"Contatto '{nome}' non trovato")
  
    def elimina(self, nome):
        """Elimina un contatto"""
        if nome in self.contatti:
            del self.contatti[nome]
            self.salva_contatti()
            print(f"Contatto '{nome}' eliminato")
        else:
            print(f"Contatto '{nome}' non trovato")
  
    def elenca(self):
        """Elenca tutti i contatti"""
        if not self.contatti:
            print("Rubrica vuota")
            return
      
        print("\n=== RUBRICA ===")
        for nome, telefono in sorted(self.contatti.items()):
            print(f"{nome}: {telefono}")
        print("=" * 15)

def menu():
    """Mostra il menu e gestisce l'interazione"""
    rubrica = Rubrica()
  
    while True:
        print("\n--- RUBRICA TELEFONICA ---")
        print("1. Aggiungi contatto")
        print("2. Cerca contatto")
        print("3. Elimina contatto")
        print("4. Elenca tutti")
        print("5. Esci")
      
        scelta = input("\nScegli un'opzione: ")
      
        if scelta == "1":
            nome = input("Nome: ")
            telefono = input("Telefono: ")
            rubrica.aggiungi(nome, telefono)
      
        elif scelta == "2":
            nome = input("Nome da cercare: ")
            rubrica.cerca(nome)
      
        elif scelta == "3":
            nome = input("Nome da eliminare: ")
            rubrica.elimina(nome)
      
        elif scelta == "4":
            rubrica.elenca()
      
        elif scelta == "5":
            print("Arrivederci!")
            break
      
        else:
            print("Opzione non valida!")

# Esegui il programma
if __name__ == "__main__":
    menu()
```

### Esercizio 6: Analisi CSV avanzata

```python
"""
Leggi un CSV di vendite e calcola statistiche.
"""
import csv
from collections import defaultdict

def analizza_vendite(file_csv):
    """Analizza un file CSV di vendite e calcola statistiche"""
  
    vendite_per_prodotto = defaultdict(float)
    vendite_per_mese = defaultdict(float)
  
    with open(file_csv, "r", encoding="utf-8") as f:
        lettore = csv.DictReader(f)
      
        for riga in lettore:
            prodotto = riga["prodotto"]
            importo = float(riga["importo"])
            mese = riga["mese"]
          
            # Accumula vendite
            vendite_per_prodotto[prodotto] += importo
            vendite_per_mese[mese] += importo
  
    # Stampa risultati
    print("=== VENDITE PER PRODOTTO ===")
    for prodotto, totale in sorted(vendite_per_prodotto.items()):
        print(f"{prodotto}: €{totale:.2f}")
  
    print("\n=== VENDITE PER MESE ===")
    for mese, totale in sorted(vendite_per_mese.items()):
        print(f"{mese}: €{totale:.2f}")
  
    # Prodotto più venduto
    prodotto_top = max(vendite_per_prodotto, key=vendite_per_prodotto.get)
    print(f"\nProdotto più venduto: {prodotto_top} (€{vendite_per_prodotto[prodotto_top]:.2f})")

# Crea file CSV di esempio
with open("vendite.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["prodotto", "importo", "mese"])
    writer.writeheader()
    writer.writerow({"prodotto": "Laptop", "importo": "999.99", "mese": "Gennaio"})
    writer.writerow({"prodotto": "Mouse", "importo": "29.99", "mese": "Gennaio"})
    writer.writerow({"prodotto": "Laptop", "importo": "999.99", "mese": "Febbraio"})
    writer.writerow({"prodotto": "Tastiera", "importo": "79.99", "mese": "Febbraio"})

# Esegui analisi
analizza_vendite("vendite.csv")
```

---

## 7. Reimplementazione da Altri Linguaggi

### Esempio: FizzBuzz (da JavaScript a Python)

**JavaScript:**

```javascript
for (let i = 1; i <= 100; i++) {
    if (i % 15 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}
```

**Python:**

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Esempio: Trova duplicati (da Java a Python)

**Java:**

```java
import java.util.*;

public class FindDuplicates {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 2, 4, 5, 3};
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();
      
        for (int num : numbers) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
      
        System.out.println(duplicates);
    }
}
```

**Python:**

```python
numbers = [1, 2, 3, 2, 4, 5, 3]

# Metodo 1: usando set
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)  # {2, 3}

# Metodo 2: usando Counter
from collections import Counter

conteggi = Counter(numbers)
duplicates = {num for num, count in conteggi.items() if count > 1}
print(duplicates)  # {2, 3}

# Metodo 3: list comprehension
duplicates = list(set([num for num in numbers if numbers.count(num) > 1]))
print(duplicates)
```

---

## 8. Riepilogo Giorno 2

### Concetti chiave appresi

✅ **Strutture dati:**

* **Liste** : ordinate, modificabili, permettono duplicati
* **Tuple** : ordinate, immutabili, più veloci delle liste
* **Set** : non ordinati, elementi unici, operazioni insiemistiche
* **Dizionari** : coppie chiave-valore, accesso O(1)

✅ **Stringhe:**

* Metodi di trasformazione: `lower()`, `upper()`, `strip()`
* Ricerca e sostituzione: `find()`, `replace()`, `split()`, `join()`
* Formattazione con f-string

✅ **File I/O:**

* Lettura/scrittura file di testo con `open()`
* Gestione CSV con modulo `csv`
* Best practice: usare `with` statement

✅ **Moduli:**

* Import da libreria standard
* Creare moduli personalizzati
* Organizzare codice in pacchetti

✅ **Ambienti virtuali:**

* Isolamento dipendenze con `venv`
* Gestione pacchetti con `pip`
* File `requirements.txt`

---

## 9. Preparazione per il Giorno 3

Nel **Giorno 3** approfondiremo:

* **Gestione eccezioni** avanzata
* **Programmazione orientata agli oggetti** (classi, ereditarietà)
* **Librerie esterne** utili (requests, pandas, matplotlib)
* **Introduzione a Flask** per creare web server

### Compiti per casa (opzionali)

1. Creare un programma che legga un file CSV e generi statistiche
2. Implementare una to-do list con salvataggio su JSON
3. Esplorare il modulo `collections` (Counter, defaultdict, namedtuple)
4. Creare un modulo personale con almeno 3 funzioni utili

---

## 🔗 Riferimenti utili

### Documentazione

* [Python Standard Library](https://docs.python.org/3/library/) - Moduli built-in
* [Python Tutorial - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Working with Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

### Risorse aggiuntive

* [Real Python - File I/O](https://realpython.com/working-with-files-in-python/)
* [PyPI](https://pypi.org/) - Repository pacchetti Python
* [Python Module of the Week](https://pymotw.com/)

---

## 📝 Note finali

Ottimo lavoro! Hai completato il **Giorno 2** del corso Python.

**Punti chiave da ricordare:**

* Le **strutture dati** giuste rendono il codice più efficiente
* I **moduli** organizzano e riutilizzano il codice
* Gli **ambienti virtuali** evitano conflitti tra progetti
* **Pratica** con file reali per consolidare le competenze

**Skill acquisite:**

* ✅ Manipolare collezioni complesse
* ✅ Processare file di testo e CSV
* ✅ Creare e usare moduli
* ✅ Gestire dipendenze con pip

Ci vediamo al  **Giorno 3** ! 🚀
