# Quiz Corso Python - 30 Domande per Giorno

## GIORNO 1 - Fondamenti Python

### 1. Qual è l'estensione corretta per un file Python?

* A) .python
* B) .py
* C) .pyt
* D) .pt

**Risposta: B) .py**

**Spiegazione:** I file Python hanno estensione `.py`. Questa è la convenzione standard riconosciuta da tutti gli interpreti e IDE.

---

### 2. Quale keyword si usa per definire una funzione in Python?

* A) function
* B) def
* C) func
* D) define

**Risposta: B) def**

**Spiegazione:** In Python si usa `def` seguito dal nome della funzione e parentesi. Esempio: `def mia_funzione():`

---

### 3. Quale tipo di dato è `42`?

* A) str
* B) float
* C) int
* D) bool

**Risposta: C) int**

**Spiegazione:** `42` senza punto decimale è un intero (int). Se fosse `42.0` sarebbe un float.

---

### 4. Cosa stampa `print(type("Ciao"))`?

* A) `<class 'string'>`
* B) `<class 'str'>`
* C) `<class 'text'>`
* D) `string`

**Risposta: B) `<class 'str'>`**

**Spiegazione:** Il tipo delle stringhe in Python è `str`, abbreviazione di string.

---

### 5. Qual è il risultato di `10 // 3`?

* A) 3.333...
* B) 3
* C) 4
* D) 3.0

**Risposta: B) 3**

**Spiegazione:** L'operatore `//` esegue la divisione intera (floor division), restituendo solo la parte intera del risultato.

---

### 6. Quale operatore si usa per l'elevamento a potenza?

* A) ^
* B) pow
* C) **
* D) ^^

**Risposta: C) ****

**Spiegazione:** In Python `**` è l'operatore di potenza. Esempio: `2 ** 3 = 8`

---

### 7. Cosa fa `input()` in Python?

* A) Stampa un messaggio
* B) Legge input dall'utente come stringa
* C) Legge input dall'utente come intero
* D) Crea una variabile

**Risposta: B) Legge input dall'utente come stringa**

**Spiegazione:** `input()` restituisce sempre una stringa. Per ottenere un numero serve convertire: `int(input())`

---

### 8. Quale sarà l'output di questo codice?

```python
x = 5
if x > 3:
    print("A")
else:
    print("B")
```

* A) A
* B) B
* C) AB
* D) Errore

**Risposta: A) A**

**Spiegazione:** La condizione `x > 3` è vera (5 > 3), quindi viene eseguito il primo blocco.

---

### 9. Cosa produce `range(5)`?

* A) [0, 1, 2, 3, 4, 5]
* B) [1, 2, 3, 4, 5]
* C) [0, 1, 2, 3, 4]
* D) 5

**Risposta: C) [0, 1, 2, 3, 4]**

**Spiegazione:** `range(5)` genera numeri da 0 a 4 (5 escluso). L'inizio è 0 per default.

---

### 10. Quale keyword termina un loop anticipatamente?

* A) stop
* B) exit
* C) break
* D) end

**Risposta: C) break**

**Spiegazione:** `break` esce immediatamente dal loop più interno in cui si trova.

---

### 11. Cosa fa `continue` in un loop?

* A) Termina il loop
* B) Salta all'iterazione successiva
* C) Riavvia il loop dall'inizio
* D) Mette in pausa il loop

**Risposta: B) Salta all'iterazione successiva**

**Spiegazione:** `continue` salta il resto del codice nel loop corrente e passa alla prossima iterazione.

---

### 12. Quale è la sintassi corretta per un commento su una riga?

* A) // commento
* B) /* commento */
* C) # commento
* D) -- commento

**Risposta: C) # commento**

**Spiegazione:** In Python i commenti su singola riga iniziano con `#`.

---

### 13. Qual è il valore di `x` dopo questo codice?

```python
x = 10
x += 5
```

* A) 10
* B) 5
* C) 15
* D) 105

**Risposta: C) 15**

**Spiegazione:** `x += 5` è equivalente a `x = x + 5`, quindi 10 + 5 = 15.

---

### 14. Cosa restituisce una funzione senza `return`?

* A) 0
* B) None
* C) False
* D) Errore

**Risposta: B) None**

**Spiegazione:** Se una funzione non ha `return`, restituisce implicitamente `None`.

---

### 15. Quale operatore logico inverte un valore booleano?

* A) !
* B) NOT
* C) not
* D) ~

**Risposta: C) not**

**Spiegazione:** L'operatore `not` inverte True in False e viceversa. Python usa lowercase per le keyword.

---

### 16. Quale sarà l'output?

```python
print(3 * "Ha")
```

* A) 3Ha
* B) HaHaHa
* C) Ha Ha Ha
* D) Errore

**Risposta: B) HaHaHa**

**Spiegazione:** L'operatore `*` con stringhe ripete la stringa n volte.

---

### 17. Quale è il modo corretto per creare una f-string?

