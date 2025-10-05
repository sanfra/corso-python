# Tipologie di Linguaggi di Programmazione

## Introduzione

I linguaggi di programmazione possono essere classificati in base a **come** il codice viene trasformato in istruzioni che il computer può eseguire. Esistono tre categorie principali:  **linguaggi compilati** , **linguaggi interpretati** e  **linguaggi ibridi** .

Prima di capire le differenze, è importante sapere che:

* Il computer capisce solo **linguaggio macchina** (sequenze di 0 e 1)
* Noi scriviamo codice in **linguaggi ad alto livello** (più comprensibili per gli umani)
* Serve un "traduttore" per convertire il nostro codice in linguaggio macchina

---

## 1. Linguaggi Compilati

### Come Funzionano

Un **linguaggio compilato** richiede un passaggio di **compilazione** prima dell'esecuzione. Il codice sorgente viene trasformato completamente in linguaggio macchina (file eseguibile) prima di essere eseguito.

### Il Processo

```
Codice Sorgente (.c, .cpp, .java)
         ↓
    COMPILATORE
         ↓
File Eseguibile (.exe, .out)
         ↓
    ESECUZIONE
```

### Fasi della Compilazione

1. **Scrittura del codice** : scrivi il programma in un file (es. `program.c`)
2. **Compilazione** : il compilatore traduce tutto il codice in linguaggio macchina
3. **Creazione eseguibile** : si genera un file eseguibile (es. `program.exe`)
4. **Esecuzione** : esegui il file già compilato

### Esempio Pratico (C)

```c
// File: hello.c
#include <stdio.h>

// Funzione principale del programma
int main() {
    // Stampa un messaggio
    printf("Ciao, mondo!\n");
    // return 0 indica che il programma è terminato correttamente
    return 0;
}
```

**Per eseguire questo programma:**

```bash
# Passo 1: Compila il codice (crea l'eseguibile)
gcc hello.c -o hello.exe

# Passo 2: Esegui il file compilato
./hello.exe
```

### Vantaggi dei Linguaggi Compilati

✅  **Velocità di esecuzione** : il codice è già in linguaggio macchina, quindi molto veloce
✅  **Ottimizzazione** : il compilatore può ottimizzare il codice durante la compilazione
✅  **Errori anticipati** : molti errori vengono trovati durante la compilazione
✅  **Sicurezza** : il codice sorgente non è distribuito, solo l'eseguibile

### Svantaggi dei Linguaggi Compilati

❌  **Tempo di sviluppo** : devi ricompilare ogni volta che modifichi il codice
❌  **Portabilità** : l'eseguibile funziona solo sul sistema operativo per cui è stato compilato
❌  **Debugging più difficile** : trovare errori può essere più complesso

### Esempi di Linguaggi Compilati

* **C** : linguaggio di sistema, molto veloce
* **C++** : estensione di C con supporto OOP
* **Rust** : linguaggio moderno, sicuro e performante
* **Go** : creato da Google, semplice e veloce

---

## 2. Linguaggi Interpretati

### Come Funzionano

Un **linguaggio interpretato** viene eseguito **riga per riga** da un programma chiamato  **interprete** . Non c'è bisogno di compilare prima: l'interprete legge, traduce ed esegue il codice in tempo reale.

### Il Processo

```
Codice Sorgente (.py, .js, .rb)
         ↓
    INTERPRETE
         ↓
    ESECUZIONE (riga per riga)
```

### Fasi dell'Interpretazione

1. **Scrittura del codice** : scrivi il programma in un file (es. `script.py`)
2. **Esecuzione diretta** : l'interprete legge e esegue il codice immediatamente
3. **Nessun file intermedio** : non si crea un eseguibile

### Esempio Pratico (Python)

