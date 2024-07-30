from package_Funciones.package_Validaciones.Validaciones import *
from package_Funciones.Funciones import Obtener_Nombre, Obtener_Habilidades, Obtener_Tipos, Obtener_Poder, Obtener_Defensa, Obtener_Tamaño
from package_Ordenamiento.Ordenamiento import bubble_sort

def Obtener_Datos_Pokemones():
    Nombre = Obtener_Nombre()
    Habilidades_Pokemon = Obtener_Habilidades()
    Tipos_Pokemon = Obtener_Tipos()
    Poder = Obtener_Poder()
    Defensa = Obtener_Defensa()
    Tamaño = Obtener_Tamaño()

    Datos_Pokemon = {
        'Nombre': Nombre,
        'Tipos': Tipos_Pokemon,
        'Poder': Poder,
        'Defensa': Defensa,
        'Tamaño': Tamaño,
        'Habilidades': Habilidades_Pokemon
        }
    return Datos_Pokemon


def Dar_Alta(pokemones: list):
    Nuevo_ID = len(pokemones) + 1
    Datos_Pokemon = Obtener_Datos_Pokemones()
    nuevo_pokemon = {
        "ID": Nuevo_ID,
        "Nombre": Datos_Pokemon['Nombre'],
        "Tipos": Datos_Pokemon['Tipos'],
        "PoderPelea": Datos_Pokemon['Poder']['Ataque'],
        "PoderDefensa": Datos_Pokemon['Defensa']['Defensa'],
        "Tamaño": Datos_Pokemon['Tamaño'],
        "Habilidades": Datos_Pokemon['Habilidades']}
    
    pokemones.append(nuevo_pokemon)
    print(f"Pokemón {Datos_Pokemon['Nombre']} ha sido dado de alta con el ID {Nuevo_ID}.")


def Mostrar_pokemónes(pokemones: list):
    if pokemones:
        titulos = "ID | Nombre      | Tipo      |Poder de Ataque      | Poder de Defensa      | Tamaño      | Habilidades "
        separador = "-" * len(titulos)
        print(titulos)
        print(separador)
        for pokemon in pokemones:
            Tipos = ', '.join(pokemon['Tipos'])
            Habilidades = ', '.join(pokemon['Habilidades'])
            print(f"{pokemon['ID']:2} | {pokemon['Nombre']:<14} | {Tipos:<13} | {pokemon['PoderPelea']:13} | {pokemon['PoderDefensa']:13} | {pokemon['Tamaño']} | {Habilidades}")
    else:
        print("No hay pokemónes registrados.")

def Modificar_Pokemon(Lista_Pokemones: list):
    id_modificar = Solicitar_Entero("Ingrese el ID del Pokemón que desea modificar: ")
    for Pokemon in Lista_Pokemones:
        if Pokemon["ID"] == id_modificar:
            print(f"EL pokemon solicitado fue encontrado, sus datos son: {Pokemon}.")
            while True:
                opcion = input('''Menú
                    1) Nombre del Pokemón.
                    2) Tipo del Pokemón.
                    3) Poder de Ataque.
                    4) Poder de Defensa.
                    5) Tamaño del Pokemón.
                    6) Habilidades del Pokemón.
                    7) Salir.
                    Elija la opcion que desea cambiar: ''')
                match opcion:
                    case "1":
                        Nombre = input("Ingrese el nuevo nombre del Pokemón: ")
                        Pokemon['Nombre'] = Nombre
                    case "2":
                        Tipo = input("Ingrese el nuevo tipo del Pokemón: ")
                        Pokemon['Tipos'] = Tipo.split(",")
                    case "3":
                        poder_ataque = int(input("Ingrese el nuevo Poder de pelea: "))
                        Pokemon['Poder Ataque'] = poder_ataque
                    case "4":
                        poder_defensa = int(input("Ingrese la nueva defensa: "))
                        Pokemon['Poder Defensa'] = poder_defensa
                    case "5":
                        Tamaño = input("Ingrese el nuevo Tamaño del Pokemón: ")
                        Pokemon['Tamaño'] = Tamaño
                    case "6":
                        Habilidades = input("Ingrese las nuevas habilidades: ")
                        Pokemon['Habilidades'] = Habilidades.split(",")
                    case "7":
                        break
            print(f"El Pokemón con ID {id_modificar} ha sido modificado correctamente.")
            return Mostrar_pokemónes(Lista_Pokemones)
        
