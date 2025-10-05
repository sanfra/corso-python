# Caratteristiche OOP in Python 

## Introduzione all'OOP

**OOP** significa **Object-Oriented Programming** (Programmazione Orientata agli Oggetti). È un modo di scrivere codice che organizza il programma attorno a "oggetti" che rappresentano cose del mondo reale.

Immagina di dover descrivere una persona: ha delle caratteristiche (nome, età) e può fare delle azioni (camminare, parlare). In OOP, creiamo una "classe" Persona che descrive queste caratteristiche e azioni, poi creiamo "oggetti" (persone specifiche) da questa classe.

---

## 1. Classi e Oggetti

 **Classe** : è come un progetto, uno stampo, un "blueprint" (termine inglese che significa "schema" o "modello"). È la descrizione generale di come dovrebbe essere fatto qualcosa.

 **Oggetto** : è la cosa concreta creata seguendo quel progetto. Se la classe è il progetto di una casa, l'oggetto è la casa vera costruita.

```python
# Definiamo una classe chiamata Persona
# 'class' è la parola chiave per creare una classe
class Persona:
    # __init__ è il costruttore: viene eseguito quando creiamo un nuovo oggetto
    # 'self' rappresenta l'oggetto stesso (ogni persona ha il proprio nome e età)
    def __init__(self, nome, eta):
        # self.nome crea un attributo (caratteristica) chiamato nome
        # lo assegna al valore ricevuto come parametro
        self.nome = nome
        # self.eta crea un attributo età
        self.eta = eta
  
    # Definiamo un metodo (azione che la persona può fare)
    # 'def' serve per definire una funzione/metodo
    def saluta(self):
        # return restituisce un valore (in questo caso una stringa)
        # f"..." è una f-string: permette di inserire variabili dentro una stringa
        return f"Ciao, sono {self.nome}"

# Creiamo due oggetti (due persone diverse) dalla classe Persona
# Questo è come costruire due case dallo stesso progetto
persona1 = Persona("Mario", 30)  # Prima persona
persona2 = Persona("Laura", 25)  # Seconda persona

# Chiamiamo il metodo saluta() sull'oggetto persona1
# print() stampa il risultato a schermo
print(persona1.saluta())  # Output: Ciao, sono Mario
```

---

## 2. Incapsulamento

 **Incapsulamento** : significa "nascondere" i dettagli interni di un oggetto e proteggere i dati. È come avere un salvadanaio: puoi inserire monete attraverso la fessura (metodo deposita), ma non puoi aprirlo direttamente per prendere i soldi (attributo privato).

```python
# Creiamo una classe per gestire un conto bancario
class ContoBancario:
    # Il costruttore riceve il saldo iniziale
    def __init__(self, saldo_iniziale):
        # __saldo ha due underscore (__) all'inizio
        # Questo lo rende PRIVATO: accessibile solo dentro la classe
        self.__saldo = saldo_iniziale
  
    # Metodo per depositare denaro
    def deposita(self, importo):
        # if controlla una condizione
        # Verifichiamo che l'importo sia maggiore di 0
        if importo > 0:
            # += significa "aggiungi a": saldo = saldo + importo
            self.__saldo += importo
  
    # Metodo per prelevare denaro
    def preleva(self, importo):
        # Controlliamo che l'importo sia valido e ci siano abbastanza soldi
        # 'and' significa che entrambe le condizioni devono essere vere
        if 0 < importo <= self.__saldo:
            # -= significa "sottrai da": saldo = saldo - importo
            self.__saldo -= importo
            # return True indica che l'operazione è riuscita
            return True
        # Se arriviamo qui, il prelievo non è possibile
        return False
  
    # Getter: metodo per LEGGERE il saldo (senza modificarlo)
    def get_saldo(self):
        # Restituiamo il valore del saldo
        return self.__saldo

# Creiamo un conto con 1000 euro
conto = ContoBancario(1000)
# Depositiamo 500 euro usando il metodo
conto.deposita(500)
# Stampiamo il saldo usando il getter
print(conto.get_saldo())  # Output: 1500
# print(conto.__saldo)  # Questo darebbe ERRORE! __saldo è privato
```

**Livelli di privacy in Python:**