```python
# File: hello.py

# Stampa un messaggio (eseguito immediatamente dall'interprete)
print("Ciao, mondo!")

# Definiamo una funzione
def saluta(nome):
    # f-string per formattare la stringa
    return f"Ciao, {nome}!"

# Chiamiamo la funzione
risultato = saluta("Mario")
# Stampiamo il risultato
print(risultato)
```

**Per eseguire questo programma:**

```bash
# Un solo comando: l'interprete Python esegue direttamente il file
python hello.py
```

### Vantaggi dei Linguaggi Interpretati

✅  **Sviluppo rapido** : scrivi ed esegui immediatamente, senza compilare
✅  **Portabilità** : lo stesso codice funziona su qualsiasi sistema con l'interprete
✅  **Debugging facile** : errori più chiari e immediati
✅  **Flessibilità** : puoi modificare il codice anche durante l'esecuzione (in alcuni casi)
✅  **REPL** : puoi testare codice interattivamente (Read-Eval-Print Loop)

### Svantaggi dei Linguaggi Interpretati

❌  **Velocità** : più lenti dei linguaggi compilati (traduzione in tempo reale)
❌  **Dipendenza dall'interprete** : serve l'interprete installato sul sistema
❌  **Codice esposto** : il codice sorgente è distribuito e leggibile
❌  **Errori a runtime** : alcuni errori emergono solo durante l'esecuzione

### Esempi di Linguaggi Interpretati

* **Python** : versatile, facile da imparare
* **JavaScript** : linguaggio del web (browser)
* **Ruby** : elegante, usato per web development
* **PHP** : server-side scripting per il web
* **Bash/Shell** : script per automazione di sistema

---

## 3. Linguaggi Ibridi

### Come Funzionano

I **linguaggi ibridi** combinano compilazione e interpretazione. Il codice viene prima **compilato in bytecode** (codice intermedio), poi questo bytecode viene **interpretato** da una macchina virtuale.

### Il Processo

```
Codice Sorgente (.java, .py)
         ↓
    COMPILATORE
         ↓
    BYTECODE (.class, .pyc)
         ↓
    MACCHINA VIRTUALE (JVM, PVM)
         ↓
    ESECUZIONE
```

### Fasi del Processo Ibrido

1. **Scrittura del codice** : scrivi il programma (es. `Program.java`)
2. **Compilazione in bytecode** : il compilatore crea bytecode
3. **Bytecode** : codice intermedio, non linguaggio macchina ma nemmeno codice sorgente
4. **Interpretazione** : la macchina virtuale interpreta il bytecode
5. **Esecuzione** : il programma viene eseguito

### Esempio Pratico (Java)

```java
// File: Hello.java

// Definiamo una classe pubblica (il nome deve corrispondere al file)
public class Hello {
    // main è il punto di ingresso del programma
    // 'static' significa che appartiene alla classe, non a un oggetto
    // 'void' significa che non restituisce nulla
    // String[] args sono gli argomenti da linea di comando
    public static void main(String[] args) {
        // System.out.println stampa un messaggio
        System.out.println("Ciao, mondo!");
    }
}
```

**Per eseguire questo programma:**

```bash
# Passo 1: Compila in bytecode (crea Hello.class)
javac Hello.java

# Passo 2: La JVM (Java Virtual Machine) interpreta il bytecode
java Hello
```

### Vantaggi dei Linguaggi Ibridi

✅  **Portabilità** : "Write once, run anywhere" - il bytecode funziona ovunque ci sia la VM
✅  **Ottimizzazione** : la VM può ottimizzare il bytecode durante l'esecuzione (JIT)
✅  **Bilanciamento** : compromesso tra velocità e flessibilità
✅  **Sicurezza** : il bytecode può essere verificato prima dell'esecuzione

### Svantaggi dei Linguaggi Ibridi

❌  **Complessità** : sistema più complesso rispetto a interpretati puri
❌  **Overhead** : la VM aggiunge un livello di astrazione
❌  **Dipendenza dalla VM** : serve la macchina virtuale installata
❌  **Startup lento** : caricare la VM può richiedere tempo

