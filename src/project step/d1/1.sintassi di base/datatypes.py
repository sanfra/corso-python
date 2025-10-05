# Variabili e tipi di dato
nome = "Alice"      # stringa (testo)
eta = 25            # intero
altezza = 1.70      # numero decimale (float)
studente = True     # booleano (vero/falso)
nessun_valore = None  # valore nullo
lista_numeri = [1, 2, 3, 4, 5]  # lista
coordinate = (10, 20)  # tupla
numeri_unici = {1, 2, 3, 3, 4}  # set (elimina duplicati)
persona = {"nome": "Mario", "eta": 30}  # dizionario

# Verificare il tipo di TUTTI i tipi di dato
print("=" * 50)
print("VERIFICA TIPI DI DATO")
print("=" * 50)

print(f"\nnome = {nome}")
print(f"Tipo: {type(nome)}")  # <class 'str'>

print(f"\neta = {eta}")
print(f"Tipo: {type(eta)}")  # <class 'int'>

print(f"\naltezza = {altezza}")
print(f"Tipo: {type(altezza)}")  # <class 'float'>

print(f"\nstudente = {studente}")
print(f"Tipo: {type(studente)}")  # <class 'bool'>

print(f"\nnessun_valore = {nessun_valore}")
print(f"Tipo: {type(nessun_valore)}")  # <class 'NoneType'>

print(f"\nlista_numeri = {lista_numeri}")
print(f"Tipo: {type(lista_numeri)}")  # <class 'list'>
print(f"Lunghezza: {len(lista_numeri)}")

print(f"\ncoordinate = {coordinate}")
print(f"Tipo: {type(coordinate)}")  # <class 'tuple'>
print(f"Lunghezza: {len(coordinate)}")

print(f"\nnumeri_unici = {numeri_unici}")
print(f"Tipo: {type(numeri_unici)}")  # <class 'set'>
print(f"Elementi unici: {len(numeri_unici)}")

print(f"\npersona = {persona}")
print(f"Tipo: {type(persona)}")  # <class 'dict'>
print(f"Chiavi: {len(persona)}")

print("\n" + "=" * 50)

# Verifica con isinstance (metodo alternativo)
print("\nVERIFICA CON isinstance():")
print(f"nome è una stringa? {isinstance(nome, str)}")
print(f"eta è un intero? {isinstance(eta, int)}")
print(f"altezza è un float? {isinstance(altezza, float)}")
print(f"studente è un booleano? {isinstance(studente, bool)}")
print(f"lista_numeri è una lista? {isinstance(lista_numeri, list)}")
print(f"coordinate è una tupla? {isinstance(coordinate, tuple)}")
print(f"numeri_unici è un set? {isinstance(numeri_unici, set)}")
print(f"persona è un dizionario? {isinstance(persona, dict)}")

# Conversioni tra tipi (casting)
print("\n" + "=" * 50)
print("CONVERSIONI TRA TIPI")
print("=" * 50)

# String to int
testo_numero = "42"
print(f"\n'{testo_numero}' (str) → {int(testo_numero)} (int)")

# Int to string
numero = 100
print(f"{numero} (int) → '{str(numero)}' (str)")

# String to float
testo_decimale = "3.14"
print(f"'{testo_decimale}' (str) → {float(testo_decimale)} (float)")

# Int to float
intero = 5
print(f"{intero} (int) → {float(intero)} (float)")

# Float to int (tronca i decimali)
decimale = 9.99
print(f"{decimale} (float) → {int(decimale)} (int)")

# List to tuple
lista = [1, 2, 3]
print(f"{lista} (list) → {tuple(lista)} (tuple)")

# Tuple to list
tupla = (4, 5, 6)
print(f"{tupla} (tuple) → {list(tupla)} (list)")

# List to set (rimuove duplicati)
lista_con_duplicati = [1, 2, 2, 3, 3, 3]
print(f"{lista_con_duplicati} (list) → {set(lista_con_duplicati)} (set)")

# Set to list
insieme = {7, 8, 9}
print(f"{insieme} (set) → {list(insieme)} (list)")

print("\n" + "=" * 50)