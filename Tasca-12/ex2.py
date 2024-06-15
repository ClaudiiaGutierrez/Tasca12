import json
import os

# Funció per guardar el diccionari en un arxiu JSON abans de sortir
def acabar(diccionari, nom="lista_compra.json"):
    with open(nom, "w") as f:
        json.dump(diccionari, f, indent=4)  # Guarda el diccionari en l'arxiu JSON amb format indentat
    print("Dades guardades en lista_compra.json")  # Missatge de confirmació

# Funció per crear un nou arxiu de llista de compres
def crear_fitxer():
    with open("lista_compra.json", "w") as f:
        print("Fitxer Lista de la Compra creat \n")  # Imprimeix un missatge indicant que l'arxiu ha estat creat

# Funció per inserir un nou element en el diccionari (producte i quantitat)
def inserir_element(diccionari):
    item = input("Nom del producte: ")  
    Unitat = input("Unitats: ") 
    diccionari[item] = Unitat  # Afegeix el producte i la seva quantitat al diccionari
    print(f"Producte {item} afegit.")  # Missatge de confirmació

# Funció per llistar els elements del diccionari (productes i quantitats)
def llista_fitxer(diccionari):
    if not diccionari:
        print("No hi ha productes en la llista de la compra.")  # Missatge si el diccionari està buit
    else:
        for item, cantidad in diccionari.items():
            print(f"Producte: {item}, Quantitat: {cantidad}")  # Imprimeix cada producte i la seva quantitat

# Funció per eliminar un element del diccionari pel nom del producte
def eliminar_element(diccionari):
    item = input("Nom del producte a eliminar: ") 
    if item in diccionari:
        del diccionari[item]  # Elimina el producte del diccionari si existeix
        print(f"Producte {item} eliminat.")  # Missatge de confirmació
    else:
        print("Producte no trobat.")  # Missatge si el producte no està en el diccionari

# Funció per modificar la quantitat d'un producte en el diccionari
def modificar_element(diccionari):
    item = input("Nom del producte a modificar: ") 
    if item in diccionari:
        cantidad = input("Nova quantitat: ")  
        diccionari[item] = cantidad  # Actualitza la quantitat del producte en el diccionari
        print(f"Producte {item} modificat.")  # Missatge de confirmació
    else:
        print("Producte no trobat.") 
# Funció per mostrar el menú d'opcions i obtenir la elecció de l'usuari
def menu_fitxer():
    print("""
    Menú Llista de la Compra:
    1. Afegir producte a la llista
    2. Llistar productes de la llista
    3. Eliminar un producte de la llista
    4. Modificar un producte de la llista
    5. Sortir
    """)
    
    op = int(input("Eligeix una opció: "))  
    return op  

# Funció principal que maneja la lògica del programa
def pex2():
    nom = "lista_compra.json"  
    diccionari = {}  # Diccionari que emmagatzemarà els productes i les seves quantitats
    
    # Si existeix l'arxiu, el llegim i guardem en el diccionari
    if os.path.isfile(nom):
        with open(nom, "r") as f:
            diccionari = json.load(f)
    else:
        crear_fitxer()
    
    op = 0
    while op != 5:
        op = menu_fitxer()
        if op == 1:
            inserir_element(diccionari)
        elif op == 2:
            llista_fitxer(diccionari)
        elif op == 3:
            eliminar_element(diccionari)
        elif op == 4:
            modificar_element(diccionari)
        elif op == 5:
            acabar(diccionari, nom)
            print("Surtint del programa...")
        else:
            print("Opció no vàlida. Si us plau, tria novament.")

# Executar la funció principal quan el programa es cridi directament
if __name__ == "__main__":
    pex2()
