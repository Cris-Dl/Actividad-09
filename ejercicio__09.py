#Menú de catalogo de peliculas
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
        case "2":
            print("Peliculass registras")
        case "3":
            print("Buscarr pelicas por genero")
        case "4":
            print("Eliminar pelicula")
        case "5":
            print("Estadisticas del catalogo")
        case "6":
            print("Saliendo del programa, gracias por su preferencia")
        case _:
            print("Valor invalido, vuelva a intentar")