* A) print(f"Valore: {x}")
* B) print("Valore: {x}")
* C) print(s"Valore: {x}")
* D) print("Valore: " + x)

**Risposta: A) print(f"Valore: {x}")**

**Spiegazione:** Le f-string iniziano con `f` prima delle virgolette e permettono di inserire variabili con `{}`.

---

### 18. Cosa significa 'scope' di una variabile?

* A) Il suo tipo
* B) Il suo valore
* C) Dove è accessibile nel codice
* D) Quanto spazio occupa in memoria

**Risposta: C) Dove è accessibile nel codice**

**Spiegazione:** Lo scope determina in quali parti del codice una variabile può essere usata (locale vs globale).

---

### 19. Quale loop è meglio quando non si conosce il numero di iterazioni?

* A) for
* B) while
* C) do-while
* D) until

**Risposta: B) while**

**Spiegazione:** `while` continua finché una condizione è vera, ideale quando il numero di iterazioni non è predeterminato.

---

### 20. Cosa produce `5 % 2`?

* A) 2.5
* B) 2
* C) 1
* D) 0

**Risposta: C) 1**

**Spiegazione:** L'operatore `%` (modulo) restituisce il resto della divisione. 5 diviso 2 fa 2 con resto 1.

---

### 21. Quale è la differenza tra `=` e `==`?

* A) Nessuna differenza
* B) `=` assegna, `==` confronta
* C) `=` confronta, `==` assegna
* D) Sono intercambiabili

**Risposta: B) `=` assegna, `==` confronta**

**Spiegazione:** `=` assegna un valore a una variabile, `==` verifica l'uguaglianza tra due valori.

---

### 22. Quale sarà il risultato?

```python
def test():
    return 5
    print("Ciao")

test()
```

* A) Stampa "Ciao" e restituisce 5
* B) Restituisce 5 e stampa "Ciao"
* C) Solo restituisce 5
* D) Errore

**Risposta: C) Solo restituisce 5**

**Spiegazione:** `return` termina immediatamente la funzione. Il codice dopo `return` non viene eseguito.

---

### 23. Come si converte una stringa "42" in intero?

* A) integer("42")
* B) int("42")
* C) toInt("42")
* D) Integer.parse("42")

**Risposta: B) int("42")**

**Spiegazione:** La funzione built-in `int()` converte stringhe (e altri tipi) in interi.

---

### 24. Quale valore è considerato False in Python?

* A) 1
* B) "False"
* C) 0
* D) "0"

**Risposta: C) 0**

**Spiegazione:** In Python, 0, 0.0, "", [], {}, None e False sono considerati "falsy". Il numero 1 e le stringhe non vuote sono "truthy".

---

### 25. Cosa fa `pass` in Python?

* A) Passa il controllo alla funzione successiva
* B) È un placeholder che non fa nulla
* C) Termina la funzione
* D) Salta una riga

**Risposta: B) È un placeholder che non fa nulla**

**Spiegazione:** `pass` è un'operazione nulla, utile quando serve sintatticamente un'istruzione ma non si vuole fare nulla.

---

### 26. Qual è l'output?

```python
x = "5"
y = 3
print(x + y)
```

* A) 8
* B) "8"
* C) "53"
* D) Errore

**Risposta: D) Errore**

**Spiegazione:** Python non può concatenare direttamente una stringa e un intero. Serve convertire: `x + str(y)` o `int(x) + y`.

---

### 27. Quale è il modo corretto per definire parametri con valore default?

* A) `def func(x=5, y):`
* B) `def func(y, x=5):`
* C) `def func(x default 5):`
* D) `def func(x:=5):`

**Risposta: B) `def func(y, x=5):`**

**Spiegazione:** I parametri con default devono venire dopo quelli senza default.

---

### 28. Cosa stampa questo codice?

```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```

* A) 0 1 2
* B) 0 2
* C) 1 2
* D) 0 1

**Risposta: B) 0 2**

**Spiegazione:** Quando `i == 1`, `continue` salta il `print`, quindi stampa solo 0 e 2.

---

### 29. Quale funzione restituisce il tipo di una variabile?

* A) typeof()
* B) type()
* C) getType()
* D) vartype()

**Risposta: B) type()**

**Spiegazione:** `type(variabile)` restituisce il tipo della variabile.

---

### 30. Quale operatore verifica se due variabili riferiscono lo stesso oggetto?

* A) ==
* B) ===
* C) is
* D) equals

**Risposta: C) is**

**Spiegazione:** `is` verifica l'identità (stesso oggetto in memoria), `==` verifica l'uguaglianza dei valori.

---

## GIORNO 2 - Strutture Dati e Strumenti

### 1. Quale struttura dati è ordinata e modificabile?

* A) tuple
* B) set
* C) list
* D) frozenset

**Risposta: C) list**

**Spiegazione:** Le liste sono ordinate (mantengono l'ordine di inserimento) e modificabili (mutable).

---

### 2. Come si accede al primo elemento di una lista?

* A) lista[1]
* B) lista[0]
* C) lista.first()
* D) lista.get(0)