def Eliminar_Pokemón(pokemones: list):
    id_pokemon = Solicitar_Entero("Ingrese el ID del pokemón que desea eliminar: ")
    for pokemon in pokemones:
        if pokemon['ID'] == id_pokemon:
            pokemones.remove(pokemon)
            print(f"El Pokemón con el ID {id_pokemon} ha sido eliminado con éxito.")
            break
    else:
        print(f"No se encontró al pokemón con ID {id_pokemon}.")


def Ordenar_Pokemones(Pokemones: list):
    print('''Menú de ordenamiento
                1) Por el nombre de forma ascendente.
                2) Por el nombre de forma descendente.
                3) Por el Tipo de forma ascendente.
                4) Por el Tipo de forma descendente.
                5) Por el ataque de forma ascendente.
                6) Por el ataque de forma descendente.
                7) Por la defensa de forma ascendente.
                8) Por la defensa de forma descendente.
                Seleccione la opcion para ordenar: ''')
    
    opcion = Solicitar_Entero(" ")
    match opcion:
        case "1":
            bubble_sort(Pokemones, "Nombre")
        case "2":
            bubble_sort(Pokemones, "Nombre", reverse=True)
        case "3":
            bubble_sort(Pokemones, "Tipos")
        case "4":
            bubble_sort(Pokemones, "Tipos", reverse=True)
        case "5":
            bubble_sort(Pokemones, "PoderPelea")
        case "6":
            bubble_sort(Pokemones, "PoderPelea", reverse=True)
        case "7":
            bubble_sort(Pokemones, "PoderDefensa")
        case "8":
            bubble_sort(Pokemones, "PoderDefensa", reverse=True)
        case "9":
            print("opcion invalida.")
            return 
    print("pokemones ordenador: ")
    Mostrar_pokemónes(Pokemones)

def Buscar_Pokemones(pokemones, Id_Pokemon):
    Id_Pokemon = Solicitar_Entero("Ingrese el ID del Pokémon que desea buscar: ")
    for Pokemon in pokemones:
        if Pokemon['ID'] == Id_Pokemon:
            return Pokemon
        else:
            print(f"El Pokemon con el ID {Id_Pokemon} no ha sido posible encontrarlo.")

def Calcular_Promedio(pokemones):
    if not pokemones:
        print("No hay Pokemones en la lista.")
        return pokemones
    
    Promedio_Pelea_Elec = sum(p['PeleaElec'] for p in pokemones) / len(pokemones)
    Promedio_Pelea_Psi = sum(p['PeleaPsi'] for p in pokemones) / len(pokemones)
    Promedio_Defensa_Tierra = sum(p['DefensaTierra'] for p in pokemones) / len(pokemones)

def batalla_pokemon(pokemones):
    '''
    Simula una batalla pokemon basada en cierto criterios.
    Args:
        Recibe como parámetros pokemones como una lista de diccionarios con sus respectivos criterios.
    Retorna:
            None.
    '''
    pokemones_validos = [
        pokemon for pokemon in pokemones if (
            (pokemon['Tipos'][0] == 'Fuego' and pokemon['Tamaño'] == 'XL' and 'Lanzallamas' in pokemon['Habilidades'] and pokemon['PoderPelea'] > 80) or
            (pokemon['Tipos'][0] == 'Agua' and pokemon['Tamaño'] == 'L' and 'Hidrobomba' in pokemon['Habilidades'] and pokemon['PoderPelea'] > 80)
        )
    ]
    if len(pokemones_validos) >= 3:
        print("¡Ganamos la batalla contra Giovanni!")
    else:
        print("Perdimos la batalla contra Giovanni.")

def Solicitar_Entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
