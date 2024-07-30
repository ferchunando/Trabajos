from pokemones import *
from package_Funciones.package_Validaciones.Validaciones import *

def Obtener_Nombre():
        while True:
            Nombre = input("Nombre del Pokémon: ")
            if validar_nombre_pokemon(Nombre):
                return Nombre

def Obtener_Habilidades():
    habilidades_pokemon = []
    while len(habilidades_pokemon) < 3:
        habilidad_pokemon = input(f"Ingrese la habilidad del Pokémon ({len(habilidades_pokemon) + 1}/3): ")
        if validar_habilidad_pokemon(habilidad_pokemon):
            habilidades_pokemon.append(habilidad_pokemon)
            if len(habilidades_pokemon) < 3:
                otra_habilidad = input("¿Quiere ingresar otra habilidad? (si/no): ")
                if otra_habilidad.lower() != 'si':
                    break
        else:
            print("Por favor, ingrese una habilidad válida.")
    return habilidades_pokemon

def Obtener_Tipos():
    Tipos_Pokemon = []
    while len(Tipos_Pokemon) < 2:
        tipo_input = input("Ingrese el tipo del Pokémon: ")
        if validar_tipo_pokemon(tipo_input):  # Pasamos el tipo ingresado para validarlo
            if tipo_input not in Tipos_Pokemon:
                Tipos_Pokemon.append(tipo_input)
                if len(Tipos_Pokemon) < 2:
                    otro_tipo = input("¿Quiere ingresar otro tipo? (si/no): ")
                    if otro_tipo.lower() != 'si':
                        break
            else:
                print("El tipo ya fue ingresado anteriormente.")
        else:
            print("Tipo no válido. Intente nuevamente.")
    return Tipos_Pokemon

def Obtener_Poder():
    while True:
            poder_ataque = int(input("Poder de ataque: "))
            if validar_poder(poder_ataque):
                return {'Ataque': poder_ataque}
            else:
                print("El poder de ataque debe ser un número entero.")

def Obtener_Defensa():
    while True:
            poder_defensa = int(input("Poder de defensa: "))
            if Validar_Defensa(poder_defensa):
                return {'Defensa': poder_defensa}
            else: 
                print("El poder de defensa debe ser un número entero.")


def Obtener_Tamaño():
    while True:
        tamaño = input("Tamaño: ")
        if validar_tamaño_pokemon(tamaño):
            return tamaño