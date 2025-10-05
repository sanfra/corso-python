# 🐍 Corso Python – Giorno 1

## Lezione 1: Introduzione e Fondamenta del Linguaggio Python

### 🎯 Obiettivi della lezione

- Capire cos’è Python e dove si usa
- Installare e configurare l’ambiente di sviluppo
- Scrivere ed eseguire i primi script
- Conoscere i concetti base: variabili, tipi, operatori, input/output
- Utilizzare le strutture di controllo (`if`, `for`, `while`)
- Creare e usare funzioni

---

## 1. Cos’è Python

Python è un linguaggio **interpreto** (cioè eseguito riga per riga, senza compilazione preventiva), **ad alto livello** (vicino al linguaggio umano) e **multiparadigma** (supporta programmazione procedurale, a oggetti e funzionale).

### Dove si usa

- **Web development**: Django, Flask, FastAPI
- **Data science**: Pandas, NumPy, Matplotlib
- **Automazione e scripting**
- **Machine learning e AI**: TensorFlow, PyTorch

### Caratteristiche

- Sintassi chiara e leggibile
- Tipizzazione dinamica (non serve dichiarare i tipi)
- Gestione automatica della memoria
- Grande libreria standard
- Compatibile con tutti i sistemi operativi

---

## 2. Installazione e ambiente

### Installazione di Python

Scaricare da [python.org/downloads](https://www.python.org/downloads/)Durante l’installazione su Windows:

- Selezionare **“Add Python to PATH”**
- Verificare:
  ```bash
  python --version
  pip --version
  ```

### IDE consigliati

- **VS Code**: leggero, adatto a principianti
- **PyCharm**: più completo, adatto a progetti grandi

---

## 3. Primo script Python

```python
# stampa un messaggio sullo schermo
print("Hello, world!")  
```

### Come eseguirlo

Salvare in `hello.py` e lanciare nel terminale:

```bash
python hello.py
```

Output:

```
Hello, world!
```

---

## 4. Variabili e tipi di dato

In Python non serve dichiarare il tipo: viene assegnato automaticamente.

```python
nome = "Alice"      # stringa (testo)
eta = 25            # intero
altezza = 1.70      # numero decimale (float)
studente = True     # booleano (vero/falso)
```

### Tipi fondamentali

| Tipo      | Nome completo           | Esempio                          | Descrizione                                     |
| --------- | ----------------------- | -------------------------------- | ----------------------------------------------- |
| `int`   | intero                  | `10`                           | Numeri senza decimali                           |
| `float` | numero a virgola mobile | `3.14`                         | Numeri con decimali                             |
| `str`   | stringa                 | `"ciao"`                       | Testo tra virgolette                            |
| `bool`  | booleano                | `True`, `False`              | Valore logico                                   |
| `list`  | lista                   | `[1, 2, 3]`                    | Collezione ordinata e modificabile              |
| `tuple` | tupla                   | `(1, 2, 3)`                    | Collezione ordinata e**non** modificabile |
| `set`   | insieme                 | `{1, 2, 3}`                    | Collezione**senza duplicati**             |
| `dict`  | dizionario              | `{"nome": "Alice", "eta": 25}` | Coppie chiave-valore                            |

---

## 5. Operatori

### Aritmetici

```python
x = 10
y = 3
print(x + y)   # somma -> 13
print(x - y)   # sottrazione -> 7
print(x * y)   # moltiplicazione -> 30
print(x / y)   # divisione -> 3.3333
print(x // y)  # divisione intera -> 3
print(x % y)   # resto -> 1
print(x ** y)  # potenza -> 1000
```

### Confronto

```python
print(x == y)  # uguale? -> False
print(x != y)  # diverso? -> True
print(x > y)   # maggiore? -> True
print(x < y)   # minore? -> False
```

### Logici

```python
print(True and False)  # entrambi veri? -> False
print(True or False)   # almeno uno vero? -> True
print(not True)        # negazione -> False
```

---

## 6. Input e Output

```python
nome = input("Inserisci il tuo nome: ")  # chiede all'utente un testo
print("Ciao", nome)                      # stampa il valore inserito
```

---

## 7. Strutture di controllo

### Condizioni (`if`, `elif`, `else`)

```python
x = 10

if x > 0:               # se la condizione è vera
    print("Positivo")
elif x == 0:            # altrimenti, se è uguale a zero
    print("Zero")
else:                   # in tutti gli altri casi
    print("Negativo")
```

### Ciclo `for`

```python
for i in range(5):      # range(5) genera i numeri 0,1,2,3,4
    print(i)            # stampa ogni numero
```

### Ciclo `while`

```python
x = 3
while x > 0:            # continua finché la condizione è vera
    print(x)
    x -= 1              # riduce il valore di x di 1
```

---

## 8. Funzioni

```python
def somma(a, b):        # definisce una funzione con due parametri
    return a + b        # restituisce la somma

risultato = somma(3, 4) # chiama la funzione
print(risultato)        # stampa 7
```

---

## 9. Scope (visibilità delle variabili)

```python
x = 10  # variabile globale

def mostra():
    x = 5  # variabile locale
    print(x)  # stampa la variabile locale

mostra()   # stampa 5
print(x)   # stampa 10 (quella globale)
```

---

## 10. Esercizi pratici

1. Chiedi nome ed età e stampa:`"Ciao <nome>, hai <età> anni!"`
2. Calcola la somma dei numeri da 1 a 100

   ```python
   somma = 0
   for i in range(1, 101):
       somma += i      # aggiunge i alla somma
   print(somma)
   ```
3. Stampa i numeri pari tra 1 e 20

   ```python
   for i in range(1, 21):
       if i % 2 == 0:  # se il resto è zero, è pari
           print(i)
   ```
4. Crea una funzione che calcoli il quadrato di un numero

   ```python
   def quadrato(x):
       return x ** 2

   print(quadrato(5))  # stampa 25
   ```

---

## 🔗 Riferimenti utili

- [Python Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

---

**Fine Lezione 1 – Fondamenta**