### Esempi di Linguaggi Ibridi

* **Java** : bytecode eseguito dalla JVM (Java Virtual Machine)
* **C#** : bytecode eseguito dal CLR (Common Language Runtime)
* **Python** : compila in `.pyc` (bytecode) eseguito dalla PVM (Python Virtual Machine)
* **Scala** : compila in bytecode Java
* **Kotlin** : compila in bytecode Java

---

## Python: Un Caso Speciale

Python è tecnicamente un  **linguaggio ibrido** , anche se spesso viene definito "interpretato" per semplicità.

### Come Funziona Python Realmente

```
Codice Python (.py)
         ↓
    COMPILAZIONE AUTOMATICA
         ↓
    BYTECODE (.pyc nella cartella __pycache__)
         ↓
    PVM (Python Virtual Machine)
         ↓
    ESECUZIONE
```

### Il Processo in Dettaglio

1. **Scrivi il codice** : crei un file `script.py`
2. **Esecuzione** : digiti `python script.py`
3. **Compilazione automatica** : Python compila il codice in bytecode
4. **Bytecode** : salvato in file `.pyc` (se possibile, per velocizzare esecuzioni future)
5. **Interpretazione** : la PVM interpreta il bytecode
6. **Esecuzione** : il programma viene eseguito

### Perché Python Sembra Interpretato?

La compilazione in bytecode è **trasparente** all'utente:

* Avviene automaticamente
* Non devi compilare manualmente
* I file `.pyc` sono nascosti nella cartella `__pycache__`
* Puoi eseguire direttamente con `python script.py`

### Esempio Pratico

```python
# File: esempio.py

# Questo codice viene automaticamente compilato in bytecode
def calcola_quadrato(numero):
    # Calcola il quadrato di un numero
    risultato = numero ** 2
    # Restituisce il risultato
    return risultato

# Quando esegui questo file, Python:
# 1. Compila questo codice in bytecode
# 2. Salva il bytecode in __pycache__/esempio.cpython-XX.pyc
# 3. La PVM esegue il bytecode

# Loop per calcolare i quadrati da 1 a 5
for i in range(1, 6):
    # Chiamiamo la funzione
    quadrato = calcola_quadrato(i)
    # Stampiamo il risultato
    print(f"Il quadrato di {i} è {quadrato}")
```

**Esecuzione:**

```bash
# Esegui il file
python esempio.py

# Python automaticamente:
# - Compila in bytecode
# - Crea __pycache__/esempio.cpython-39.pyc (o simile)
# - Esegue il bytecode tramite la PVM
```

### File .pyc (Python Compiled)

```python
# Quando importi un modulo, Python crea automaticamente il .pyc

# File: modulo_helper.py
def somma(a, b):
    return a + b

# File: main.py
# Quando fai l'import, Python compila modulo_helper.py in .pyc
import modulo_helper

# La prossima volta che importi, Python usa il .pyc (più veloce)
risultato = modulo_helper.somma(5, 3)
print(risultato)
```

---

## Caratteristiche di Python

### 1. Tipizzazione Dinamica

Python non richiede di dichiarare il tipo delle variabili. Il tipo viene determinato automaticamente a runtime.

```python
# Non serve dichiarare il tipo
x = 5           # x è un intero
x = "ciao"      # ora x è una stringa (cambio di tipo permesso!)
x = [1, 2, 3]   # ora x è una lista

# Python determina il tipo automaticamente
numero = 42              # int
decimale = 3.14          # float
testo = "Python"         # str
lista = [1, 2, 3]        # list
dizionario = {"a": 1}    # dict
```

**Confronto con Java (tipizzazione statica):**

```java
// In Java devi dichiarare il tipo
int x = 5;
// x = "ciao";  // ERRORE! x è int, non può essere string
String nome = "Mario";
```

### 2. Tipizzazione Forte