* `attributo`: pubblico (tutti possono accedervi)
* `_attributo`: protected (convenzione: uso interno, ma non bloccato)
* `__attributo`: privato (difficile accedervi dall'esterno)

---

## 3. Ereditarietà

 **Ereditarietà** : permette a una classe di "ereditare" (ricevere) caratteristiche e comportamenti da un'altra classe. È come un figlio che eredita caratteristiche dai genitori.

**Classe padre** (o superclasse): la classe da cui si eredita
**Classe figlia** (o sottoclasse): la classe che eredita

```python
# Classe padre: Veicolo (rappresenta un veicolo generico)
class Veicolo:
    # Costruttore della classe padre
    def __init__(self, marca, modello):
        # Attributi comuni a tutti i veicoli
        self.marca = marca
        self.modello = modello
  
    # Metodo che descrive il veicolo
    def descrizione(self):
        # Restituisce una stringa con marca e modello
        return f"{self.marca} {self.modello}"

# Classe figlia: Auto eredita da Veicolo
# (Auto) indica che Auto eredita da Veicolo
class Auto(Veicolo):
    # Costruttore della classe Auto
    def __init__(self, marca, modello, porte):
        # super() chiama il costruttore della classe padre
        # Così evitiamo di riscrivere il codice per marca e modello
        super().__init__(marca, modello)
        # Aggiungiamo un attributo specifico per le auto
        self.porte = porte
  
    # Override: riscriviamo il metodo descrizione()
    # Questo sostituisce il metodo del padre
    def descrizione(self):
        # super().descrizione() chiama il metodo del padre
        # Poi aggiungiamo informazioni sulle porte
        return f"{super().descrizione()} con {self.porte} porte"

# Altra classe figlia: Moto eredita da Veicolo
class Moto(Veicolo):
    # Costruttore della classe Moto
    def __init__(self, marca, modello, cilindrata):
        # Chiamiamo il costruttore del padre
        super().__init__(marca, modello)
        # Attributo specifico per le moto
        self.cilindrata = cilindrata

# Creiamo un'auto e una moto
auto = Auto("Fiat", "Panda", 5)
moto = Moto("Ducati", "Monster", 800)

# Stampiamo le descrizioni
print(auto.descrizione())  # Output: Fiat Panda con 5 porte
print(moto.descrizione())  # Output: Ducati Monster (usa il metodo del padre)
```

### Ereditarietà Multipla

Python permette di ereditare da **più classi** contemporaneamente (non tutti i linguaggi lo permettono).

```python
# Prima classe: definisce la capacità di volare
class Volante:
    # Metodo per volare
    def vola(self):
        return "Sto volando"

# Seconda classe: definisce la capacità di nuotare
class Nuotante:
    # Metodo per nuotare
    def nuota(self):
        return "Sto nuotando"

# Anatra eredita da ENTRAMBE le classi
# Quindi può sia volare che nuotare
class Anatra(Volante, Nuotante):
    # Costruttore dell'anatra
    def __init__(self, nome):
        self.nome = nome

# Creiamo un'anatra
paperino = Anatra("Paperino")
# Possiamo usare metodi da entrambe le classi padre
print(paperino.vola())   # Output: Sto volando
print(paperino.nuota())  # Output: Sto nuotando
```

---

## 4. Polimorfismo

 **Polimorfismo** : significa "molte forme". Oggetti di classi diverse possono rispondere allo stesso metodo in modo diverso. È come chiedere a diversi animali di "parlare": ognuno lo fa a modo suo.

```python
# Classe Cane
class Cane:
    # Metodo che fa parlare il cane
    def parla(self):
        return "Bau!"

# Classe Gatto
class Gatto:
    # Metodo che fa parlare il gatto
    def parla(self):
        return "Miao!"

# Classe Mucca
class Mucca:
    # Metodo che fa parlare la mucca
    def parla(self):
        return "Muuu!"

# Creiamo una lista con oggetti di classi diverse
# [] crea una lista (collezione di elementi)
animali = [Cane(), Gatto(), Mucca()]

# for loop: ripete il codice per ogni animale nella lista
# 'in' serve per iterare (scorrere) la lista
for animale in animali:
    # Chiamiamo parla() su ogni animale
    # Ognuno risponde in modo diverso (polimorfismo!)
    print(animale.parla())
# Output:
# Bau!
# Miao!
# Muuu!
```

### Duck Typing

 **Duck Typing** : è una filosofia di Python. Se un oggetto "cammina come un'anatra e fa qua qua come un'anatra, allora è un'anatra". In pratica: non importa il tipo dell'oggetto, importa cosa sa fare.

```python
# Classe Quadrato
class Quadrato:
    # Costruttore: riceve la lunghezza del lato
    def __init__(self, lato):
        self.lato = lato
  
    # Metodo per calcolare l'area
    def area(self):
        # ** significa "elevato a": lato²
        return self.lato ** 2

# Classe Cerchio
class Cerchio:
    # Costruttore: riceve il raggio
    def __init__(self, raggio):
        self.raggio = raggio
  
    # Metodo per calcolare l'area
    # Stessa firma (stesso nome) del metodo in Quadrato
    def area(self):
        # 3.14 è pi greco approssimato
        return 3.14 * self.raggio ** 2

# Funzione che stampa l'area di una forma qualsiasi
# Non specifichiamo il tipo di 'forma': duck typing!
def stampa_area(forma):
    # Non importa se è un Quadrato o un Cerchio
    # Basta che abbia il metodo area()
    print(f"Area: {forma.area()}")

# Funziona con entrambe le classi
stampa_area(Quadrato(5))   # Output: Area: 25
stampa_area(Cerchio(3))    # Output: Area: 28.26
```

---

## 5. Astrazione

 **Astrazione** : definisce COSA deve fare un oggetto, ma non COME. È come un contratto: "se vuoi essere una Forma, DEVI avere un metodo area()". Le classi astratte non possono essere usate direttamente, servono solo come modello.

```python
# Importiamo ABC (Abstract Base Class) e abstractmethod
# ABC serve per creare classi astratte
from abc import ABC, abstractmethod

# Forma è una classe astratta (eredita da ABC)
class Forma(ABC):
    # @abstractmethod è un decoratore: indica che questo metodo è astratto
    # Le classi figlie DEVONO implementare questo metodo
    @abstractmethod
    def area(self):
        # pass significa "non fare nulla"
        # Il metodo non ha implementazione qui
        pass
  
    # Altro metodo astratto
    @abstractmethod
    def perimetro(self):
        pass

# Rettangolo eredita da Forma
class Rettangolo(Forma):
    # Costruttore
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
  
    # DOBBIAMO implementare area() (era astratto nel padre)
    def area(self):
        # Area rettangolo = base × altezza
        return self.base * self.altezza
  
    # DOBBIAMO implementare perimetro() (era astratto nel padre)
    def perimetro(self):
        # Perimetro = 2 × (base + altezza)
        return 2 * (self.base + self.altezza)

# forma = Forma()  # ERRORE! Non possiamo creare oggetti da classi astratte
# Possiamo creare oggetti solo dalle classi concrete (non astratte)
rett = Rettangolo(5, 3)
print(rett.area())  # Output: 15
```

---

## 6. Metodi Speciali (Magic Methods)

**Metodi speciali** (o magic methods): metodi con nomi speciali che iniziano e finiscono con `__` (doppio underscore). Permettono di personalizzare come gli oggetti si comportano con operatori (+, ==, ecc.) e funzioni built-in (print, len, ecc.).

```python
# Classe che rappresenta un punto nel piano cartesiano
class Punto:
    # Costruttore
    def __init__(self, x, y):
        # Coordinate del punto
        self.x = x
        self.y = y
  
    # __str__ viene chiamato da print()
    # Definisce come stampare l'oggetto in modo "leggibile"
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
  
    # __repr__ definisce la rappresentazione "ufficiale" dell'oggetto
    # Usata quando digiti l'oggetto nella console
    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"
  
    # __add__ viene chiamato quando usiamo l'operatore +
    # Permette di sommare due punti
    def __add__(self, altro):
        # Creiamo un nuovo punto con coordinate sommate
        return Punto(self.x + altro.x, self.y + altro.y)
  
    # __eq__ viene chiamato quando usiamo l'operatore ==
    # Definisce quando due punti sono uguali
    def __eq__(self, altro):
        # Due punti sono uguali se hanno stesse coordinate
        # 'and' significa che entrambe le condizioni devono essere vere
        return self.x == altro.x and self.y == altro.y

# Creiamo tre punti
p1 = Punto(1, 2)
p2 = Punto(3, 4)
# Usiamo l'operatore + che abbiamo definito
p3 = p1 + p2

# print() chiama automaticamente __str__
print(p3)  # Output: Punto(4, 6)
# == chiama automaticamente __eq__
print(p1 == p2)  # Output: False
```

**Altri metodi speciali comuni:**

* `__len__`: chiamato da `len(oggetto)` per ottenere la lunghezza
* `__getitem__`: chiamato quando usi `oggetto[chiave]` per leggere
* `__setitem__`: chiamato quando usi `oggetto[chiave] = valore` per scrivere
* `__iter__`: rende un oggetto iterabile (usabile con for)
* `__call__`: permette di chiamare un oggetto come se fosse una funzione

---

## 7. Proprietà (Properties)

 **Property** : permette di controllare come si legge o si scrive un attributo. Dall'esterno sembra un semplice attributo, ma internamente possiamo aggiungere controlli e logica.

```python
# Classe per gestire temperature
class Temperatura:
    # Costruttore: riceve temperatura in Celsius
    def __init__(self, celsius):
        # _celsius ha un solo underscore: convenzione per "interno"
        self._celsius = celsius
  
    # @property rende celsius una proprietà (leggibile come attributo)
    @property
    def celsius(self):
        # Quando leggiamo temp.celsius, viene chiamato questo metodo
        return self._celsius
  
    # @celsius.setter permette di scrivere su celsius
    @celsius.setter
    def celsius(self, valore):
        # Controlliamo che la temperatura sia valida
        # -273.15°C è lo zero assoluto (minimo fisico possibile)
        if valore < -273.15:
            # raise solleva un'eccezione (errore)
            raise ValueError("Temperatura sotto lo zero assoluto!")
        # Se il valore è valido, lo salviamo
        self._celsius = valore
  
    # Proprietà calcolata: fahrenheit basata su celsius
    @property
    def fahrenheit(self):
        # Convertiamo da Celsius a Fahrenheit
        # Formula: F = C × 9/5 + 32
        return self._celsius * 9/5 + 32
  
    # Setter per fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, valore):
        # Convertiamo da Fahrenheit a Celsius
        # Formula: C = (F - 32) × 5/9
        self._celsius = (valore - 32) * 5/9

# Creiamo un oggetto temperatura
temp = Temperatura(25)
# Leggiamo celsius (chiama il getter)
print(temp.celsius)      # Output: 25
# Leggiamo fahrenheit (viene calcolato automaticamente)
print(temp.fahrenheit)   # Output: 77.0

# Scriviamo fahrenheit (chiama il setter)
temp.fahrenheit = 86
# celsius viene aggiornato automaticamente
print(temp.celsius)      # Output: 30.0
```

---

## 8. Metodi di Classe e Metodi Statici

 **Metodo di istanza** : opera su un oggetto specifico (usa `self`)
 **Metodo di classe** : opera sulla classe stessa (usa `cls`)
 **Metodo statico** : non opera né su oggetti né sulla classe (come una funzione normale dentro la classe)

```python
# Classe Studente
class Studente:
    # Attributo di classe: condiviso da TUTTE le istanze
    # Conta quanti studenti esistono
    numero_studenti = 0
  
    # Costruttore normale
    def __init__(self, nome):
        self.nome = nome
        # Incrementiamo il contatore di classe
        # Studente.numero_studenti accede all'attributo di classe
        Studente.numero_studenti += 1
  
    # @classmethod indica un metodo di classe
    # 'cls' rappresenta la classe (come 'self' rappresenta l'oggetto)
    @classmethod
    def crea_da_stringa(cls, stringa):
        # Factory method: modo alternativo di creare oggetti
        # split(',') divide la stringa dove trova una virgola
        # [0] prende il primo elemento
        nome = stringa.split(',')[0]
        # cls(nome) crea un nuovo oggetto della classe
        return cls(nome)
  
    # @staticmethod indica un metodo statico
    # Non riceve né self né cls
    @staticmethod
    def is_maggiorenne(eta):
        # Funzione di utilità che non usa dati della classe
        # Restituisce True se età >= 18, altrimenti False
        return eta >= 18
  
    # Metodo di classe che restituisce il numero di studenti
    @classmethod
    def conta_studenti(cls):
        # Accediamo all'attributo di classe
        return cls.numero_studenti

# Creiamo uno studente in modo normale
s1 = Studente("Mario")
# Creiamo uno studente usando il factory method
# Passiamo una stringa e il metodo estrae il nome
s2 = Studente.crea_da_stringa("Laura,20")

# Chiamiamo il metodo di classe sulla classe (non su un oggetto)
print(Studente.conta_studenti())  # Output: 2
# Chiamiamo il metodo statico
print(Studente.is_maggiorenne(17))  # Output: False
```

---

## Riepilogo Finale

Python supporta completamente l'OOP con queste caratteristiche:

✅  **Classi e Oggetti** : blueprint (modello) e istanze concrete
✅  **Incapsulamento** : proteggere i dati con attributi privati (`__`)
✅  **Ereditarietà** : riutilizzare codice (singola e multipla)
✅  **Polimorfismo** : stesso metodo, comportamenti diversi
✅  **Astrazione** : definire interfacce senza implementazione
✅  **Metodi Speciali** : personalizzare operatori (`+`, `==`, ecc.)
✅  **Properties** : controllare accesso agli attributi
✅  **Metodi di Classe/Statici** : operare su classi anziché oggetti

---

## Glossario dei Termini

* **Blueprint** : schema, progetto, modello (come il progetto di una casa)
* **Classe** : modello per creare oggetti
* **Oggetto/Istanza** : elemento concreto creato da una classe
* **Attributo** : caratteristica di un oggetto (variabile)
* **Metodo** : azione che un oggetto può fare (funzione)
* **self** : riferimento all'oggetto stesso
* **Costruttore** (`__init__`): metodo chiamato quando si crea un oggetto
* **Override** : riscrivere un metodo ereditato
* **Decoratore** : simbolo `@` che modifica il comportamento di un metodo
* **Duck Typing** : "se sembra un'anatra, è un'anatra" - non importa il tipo, importa cosa sa fare
* **Factory Method** : metodo che crea oggetti in modo alternativo
* **Getter** : metodo per leggere un attributo
* **Setter** : metodo per scrivere un attributo
