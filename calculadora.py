def seleccion_opcion(opcion):
    opciones = {
        1: suma,
        2: resta,
        3: multiplicacion,
        4: division,
        5: salir
    }
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción no válida, por favor elija una opción correcta.")
        
        
def suma():
    numero_uno = float(input("Ingrese los numeros:\n"))
    print("+")
    numero_dos = float(input())
    print("_____________")
    print(numero_uno + numero_dos)

def resta():
    numero_uno = float(input("Ingrese los numeros:\n"))
    print("-")
    numero_dos = float(input())
    print("_____________")
    print(numero_uno - numero_dos)
    
def multiplicacion():
    numero_uno = float(input("Ingrese los numeros:\n"))
    print("x")
    numero_dos = float(input())
    print("_____________")
    print(numero_uno * numero_dos)
    
def division():
    numero_uno = float(input("Ingrese los numeros:\n"))
    print("/")
    numero_dos = float(input())
    print("_____________")
    if numero_dos == 0:
        print("No se puede dividir por 0 (cero)")
    else:
        print(numero_uno / numero_dos)

def salir():
    print("OFF")
    global bandera_menu
    bandera_menu = False
    

# Menu
bandera_menu = True
while (bandera_menu):
    print("\nOpciones: \n1- Suma\n2- Resta\n3- Multiplicacion\n4- Division\n5- Salir")
    opcion_menu = int(input("Ingrese número de operacion a realizar: "))
    seleccion_opcion(opcion_menu)  # Funcion selectora de funcion
    


        



