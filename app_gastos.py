from colorama import Fore, Style, init
from logica_gastos import *
init()

historial = []

while True:
    
    print()
    print(f"{Fore.GREEN}1. Buscar Gasto"+ Style.RESET_ALL)
    print(f"{Fore.GREEN}2. Agregar Gasto"+ Style.RESET_ALL)
    print(f"{Fore.GREEN}3. Editar Gasto"+ Style.RESET_ALL)
    print(f"{Fore.GREEN}4. Eliminar Gasto"+ Style.RESET_ALL)
    print(f"{Fore.CYAN}5. Ver Historial"+ Style.RESET_ALL)
    print(f"{Fore.YELLOW}6. Calcular Total"+ Style.RESET_ALL)
    print(f"{Fore.YELLOW}7. Generar Reporte"+ Style.RESET_ALL)
    print(f"{Fore.RED}8. Salir"+ Style.RESET_ALL)
    print()
    
    opcion_usuario = input("Elija una opcion: ")
    
    match opcion_usuario:
        case "1":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}BUSCAR GASTO")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            termino = input("Ingrese el gasto que desea buscar: ").strip().title()
            buscar_gasto(historial, termino)
            
        case "2":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}AGREGAR GASTO")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            categoria = input("Ingrese la categoria de su gasto ('ej: Alquiler'): ").strip()
            monto = int(input("Indique el monto: "))
            descripcion = input("Ingrese una descripcion corta: ").strip()
            
            agregar_gasto(historial, categoria, monto, descripcion)
            print(f"{Fore.GREEN}====================")
            print(f"{Fore.GREEN}Gasto registrado con exito!")
            print(f"{Fore.GREEN}===================="+ Style.RESET_ALL)
            
        case "3":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}EDITAR GASTO")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            editar_gasto(historial)
            print(f"{Fore.GREEN}Gastos editados con exito!"+ Style.RESET_ALL)
            
        case "4":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}ELIMINAR GASTO")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            eliminar_gasto(historial)
            print(f"{Fore.GREEN}====================")
            print(f"{Fore.GREEN}Gasto eliminado con exito!")
            print(f"{Fore.GREEN}===================="+ Style.RESET_ALL)
            
        case "5":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}VER HISTORIAL")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            ver_historial(historial)
            
        case "6":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}CALCULAR TOTAL")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            print(calcular_total(historial)+ Style.RESET_ALL)
            
        case "7":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}GENERAR REPORTE")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            mostrar_reporte(historial)
            
        case "8":
            print(f"{Fore.CYAN}====================")
            print(f"{Fore.CYAN}SALIR")
            print(f"{Fore.CYAN}===================="+ Style.RESET_ALL)
            
            print(f"{Fore.YELLOW}ADIOS!"+ Style.RESET_ALL)
            break
        
        case _:
            print(f"{Fore.RED}Opcion incorrecta!"+ Style.RESET_ALL)