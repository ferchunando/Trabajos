import csv
import json
from package_Funciones.package_Validaciones.Validaciones import *
from package_Funciones.Funciones import *
from package_Ordenamiento.Ordenamiento import *

def Guardar_Pokemones_Json(Tipo, Pokemones):
    '''
    Guarda los datos de los pokemones de un tipo específico en un archivo json.
    Args:
        Recibe como parámetros: "tipo" como un str, el cual es un tipo de pokemon filtrado para guardarse en el archivo Json.
        "pokemones" como una lista de diccionarios, con cada uno de los atributos de los pokemones filtrados.
    Retorna:
        None.
    '''
    pokemones_filtrados = [
        {
            'nombre': pokemon['Nombre'],
            'mayor_valor': max(pokemon['PoderPelea'], pokemon['PoderDefensa']),
            'tipo_habilidad': 'Ataque' if pokemon['PoderPelea'] > pokemon['PoderDefensa'] else 'Defensa' if pokemon['PoderDefensa'] > pokemon['PoderPelea'] else 'Ambos'
        }
        for pokemon in Pokemones if Tipo in pokemon['Tipos']
    ]

    if not pokemones_filtrados:
        print(f"No se encontraron pokemones del tipo '{Tipo}'.")
        return

    with open(f"{Tipo.lower()}_pokemones.json", "w") as file:
        json.dump(pokemones_filtrados, file, indent=4)

def pokemon_a_fila(pokemon):
    '''
    Toma un diccionario que representa un Pokémon y convierte su información en una lista de valores. 
    La cual está diseñada para ser fácilmente escribible en una fila de un archivo CSV.
    Args:
        La lista de diccionarios de los pokemones
    Retorna:
            Una lista con: El ID, el nombre, tipos, poder de pelea, poder de defensa, tamaño y las habilidades.
    '''
    tipos = pokemon['Tipos']
    habilidades = ';'.join(pokemon['Habilidades'])
    return [
        pokemon['ID'], pokemon['Nombre'], tipos[0], tipos[1] if len(tipos) > 1 else '', 
        pokemon['PoderPelea'], pokemon['PoderDefensa'], pokemon['Tamaño'], habilidades
    ]

def Guardar_Pokemones_Csv(nombre_archivo, pokemones):
    '''
    Guarda los datos de los pokemones en un archivo CSV.
    Args:
        Recibe como parámetros: "Nombre archivo" como un str, que es donde se van a guardar los datos de los pokemones.
        Pokemones como una lista de diccionarios, donde estan los atributos de los pokemones.
    Retorna:
            None.
    '''
    if not isinstance(nombre_archivo, str):
        raise TypeError("nombre_archivo debe ser una cadena que representa el nombre del archivo CSV.")
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["ID", "Nombre", "Tipo1", "Tipo2", "PoderPelea", "PoderDefensa", "Tamaño", "Habilidades"]) # Escribir el encabezado del CSV
        for pokemon in pokemones:
            escritor_csv.writerow(pokemon_a_fila(pokemon))

def Cargar_Pokemones_Csv(archivo: str):
    Pokemones = []
    try:
        with open(archivo, mode='r') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                Pokemones.append({
                    "ID": int(fila["ID"]),
                    "Nombre": fila["Nombre"],
                    "Tipos": fila["Tipos"].split(", "), 
                    "PoderPelea": int(fila["PoderPelea"]),
                    "PoderDefensa": int(fila["PoderDefensa"]),
                    "Tamaño": fila["Tamaño"],
                    "Habilidades": fila["Habilidades"].split(", ")
                })
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
    return Pokemones