Anche se dinamica, Python è  **fortemente tipizzato** : non puoi fare operazioni tra tipi incompatibili senza conversione esplicita.

```python
# Python impedisce operazioni tra tipi incompatibili
numero = 5
testo = "10"

# Questo darebbe ERRORE
# risultato = numero + testo  # TypeError!

# Devi convertire esplicitamente
risultato = numero + int(testo)      # Converto testo in int: 15
risultato = str(numero) + testo      # Converto numero in str: "510"
```

**Confronto con JavaScript (tipizzazione debole):**

```javascript
// JavaScript converte automaticamente (coercion)
let risultato = 5 + "10";  // "510" (converte 5 in stringa)
```

### 3. Linguaggio Multi-Paradigma

Python supporta diversi stili di programmazione:

#### Programmazione Procedurale

```python
# Stile procedurale: sequenza di istruzioni e funzioni

# Definiamo una funzione
def calcola_area_rettangolo(base, altezza):
    # Calcoliamo l'area
    area = base * altezza
    # Restituiamo il risultato
    return area

# Chiamiamo la funzione
base = 5
altezza = 3
area = calcola_area_rettangolo(base, altezza)
print(f"Area: {area}")
```

#### Programmazione Orientata agli Oggetti (OOP)

```python
# Stile OOP: organizzato in classi e oggetti

# Definiamo una classe
class Rettangolo:
    # Costruttore
    def __init__(self, base, altezza):
        # Attributi dell'oggetto
        self.base = base
        self.altezza = altezza
  
    # Metodo per calcolare l'area
    def area(self):
        # Usiamo gli attributi dell'oggetto
        return self.base * self.altezza

# Creiamo un oggetto
rett = Rettangolo(5, 3)
# Chiamiamo il metodo
print(f"Area: {rett.area()}")
```

#### Programmazione Funzionale

```python
# Stile funzionale: usa funzioni pure, immutabilità, composizione

# Lambda: funzione anonima (senza nome)
# lambda parametri: espressione
quadrato = lambda x: x ** 2

# map: applica una funzione a ogni elemento di una lista
numeri = [1, 2, 3, 4, 5]
# map(funzione, lista) applica la funzione a ogni elemento
quadrati = list(map(quadrato, numeri))
print(quadrati)  # [1, 4, 9, 16, 25]

# filter: filtra elementi in base a una condizione
# lambda x: x % 2 == 0 controlla se x è pari
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)  # [2, 4]

# List comprehension: modo compatto di creare liste
# [espressione for elemento in lista if condizione]
quadrati_pari = [x**2 for x in numeri if x % 2 == 0]
print(quadrati_pari)  # [4, 16]
```

### 4. Gestione Automatica della Memoria

Python ha un **garbage collector** che gestisce automaticamente la memoria.

```python
# Crei oggetti senza preoccuparti della memoria
lista_grande = [i for i in range(1000000)]

# Quando lista_grande non serve più, Python la elimina automaticamente
# Non devi fare nulla (no free() o delete come in C/C++)

def crea_lista():
    # Questa lista esiste solo dentro la funzione
    lista_temporanea = [1, 2, 3, 4, 5]
    return lista_temporanea[0]

# Quando la funzione termina, lista_temporanea viene eliminata automaticamente
risultato = crea_lista()
```

**Garbage Collection in azione:**

```python
import sys

# Creiamo un oggetto
class MioOggetto:
    pass

# Creiamo un'istanza
obj = MioOggetto()
# sys.getrefcount conta i riferimenti all'oggetto
print(sys.getrefcount(obj))  # 2 (obj + parametro getrefcount)

# Creiamo un altro riferimento
obj2 = obj
print(sys.getrefcount(obj))  # 3

# Rimuoviamo i riferimenti
obj = None
obj2 = None
# Ora l'oggetto non ha più riferimenti
# Il garbage collector lo eliminerà automaticamente
```

### 5. Duck Typing

"Se cammina come un'anatra e fa qua qua come un'anatra, è un'anatra"

