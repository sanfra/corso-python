# 🐍 Corso Python – Giorno 2

## Lezione 2: Strutture Dati e Strumenti di Lavoro

### 🎯 Obiettivi della lezione

- Comprendere e utilizzare le principali strutture dati di Python
- Manipolare stringhe e file
- Gestire pacchetti e ambienti virtuali
- Reimplementare piccoli programmi scritti in altri linguaggi

---

## 1. Liste, Tuple, Set, Dizionari

### Liste

```python
frutti = ["mela", "banana", "pera"]
print(frutti)           # stampa l'intera lista
print(frutti[0])        # accesso per indice -> 'mela'
frutti.append("kiwi")   # aggiunge un elemento
print(len(frutti))      # numero di elementi
```

### Tuple

```python
coordinate = (10, 20)
print(coordinate[0])    # accesso per indice -> 10
# coordinate[0] = 5     # errore: le tuple non si modificano
```

### Set

```python
numeri = {1, 2, 3, 3}
print(numeri)           # elimina i duplicati -> {1, 2, 3}
numeri.add(4)
print(2 in numeri)      # verifica presenza elemento -> True
```

### Dizionari

```python
persona = {"nome": "Anna", "eta": 30}
print(persona["nome"])           # accesso per chiave -> 'Anna'
persona["citta"] = "Torino"      # aggiunge una chiave
print(persona.keys())            # mostra tutte le chiavi
```

---

## 2. Gestione delle stringhe

```python
testo = "  Ciao Mondo  "
print(testo.lower())       # tutto minuscolo
print(testo.upper())       # tutto maiuscolo
print(testo.strip())       # rimuove spazi ai bordi
print(testo.replace("Ciao", "Hello"))  # sostituzione
print("Mondo" in testo)    # verifica presenza -> True
```

---

## 3. File I/O

### Lettura di un file di testo

```python
with open("testo.txt", "r") as f:    # 'r' = read
    contenuto = f.read()
    print(contenuto)
```

### Scrittura su file

```python
with open("output.txt", "w") as f:   # 'w' = write
    f.write("Salvataggio riuscito!")
```

### File CSV

```python
import csv

with open("dati.csv", "r") as file:
    lettore = csv.reader(file)
    for riga in lettore:
        print(riga)
```

---

## 4. Moduli e pacchetti

### Import di un modulo standard

```python
import math
print(math.sqrt(16))  # radice quadrata -> 4.0
```

### Creazione di un modulo personale

Creare file `mio_modulo.py`:

```python
def saluta():
    print("Ciao da mio_modulo!")
```

Usarlo in un altro file:

```python
import mio_modulo
mio_modulo.saluta()
```

---

## 5. Ambienti virtuali e pacchetti

### Creare ambiente virtuale

```bash
python -m venv venv
```

### Attivarlo

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Installare pacchetti

```bash
pip install requests
pip list
```

### Salvare i pacchetti installati

```bash
pip freeze > requirements.txt
```

### Reinstallarli

```bash
pip install -r requirements.txt
```

---

## 6. Esercizi pratici

1. Leggi un file di testo e conta quante righe contiene
2. Crea un dizionario con 3 studenti e le loro età, poi stampa il più giovane
3. Scrivi un programma che legga un CSV e mostri solo la prima colonna
4. Usa un modulo (`math`, `datetime`, ecc.) per risolvere un problema semplice

---

**Fine Lezione 2 – Strutture dati e strumenti**
