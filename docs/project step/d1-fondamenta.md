# Corso Python – Giorno 1

## Lezione 1: Introduzione e Fondamenta del Linguaggio Python

### 🎯 Obiettivi della lezione

* Capire cos'è Python e dove si usa
* Installare e configurare l'ambiente di sviluppo
* Scrivere ed eseguire i primi script
* Conoscere i concetti base: variabili, tipi, operatori, input/output
* Utilizzare le strutture di controllo (`if`, `for`, `while`)
* Creare e usare funzioni

---

## 1. Cos'è Python

Python è un linguaggio **interpretato** (in realtà ibrido - vedi sezione dedicata), **ad alto livello** (vicino al linguaggio umano) e **multiparadigma** (supporta programmazione procedurale, orientata agli oggetti e funzionale).

### Origini e storia di Python

Python nasce alla fine degli anni '80 grazie a  **Guido van Rossum** , informatico olandese del CWI (Centrum Wiskunde & Informatica) di Amsterdam. Il nome *Python* è un omaggio ai  **Monty Python** , gruppo comico britannico che Van Rossum amava seguire.

La prima versione ufficiale ( **Python 0.9.0** ) esce nel  **febbraio 1991** , seguita da **Python 1.0** nel  **gennaio 1994** , con l'obiettivo di creare un linguaggio:

* **Chiaro e leggibile** , simile al linguaggio naturale
* **Potente ma semplice da usare**
* **Portabile** , cioè eseguibile su più sistemi senza modifiche

**Evoluzione delle versioni principali:**

* **Python 1.x** (1994-2000): prima release stabile
* **Python 2.x** (2000-2020): ampia diffusione, end-of-life nel 2020
* **Python 3.x** (2008-oggi): versione moderna, non retrocompatibile con Python 2

Oggi Python è uno dei linguaggi più diffusi al mondo. È usato per:

* **Web development** (Flask, Django, FastAPI)
* **Data Science** e **AI/Machine Learning** (Pandas, NumPy, TensorFlow, PyTorch, scikit-learn)
* **Automazione e DevOps** (Ansible, scripting)
* **Cybersecurity** e **scripting di sistema**
* **Game development** (Pygame)
* **Desktop applications** (Tkinter, PyQt)

---

## 2. Python – Tipologia di linguaggio

### Linguaggio interpretato vs ibrido

Python viene comunemente definito  **interpretato** , ma tecnicamente è un  **linguaggio ibrido** . Ecco cosa succede realmente quando esegui un file Python:

1. **Il file sorgente** (`.py`) viene **compilato automaticamente** in **bytecode** (`.pyc`)
2. Il bytecode viene salvato nella cartella `__pycache__` per velocizzare esecuzioni successive
3. Il bytecode viene eseguito dalla **Python Virtual Machine (PVM)**

Questa architettura è  **simile a Java** , dove il codice (`.java`) viene compilato in bytecode (`.class`) e poi interpretato dalla  **Java Virtual Machine (JVM)** .

**Differenza chiave:** In Python la compilazione in bytecode è automatica e trasparente, quindi dal punto di vista dell'utente sembra un linguaggio puramente interpretato.

### Caratteristiche principali

* **Ad alto livello** : il programmatore non deve gestire manualmente memoria, registri o dettagli hardware
* **Tipizzazione dinamica** : non serve dichiarare il tipo delle variabili
* **Tipizzazione forte** : non permette operazioni tra tipi incompatibili senza conversione esplicita
* **Multiparadigma** : supporta più stili di programmazione

---

## 3. Paradigmi di programmazione in Python

Python supporta tre paradigmi principali che possono essere usati separatamente o combinati.

### 3.1 Programmazione procedurale

La programmazione procedurale si basa su una serie di istruzioni eseguite in ordine, con funzioni che suddividono il codice in blocchi riutilizzabili.

```python
# definisce una funzione chiamata 'saluta' che riceve un parametro 'nome'
def saluta(nome):
    # stampa a schermo la parola "Ciao" seguita dal valore di 'nome'
    print("Ciao", nome)

# chiama la funzione passando la stringa "Marco"
saluta("Marco")
```

**Quando usarla:** script semplici, automazioni, elaborazioni sequenziali.

---

### 3.2 Programmazione orientata agli oggetti (OOP)

L'OOP organizza il codice in **classi** (modelli/blueprint) e **oggetti** (istanze reali). Ogni oggetto rappresenta un'entità con **stato** (attributi) e **comportamento** (metodi).

