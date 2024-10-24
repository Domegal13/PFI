import re
from colorama import init, Fore, Back, Style
init()

regex_nombre = r'^[A-Za-zÀ-ÿ\s]+$'
lista_productos = []
lista_nombres_productos = []
lista_cant_prod = []

def validar_nombre(nombre):
    
    if len(nombre) < 2 or len(nombre) >= 50:
        return False
    else:
        if re.match(regex_nombre, nombre):
            return True
        else:
            return False

def validar_cantidad(cantidad):

    if cantidad <= 0 :
        print("El valor de ser mayor a 0")
        return False
    else:
        return True


def mostrar_menu():
    print( "\n" + Fore.YELLOW +  Style.BRIGHT + "Menú de Gestión de Productos: \n" + Style.RESET_ALL) 
    print("1- Registro: Alta de productos nuevos")
    print("2- Visualización: Consulta datos de productos")
    print("3- Actualización: Modificar cantidad de stock del producto")
    print("4- Elimininación: Dar de baja productos")
    print("5- Listado: Listado completo de los productos en la base de datos")
    print("6- Reporte de bajo stock: Lista de productos con cantidad bajo mínimo")
    print("7- Salir\n")


def agregar_producto():
    nombre_producto = input("Introzca el nombre del producto: ")
    nombre_validado = validar_nombre(nombre_producto)
    if nombre_validado :
        try:
            cantidad_producto = int(input("intruduzca la cantidad: "))
            cantidad_validada = validar_cantidad(cantidad_producto)
            if cantidad_validada :
                
                if nombre_producto in lista_nombres_productos:
                    print(f"El producto {nombre_producto} ya existe...")
                else:
                    lista_nombres_productos.append(nombre_producto)
                    lista_cant_prod.append(cantidad_producto)
                    print("Producto agregado exitosamente...")

        except ValueError:
            print("La cantidad debe ser numérica")       
    else:
        print("Introduzca un nombre correcto")
        agregar_producto()


def agregar_producto_001():
    nombre_producto = input(Style.RESET_ALL + "\nIntrozca el nombre del producto: ")
    nombre_validado = validar_nombre(nombre_producto)
    if nombre_validado :
        if nombre_producto in lista_nombres_productos:
            print(f"El producto {nombre_producto} ya existe...")
        else:

            try:
                cantidad_producto = int(input("intruduzca la cantidad: "))
                cantidad_validada = validar_cantidad(cantidad_producto)
                if cantidad_validada :
                    
                    if nombre_producto in lista_nombres_productos:
                        print(f"El producto {nombre_producto} ya existe...")
                    else:
                        lista_nombres_productos.append(nombre_producto)
                        lista_cant_prod.append(cantidad_producto)
                        print("Producto agregado exitosamente...")

            except ValueError:
                print("\nLa cantidad debe ser numérica")       
    else:
        print("\nIntroduzca un nombre correcto\n")
        agregar_producto()

def mostrar_productos():
    print(Fore.YELLOW + "\nLista de Productos")
    for nombre in lista_nombres_productos:
        index = lista_nombres_productos.index(nombre)
        print(Fore.LIGHTGREEN_EX + f"{nombre} Stock: {lista_cant_prod[index]}" + Style.RESET_ALL)

def modificar_stock():
    nombre_producto = input(Style.RESET_ALL + "\nIntrozca el nombre del producto: ")
    nombre_validado = validar_nombre(nombre_producto)
    if nombre_validado :
        if nombre_producto in lista_nombres_productos:
            try:
                cantidad_producto = int(input("intruduzca la cantidad: "))
                cantidad_validada = validar_cantidad(cantidad_producto)
                if cantidad_validada:
                    index = lista_nombres_productos.index(nombre_producto)
                    lista_cant_prod[index] += cantidad_producto
                else:
                    print("La cantidad debe ser mayor a cero")    
            except ValueError:
                print("La cantidad debe ser numérica")   
        else:
            print(f"El producto {nombre_producto}, no existe...")
    else:
        print("Introduzca un nombre correcto")       



def menu_switch_case(opcion_seleccionada):
        match opcion_seleccionada:
            case 1:
                # agregar_producto()
                agregar_producto_001()
            case 2:
                mostrar_productos()
            case 3:
                modificar_stock()                
            case 4:
                print("La opcion seleccionada fue: " , opcion_seleccionada, "\n")
            case 5:
                print("La opcion seleccionada fue: " , opcion_seleccionada, "\n")
            case 6:
                print("La opcion seleccionada fue: " , opcion_seleccionada, "\n")
            case 7:
                print(Style.RESET_ALL + "Saliendo del Sistema, gracias... \n")
            case _:
                print("La opcion seleccionada es inválida: \n")    