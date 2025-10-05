# possiamo definire pyhton un linguaggio ad oggetti?


## Sì, Python è un linguaggio  **orientato agli oggetti** , ma con una precisazione importante:

## Python è un linguaggio multi-paradigma

Python supporta diversi paradigmi di programmazione:

* **Object-Oriented** (orientato agli oggetti)
* **Procedurale**
* **Funzionale**

## Caratteristiche OOP in Python

Python ha tutte le caratteristiche fondamentali dell'OOP:

* **Classi e oggetti**
* **Ereditarietà** (anche multipla)
* **Incapsulamento**
* **Polimorfismo**

python

```python
classAnimale:
def__init__(self, nome):
        self.nome = nome
  
defparla(self):
pass

classCane(Animale):
defparla(self):
returnf"{self.nome} dice: Bau!"
```

## Ma...

A differenza di linguaggi **puramente** orientati agli oggetti come Java o C#, in Python:

* Non sei **obbligato** a usare classi
* Puoi scrivere codice procedurale o funzionale
* Tutto è oggetto (anche i tipi primitivi), ma puoi ignorarlo

python

```python
# Valido in Python, non in Java
defsomma(a, b):
return a + b

risultato = somma(5,3)
```

## Conclusione

Python è **orientato agli oggetti** ma **non puramente** OOP. È un linguaggio flessibile che ti permette di scegliere il paradigma più adatto al problema.