```python
# definisce una classe chiamata 'Persona'
class Persona:
    # costruttore: viene chiamato quando si crea un nuovo oggetto
    def __init__(self, nome, eta):
        # assegna l'attributo 'nome' al valore passato
        self.nome = nome
        # assegna l'attributo 'eta' al valore passato
        self.eta = eta
  
    # definisce un metodo (funzione interna alla classe)
    def saluta(self):
        # stampa una frase usando gli attributi dell'oggetto
        # f-string permette di inserire variabili dentro una stringa
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni.")

# crea un oggetto della classe Persona con nome "Anna" e età 30
p1 = Persona("Anna", 30)
# chiama il metodo 'saluta' sull'oggetto creato
p1.saluta()
```

**Quando usarla:** applicazioni complesse, progetti modulari, codice riutilizzabile.

---

### 3.3 Programmazione funzionale

La programmazione funzionale tratta le  **funzioni come oggetti di prima classe** : possono essere salvate in variabili, passate come parametri e restituite da altre funzioni. Promuove l'**immutabilità** (non modificare i dati esistenti) e l'uso di **funzioni pure** (stesso input → stesso output).

```python
# crea una lista di numeri interi
numeri = [1, 2, 3, 4, 5]
# usa 'map' per applicare la funzione lambda (x**2) a ogni elemento della lista
# lambda x: x**2 è una funzione anonima che calcola il quadrato
quadrati = list(map(lambda x: x**2, numeri))
# stampa la nuova lista con i quadrati dei numeri
print(quadrati)  # Output: [1, 4, 9, 16, 25]
```

**Quando usarla:** data science, trasformazioni su collezioni, calcoli matematici.

---

### 3.4 Paradigmi integrati insieme

Python permette di combinare i diversi paradigmi nello stesso programma. È comune mescolare OOP per la struttura generale, procedurale per la logica di flusso e funzionale per le operazioni sui dati.

```python
# definisce una classe chiamata 'Calcolatrice'
class Calcolatrice:
    # costruttore: riceve una lista di numeri
    def __init__(self, numeri):
        # salva la lista come attributo dell'oggetto
        self.numeri = numeri
  
    # metodo: calcola la somma dei numeri
    def somma(self):
        # usa la funzione built-in 'sum' per sommare gli elementi
        return sum(self.numeri)
  
    # metodo: calcola i quadrati di tutti i numeri
    def quadrati(self):
        # usa la funzione 'map' e una lambda per creare una nuova lista
        return list(map(lambda x: x**2, self.numeri))

# crea un oggetto Calcolatrice con la lista [1, 2, 3]
calc = Calcolatrice([1, 2, 3])
# chiama il metodo 'somma' -> stampa 6
print(calc.somma())
# chiama 'quadrati' -> stampa [1, 4, 9]
print(calc.quadrati())
```

---

### 3.5 Riepilogo paradigmi

| Paradigma                        | Caratteristiche principali                         | Esempi d'uso                     |
| -------------------------------- | -------------------------------------------------- | -------------------------------- |
| **Procedurale**            | Codice eseguito in sequenza, con funzioni semplici | Script, automazioni              |
| **Orientato agli oggetti** | Organizzazione in classi e oggetti riutilizzabili  | Applicazioni grandi, moduli      |
| **Funzionale**             | Usa funzioni pure e trasformazioni di dati         | Data science, calcolo matematico |

La potenza di Python sta nella sua  **flessibilità multiparadigma** : consente di scegliere lo stile più adatto al problema, o di combinarli armoniosamente nello stesso progetto.

---

## 4. Installazione e ambiente

### 4.1 Installazione di Python

1. Scaricare l'ultima versione da [python.org/downloads](https://www.python.org/downloads/)
2. Durante l'installazione su  **Windows** :
   * ✅ Selezionare **"Add Python to PATH"** (importante!)
   * Scegliere "Install Now" per configurazione standard
3. Verificare l'installazione aprendo il terminale:
   ```bash
   python --version# Output atteso: Python 3.x.xpip --version# Output atteso: pip x.x.x from...
   ```

**Note per macOS/Linux:**

* Su macOS: Python 3 potrebbe essere installato come `python3`
* Su Linux: solitamente Python è già installato, verificare con `python3 --version`

---

### 4.2 IDE consigliati

**VS Code** (leggero, versatile):

