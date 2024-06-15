import ex1
import ex2
import ex3
import ex4
import ex5
import ex6

def main():
    op = 0
    while op < 1 or op > 7:
        print("""
              1. Mastermind
              2. Llista de compra
              3. Joc
              4. POO
              5. Scrapping
              6. Servei web
              7. Sortir
              """)
        try:
            op = int(input("Tria una opció: "))
            if op < 1 or op > 7: 
                print("Ópcio no válida")
        except ValueError:
            print("Per favor, introdueix un número vàlid.")
    return op

op = 0
while op != 7:
    op = main()
    if op == 1: 
        ex1.pex1()
    elif op == 2:
        ex2.pex2()
    elif op == 3:
        ex3.pex3()
    elif op == 4:
        ex4.pex4()
    elif op == 5:
        ex5.pex5()
    elif op == 6:
        ex6.pex6()
    elif op == 7:
        print("Gracies per utilitzar el joc")

main() 