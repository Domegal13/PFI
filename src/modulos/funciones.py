import os
import re
from colorama import init, Fore, Back, Style
init()

# regex_alpha = r'^[A-Za-zÀ-ÿ\s]+$'
# regex_nombre = r'^[a-zA-Z0-9\s\W]+$'
regex_nombre = r'^[a-zA-Z][a-zA-Z0-9\s\W]*$'
lista_productos = []
lista_nombres_productos = []
lista_cant_prod = []

# ########################## FUNCTION CLEAR CONSOLE ###################################################

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# ########################## FUNCTION VALIDAR NOMBRE ###################################################
def validar_nombre(nombre):
    
    if len(nombre) < 2 or len(nombre) >= 50:
        return False
    else:
        if re.match(regex_nombre, nombre):
            return True
        else:
            return False


# ########################## FUNCTION VALIDAR CANTIDAD ######################################################
def validar_cantidad(cantidad):

    if cantidad <= 0 :
        print("El valor de ser mayor a 0")
        return False
    else:
        return True

# ########################## FUNCTION MOSTRAR MENU ######################################################################
def mostrar_menu():
    print( "\n" + Fore.YELLOW +  Style.BRIGHT + "Menú de Gestión de Productos: \n" + Style.RESET_ALL) 
    print("1- Registro: Alta de productos nuevos")
    print("2- Visualización: Consulta datos de productos")
    print("3- Actualización: Modificar cantidad de stock del producto")
    print("4- Elimininación: Dar de baja productos")
    print("5- Listado: Listado completo de los productos en la base de datos")
    print("6- Reporte de bajo stock: Lista de productos con cantidad bajo mínimo")
    print("7- Salir\n")

# ##########################  OPCION 1 - Registro: Alta de productos nuevos ###################################
def agregar_producto():
    nombre_producto = input(Style.RESET_ALL + "\nIntroduzca el nombre del producto: ")
    nombre_producto = nombre_producto.upper()
    nombre_validado = validar_nombre(nombre_producto)
    if nombre_validado :
        if nombre_producto in lista_nombres_productos:
            print(Fore.YELLOW + f"El producto {nombre_producto} ya existe...")
        else:
            try:
                cantidad_producto = int(input("introduzca la cantidad: "))
                cantidad_validada = validar_cantidad(cantidad_producto)
                if cantidad_validada :
                    lista_nombres_productos.append(nombre_producto)
                    lista_cant_prod.append(cantidad_producto)
                    print(Fore.GREEN + Style.BRIGHT + "\nProducto agregado exitosamente...")
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "\nLa cantidad debe ser numérica")       
    else:
        print(Fore.RED + Style.BRIGHT + "\nIntroduzca un nombre de producto correcto\n")
        agregar_producto()

# ##########################  OPCION 2 - Visualización: Consulta datos de productos ###################################
def mostrar_un_producto():
    nombre_producto = input(Fore.YELLOW + "\nIntroduzca el nombre del producto a buscar: ")
    nombre_producto = nombre_producto.upper()
    if nombre_producto in lista_nombres_productos:
        index = lista_nombres_productos.index(nombre_producto)
        print(Fore.LIGHTGREEN_EX + f"\n{nombre_producto} Stock: {lista_cant_prod[index]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + f"El producto {nombre_producto}, no existe...")
        

              
# ##########################  OPCION 3 - Actualización: Modificar cantidad de stock del producto ###################################


#! ############# MENU STOTK
def mostrar_menu_stock():
    
    print(Fore.YELLOW +  Style.BRIGHT + "\n1- Aumentar Stock")
    print("2- Disminuir Stock")
    print("3- Salir")

#! ############  AUMENTAR EL STOCK
def aumentar_stock():
    try:
        nombre_producto = input(Style.RESET_ALL + "\nIntrozca el nombre del producto: ")
        nombre_producto = nombre_producto.upper()
        nombre_validado = validar_nombre(nombre_producto)
        if nombre_validado :
            if nombre_producto in lista_nombres_productos:
                cantidad_producto = int(input("intruduzca la cantidad: "))
                cantidad_validada = validar_cantidad(cantidad_producto)
                if cantidad_validada:
                    index = lista_nombres_productos.index(nombre_producto)
                    lista_cant_prod[index] += cantidad_producto
                else:
                    print(Fore.RED + Style.BRIGHT + "La cantidad debe ser mayor a cero")  
            else:
                print(Fore.RED + Style.BRIGHT + f"El producto {nombre_producto}, no existe...")
        else:
            print(Fore.RED + Style.BRIGHT + "Introduzca un nombre de producto correcto")              
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "La cantidad debe ser numérica") 