**Risposta: B) lista[0]**

**Spiegazione:** Gli indici in Python iniziano da 0, quindi il primo elemento è all'indice 0.

---

### 3. Quale metodo aggiunge un elemento alla fine di una lista?

* A) add()
* B) insert()
* C) append()
* D) push()

**Risposta: C) append()**

**Spiegazione:** `lista.append(elemento)` aggiunge l'elemento alla fine della lista.

---

### 4. Cosa restituisce `lista[-1]`?

* A) Il primo elemento
* B) L'ultimo elemento
* C) Errore
* D) None

**Risposta: B) L'ultimo elemento**

**Spiegazione:** Gli indici negativi contano dalla fine: -1 è l'ultimo, -2 il penultimo, ecc.

---

### 5. Quale struttura NON permette duplicati?

* A) list
* B) tuple
* C) set
* D) dict

**Risposta: C) set**

**Spiegazione:** I set sono collezioni di elementi unici. I duplicati vengono automaticamente rimossi.

---

### 6. Come si crea un dizionario vuoto?

* A) dict = []
* B) dict = ()
* C) dict = {}
* D) dict = set()

**Risposta: C) dict = {}**

**Spiegazione:** `{}` crea un dizionario vuoto. `[]` crea una lista, `()` una tupla, `set()` un set.

---

### 7. Come si accede al valore con chiave "nome" in un dizionario?

* A) dict.nome
* B) dict["nome"]
* C) dict(nome)
* D) dict->nome

**Risposta: B) dict["nome"]**

**Spiegazione:** Si accede ai valori di un dizionario usando le chiavi tra parentesi quadre.

---

### 8. Cosa fa `lista[1:4]`?

* A) Restituisce gli elementi agli indici 1, 2, 3, 4
* B) Restituisce gli elementi agli indici 1, 2, 3
* C) Restituisce gli elementi agli indici 1, 4
* D) Errore

**Risposta: B) Restituisce gli elementi agli indici 1, 2, 3**

**Spiegazione:** Lo slicing `[inizio:fine]` include l'indice di inizio ma esclude quello di fine.

---

### 9. Quale metodo rimuove e restituisce l'ultimo elemento di una lista?

* A) remove()
* B) delete()
* C) pop()
* D) del()

**Risposta: C) pop()**

**Spiegazione:** `lista.pop()` rimuove e restituisce l'ultimo elemento. `lista.pop(i)` rimuove l'elemento all'indice i.

---

### 10. Cosa produce `"hello".upper()`?

* A) "hello"
* B) "HELLO"
* C) "Hello"
* D) Errore

**Risposta: B) "HELLO"**

**Spiegazione:** Il metodo `.upper()` converte tutti i caratteri in maiuscolo.

---

### 11. Quale metodo divide una stringa in una lista?

* A) divide()
* B) split()
* C) separate()
* D) cut()

**Risposta: B) split()**

**Spiegazione:** `stringa.split()` divide la stringa su spazi bianchi. `stringa.split(",")` divide su virgole.

---

### 12. Come si uniscono elementi di una lista in una stringa?

* A) join(lista)
* B) "+".join(lista)
* C) " ".join(lista)
* D) lista.join(" ")

**Risposta: C) " ".join(lista)**

**Spiegazione:** `separatore.join(lista)` unisce gli elementi della lista usando il separatore specificato.

---

### 13. Cosa fa `with open("file.txt", "r") as f:`?

* A) Apre il file in scrittura
* B) Apre il file in lettura e lo chiude automaticamente
* C) Crea un nuovo file
* D) Elimina il file

**Risposta: B) Apre il file in lettura e lo chiude automaticamente**

**Spiegazione:** `with` è un context manager che chiude automaticamente il file alla fine del blocco. "r" significa read (lettura).

---

### 14. Quale modalità di apertura sovrascrive un file esistente?

* A) "r"
* B) "w"
* C) "a"
* D) "x"

**Risposta: B) "w"**

**Spiegazione:** "w" (write) crea un nuovo file o sovrascrive quello esistente. "a" (append) aggiunge alla fine.

---

### 15. Come si legge tutto il contenuto di un file come stringa?

* A) file.readall()
* B) file.read()
* C) file.getall()
* D) file.content()

**Risposta: B) file.read()**

**Spiegazione:** `file.read()` legge l'intero contenuto del file come una singola stringa.

---

### 16. Quale modulo si usa per lavorare con file CSV?

* A) csvlib
* B) csv
* C) file
* D) pandas

**Risposta: B) csv**

**Spiegazione:** Il modulo standard `csv` fornisce funzionalità per leggere e scrivere file CSV.

---

### 17. Come si crea un ambiente virtuale?

* A) python -m venv nome_env
* B) virtualenv create nome_env
* C) pip install venv
* D) python create env

**Risposta: A) python -m venv nome_env**

**Spiegazione:** `python -m venv` seguito dal nome crea un nuovo ambiente virtuale.

