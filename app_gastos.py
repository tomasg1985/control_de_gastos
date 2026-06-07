from colorama import Fore, Style, init
from logica_gastos import *
init()

historial = []

while True:
    
    print()
    print(f"{Fore.GREEN}1. Agregar Gasto"+ Style.RESET_ALL)
    print(f"{Fore.CYAN}2. Ver Historial"+ Style.RESET_ALL)
    print(f"{Fore.YELLOW}3. Calcular Total"+ Style.RESET_ALL)
    print(f"{Fore.RED}4. Salir"+ Style.RESET_ALL)
    print()
    
    opcion_usuario = input("Elija una opcion: ")
    
    match opcion_usuario:
        case "1":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}AGREGAR GASTO")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            categoria = input("Ingrese la categoria de su gasto ('ej: Alquiler'): ").strip().capitalize()
            monto = float(input("Indique el monto: "))
            descripcion = input("Ingrese una descripcion corta: ").strip().capitalize()
            
            agregar_gasto(historial, categoria, monto, descripcion)
            
            print(f"{Fore.GREEN}Gasto registrado con exito!"+ Style.RESET_ALL)
            
        case "2":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}VER HISTORIAL")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            ver_historial(historial)
            
        case "3":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}CALCULAR TOTAL")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            print(calcular_total(historial)+ Style.RESET_ALL)
            
        case "4":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}SALIR")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            print(f"{Fore.YELLOW}ADIOS!"+ Style.RESET_ALL)
            break
            
        case _:
            print(f"{Fore.RED}Opcion incorrecta!"+ Style.RESET_ALL)