#! ############# DISMINUIR EL STOCK
def disminuir_stock():
    try:
        nombre_producto = input(Style.RESET_ALL + "\nIntrozca el nombre del producto: ")
        nombre_producto = nombre_producto.upper()
        nombre_validado = validar_nombre(nombre_producto)
        if nombre_validado :
            if nombre_producto in lista_nombres_productos:
                cantidad_producto = int(input("intruduzca la cantidad: "))
                cantidad_validada = validar_cantidad(cantidad_producto)
                if cantidad_validada:
                    index = lista_nombres_productos.index(nombre_producto)
                    if lista_cant_prod[index] >= cantidad_producto:
                        lista_cant_prod[index] -= cantidad_producto
                    else:
                        print(Fore.RED + Style.BRIGHT + "No hay Stock suficente...")  
                else:
                    print(Fore.RED + Style.BRIGHT + "La cantidad debe ser mayor a cero")  
            else:
                print(Fore.RED + Style.BRIGHT + f"El producto {nombre_producto}, no existe...")
        else:
            print(Fore.RED + Style.BRIGHT + "Introduzca un nombre de producto correcto")   
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "La cantidad debe ser numérica") 

#! ############# SWITCH CASE MODIFICAR STOCK
def switch_case_stock(opc):
    match(opc):
        case 1:
            aumentar_stock()
        case 2:
            disminuir_stock()
        case 3:
            print(Fore.YELLOW + Style.BRIGHT + "Saliendo de Modificar Stock" + Style.RESET_ALL)
        case _:
            print(Fore.RED + Style.BRIGHT + "Opción inválida..." + Style.RESET_ALL)

