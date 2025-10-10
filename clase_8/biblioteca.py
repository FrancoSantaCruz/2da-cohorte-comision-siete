def crear_libro(titulo, autor, anio):
    libro = {
        "titulo": titulo,
        "autor": autor,
        "año": anio
    }
    return libro

def agregar_libro(biblioteca, libro):
    biblioteca.append(libro)

def buscar_libro(biblioteca, titulo):
    # biblioteca = [
    #               {"titulo":"libro1", ...}, 
    #               {"titulo":"libro2", ...}, 
    #               {"titulo":"libro3", ...}
    # ]
    for libro in biblioteca:
        if libro["titulo"] == titulo:
            return libro
    return None

def mostrar_todos_libros(biblioteca):
    for libro in biblioteca:
        print(f"~ {libro["titulo"]} escrito por {libro["autor"]} en el año {libro["año"]}.")