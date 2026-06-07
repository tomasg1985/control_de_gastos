# AGREGAR GASTO

def agregar_gasto(historial, categoria, monto, descripcion):
    
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
        "descripcion" : descripcion
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
        print(f"Categoria: {datos['categoria']} | Monto: ${datos['monto']:.2f}")

# CALCULO TOTAL DE GASTOS

def calcular_total(historial):
    
    """
    PROPÓSITO:
    Realizar el calculo de todos los gastos registrados.
    
    PARAMETROS:
    historial: list -> Retorna un str ya que el mensaje devuelto es formateado.
    
    """
    
    total = sum(gasto['monto'] for gasto in historial)
    return f"El total de los gastos registrados es de: {total:,.2f}"