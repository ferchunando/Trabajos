from os import system
from package_Funciones.package_Validaciones.Validaciones import *
from pokemones import *
from archivos import *
from Matriz import *

def Mostrar_Menu():
    opcion = input('''Menu Pokedex.
    1) Dar de alta Pokemón.
    2) Modificar Pokemón.
    3) Eliminar Pokemón.
    4) Mostrar todos los Pokemónes.
    5) Ordenar Pokemónes.
    6) Buscar Pokemones por ID.
    7) Calcular promedio por tipo.
    8) Contar Pokemones por Tipo.
    9) Batalla Pokemon.
    10) Guardar Pokemones en Json.
    11) Salir.
    Elija una opción: ''')
    return opcion

archivos_csv = 'Pokemones.csv'

Pokemones = Cargar_Pokemones_Csv(archivos_csv)

system("cls")

flag_primero = False

while True: 
    opcion = Mostrar_Menu()
    if opcion == "1":
        Dar_Alta(Pokemones)
        flag_primero = True
    elif not flag_primero:
        print("Primero debe dar de alta a los pokemones.")
    else:
        match opcion:
            case "2":
                Modificar_Pokemon(Pokemones)
            case "3":
                Eliminar_Pokemón(Pokemones)
            case "4":
                Mostrar_pokemónes(Pokemones)
            case "5":
                Ordenar_Pokemones(Pokemones)
            case "6":
                Buscar_Pokemones(Pokemones, Id_Pokemon=Pokemones)
            case "7":
                Calcular_Promedio(Pokemones)
            case "8":
                Resultados = Contar_Pokemones_Tipo(Pokemones, Matriz_A)
                Mostrar_Matriz(Resultados)
            case "9":
                batalla_pokemon(Pokemones)
            case "10":
                Tipo = input("Ingrese el tipo de Pokémon: ")
                Guardar_Pokemones_Json(Tipo, Pokemones)
            case "11":
                Guardar_Pokemones_Csv(archivos_csv,Pokemones)
                print("El programa a finalizado!")
                break
            
    system("pause")
    system("cls")
