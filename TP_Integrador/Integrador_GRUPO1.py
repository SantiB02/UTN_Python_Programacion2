import sqlite3

class ProgramaPrincipal():
    def menu(self):
        repite = 1
        while repite != 0:
            print("LIBRERÍA 'Buscalibre' - Menú de opciones")
            print("1- Cargar Libros") #Coria
            print("2- Modificar precio de un libro") #Santi
            print("3- Borrar un libro")
            print("4- Cargar disponibilidad") #Ivo
            print("5- Listado de libros")
            print("6- Ventas")
            print("7- Actualizar Precios")
            print("8- Registros anteriores a una fecha")
            print("0- Salir del menú")
            respuesta = int(input("Ingrese una opción del menú:"))
            if respuesta == 1:
                self.cargar_libros()  #Coria
            if respuesta == 2:
                self.modificar_precio_libro()
            if respuesta == 3:
                self.borrar_libro()
            if respuesta == 4:
                self.cargar_disponibilidad()
            if respuesta == 5:
                self.listado_libros()
            if respuesta == 6:
                self.ventas()
            if respuesta == 7:
                self.actualizar_precios()
            if respuesta == 8:
                self.registros_anteriores()
            if respuesta == 0:
                repite = 0

    def cargar_libros(self):
        # Conectarse a la base de datos
        conexion = sqlite3.connect('libros.db')
        cursor = conexion.cursor()

        # Solicitar los datos al usuario para un libro
        id_libro = int(input("Ingrese el ID del libro: "))
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        precio = float(input("Ingrese el precio del libro: "))

        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO libros (ID, ISBN, Título, Autor, Género, Precio) VALUES (?, ?, ?, ?, ?, ?)",
                       (id_libro, isbn, titulo, autor, genero, precio))

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()

         # Volver al menú principal
        return

programa = ProgramaPrincipal()
programa.menu()