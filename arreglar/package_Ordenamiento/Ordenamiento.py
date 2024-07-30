def bubble_sort(pokemones, key, reverse=False):
    '''
    La funcion  ordena una lista de diccionarios (pokemones), permite ordenar en orden ascendente o descendente.
    Recibe por parámetros: pokemones (Una lista de diccionarios) donde cada diccionario representa a un Pokémon.
    key: Una cadena que representa la clave del diccionario por la cual se debe ordenar la lista.
    reverse: Un booleano que determina si la lista debe ser ordenada en orden ascendente (False) o en orden descendente (True).
    
    '''
    n = len(pokemones)
    for i in range(n):
        for j in range(0, n-i-1):
            if reverse:
                if pokemones[j][key] < pokemones[j+1][key]:
                    pokemones[j], pokemones[j+1] = pokemones[j+1], pokemones[j]
            else:
                if pokemones[j][key] > pokemones[j+1][key]:
                    pokemones[j], pokemones[j+1] = pokemones[j+1], pokemones[j]
                    