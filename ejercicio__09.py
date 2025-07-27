#Menú de catalogo de peliculas
total_pelis = []
def add_info_movie(titule, year, genero):
    info_peli = [titule, year, genero]
    total_pelis.append(info_peli)

def view_info_movies():
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

def search_movies_genre():
    number_movies = len(total_pelis)
    attemps = 0
    if number_movies != 0:
        genre = str(input("Ingrese algun genero de peliculas: ")).lower()
        print(f"Peliculas del genero {genre}")
        for i, j in enumerate(total_pelis):
            for k, l in enumerate(j):
                if k == 2:
                    if l != genre:
                        if attemps != i:
                            attemps += 1
                        else:
                            print("No hay ninguna pelicula")
                    else:
                        print(j)
    else:
        print("No hay ni una pelicula registrada")
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
                titule_peli = str(input("Ingrese el titulo de la pelicula: "))
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
            number_movies = len(total_pelis)
            attemps = 0
            if number_movies != 0:
                delete_movie = str(input("Ingrese el nombre de la pelicula que desea eliminar: "))
                print(f"Peliculas del genero {delete_movie}")
                for i, j in enumerate(total_pelis):
                    for k, l in enumerate(j):
                        if k == 0:
                            if l != delete_movie:
                                if attemps != i:
                                    attemps += 1
                                else:
                                    print("No existe esa pelicula")
                            else:
                                del total_pelis[k]
            else:
                print("No hay ni una pelicula registrada")
                print()
        case "5":
            print("Estadisticas del catalogo")
        case "6":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")