```python
# Non importa il tipo dell'oggetto, importa cosa sa fare

# Classe Pato (Anatra in spagnolo)
class Pato:
    # Metodo per nuotare
    def nuota(self):
        return "Sto nuotando"

# Classe Persona
class Persona:
    # Anche la persona ha un metodo nuota
    def nuota(self):
        return "Sto facendo il crawl"

# Classe Pesce
class Pesce:
    # Anche il pesce ha un metodo nuota
    def nuota(self):
        return "Sto pinneggiando"

# Funzione che accetta qualsiasi oggetto con il metodo nuota()
# Non specifichiamo il tipo!
def fai_nuotare(essere):
    # Se l'oggetto ha nuota(), funziona
    # Non ci interessa se è Pato, Persona o Pesce
    print(essere.nuota())

# Funziona con tutti
fai_nuotare(Pato())      # Sto nuotando
fai_nuotare(Persona())   # Sto facendo il crawl
fai_nuotare(Pesce())     # Sto pinneggiando
```

### 6. Indentazione Significativa

Python usa l'**indentazione** (spazi all'inizio della riga) per definire i blocchi di codice, invece delle parentesi graffe `{}`.

```python
# L'indentazione è OBBLIGATORIA e definisce la struttura

# Funzione: il corpo è indentato
def mia_funzione():
    # Questo è dentro la funzione (4 spazi)
    print("Sono dentro la funzione")
  
    # Condizione: il corpo è ulteriormente indentato
    if True:
        # Questo è dentro l'if (8 spazi)
        print("Sono dentro l'if")
  
    # Questo è ancora dentro la funzione (4 spazi)
    print("Sono tornato nella funzione")

# Questo è fuori dalla funzione (0 spazi)
print("Sono fuori dalla funzione")
```

**Confronto con altri linguaggi:**

```java
// Java usa le parentesi graffe
public void miaFunzione() {
    System.out.println("Dentro la funzione");
  
    if (true) {
        System.out.println("Dentro l'if");
    }
  
    System.out.println("Ancora nella funzione");
}
```

### 7. Batterie Incluse (Batteries Included)

Python include una **libreria standard** molto ricca. Puoi fare molte cose senza installare librerie esterne.

```python
# Lavorare con file
import os
# os.listdir elenca i file in una cartella
# '.' significa cartella corrente
file_in_cartella = os.listdir('.')
print(file_in_cartella)

# Lavorare con date
import datetime
# datetime.datetime.now() restituisce data e ora correnti
oggi = datetime.datetime.now()
print(f"Oggi è {oggi}")

# Lavorare con JSON
import json
# Dizionario Python
dati = {"nome": "Mario", "età": 30}
# json.dumps converte in stringa JSON
json_string = json.dumps(dati)
print(json_string)  # {"nome": "Mario", "età": 30}

# Richieste HTTP
import urllib.request
# Scarica il contenuto di una pagina web
# response = urllib.request.urlopen('http://example.com')
# html = response.read()

# Matematica avanzata
import math
# math.sqrt calcola la radice quadrata
radice = math.sqrt(16)
print(radice)  # 4.0

# Espressioni regolari
import re
# re.findall cerca pattern in una stringa
# r'\d+' cerca sequenze di cifre
numeri = re.findall(r'\d+', 'Ho 3 gatti e 2 cani')
print(numeri)  # ['3', '2']
```

### 8. Interpretato Interattivamente (REPL)

Python offre una **REPL** (Read-Eval-Print Loop) per testare codice interattivamente.

```python
# Puoi aprire la shell Python digitando 'python' nel terminale
# Poi scrivere codice che viene eseguito immediatamente

>>> 2 + 2
4

>>> nome = "Mario"
>>> print(f"Ciao {nome}")
Ciao Mario

>>> def somma(a, b):
...     return a + b
...
>>> somma(5, 3)
8

>>> [x**2 for x in range(5)]
[0, 1, 4, 9, 16]
```