---

### 18. Quale comando installa un pacchetto con pip?

* A) pip get nomepacchetto
* B) pip install nomepacchetto
* C) pip add nomepacchetto
* D) pip download nomepacchetto

**Risposta: B) pip install nomepacchetto**

**Spiegazione:** `pip install` è il comando standard per installare pacchetti Python.

---

### 19. Cosa fa `pip freeze > requirements.txt`?

* A) Congela pip
* B) Salva l'elenco dei pacchetti installati
* C) Installa pacchetti da file
* D) Aggiorna pip

**Risposta: B) Salva l'elenco dei pacchetti installati**

**Spiegazione:** `pip freeze` elenca tutti i pacchetti installati con le loro versioni. `>` redirige l'output in un file.

---

### 20. Come si importa solo una funzione specifica da un modulo?

* A) import modulo.funzione
* B) from modulo import funzione
* C) import funzione from modulo
* D) modulo import funzione

**Risposta: B) from modulo import funzione**

**Spiegazione:** `from modulo import funzione` importa solo la funzione specifica, permettendo di usarla senza il prefisso del modulo.

---

### 21. Cosa restituisce `len([1, 2, 3])`?

* A) [1, 2, 3]
* B) 3
* C) 6
* D) Errore

**Risposta: B) 3**

**Spiegazione:** `len()` restituisce il numero di elementi in una collezione.

---

### 22. Quale è la differenza tra `lista.sort()` e `sorted(lista)`?

* A) Nessuna
* B) sort() modifica la lista originale, sorted() restituisce una nuova lista
* C) sorted() modifica la lista originale, sort() restituisce una nuova lista
* D) sort() è più veloce

**Risposta: B) sort() modifica la lista originale, sorted() restituisce una nuova lista**

**Spiegazione:** `lista.sort()` ordina in-place, `sorted(lista)` restituisce una nuova lista ordinata lasciando l'originale invariata.

---

### 23. Come si verifica se una chiave esiste in un dizionario?

* A) key.exists(dict)
* B) key in dict
* C) dict.hasKey(key)
* D) dict.contains(key)

**Risposta: B) key in dict**

**Spiegazione:** L'operatore `in` verifica la presenza di una chiave in un dizionario.

---

### 24. Cosa produce `{"a": 1, "b": 2}.keys()`?

* A) ["a", "b"]
* B) [1, 2]
* C) dict_keys(['a', 'b'])
* D) ("a", "b")

**Risposta: C) dict_keys(['a', 'b'])**

**Spiegazione:** `.keys()` restituisce un oggetto dict_keys con tutte le chiavi. Si può convertire in lista con `list()`.

---

### 25. Come si rimuove un elemento con chiave specifica da un dizionario?

* A) dict.remove(key)
* B) del dict[key]
* C) dict.delete(key)
* D) dict.pop(key)

**Risposta: B) del dict[key] oppure D) dict.pop(key)**

**Spiegazione:** Entrambi funzionano. `del dict[key]` elimina l'elemento, `dict.pop(key)` lo elimina e restituisce il valore.

---

### 26. Cosa fa `"  hello  ".strip()`?

* A) Rimuove tutte le 'l'
* B) Rimuove spazi all'inizio e alla fine
* C) Rimuove tutti gli spazi
* D) Converte in maiuscolo

**Risposta: B) Rimuove spazi all'inizio e alla fine**

**Spiegazione:** `.strip()` rimuove whitespace (spazi, tab, newline) all'inizio e alla fine della stringa.

---

### 27. Come si crea una list comprehension per i quadrati da 0 a 4?

* A) [x^2 for x in range(5)]
* B) [x**2 for x in range(5)]
* C) [x*x in range(5)]
* D) {x**2 for x in range(5)}

**Risposta: B) [x**2 for x in range(5)]**

**Spiegazione:** La sintassi è `[espressione for variabile in iterabile]`. `**` è l'operatore di potenza.

---

### 28. Quale struttura dati è immutabile?

* A) list
* B) dict
* C) tuple
* D) set

**Risposta: C) tuple**

**Spiegazione:** Le tuple non possono essere modificate dopo la creazione (immutabili).

---

### 29. Come si legge un file JSON in Python?

* A) json.read(file)
* B) json.load(file)
* C) json.parse(file)
* D) json.open(file)

**Risposta: B) json.load(file)**

**Spiegazione:** `json.load()` legge un file JSON e lo converte in strutture dati Python (dict, list, ecc.).

---

### 30. Cosa restituisce `list(range(2, 8, 2))`?

* A) [2, 4, 6, 8]
* B) [2, 4, 6]
* C) [2, 3, 4, 5, 6, 7]
* D) [4, 6, 8]

**Risposta: B) [2, 4, 6]**

**Spiegazione:** `range(inizio, fine, passo)` genera numeri da 2 a 7 (8 escluso) con passo 2.

---

## GIORNO 3 - OOP e Web Development

