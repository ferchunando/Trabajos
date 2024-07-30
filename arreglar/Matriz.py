def Contar_Pokemones_Tipo(lista_pokemones, matriz_tipo):
    Resultados = [["Tipo", "Cantidad", "Es Bueno Contra", "Es Malo Contra"]]
    
    contador_tipos = {tipo[0]: 0 for tipo in matriz_tipo[1:]}
    
    for pokemon in lista_pokemones:
        tipos = pokemon['Tipos']
        for tipo in tipos:
            if tipo in contador_tipos:
                contador_tipos[tipo] += 1
    
    for fila in matriz_tipo[1:]:
        tipo = fila[0]
        buenos = fila[1]
        malos = fila[2]
        cantidad = contador_tipos[tipo]
        Resultados.append([tipo, cantidad, buenos, malos])
    
    return Resultados

def Mostrar_Matriz(Matriz):
    for Fila in Matriz:
        print(f"{Fila[0]:<10} | {Fila[1]:<20} | {Fila[2]:<30} | {Fila[3]:<60}")

Matriz_A = [
    ["Tipo", "Es Bueno Contra", "Es Malo Contra"],
    ["Acero", "Hada, Hielo, Roca", "Acero, Agua, Eléctrico, Fuego"],
    ["Agua", "Fuego, Roca, Tierra", "Agua, Dragón, Planta"],
    ["Bicho", "Planta, Psíquico, Siniestro", "Fuego, Volador, Roca"],
    ["Dragón", "Dragón", "Acero, Hada"],
    ["Electrico", "Agua, Volador", "Dragón, Eléctrico, Planta, Tierra"],
    ["Fantasma", "Fantasma, Psíquico", "Siniestro, Normal"],
    ["Fuego", "Bicho, Hielo, Planta, Acero", "Dragón, Fuego, Roca, Agua"],
    ["Hada", "Dragón, Lucha, Siniestro", "Acero, Fuego, Veneno"],
    ["Hielo", "Dragón, Planta, Tierra, Volador", "Acero, Fuego, Hielo, Agua"],
    ["Lucha", "Acero, Hielo, Normal, Roca, Siniestro", "Hada, Psíquico, Volador"],
    ["Normal", "Ninguno", "Acero, Roca, Fantasma"],
    ["Planta", "Agua, Roca, Tierra", "Bicho, Dragón, Fuego, Volador, Planta, Veneno"],
    ["Psiquico", "Lucha, Veneno", "Acero, Psíquico, Siniestro"],
    ["Roca", "Bicho, Fuego, Hielo, Volador", "Acero, Lucha, Planta, Tierra, Agua"],
    ["Siniestro", "Fantasma, Psíquico", "Hada, Lucha, Siniestro"],
    ["Tierra", "Acero, Eléctrico, Fuego, Roca, Veneno", "Bicho, Planta, Volador"],
    ["Veneno", "Hada, Planta", "Fantasma, Roca, Tierra, Veneno, Acero"],
    ["Volador", "Bicho, Lucha, Planta", "Acero, Eléctrico, Roca"]
]