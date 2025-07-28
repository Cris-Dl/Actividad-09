#Menú de catalogo de peliculas
total_pelis = []
def add_info_movie(titule, year, genero):
    info_peli = [titule, year, genero]
    total_pelis.append(info_peli)

def view_info_movies():
    number_movies = len(total_pelis)
    if number_movies != 0:
        for i, j in enumerate(total_pelis):
            print(f"Entrada {i + 1}")
            for k, l in enumerate(j):
                if k == 0:
                    print(f"Nombre: {l}")
                elif k == 1:
                    print(f"Año de estreno: {l}")
                elif k == 2:
                    print(f"Genero: {l}")
                    print()
                else:
                    print("Datos desconocido")
                    print()
    else:
        print("No hay ninguna pelicula registrada")

def search_movies_genre():
    number_movies = len(total_pelis)
    attemps = 0
    if number_movies != 0:
        genre = str(input("Ingrese algun genero de peliculas: ")).lower()
        print(f"Peliculas del genero {genre}")
        for i, j in enumerate(total_pelis):
            for k, l in enumerate(j):
                if k == 2:
                    if genre == l:
                        print(j)
                    elif genre!= l:
                        if attemps != i:
                            attemps += 1
                        else:
                            print("No hay ninguna pelicula")
    else:
        print("No hay ni una pelicula registrada")
        print()

def delete_movie():
    number_movies = len(total_pelis)
    attemps = 0
    if number_movies != 0:
        delete_movie = str(input("Ingrese el nombre de la pelicula que desea eliminar: ")).lower()
        for i, j in enumerate(total_pelis):
            for k, l in enumerate(j):
                if k == 0:
                    if delete_movie == l:
                        total_pelis.remove(j)
                    elif l != delete_movie:
                        if attemps != i:
                            attemps += 1
    else:
        print("No hay ni una pelicula registrada")
        print()

def count_movie_and_genre():
    number_pelis = len(total_pelis)
    if number_pelis != 0:
        print(f"Hay un total de {number_pelis} peliculas registradas")
        conteo = {}
        for i, j in enumerate(total_pelis):
            for k, l in enumerate(j):
                if k == 2:
                    if l in conteo:
                        conteo[l] += 1
                    else:
                        conteo[l] = 1
        print(f"Cantidad de peliculas por genero: {conteo}")
    else:
        print("No hay ninguna pelicula registrada")

def old_movie():
    number_pelis = len(total_pelis)
    if number_pelis !=0:
        min_actual = float('inf')
        for i, j in enumerate(total_pelis):
            for k, l in enumerate(j):
                if k == 1:
                    if l < min_actual:
                        min_actual = l
                        peli = j
        print(f"La pelica más antigua es: {peli}")
    else:
        print()

while True:
    print(" --Menú-- ")
    print("1.- Agregar peliculas")
    print("2.- Mostrar todas la peliculas registradas")
    print("3.- Buscar peliculas por genero")
    print("4.- Eliminar una pelicula por titulo")
    print("5.- Ver estadisticas del catalogo")
    print("6.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Agregar peliculas")
            number_pelis = int(input("Cuantas peliculas deseass ingresar: "))
            for i in range(number_pelis):
                titule_peli = str(input("Ingrese el titulo de la pelicula: ")).lower()
                year_peli = int(input("Ingrese el año de estreno: "))
                genero_peli = str(input("Ingrese el genero de la pelicula: ")).lower()
                print()
                add_info_movie(titule_peli, year_peli, genero_peli)
            print()
        case "2":
            print("Peliculas registradas")
            view_info_movies()
            print()
        case "3":
            print("Buscar peliculas por genero")
            search_movies_genre()
            print()
        case "4":
            print("Eliminar pelicula")
            delete_movie()
            print()
        case "5":
            print("Estadisticas del catalogo")
            count_movie_and_genre()
            old_movie()
        case "6":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")