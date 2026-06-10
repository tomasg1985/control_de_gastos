import datetime


# AGREGAR GASTO

def agregar_gasto(historial, categoria, monto, descripcion):

    try:
        with open("mis_gastos.txt", "a") as archivo:
            fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            archivo.write(f"{fecha} | {categoria} | $ {monto} | {descripcion} \n")
        print("✅ ¡El archivo se actualizó correctamente!")
    except Exception as e:
        print(f"❌ Error detectado: {e}")
        
    """
    PROPÓSITO:
    Esta funcion es la encargada de realizar el registro del gasto y agregarlo a la lista historial = [].
    
    PARAMETROS:
    historial (list) -> Lista donde estan alojados los registros de gastos.
    
    DATOS DICCIONARIO:
    categoria (str) -> Categoria del gasto (ej. "Alquiler")
    monto (float) -> Monto total del gasto.
    descripcion (str) -> Descripcion del gasto.
    
    RETORNO:
    Devuelve True
    
    """

    nuevo_gasto = {
        "categoria" : categoria,
        "monto" : monto,
        "descripcion" : descripcion,
        "fecha" : datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    historial.append(nuevo_gasto)
    return True


# HISTORIAL DE GASTOS

def ver_historial(historial):
    
    """
    PROPÓSITO:
    Esta funcion es la encargada de mostrar el historial de gastos que se han realizado.
    
    PARAMETROS:
    historial: list -> No retorna ningun valor solo sirve de almacenamiento para los datos que se agregan.
    
    RETORNO: None
    
    """
    if not historial:
        print("No hay gastos registrados")
        return
    
    for datos in historial:
        print(f"Categoria: {datos['categoria']} | Monto: ${datos['monto']}")

# CALCULO TOTAL DE GASTOS

def calcular_total(historial):
    
    """
    PROPÓSITO:
    Realizar el calculo de todos los gastos registrados.
    
    PARAMETROS:
    historial: list -> Retorna un str ya que el mensaje devuelto es formateado.
    
    """
    
    total = sum(gasto['monto'] for gasto in historial)
    return f"El total de los gastos registrados es de: {total}"

# BUSQUEDA DE GASTOS

def buscar_gasto(historial, termino):
    
    encontrado = False
    
    for busqueda in historial:
        
        if termino.lower() in busqueda['categoria'] or termino.lower() in busqueda['descripcion']:
            print(f"Categoria: {busqueda['categoria']} | Descripción: {busqueda['descripcion']}")
            encontrado = True
            
    if not encontrado:
        print(f"No se encontraron coincidencias para su busqueda")
        
# ELIMINAR GASTOS

def eliminar_gasto(historial):
    for i, gasto in enumerate(historial, start=1):
        print(f"{i}. {gasto['categoria']} - ${gasto['monto']}")
        

    solicitud_eliminar = int(input("Indique el numero del registro que desea eliminar: "))

    if solicitud_eliminar < 1 or solicitud_eliminar > len(historial):
        print("No se encontraron registros a su solicitud")
    else:
        eliminado = historial.pop(solicitud_eliminar - 1)
        print(f"Registro de '{eliminado['categoria']}' eliminado con éxito.")
        
# EDITAR GASTOS

def editar_gasto(historial):
    for i, gasto in enumerate(historial, start=1):
        print(f"{i}. {gasto['categoria']} - ${gasto['monto']}")
        
    solicitud_editar = int(input("Indique el numero del registro que desea editar: "))
    
    if 1 <= solicitud_editar <= len(historial):
        print(f"El registro que busca existe!")
        
        nueva_categoria = input("Indique la nueva categoria: ")
        nuevo_monto = int(input("Indique el nuevo monto: "))
        nueva_descripcion = input("Indique la nueva descripción: ")
        
        historial[solicitud_editar - 1].update({'categoria':nueva_categoria, 'monto':nuevo_monto, 'descripcion':nueva_descripcion})
        print(f"Datos reeplazados satisfactoriamente")
        print(f"Sus nuevos datos son: {historial[solicitud_editar - 1]}")
    else:
        print("El registro que busca no extiste!")
        
# REPORTE DE GASTOS

def mostrar_reporte(historial):
    if not historial:
        return 
    
    montos = [gasto['monto'] for gasto in historial]
    total = sum(montos)
    promedio = total / len(montos)
    maximo = max(montos)
    minimo = min(montos)

    print(f"--- REPORTE ESTADÍSTICO ---")
    print(f"Total gastado:      ${total}")
    print(f"Promedio de gastos: ${promedio}")
    print(f"Gasto más elevado:  ${maximo}")
    print(f"Gasto más bajo:     ${minimo}")