### 9. Gestione delle Eccezioni

Python usa un sistema robusto di gestione degli errori.

```python
# try-except per gestire gli errori

# Funzione che divide due numeri
def dividi(a, b):
    # try: prova a eseguire questo codice
    try:
        # Tentiamo la divisione
        risultato = a / b
        return risultato
    # except: se c'è un errore, esegui questo
    except ZeroDivisionError:
        # Questo blocco viene eseguito se b è zero
        print("Errore: divisione per zero!")
        return None
    # except generico per altri errori
    except Exception as e:
        # 'as e' cattura l'oggetto errore
        print(f"Errore imprevisto: {e}")
        return None
    # finally: eseguito sempre, con o senza errore
    finally:
        print("Operazione completata")

# Esempi di utilizzo
print(dividi(10, 2))   # 5.0, poi "Operazione completata"
print(dividi(10, 0))   # Errore, poi None, poi "Operazione completata"
```

### 10. Comprensioni (Comprehensions)

Modo conciso di creare collezioni.

```python
# List comprehension
# [espressione for elemento in iterabile if condizione]

# Crea una lista di quadrati
quadrati = [x**2 for x in range(10)]
print(quadrati)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Crea una lista di numeri pari
pari = [x for x in range(20) if x % 2 == 0]
print(pari)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Dictionary comprehension
# {chiave: valore for elemento in iterabile}
quadrati_dict = {x: x**2 for x in range(5)}
print(quadrati_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
# {espressione for elemento in iterabile}
quadrati_set = {x**2 for x in range(-3, 4)}
print(quadrati_set)  # {0, 1, 4, 9} (no duplicati)
```

---

## Tabella Comparativa

| Caratteristica                       | Compilato  | Interpretato | Ibrido     | Python     |
| ------------------------------------ | ---------- | ------------ | ---------- | ---------- |
| **Velocità di esecuzione**    | ⭐⭐⭐⭐⭐ | ⭐⭐         | ⭐⭐⭐     | ⭐⭐⭐     |
| **Velocità di sviluppo**      | ⭐⭐       | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐   | ⭐⭐⭐⭐⭐ |
| **Portabilità**               | ⭐⭐       | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Debugging**                  | ⭐⭐       | ⭐⭐⭐⭐     | ⭐⭐⭐     | ⭐⭐⭐⭐   |
| **Facilità di apprendimento** | ⭐⭐       | ⭐⭐⭐⭐     | ⭐⭐⭐     | ⭐⭐⭐⭐⭐ |

---

## Quando Usare Python?

✅ **Ideale per:**

* Sviluppo rapido di prototipi
* Scripting e automazione
* Data Science e Machine Learning
* Web development (Django, Flask)
* Didattica e apprendimento
* Progetti dove la velocità di sviluppo è più importante della velocità di esecuzione

❌ **Meno adatto per:**

* Applicazioni real-time critiche
* Sistemi embedded con risorse limitate
* Applicazioni che richiedono massime prestazioni (game engines, HFT)
* Mobile development (nativo)

---

## Riepilogo

### Linguaggi Compilati

* Traduzione completa prima dell'esecuzione
* Molto veloci
* Esempi: C, C++, Rust

### Linguaggi Interpretati

* Esecuzione diretta riga per riga
* Sviluppo rapido e flessibile
* Esempi: JavaScript, Ruby, PHP

### Linguaggi Ibridi

* Compilazione in bytecode + interpretazione
* Bilanciamento tra velocità e portabilità
* Esempi: Java, C#, Python

### Python è:

* ✅ Ibrido (bytecode + PVM)
* ✅ Tipizzazione dinamica e forte
* ✅ Multi-paradigma
* ✅ Gestione automatica memoria
* ✅ Duck typing
* ✅ Indentazione significativa
* ✅ Libreria standard ricca
* ✅ REPL integrato
* ✅ Facile da imparare
