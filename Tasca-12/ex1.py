import random

# Función para generar una lista aleatoria de 3 números entre 1 y 9
def gllistaaleatoris():
    l=[]
    for i in range(3):
        l.append(random.randint(1,9))  # Genera un número aleatorio entre 1 y 9
    return l
    
# Función para que el usuario ingrese una lista de 3 números
def llegir_llista():
    l=[]
    for e in range(3):
        a = int(input("Introudueixi el número: "))  # Solicita al usuario un número
        l.append(a)  # Agrega el número a la lista
    return l

# Función para comparar la lista aleatoria con la lista ingresada por el usuario
def comparar(l, m):
    a=[0,0,0,0]
    for i in range(3):
        if l[i]==m[i]:
            a[i]=10  # Marca con 10 si el número y la posición son correctos
    if a[0]==10 and a[1]==10 and a[2]==10:
        print("Enhorabona, ho has encertat tot ")  # Mensaje si todas las posiciones son correctas
        return 0  # Retorna 0 para indicar que el juego ha terminado
    for i in range(3):
        if a[i]==0:
            if m[i] in l:
                a[i]=5  # Marca con 5 si el número está en la lista pero no en la posición correcta
    for i in range(3):
        if a[i]==10:
            print("L'element {} és correcte".format(m[i]))  # Mensaje para números en la posición correcta
        elif a[i]==5:
            print("L'element {} existeix, però no està al seu lloc".format(m[i]))  # Mensaje para números en la lista pero posición incorrecta
        else:
            print("L'element {} no existeix".format(m[i]))  # Mensaje para números que no están en la lista

# Función principal que maneja el juego de adivinanza
def pex1():
    op = 1
    while op != 0:
        l = gllistaaleatoris()  # Genera la lista aleatoria
        m = llegir_llista()  # El usuario ingresa la lista de números
        op = comparar(l, m)  # Compara las listas y actualiza op según el resultado
        
        if op == 0:
            break
        
        continuar = input("Vols seguir jugant? (s/n): ").lower()
        if continuar != 's':
            break
    print("Gràcies per jugar!")

# Entrada principal del programa
if __name__ == "__main__":
    pex1()
