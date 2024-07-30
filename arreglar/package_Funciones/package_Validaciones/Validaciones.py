def validar_nombre_pokemon(nombre: str):
        '''
        Valida el nombre del pokemon ingresado.
        Args: Recibe como parámetros "nombre" como un str.
        Con el ".isalpha()" me aseguro que sean solo caracteres alfabéticos.
        Con el "[0].isupper()" me aseguro que el primer caracter sea mayúscula.
        Con el "len(nombre) <=20" me aseguro que el rango máximo de caracteres no sea mayor a 20.
        Retorna: si el nombre ingresado es valido.
        '''
        nombre = nombre.strip() 
        nombre_valido = nombre.isalpha() and nombre[0].isupper() and len(nombre) <= 20
        if not nombre_valido: 
                print("El nombre del pokemón ingresado no es valido.                         ")
        return nombre_valido

def validar_tipo_pokemon(tipos: str):
    '''
    Valida que el tipo de pokemon ingresado sea uno de los ya establecidos dentro de la lista de tipos.
    Args: recibe como parámetros "tipos" como un str.
    Retorna: 
    El tipo del pokemon con el primer caracter mayúscula, por el ".capitalize()", en caso de se cumpla lo solicitado.
    y no retorna nada en caso de que no se cumpla.
    '''
    tipos = tipos.strip()
    lista_tipos = ["Agua", "Acero", "Bicho", "Dragon", "Electrico", "Fantasma",
                "Fuego", "Hada", "Hielo", "Lucha", "Normal", "Planta",
                "Psiquico", "Roca", "Siniestro", "Tierra", "Veneno", "Volador"]
    
    if tipos in lista_tipos:
        print("Tipo de Pokemón ingresado es valido.")
        return tipos.capitalize()
    else:
        print("El tipo de pokemon es invalido, vuelva a ingresar un tipo valido.")
        return None

def validar_poder(poder: int):
    '''
    valida el poder del pokemon ingresado.
    args: Recibe como parametros "poder" como un int.
    con el isinstance verificamos si poder es del tipo int.
    con el 0 <= poder <= 150 nos aseguramos que este en un rango de 0 a 150.
    '''
    poder_valido = isinstance(poder, int) and 0 <= poder <= 150
    if not poder_valido:
        print("El poder ingresado no es valido, vuelva a ingresar otro.")
    return poder_valido

def Validar_Defensa(defensa: int):
    '''
    valida la defensa del pokemon ingresado.
    args: Recibe como parametros "poder" como un int.
    con el isinstance verificamos si poder es del tipo int.
    con el 0 <= poder <= 150 nos aseguramos que este en un rango de 0 a 150.
    '''
    Defensa_Valida = isinstance(defensa, int) and 0 <= defensa <= 150
    if not Defensa_Valida:
        print("La defensa ingresada no es valida, vuelva a ingresar otro.")
    return Defensa_Valida

def validar_tamaño_pokemon(tamaño: str):
    '''
    Valida el tamaño del pokemon ingresado.
    Args: Recibe como parámetros "tamaño" como un str.
    Con el ".isalpha()" me aseguro que sean solo caracteres alfabéticos.
    Con el "isupper()" me aseguro que todos los caracter sean mayúscula.
    Con el "len(tamaño) <= 2" me aseguro que el rango máximo de caracteres no sea mayor a 2.
    Retorna: El tamaño de pokemon.
    '''
    tamaño = tamaño.strip()
    tamaño_valido = tamaño.isalpha() and tamaño.isupper() and len(tamaño) <= 2
    if not tamaño_valido:
        print("El tamaño ingresado no es valido, debe ser mayúscula y no superar los 2 caracteres.")
    return tamaño_valido

def validar_habilidad_pokemon(habilidad: str):
    '''
    valida la o las habilidades del pokemon ingresado.
    Args: Recibe como parámetros "habilidad" como un str.
    Con el ".isalpha()" me aseguro que sean solo caracteres alfabéticos.
    Con el "[0].isupper()" me aseguro que el primer caracter ingresado este en mayúsculas.
    Con el len(habilidad) <= 20 me aseguro que los caracteres ingresados no supere los 20.
    Retorna: La habilidad del pokemon.
    '''
    habilidad = habilidad.strip()
    habilidad_valida = habilidad.isalpha() and habilidad[0].isupper() and len(habilidad) <= 20
    if not habilidad_valida:
        print("La habilidad ingresa no es valida.")
    return habilidad_valida