#! ############ FUNCTION MODIFICAR STOTK
def modificar_stock():
    opc = 0
    while opc != 3:
        print(Fore.YELLOW + Style.BRIGHT + "Menú Modificar Stock") 
        mostrar_menu_stock()
        try:
            opc = int(input(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una opción 1-3: "))
            switch_case_stock(opc)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Opción Inválida...")  
    
    limpiar_consola()
        

# ##########################  OPCION 4 -  Elimininación: Dar de baja productos #########################################################

def eliminar_producto():
    nombre_producto = input(Fore.YELLOW + "\n Introduzca el Producto a eliminar: " + Style.RESET_ALL)
    nombre_producto = nombre_producto.upper()
    validar_nombre(nombre_producto)
    if validar_nombre:
        if nombre_producto in lista_nombres_productos:
            resp = input(Fore.LIGHTMAGENTA_EX + f"Está seguro de elimiar el producto: " + Fore.BLUE + Style.BRIGHT + f"{nombre_producto}" + Fore.LIGHTMAGENTA_EX  + " - S/N:")
            if resp == "S" or resp == "s":
                index = lista_nombres_productos.index(nombre_producto)
                producto_eliminado = lista_nombres_productos.pop(index)
                del lista_cant_prod[index]
            else:
                pass
        else:
            print(Fore.RED + Style.BRIGHT + f"Producto no encontrado..." + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + f"Introduzca un valor correcto..." + Style.RESET_ALL)


# ##########################  OPCION 5 - Listado: Listado completo de los productos en la base de datos ###################################


def mostrar_productos():
    if len(lista_nombres_productos) > 0:
        print(Fore.YELLOW + "\nLista de Productos")
        for nombre in lista_nombres_productos:
            index = lista_nombres_productos.index(nombre)
            # print(Fore.LIGHTGREEN_EX + f"{nombre}" + Fore.YELLOW + f" --Stock: {lista_cant_prod[index]}" + Style.RESET_ALL) 
            print(Fore.LIGHTGREEN_EX + f"{nombre}" + Fore.YELLOW + " --Stock:" + Fore.GREEN +  f"  {lista_cant_prod[index]}" + Style.RESET_ALL) 
           
    else:
        print(Fore.RED + Style.BRIGHT + "No hay productos para mostrar")  
        

# ##########################  OPCION 6 - Reporte de bajo stock: Lista de productos con cantidad bajo mínimo ###################################

def mostrar_menu_reporte_stock():
    print(Fore.YELLOW +  Style.BRIGHT + "\n1- Stock Alto")
    print("2- Stock Medio")
    print("3- Stock Bajo")
    print("4- Salir")

def reporte_stock(opc):
    
    if len(lista_nombres_productos) > 0:
        if opc == 1:
            lista_stock_alto = []
            print(Fore.YELLOW + "\nLista de Productos")
            for nombre in lista_nombres_productos:
                index = lista_nombres_productos.index(nombre)
                if lista_cant_prod[index] > 10:
                    lista_stock_alto.append([nombre, lista_cant_prod[index]])
            if len(lista_stock_alto) > 0:
                for alto in lista_stock_alto:
                    print(Fore.LIGHTGREEN_EX + f"{alto[0]} Stock: {alto[1]}" + Fore.LIGHTBLUE_EX + "  -- Stock Alto" + Style.RESET_ALL)   
            else:
                print(Fore.RED + Style.BRIGHT + "No hay productos para mostrar")    
        elif opc == 2:
            lista_stock_medio = []
            print(Fore.YELLOW + "\nLista de Productos")
            for nombre in lista_nombres_productos:
                index = lista_nombres_productos.index(nombre)
                if lista_cant_prod[index] > 5 and lista_cant_prod[index] <=10:
                    lista_stock_medio.append([nombre, lista_cant_prod[index]])
            if len(lista_stock_medio) > 0:
                for medio in lista_stock_medio:
                    print(Fore.LIGHTGREEN_EX + f"{medio[0]} Stock: {medio[1]}" + Fore.YELLOW + "  -- Stock Medio" + Style.RESET_ALL)   
            else:
                print(Fore.RED + Style.BRIGHT + "No hay productos para mostrar")    
        elif opc == 3:
            lista_stock_bajo = []
            print(Fore.YELLOW + "\nLista de Productos")
            for nombre in lista_nombres_productos:
                index = lista_nombres_productos.index(nombre)
                if lista_cant_prod[index] <= 5:
                    lista_stock_bajo.append([nombre, lista_cant_prod[index]])
            if len(lista_stock_bajo) > 0:
                for bajo in lista_stock_bajo:        
                    print(Fore.LIGHTGREEN_EX + f"{bajo[0]} Stock: {bajo[1]}" + Fore.RED + "  -- Stock Bajo" + Style.RESET_ALL)
            else:
                print(Fore.RED + Style.BRIGHT + "No hay productos para mostrar")  
        elif opc == 4:
            print(Fore.YELLOW + Style.BRIGHT + "Saliendo del Reporte de Stock..." + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Opción inválida..." + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "No hay productos para mostrar")  


def mostrar_reporte_productos():
    opc = 0
    while opc != 4:
        print(Fore.YELLOW + Style.BRIGHT + "\nMostrar Stock") 
        mostrar_menu_reporte_stock()
        try:
            opc = int(input(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una opción 1-4: "))
            reporte_stock(opc)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nOpción Inválida...")  

    limpiar_consola()



# ##########################   SWITCH CASE OPTIONS MAIN ######################################################################
def menu_switch_case(opcion_seleccionada):
        match opcion_seleccionada:
            case 1:                
                agregar_producto()
            case 2:
                mostrar_un_producto()
            case 3:
                modificar_stock()              
            case 4:
                eliminar_producto()
            case 5:
                mostrar_productos()
            case 6:
                mostrar_reporte_productos()
            case 7:
                print(Style.RESET_ALL + "Saliendo del Sistema, gracias... \n")
            case _:
                print(Fore.RED + Style.BRIGHT + "La opcion seleccionada es inválida: \n")    