### 1. Quale keyword definisce una classe in Python?

* A) class
* B) Class
* C) object
* D) def

**Risposta: A) class**

**Spiegazione:** `class NomeClasse:` definisce una nuova classe in Python.

---

### 2. Cosa rappresenta `self` in un metodo di classe?

* A) La classe stessa
* B) L'istanza corrente dell'oggetto
* C) Il metodo padre
* D) Una variabile globale

**Risposta: B) L'istanza corrente dell'oggetto**

**Spiegazione:** `self` è un riferimento all'istanza corrente e permette di accedere ai suoi attributi e metodi.

---

### 3. Quale metodo viene chiamato quando si crea un oggetto?

* A) **create**
* B) **new**
* C) **init**
* D) **start**

**Risposta: C) **init****

**Spiegazione:** `__init__` è il costruttore che inizializza l'oggetto appena creato.

---

### 4. Come si crea ereditarietà in Python?

* A) class Figlio extends Padre:
* B) class Figlio(Padre):
* C) class Figlio inherit Padre:
* D) class Figlio < Padre:

**Risposta: B) class Figlio(Padre):**

**Spiegazione:** La sintassi per l'ereditarietà è mettere la classe padre tra parentesi dopo il nome della classe figlia.

---

### 5. Cosa fa `super().__init__()`?

* A) Crea un nuovo oggetto
* B) Chiama il costruttore della classe padre
* C) Elimina l'oggetto
* D) Restituisce la classe padre

**Risposta: B) Chiama il costruttore della classe padre**

**Spiegazione:** `super()` permette di accedere ai metodi della classe padre, spesso usato per chiamare `__init__`.

---

### 6. Cosa indica `__` (doppio underscore) prima di un attributo?

* A) È pubblico
* B) È protetto
* C) È privato
* D) È statico

**Risposta: C) È privato**

**Spiegazione:** `__attributo` rende l'attributo privato (name mangling). `_attributo` (singolo underscore) è una convenzione per "protetto".

---

### 7. Quale decoratore crea un metodo di classe?

* A) @class
* B) @classmethod
* C) @staticmethod
* D) @method

**Risposta: B) @classmethod**

**Spiegazione:** `@classmethod` definisce un metodo che opera sulla classe piuttosto che sull'istanza. Riceve `cls` come primo parametro.

---

### 8. Cosa fa `@property`?

* A) Rende un attributo privato
* B) Permette di accedere a un metodo come se fosse un attributo
* C) Crea una proprietà statica
* D) Definisce una costante

**Risposta: B) Permette di accedere a un metodo come se fosse un attributo**

**Spiegazione:** `@property` crea un getter, permettendo di chiamare un metodo senza parentesi: `obj.metodo` invece di `obj.metodo()`.

---

### 9. Come si gestisce un'eccezione in Python?

* A) catch/finally
* B) try/catch
* C) try/except
* D) handle/error

**Risposta: C) try/except**

**Spiegazione:** La sintassi è `try: ... except TipoErrore: ...` per catturare e gestire eccezioni.

---

### 10. Quale blocco viene sempre eseguito, con o senza eccezioni?

* A) else
* B) finally
* C) catch
* D) always

**Risposta: B) finally**

**Spiegazione:** Il blocco `finally` viene eseguito sempre, anche se c'è un'eccezione o un return.

---

### 11. Come si solleva un'eccezione personalizzata?

* A) throw Exception("messaggio")
* B) raise Exception("messaggio")
* C) error("messaggio")
* D) exception("messaggio")

**Risposta: B) raise Exception("messaggio")**

**Spiegazione:** `raise` solleva un'eccezione. Si può usare con classi di eccezione built-in o personalizzate.

---

### 12. Quale libreria si usa per fare richieste HTTP?

* A) http
* B) urllib
* C) requests
* D) httplib

**Risposta: C) requests**

**Spiegazione:** `requests` è la libreria più popolare e user-friendly per HTTP. Non è built-in, va installata con pip.

---

### 13. Come si fa una GET request con requests?

* A) requests.get(url)
* B) requests.request("GET", url)
* C) requests.fetch(url)
* D) requests.download(url)

**Risposta: A) requests.get(url)**

**Spiegazione:** `requests.get(url)` esegue una richiesta GET e restituisce un oggetto Response.

---

### 14. Come si accede al JSON di una risposta HTTP?

* A) response.json
* B) response.json()
* C) response.to_json()
* D) json.parse(response)

**Risposta: B) response.json()**

**Spiegazione:** `.json()` è un metodo che parsa automaticamente il contenuto JSON della risposta.

---

### 15. Quale libreria si usa per analisi dati in Python?

* A) numpy
* B) pandas
* C) matplotlib
* D) Tutte le precedenti

**Risposta: D) Tutte le precedenti**

**Spiegazione:** NumPy per calcoli numerici, Pandas per manipolazione dati, Matplotlib per visualizzazione. Spesso usate insieme.

---

### 16. Come si crea un DataFrame pandas da un dizionario?

