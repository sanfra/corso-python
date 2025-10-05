# 🐍 Corso Python – Giorno 3

## Lezione 3: Programmazione Avanzata e Introduzione al Web

### 🎯 Obiettivi della lezione

- Capire la gestione delle eccezioni
- Utilizzare le classi e la programmazione a oggetti
- Conoscere librerie esterne comuni
- Comprendere i concetti base di Flask e delle API web

---

## 1. Eccezioni e gestione errori

```python
try:
    numero = int(input("Inserisci un numero: "))
    print(10 / numero)
except ValueError:
    print("Errore: devi inserire un numero valido.")
except ZeroDivisionError:
    print("Errore: divisione per zero non consentita.")
finally:
    print("Operazione completata.")
```

---

## 2. Classi e oggetti (OOP base)

```python
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome      # attributo di istanza
        self.eta = eta

    def saluta(self):         # metodo di istanza
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

p1 = Persona("Luca", 25)
p1.saluta()
```

---

## 3. Librerie esterne utili

### `requests`

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)     # codice HTTP
print(response.json())          # contenuto JSON
```

### `pandas`

```python
import pandas as pd

dati = {"Nome": ["Anna", "Luca"], "Età": [30, 25]}
df = pd.DataFrame(dati)
print(df)
```

### `matplotlib`

```python
import matplotlib.pyplot as plt

numeri = [1, 2, 3, 4, 5]
quadrati = [n ** 2 for n in numeri]

plt.plot(numeri, quadrati)
plt.title("Numeri e loro quadrati")
plt.xlabel("Numero")
plt.ylabel("Quadrato")
plt.show()
```

---

## 4. Introduzione a Flask – web server di base

Installazione:

```bash
pip install flask
```

Creare file `app.py`:

```python
from flask import Flask

app = Flask(__name__)  # crea l'app Flask

@app.route("/")        # definisce una rotta
def home():
    return "Benvenuto nel mio server Flask!"

if __name__ == "__main__":
    app.run(debug=True)  # avvia il server
```

Esegui e visita: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 5. Mini-esercizi

1. Crea una classe `Studente` con attributi nome, corso e voto medio.
2. Scrivi una funzione che gestisca una divisione con `try/except`.
3. Fai una chiamata a un’API pubblica e stampa il risultato.
4. Crea un piccolo server Flask che risponda con “Ciao, mondo!”.

---

**Fine Lezione 3 – Programmazione avanzata e introduzione web**