* Scaricare da [code.visualstudio.com](https://code.visualstudio.com/)
* Installare l'estensione "Python" di Microsoft
* Configurare l'interprete Python (Ctrl+Shift+P → "Python: Select Interpreter")

**PyCharm** (completo, professionale):

* Scaricare la Community Edition da [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
* Più pesante ma con più funzionalità integrate

**Alternative:**

* **Jupyter Notebook** : ottimo per data science e sperimentazione
* **Google Colab** : Jupyter notebook online, gratuito
* **IDLE** : editor semplice incluso con Python

---

## 5. Primo script Python

### 5.1 Hello World

```python
# stampa un messaggio sullo schermo
# print() è una funzione built-in (incorporata) di Python
print("Hello, world!")
```

### 5.2 Come eseguirlo

1. Salvare il codice in un file chiamato `hello.py`
2. Aprire il terminale nella cartella del file
3. Eseguire il comando:
   ```bash
   python hello.py
   ```
4. Output atteso:
   ```
   Hello, world!
   ```

### 5.3 Eseguire Python interattivamente (REPL)

Puoi anche usare Python in modalità interattiva:

```bash
# Avviare la shell Python
python

# Appare il prompt >>>
>>> print("Ciao!")
Ciao!
>>> 2 + 2
4
>>> exit()  # per uscire
```

---

## 6. Variabili e tipi di dato

In Python **non serve dichiarare il tipo** delle variabili: viene assegnato automaticamente in base al valore (tipizzazione dinamica).

```python
# stringa (testo)
nome = "Alice"
# intero
eta = 25
# numero decimale (float)
altezza = 1.70
# booleano (vero/falso)
studente = True
```

### 6.1 Tipi fondamentali

| Tipo         | Nome completo           | Esempio                          | Descrizione                                    |
| ------------ | ----------------------- | -------------------------------- | ---------------------------------------------- |
| `int`      | intero                  | `10`                           | Numeri senza decimali                          |
| `float`    | numero a virgola mobile | `3.14`                         | Numeri con decimali                            |
| `str`      | stringa                 | `"ciao"`                       | Testo tra virgolette (singole o doppie)        |
| `bool`     | booleano                | `True`,`False`               | Valore logico                                  |
| `list`     | lista                   | `[1, 2, 3]`                    | Collezione ordinata e modificabile             |
| `tuple`    | tupla                   | `(1, 2, 3)`                    | Collezione ordinata e**non**modificabile |
| `set`      | insieme                 | `{1, 2, 3}`                    | Collezione**senza duplicati**            |
| `dict`     | dizionario              | `{"nome": "Alice", "eta": 25}` | Coppie chiave-valore                           |
| `NoneType` | None                    | `None`                         | Valore nullo/assenza di valore                 |

### 6.2 Verificare il tipo di una variabile

```python
# type() restituisce il tipo di una variabile
nome = "Alice"
print(type(nome))  # <class 'str'>

eta = 25
print(type(eta))   # <class 'int'>
```

### 6.3 Conversione tra tipi (casting)

```python
# Convertire stringa in intero
testo = "42"
numero = int(testo)  # numero diventa 42 (intero)

# Convertire intero in stringa
eta = 25
eta_str = str(eta)   # eta_str diventa "25" (stringa)

# Convertire stringa in float
prezzo = "19.99"
prezzo_num = float(prezzo)  # prezzo_num diventa 19.99 (float)
```

---

## 7. Operatori

### 7.1 Operatori aritmetici

```python
x = 10
y = 3

# somma
print(x + y)   # 13
# sottrazione
print(x - y)   # 7
# moltiplicazione
print(x * y)   # 30
# divisione (restituisce sempre float)
print(x / y)   # 3.3333...
# divisione intera (arrotonda verso il basso)
print(x // y)  # 3
# resto della divisione (modulo)
print(x % y)   # 1
# potenza (elevamento a potenza)
print(x ** y)  # 1000 (10 elevato alla 3)
```

### 7.2 Operatori di confronto

Restituiscono sempre un valore booleano (`True` o `False`).

```python
x = 10
y = 3

# uguale?
print(x == y)  # False
# diverso?
print(x != y)  # True
# maggiore?
print(x > y)   # True
# minore?
print(x < y)   # False
# maggiore o uguale?
print(x >= y)  # True
# minore o uguale?
print(x <= y)  # False
```

### 7.3 Operatori logici

Utilizzati per combinare condizioni booleane.

```python
# AND: entrambe le condizioni devono essere vere
print(True and False)  # False
print(True and True)   # True

# OR: almeno una condizione deve essere vera
print(True or False)   # True
print(False or False)  # False

# NOT: inverte il valore booleano
print(not True)        # False
print(not False)       # True
```

### 7.4 Operatori di assegnazione

```python
x = 5        # assegnazione semplice
x += 3       # equivale a: x = x + 3  (ora x è 8)
x -= 2       # equivale a: x = x - 2  (ora x è 6)
x *= 2       # equivale a: x = x * 2  (ora x è 12)
x /= 3       # equivale a: x = x / 3  (ora x è 4.0)
x //= 2      # equivale a: x = x // 2 (ora x è 2.0)
x %= 2       # equivale a: x = x % 2  (ora x è 0.0)
x ** = 3     # equivale a: x = x ** 3 (ora x è 0.0)
```

---

## 8. Input e Output

### 8.1 Output con print()

```python
# Stampa semplice
print("Ciao, mondo!")

# Stampare più valori separati da spazio
nome = "Alice"
eta = 25
print("Nome:", nome, "Età:", eta)

# Usare f-string (modo moderno e consigliato)
print(f"Nome: {nome}, Età: {eta}")

# Specificare il separatore
print("a", "b", "c", sep="-")  # Output: a-b-c

# Evitare il ritorno a capo
print("Ciao", end=" ")
print("mondo")  # Output: Ciao mondo (sulla stessa riga)
```

### 8.2 Input dall'utente

```python
# input() legge sempre una stringa
nome = input("Inserisci il tuo nome: ")
print("Ciao", nome)

# Per leggere numeri, serve convertire
eta = input("Inserisci la tua età: ")  # eta è una stringa
eta = int(eta)  # convertiamo in intero
print(f"Tra un anno avrai {eta + 1} anni")

# Conversione diretta
altezza = float(input("Inserisci la tua altezza (m): "))
print(f"La tua altezza è {altezza} metri")
```

---

## 9. Strutture di controllo

### 9.1 Condizioni (if, elif, else)

```python
x = 10

# if: esegue il blocco se la condizione è vera
if x > 0:
    print("Positivo")
# elif: altrimenti, se questa condizione è vera
elif x == 0:
    print("Zero")
# else: in tutti gli altri casi
else:
    print("Negativo")
```

**Nota importante:** Python usa l'**indentazione** (spazi all'inizio della riga) per definire i blocchi di codice. Usare sempre 4 spazi.

### 9.2 Operatore ternario (condizione in una riga)

```python
# sintassi: valore_se_vero if condizione else valore_se_falso
eta = 20
categoria = "adulto" if eta >= 18 else "minorenne"
print(categoria)  # adulto
```

### 9.3 Ciclo for

Il ciclo `for` itera su una sequenza (lista, stringa, range, ecc.).

```python
# range(5) genera i numeri da 0 a 4
for i in range(5):
    # stampa ogni numero
    print(i)
# Output: 0, 1, 2, 3, 4

# range(inizio, fine, passo)
for i in range(1, 10, 2):  # da 1 a 9, incremento di 2
    print(i)
# Output: 1, 3, 5, 7, 9

# Iterare su una lista
frutti = ["mela", "banana", "arancia"]
for frutto in frutti:
    print(f"Mi piace la {frutto}")

# Iterare con indice usando enumerate()
for indice, frutto in enumerate(frutti):
    print(f"{indice}: {frutto}")
```

### 9.4 Ciclo while

Il ciclo `while` continua finché la condizione è vera.

```python
x = 3
# continua finché x è maggiore di 0
while x > 0:
    print(x)
    # riduce il valore di x di 1
    x -= 1
# Output: 3, 2, 1

# ATTENZIONE: evitare loop infiniti!
# while True:  # questo continuerebbe all'infinito
#     print("loop infinito")
```

### 9.5 Break e Continue

```python
# break: esce dal ciclo immediatamente
for i in range(10):
    if i == 5:
        break  # esce quando i raggiunge 5
    print(i)
# Output: 0, 1, 2, 3, 4

# continue: salta all'iterazione successiva
for i in range(10):
    if i % 2 == 0:
        continue  # salta i numeri pari
    print(i)
# Output: 1, 3, 5, 7, 9
```

---

## 10. Funzioni

Le funzioni permettono di **riutilizzare** il codice e rendere il programma più  **organizzato** .

### 10.1 Definizione base

```python
# def: keyword per definire una funzione
# somma: nome della funzione
# a, b: parametri (input)
def somma(a, b):
    # return: restituisce un valore
    return a + b

# chiamata della funzione
risultato = somma(3, 4)
# stampa il risultato
print(risultato)  # 7
```

### 10.2 Funzioni senza return

```python
# una funzione può solo eseguire azioni senza restituire valori
def saluta(nome):
    print(f"Ciao {nome}!")
    # se non c'è return, la funzione restituisce None

saluta("Mario")  # Ciao Mario!
```

### 10.3 Parametri con valori di default

```python
# età ha un valore di default di 18
def presenta(nome, eta=18):
    print(f"Mi chiamo {nome} e ho {eta} anni")

# chiamata con entrambi i parametri
presenta("Alice", 25)  # Mi chiamo Alice e ho 25 anni
# chiamata con solo il parametro obbligatorio
presenta("Bob")        # Mi chiamo Bob e ho 18 anni
```

### 10.4 Parametri nominati (keyword arguments)

```python
def crea_profilo(nome, eta, citta):
    print(f"{nome}, {eta} anni, vive a {citta}")

# chiamata con parametri nominati (ordine non importante)
crea_profilo(eta=30, nome="Laura", citta="Roma")
```

### 10.5 Funzioni con numero variabile di argomenti

```python
# *args: accetta un numero variabile di argomenti posizionali
def somma_tutti(*numeri):
    totale = 0
    for num in numeri:
        totale += num
    return totale

print(somma_tutti(1, 2, 3))        # 6
print(somma_tutti(1, 2, 3, 4, 5))  # 15

# **kwargs: accetta un numero variabile di argomenti nominati
def stampa_info(**dati):
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")

stampa_info(nome="Alice", eta=25, citta="Milano")
```

### 10.6 Documentare le funzioni (docstring)

```python
def calcola_area_rettangolo(base, altezza):
    """
    Calcola l'area di un rettangolo.
  
    Parametri:
        base (float): la base del rettangolo
        altezza (float): l'altezza del rettangolo
  
    Restituisce:
        float: l'area del rettangolo
    """
    return base * altezza

# Accedere alla documentazione
print(calcola_area_rettangolo.__doc__)
# oppure con help()
help(calcola_area_rettangolo)
```

---

## 11. Scope (visibilità delle variabili)

Lo **scope** determina dove una variabile è accessibile nel codice.

```python
# variabile globale (accessibile ovunque)
x = 10

def mostra():
    # variabile locale (accessibile solo dentro la funzione)
    x = 5
    print(x)  # stampa la variabile locale

# chiama la funzione
mostra()    # stampa 5
# accede alla variabile globale
print(x)    # stampa 10 (quella globale non è stata modificata)
```

### 11.1 Modificare una variabile globale

```python
x = 10

def modifica():
    # 'global' permette di modificare la variabile globale
    global x
    x = 5
    print(f"Dentro la funzione: x = {x}")

modifica()  # Dentro la funzione: x = 5
print(f"Fuori dalla funzione: x = {x}")  # Fuori dalla funzione: x = 5
```

**Nota:** Modificare variabili globali è generalmente sconsigliato. Meglio passare parametri e restituire valori.

---

## 12. Esercizi pratici

### Esercizio 1: Input e output

Chiedi nome ed età all'utente e stampa: `"Ciao <nome>, hai <età> anni!"`

```python
nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))
print(f"Ciao {nome}, hai {eta} anni!")
```

---

### Esercizio 2: Ciclo for e somma

Calcola la somma dei numeri da 1 a 100.

```python
somma = 0
# range(1, 101) genera numeri da 1 a 100
for i in range(1, 101):
    # aggiunge i alla somma
    somma += i
print(f"La somma è: {somma}")  # 5050
```

---

### Esercizio 3: Condizioni e cicli

Stampa solo i numeri pari tra 1 e 20.

```python
for i in range(1, 21):
    # se il resto della divisione per 2 è zero, è pari
    if i % 2 == 0:
        print(i)
```

---

### Esercizio 4: Funzioni

Crea una funzione che calcoli il quadrato di un numero.

```python
def quadrato(x):
    # ** è l'operatore di elevamento a potenza
    return x ** 2

print(quadrato(5))   # 25
print(quadrato(10))  # 100
```

---

### Esercizio 5: Temperatura (combinazione di concetti)

Crea un programma che converta temperature da Celsius a Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    """Converte temperatura da Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# Richiesta input
celsius = float(input("Inserisci la temperatura in Celsius: "))
# Conversione
fahrenheit = celsius_to_fahrenheit(celsius)
# Output
print(f"{celsius}°C corrispondono a {fahrenheit}°F")
```

---

### Esercizio 6: Numeri primi

Verifica se un numero è primo (divisibile solo per 1 e se stesso).

```python
def is_primo(n):
    """Verifica se un numero è primo"""
    # i numeri minori di 2 non sono primi
    if n < 2:
        return False
    # verifica divisibilità da 2 a n-1
    for i in range(2, n):
        # se è divisibile, non è primo
        if n % i == 0:
            return False
    # se non ha trovato divisori, è primo
    return True

numero = int(input("Inserisci un numero: "))
if is_primo(numero):
    print(f"{numero} è primo")
else:
    print(f"{numero} non è primo")
```

---

## 13. Appendice: Funzioni Lambda

Le **funzioni lambda** sono funzioni anonime (senza nome) definite in una sola riga. Si usano per operazioni semplici e temporanee.

### 13.1 Sintassi di base

```python
# sintassi: lambda argomenti: espressione
lambda x: x ** 2
```

* `lambda`: keyword per creare la funzione
* `x`: parametro di input
* `x ** 2`: espressione che viene restituita automaticamente

### 13.2 Esempio base

```python
# assegnare lambda a una variabile
quadrato = lambda x: x ** 2
# chiamare la funzione
print(quadrato(4))  # 16
```

Equivalente a:

```python
def quadrato(x):
    return x ** 2
```

### 13.3 Lambda con map()

`map()` applica una funzione a ogni elemento di una sequenza.

```python
numeri = [1, 2, 3, 4, 5]
# moltiplica ogni elemento per 10
risultato = list(map(lambda x: x * 10, numeri))
print(risultato)  # [10, 20, 30, 40, 50]
```

### 13.4 Lambda con filter()

`filter()` mantiene solo gli elementi per cui la funzione restituisce `True`.

```python
numeri = [1, 2, 3, 4, 5, 6]
# filtra solo i numeri pari (divisibili per 2)
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)  # [2, 4, 6]
```

### 13.5 Lambda con sorted()

```python
nomi = ["Luca", "Anna", "Giovanni", "Bea"]
# ordina in base alla lunghezza del nome
ordinati = sorted(nomi, key=lambda n: len(n))
print(ordinati)  # ['Bea', 'Luca', 'Anna', 'Giovanni']
```

### 13.6 Lambda con più parametri

```python
# lambda con due parametri
somma = lambda a, b: a + b
print(somma(3, 5))  # 8

# lambda con tre parametri
media = lambda a, b, c: (a + b + c) / 3
print(media(10, 20, 30))  # 20.0
```

### 13.7 Quando usare lambda

✅ **Usare lambda quando:**

* La funzione è molto breve (una sola espressione)
* Serve solo in un punto del codice
* Si passa come parametro a funzioni come `map()`, `filter()`, `sorted()`

❌ **Evitare lambda quando:**

* Serve una logica complessa o più istruzioni
* La funzione deve essere riutilizzata in più punti
* Serve documentazione (docstring)

### 13.8 Riepilogo lambda

Le funzioni lambda rendono il codice più **conciso** e **leggibile** quando si vogliono definire funzioni semplici al volo. Sono uno strumento fondamentale della **programmazione funzionale** in Python, perfette per operazioni rapide come trasformazioni o filtri su liste e collezioni di dati.

---

## 14. Best Practices e Consigli

### 14.1 Convenzioni di stile (PEP 8)

PEP 8 è la guida ufficiale di stile per Python. Alcuni punti chiave:

```python
# Nomi delle variabili: snake_case (parole minuscole separate da _)
nome_completo = "Mario Rossi"
eta_utente = 25

# Nomi delle costanti: MAIUSCOLE
PI_GRECO = 3.14159
MAX_TENTATIVI = 3

# Nomi delle classi: PascalCase (ogni parola inizia con maiuscola)
class CalcolatriceScientifica:
    pass

# Nomi delle funzioni: snake_case
def calcola_area_cerchio(raggio):
    return PI_GRECO * raggio ** 2

# Spazi intorno agli operatori
x = 5 + 3  # ✅ corretto
x=5+3      # ❌ scorretto (mancano spazi)

# Indentazione: 4 spazi (non tab)
if x > 0:
    print("positivo")  # 4 spazi di indentazione

# Lunghezza massima riga: 79 caratteri
# Se una riga è troppo lunga, spezzarla
risultato = funzione_con_nome_lungo(
    parametro1,
    parametro2,
    parametro3
)
```

### 14.2 Commenti efficaci

```python
# ✅ Buon commento: spiega il PERCHÉ
# Usiamo la formula di Gauss per ottimizzare il calcolo
somma = n * (n + 1) // 2

# ❌ Commento inutile: ripete cosa fa il codice
x = x + 1  # incrementa x di 1

# Docstring per documentare funzioni
def calcola_sconto(prezzo, percentuale):
    """
    Calcola il prezzo finale dopo aver applicato uno sconto.
  
    Args:
        prezzo (float): prezzo originale del prodotto
        percentuale (float): percentuale di sconto (0-100)
  
    Returns:
        float: prezzo finale scontato
    """
    return prezzo * (1 - percentuale / 100)
```

### 14.3 Errori comuni da evitare

```python
# ❌ ERRORE: Confrontare con True/False esplicitamente
if condizione == True:
    pass

# ✅ CORRETTO: Usare direttamente la condizione
if condizione:
    pass

# ❌ ERRORE: Usare variabili mutabili come default
def aggiungi_elemento(elemento, lista=[]):  # ❌ pericoloso!
    lista.append(elemento)
    return lista

# ✅ CORRETTO: Usare None e creare nuova lista
def aggiungi_elemento(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

# ❌ ERRORE: Dimenticare la conversione di input()
eta = input("Età: ")
if eta > 18:  # ❌ TypeError! eta è stringa

# ✅ CORRETTO: Convertire sempre input()
eta = int(input("Età: "))
if eta > 18:  # ✅ funziona
    pass
```

### 14.4 Debugging - Tecniche base

```python
# Usare print() per debugging
def calcola_media(numeri):
    print(f"DEBUG: numeri = {numeri}")  # stampa input
    totale = sum(numeri)
    print(f"DEBUG: totale = {totale}")  # stampa valore intermedio
    media = totale / len(numeri)
    print(f"DEBUG: media = {media}")    # stampa risultato
    return media

# Verificare il tipo delle variabili
x = "42"
print(f"Tipo di x: {type(x)}")  # <class 'str'>

# Usare assert per verificare condizioni
def dividi(a, b):
    assert b != 0, "Il divisore non può essere zero!"
    return a / b
```

---

## 15. Riepilogo Giorno 1

### Concetti chiave appresi

✅ **Python è:**

* Un linguaggio ibrido (compilato in bytecode + interpretato)
* Ad alto livello e multiparadigma
* Con tipizzazione dinamica e forte

✅ **Tipi di dato fondamentali:**

* `int`, `float`, `str`, `bool`
* Collezioni: `list`, `tuple`, `set`, `dict`

✅ **Operatori:**

* Aritmetici: `+`, `-`, `*`, `/`, `//`, `%`, `**`
* Confronto: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Logici: `and`, `or`, `not`

✅ **Strutture di controllo:**

* Condizioni: `if`, `elif`, `else`
* Cicli: `for`, `while`
* Controllo flusso: `break`, `continue`

✅ **Funzioni:**

* Definizione con `def`
* Parametri e valori di ritorno
* Parametri default e `*args`/`**kwargs`
* Funzioni lambda per operazioni semplici

✅ **Scope:**

* Variabili locali vs globali
* Uso di `global` (da evitare quando possibile)

---

## 16. Esercizi di riepilogo

### Esercizio 7: Calcolatrice semplice

```python
def calcolatrice():
    """Calcolatrice interattiva semplice"""
    print("Calcolatrice Python")
    print("Operazioni: +, -, *, /")
  
    # Input numeri
    a = float(input("Primo numero: "))
    b = float(input("Secondo numero: "))
    operazione = input("Operazione (+, -, *, /): ")
  
    # Calcolo basato sull'operazione
    if operazione == "+":
        risultato = a + b
    elif operazione == "-":
        risultato = a - b
    elif operazione == "*":
        risultato = a * b
    elif operazione == "/":
        if b != 0:
            risultato = a / b
        else:
            print("Errore: divisione per zero!")
            return
    else:
        print("Operazione non valida!")
        return
  
    print(f"Risultato: {risultato}")

# Esegui
calcolatrice()
```

### Esercizio 8: FizzBuzz

Un classico problema di programmazione: stampa i numeri da 1 a 100, ma:

* Per multipli di 3 stampa "Fizz"
* Per multipli di 5 stampa "Buzz"
* Per multipli di entrambi stampa "FizzBuzz"

```python
def fizzbuzz():
    """Implementazione del classico problema FizzBuzz"""
    for i in range(1, 101):
        # Controlla prima multipli di entrambi (3 E 5)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Poi multipli solo di 3
        elif i % 3 == 0:
            print("Fizz")
        # Poi multipli solo di 5
        elif i % 5 == 0:
            print("Buzz")
        # Altrimenti stampa il numero
        else:
            print(i)

fizzbuzz()
```

### Esercizio 9: Indovina il numero

```python
import random

def indovina_numero():
    """Gioco: l'utente deve indovinare un numero da 1 a 100"""
    # Genera numero casuale
    numero_segreto = random.randint(1, 100)
    tentativi = 0
  
    print("Ho pensato a un numero tra 1 e 100!")
    print("Prova a indovinarlo!")
  
    while True:
        # Input utente
        tentativo = int(input("Il tuo numero: "))
        tentativi += 1
      
        # Controlla se ha indovinato
        if tentativo == numero_segreto:
            print(f"Complimenti! Hai indovinato in {tentativi} tentativi!")
            break
        elif tentativo < numero_segreto:
            print("Troppo basso! Riprova.")
        else:
            print("Troppo alto! Riprova.")

# Esegui il gioco
indovina_numero()
```

### Esercizio 10: Analisi testo

```python
def analizza_testo(testo):
    """Analizza un testo e restituisce statistiche"""
    # Conta caratteri (totali e senza spazi)
    num_caratteri = len(testo)
    num_caratteri_no_spazi = len(testo.replace(" ", ""))
  
    # Conta parole
    parole = testo.split()
    num_parole = len(parole)
  
    # Conta vocali
    vocali = "aeiouAEIOU"
    num_vocali = sum(1 for char in testo if char in vocali)
  
    # Stampa statistiche
    print(f"Caratteri totali: {num_caratteri}")
    print(f"Caratteri (senza spazi): {num_caratteri_no_spazi}")
    print(f"Parole: {num_parole}")
    print(f"Vocali: {num_vocali}")
  
    # Trova parola più lunga
    if parole:
        parola_lunga = max(parole, key=len)
        print(f"Parola più lunga: {parola_lunga} ({len(parola_lunga)} lettere)")

# Test
testo = input("Inserisci un testo: ")
analizza_testo(testo)
```

---

## 17. Preparazione per il Giorno 2

Nel **Giorno 2** approfondiremo:

* **Strutture dati avanzate** : liste, tuple, set, dizionari
* **Manipolazione stringhe** : metodi utili, formattazione, regex base
* **File I/O** : leggere e scrivere file di testo e CSV
* **Moduli e pacchetti** : import, libreria standard
* **Virtual environment** : gestione dipendenze con pip

### Compiti per casa (opzionali)

1. Rifare tutti gli esercizi visti oggi senza guardare le soluzioni
2. Creare una funzione che verifichi se una parola è palindroma (es. "anna")
3. Scrivere un programma che calcoli il fattoriale di un numero usando sia cicli che ricorsione
4. Esplorare la documentazione Python: [docs.python.org](https://docs.python.org/3/)

---

## 🔗 Riferimenti utili

### Documentazione ufficiale

* [Python Documentation](https://docs.python.org/3/) - Documentazione completa
* [Python Tutorial](https://docs.python.org/3/tutorial/) - Tutorial ufficiale
* [PEP 8 Style Guide](https://pep8.org/) - Guida di stile

### Tutorial e risorse

* [W3Schools Python](https://www.w3schools.com/python/) - Tutorial interattivo
* [Real Python](https://realpython.com/) - Articoli e tutorial approfonditi
* [Python.org Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)

### Esercizi e pratica

* [Exercism Python Track](https://exercism.org/tracks/python) - Esercizi guidati
* [HackerRank Python](https://www.hackerrank.com/domains/python) - Sfide di programmazione
* [LeetCode](https://leetcode.com/) - Problemi algoritmici

### Community

* [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - Q&A
* [r/learnpython](https://www.reddit.com/r/learnpython/) - Subreddit per principianti
* [Python Discord](https://pythondiscord.com/) - Community Discord

---

## 📝 Note finali

Congratulazioni per aver completato il **Giorno 1** del corso Python!

**Punti chiave da ricordare:**

* Python è **facile da imparare** ma **potente**
* L'**indentazione** è fondamentale (4 spazi)
* Le **funzioni** rendono il codice riutilizzabile
* **Pratica costante** è la chiave per imparare

**Prossimi passi:**

* Rivedere gli esempi e provare variazioni
* Fare gli esercizi proposti
* Sperimentare con il codice nella REPL
* Preparare domande per il Giorno 2

**Ricorda:** Non c'è bisogno di memorizzare tutto! L'importante è capire i concetti e sapere dove cercare quando serve aiuto (documentazione, Google, Stack Overflow).

Ci vediamo al  **Giorno 2** ! 🚀