* A) pandas.DataFrame(dict)
* B) pd.DataFrame(dict)
* C) DataFrame(dict)
* D) pd.create(dict)

**Risposta: B) pd.DataFrame(dict)**

**Spiegazione:** Assumendo `import pandas as pd`, `pd.DataFrame(dict)` crea un DataFrame da un dizionario.

---

### 17. Quale metodo di matplotlib mostra un grafico?

* A) plt.display()
* B) plt.show()
* C) plt.render()
* D) plt.draw()

**Risposta: B) plt.show()**

**Spiegazione:** `plt.show()` visualizza il grafico creato. Senza questa chiamata, il grafico non appare.

---

### 18. Quale framework Python è un microframework per web?

* A) Django
* B) Flask
* C) Pyramid
* D) Tornado

**Risposta: B) Flask**

**Spiegazione:** Flask è un microframework leggero e flessibile. Django è full-stack, più complesso ma con più funzionalità integrate.

---

### 19. Come si definisce una route in Flask?

* A) @app.route("/path")
* B) @route("/path")
* C) app.add_route("/path")
* D) flask.route("/path")

**Risposta: A) @app.route("/path")**

**Spiegazione:** Il decoratore `@app.route()` associa una funzione a un URL specifico.

---

### 20. Come si ottiene un parametro dall'URL in Flask?

* A) @app.route("/user/`<username>`")
* B) @app.route("/user/{username}")
* C) @app.route("/user/:username")
* D) @app.route("/user/[username]")

**Risposta: A) @app.route("/user/`<username>`")**

**Spiegazione:** I parametri URL in Flask si definiscono tra `< >`. Il valore viene passato come argomento alla funzione.

---

### 21. Quale metodo HTTP si usa per creare una risorsa?

* A) GET
* B) POST
* C) PUT
* D) DELETE

**Risposta: B) POST**

**Spiegazione:** POST crea nuove risorse. GET legge, PUT aggiorna, DELETE elimina.

---

### 22. Quale codice HTTP indica successo?

* A) 404
* B) 500
* C) 200
* D) 301

**Risposta: C) 200**

**Spiegazione:** 200 OK indica successo. 404 = Not Found, 500 = Server Error, 301 = Redirect permanente.

---

### 23. Come si restituisce JSON in Flask?

* A) return json
* B) return jsonify(data)
* C) return json.dumps(data)
* D) return JSON(data)

**Risposta: B) return jsonify(data)**

**Spiegazione:** `jsonify()` converte dati Python in risposta JSON con header corretti.

---

### 24. Cosa fa `__str__` in una classe?

* A) Converte in stringa
* B) Definisce la rappresentazione leggibile dell'oggetto
* C) Concatena stringhe
* D) Verifica se è una stringa

**Risposta: B) Definisce la rappresentazione leggibile dell'oggetto**

**Spiegazione:** `__str__` definisce come l'oggetto viene rappresentato quando usato con `print()` o `str()`.

---

### 25. Quale è la differenza tra `__str__` e `__repr__`?

* A) Nessuna
* B) `__str__` è per utenti, `__repr__` per sviluppatori
* C) `__repr__` è più veloce
* D) Sono sinonimi

**Risposta: B) `__str__` è per utenti, `__repr__` per sviluppatori**

**Spiegazione:** `__str__` crea output user-friendly, `__repr__` una rappresentazione tecnica/debug dell'oggetto.

---

### 26. Come si implementa il polimorfismo in Python?

* A) Con interfacce
* B) Con abstract classes
* C) Duck typing (se ha i metodi giusti, funziona)
* D) Con overloading

**Risposta: C) Duck typing**

**Spiegazione:** Python usa duck typing: "se cammina come un'anatra e fa qua qua come un'anatra, è un'anatra". Non serve ereditarietà esplicita.

---

### 27. Quale blocco viene eseguito solo se NON ci sono eccezioni?

* A) except
* B) else
* C) finally
* D) catch

**Risposta: B) else**

**Spiegazione:** Il blocco `else` dopo `try/except` viene eseguito solo se non si verificano eccezioni.

---

### 28. Come si accede ai dati POST in Flask?

* A) request.post
* B) request.data
* C) request.form o request.json
* D) request.body

**Risposta: C) request.form o request.json**

**Spiegazione:** `request.form` per form HTML, `request.json` per dati JSON inviati nel body.

---

### 29. Quale template engine usa Flask di default?

* A) Mustache
* B) Jinja2
* C) Handlebars
* D) Pug

**Risposta: B) Jinja2**

**Spiegazione:** Jinja2 è il template engine integrato in Flask, con sintassi `{{ variabile }}` e `{% tag %}`.

---

### 30. Come si esegue Flask in modalità debug?

* A) flask run --debug
* B) app.run(debug=True)
* C) flask debug
* D) app.debug()

**Risposta: B) app.run(debug=True)**

**Spiegazione:** `debug=True` abilita il debug mode: auto-reload del server e debugger interattivo su errori.

---

## GIORNO 4 - Framework e Progetto Finale

### 1. Quale framework Python è "batteries included"?

* A) Flask
* B) Django
* C) FastAPI
* D) Bottle

**Risposta: B) Django**

**Spiegazione:** Django include tutto (ORM, admin, auth, forms). Flask è minimalista, FastAPI moderno e veloce.

---

### 2. Quale framework ha documentazione API automatica?

* A) Flask
* B) Django
* C) FastAPI
* D) Pyramid

**Risposta: C) FastAPI**

**Spiegazione:** FastAPI genera automaticamente documentazione Swagger/OpenAPI basata sui type hints.

---

### 3. Come si definisce un modello SQLAlchemy?

* A) class Model(Base):
* B) class Model(db.Model):
* C) class Model extends Base:
* D) @model class Model:

**Risposta: A) class Model(Base): o B) class Model(db.Model):**

**Spiegazione:** Dipende dal setup. Con SQLAlchemy puro: `Base`, con Flask-SQLAlchemy: `db.Model`.

---

### 4. Quale tipo di database è SQLite?

* A) NoSQL
* B) Relazionale
* C) Document-based
* D) Graph database

**Risposta: B) Relazionale**

**Spiegazione:** SQLite è un database relazionale SQL, file-based, perfetto per sviluppo e piccole app.

---

### 5. Cosa fa `db.session.commit()`?

* A) Inizia una transazione
* B) Salva le modifiche nel database
* C) Annulla le modifiche
* D) Chiude la connessione

**Risposta: B) Salva le modifiche nel database**

**Spiegazione:** `commit()` persiste le modifiche pendenti nella sessione al database.

---

### 6. Come si crea una tabella con SQLAlchemy?

* A) db.create_table()
* B) Base.metadata.create_all(engine)
* C) model.create()
* D) db.init()

**Risposta: B) Base.metadata.create_all(engine)**

**Spiegazione:** Questo crea tutte le tabelle definite nei modelli che ereditano da Base.

---

### 7. Quale metodo recupera tutti i record di un modello?

* A) Model.get_all()
* B) Model.query.all()
* C) Model.fetch()
* D) Model.select()

**Risposta: B) Model.query.all()**

**Spiegazione:** Con Flask-SQLAlchemy, `.query.all()` restituisce tutti i record. Con SQLAlchemy puro: `session.query(Model).all()`.

---

### 8. Come si filtra una query?

* A) Model.query.filter(condizione)
* B) Model.query.where(condizione)
* C) Model.query.select(condizione)
* D) Model.filter(condizione)

**Risposta: A) Model.query.filter(condizione)**

**Spiegazione:** `.filter()` o `.filter_by()` aggiungono condizioni WHERE alla query.

---

### 9. Quale libreria si usa per password hashing in Flask?

* A) hashlib
* B) bcrypt
* C) werkzeug.security
* D) passlib

**Risposta: C) werkzeug.security**

**Spiegazione:** Werkzeug (incluso con Flask) fornisce `generate_password_hash()` e `check_password_hash()`.

---

### 10. Come si autentica un utente con Flask-Login?

* A) auth.login(user)
* B) login_user(user)
* C) user.login()
* D) session.login(user)

**Risposta: B) login_user(user)**

**Spiegazione:** `login_user()` di Flask-Login gestisce la sessione di login dell'utente.

---

### 11. Quale decoratore protegge una route che richiede login?

* A) @login_required
* B) @authenticated
* C) @require_login
* D) @protected

**Risposta: A) @login_required**

**Spiegazione:** Il decoratore `@login_required` di Flask-Login verifica che l'utente sia autenticato.

---

### 12. Come si accede all'utente corrente in Flask-Login?

* A) session.user
* B) current_user
* C) request.user
* D) g.user

**Risposta: B) current_user**

**Spiegazione:** `current_user` è un proxy che rappresenta l'utente autenticato corrente.

---

### 13. Quale framework di test si usa comunemente con Flask?

* A) unittest
* B) pytest
* C) nose
* D) doctest

**Risposta: B) pytest**

**Spiegazione:** Pytest è lo standard de facto per testing Python, molto usato con Flask. Include `pytest-flask`.

---

### 14. Come si crea un client di test in Flask?

* A) app.test()
* B) app.test_client()
* C) flask.test()
* D) TestClient(app)

**Risposta: B) app.test_client()**

**Spiegazione:** `app.test_client()` crea un client per simulare richieste HTTP nei test.

---

### 15. Quale comando crea file di migrazione database?

* A) flask db init
* B) flask db migrate
* C) flask db upgrade
* D) flask db create

**Risposta: B) flask db migrate**

**Spiegazione:** Con Flask-Migrate: `init` inizializza, `migrate` crea migrazioni, `upgrade` le applica.

---

### 16. Cosa è un ORM?

* A) Object Request Mapper
* B) Object Relational Mapping
* C) Online Resource Manager
* D) Open Record Model

**Risposta: B) Object Relational Mapping**

**Spiegazione:** ORM mappa classi Python a tabelle database, permettendo di lavorare con oggetti invece di SQL.

---

### 17. Quale server WSGI si usa in produzione?

* A) Flask development server
* B) Gunicorn
* C) python -m http.server
* D) Django runserver

**Risposta: B) Gunicorn**

**Spiegazione:** Gunicorn (Green Unicorn) è un production-ready WSGI server. Il server di sviluppo Flask non è sicuro per produzione.

---

### 18. Come si configura una variabile d'ambiente in Python?

* A) os.getenv("VAR")
* B) env.get("VAR")
* C) config.VAR
* D) sys.env["VAR"]

**Risposta: A) os.getenv("VAR")**

**Spiegazione:** `os.getenv("VAR")` o `os.environ.get("VAR")` legge variabili d'ambiente. Usare `python-dotenv` per file `.env`.

---

### 19. Quale file contiene le dipendenze Python?

* A) package.json
* B) requirements.txt
* C) dependencies.txt
* D) Pipfile

**Risposta: B) requirements.txt**

**Spiegazione:** `requirements.txt` elenca i pacchetti. Generato con `pip freeze > requirements.txt`.

---

### 20. Come si crea una relazione one-to-many in SQLAlchemy?

* A) relationship("Model")
* B) ForeignKey("table.id")
* C) Entrambe (ForeignKey + relationship)
* D) OneToMany("Model")

**Risposta: C) Entrambe (ForeignKey + relationship)**

**Spiegazione:** Serve `ForeignKey` nella colonna della tabella "many" e `relationship()` per la navigazione OOP.

---

### 21. Quale metodo HTTP è idempotente?

* A) POST
* B) GET
* C) PATCH
* D) Tutti

**Risposta: B) GET**

**Spiegazione:** GET, PUT, DELETE sono idempotenti (stessa richiesta = stesso risultato). POST non lo è (crea risorse nuove ogni volta).

---

### 22. Cosa sono i CORS?

* A) Common Object Request System
* B) Cross-Origin Resource Sharing
* C) Central Origin Response Service
* D) Custom Object Routing System

**Risposta: B) Cross-Origin Resource Sharing**

**Spiegazione:** CORS è un meccanismo di sicurezza che controlla quali domini possono accedere a un'API. Gestito con Flask-CORS.

---

### 23. Come si validano dati in FastAPI?

* A) Con decoratori
* B) Con Pydantic models
* C) Manualmente
* D) Con form validation

**Risposta: B) Con Pydantic models**

**Spiegazione:** FastAPI usa Pydantic per validazione automatica basata su type hints.

---

### 24. Quale comando avvia un server FastAPI?

* A) fastapi run
* B) uvicorn app:app
* C) python app.py
* D) fastapi start

**Risposta: B) uvicorn app:app**

**Spiegazione:** FastAPI richiede un server ASGI come Uvicorn: `uvicorn filename:app_variable`.

---

### 25. Cosa è REST?

* A) Remote Execution Service Technology
* B) Representational State Transfer
* C) Resource Exchange Standard Transfer
* D) Request Execution State Transfer

**Risposta: B) Representational State Transfer**

**Spiegazione:** REST è uno stile architetturale per API basato su risorse, metodi HTTP e stateless communication.

---

### 26. Quale status code indica "Created"?

* A) 200
* B) 201
* C) 202
* D) 204

**Risposta: B) 201**

**Spiegazione:** 201 Created indica che una nuova risorsa è stata creata con successo (tipicamente dopo POST).

---

### 27. Come si gestisce la sessione in Flask?

* A) Automaticamente con session
* B) Con cookies
* C) Con database
* D) Non è possibile

**Risposta: A) Automaticamente con session**

**Spiegazione:** Flask fornisce `session` (signed cookie) per memorizzare dati tra richieste. Richiede `SECRET_KEY`.

---

### 28. Quale libreria si usa per JWT in Python?

* A) jwt
* B) PyJWT
* C) python-jwt
* D) flask-jwt

**Risposta: B) PyJWT**

**Spiegazione:** PyJWT è la libreria standard per JSON Web Tokens in Python.

---

### 29. Come si crea un blueprint in Flask?

* A) Blueprint("name")
* B) app.blueprint("name")
* C) Blueprint("name",  **name** )
* D) flask.Blueprint("name")

**Risposta: C) Blueprint("name",  **name** )**

**Spiegazione:** `Blueprint(nome, __name__)` crea un blueprint per organizzare route in moduli separati.

---

### 30. Quale comando Docker crea un'immagine?

* A) docker create
* B) docker build
* C) docker make
* D) docker image

**Risposta: B) docker build**

**Spiegazione:** `docker build -t nome .` crea un'immagine dal Dockerfile nella directory corrente.

---

Questi 120 quiz (30 per giorno) coprono tutti i concetti principali del corso e possono essere usati per valutare la comprensione degli studenti!
