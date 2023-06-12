import sqlite3


class ProgramaPrincipal():
    def menu(self):
        repite = 1
        while repite != 0:
            print("LIBRERÍA 'Buscalibre' - Menú de opciones")
            print("1- Cargar Libros")
            print("2- Modificar precio de un libro")
            print("3- Borrar un libro")
            print("4- Cargar disponibilidad")
            print("5- Listado de libros")
            print("6- Ventas")
            print("7- Actualizar Precios")
            print("8- Registros anteriores a una fecha")
            print("0- Salir del menú")
            respuesta = int(input("Ingrese una opción del menú:"))
            if respuesta == 1:
                self.cargar_libros()
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

    def crear_tablas(self): #método de ProgramaPrincipal para crear tablas a usar
        conexion = Conexiones()
        conexion.abrir_conexion()
        try:
            conexion.mi_cursor.execute("DROP TABLE IF EXISTS Libros")
            conexion.mi_cursor.execute("""
                CREATE TABLE Libros (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ISBN TEXT UNIQUE,
                    Titulo TEXT,
                    Autor TEXT,
                    Genero TEXT,
                    Precio REAL,
                    FechaUltimoPrecio TEXT,
                    CantDisponible INTEGER
                )
            """)
            conexion.mi_cursor.execute("DROP TABLE IF EXISTS Ventas")
            conexion.mi_cursor.execute("""
                CREATE TABLE Ventas (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    LibroID INTEGER,
                    Cantidad INTEGER,
                    FechaVenta TEXT,
                    FOREIGN KEY (LibroID) REFERENCES Libros(ID)
                )
            """)
            conexion.mi_cursor.execute("DROP TABLE IF EXISTS historico_libros")
            conexion.mi_cursor.execute("""
                CREATE TABLE historico_libros (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ISBN TEXT UNIQUE,
                    Titulo TEXT,
                    Autor TEXT,
                    Genero TEXT,
                    Precio REAL,
                    FechaUltimoPrecio TEXT,
                    CantDisponible INTEGER
                )
            """)
            conexion.mi_conexion.commit()
            print("Tablas creadas exitosamente.")
        except:
            print("Error al crear las tablas.")
        finally:
            conexion.cerrar_conexion()


    def cargar_libros(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el género del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            fecha_ultimo_precio = input("Ingrese la fecha del último precio (DD-MM-YYYY): ")
            cant_disponible = int(input("Ingrese la cantidad disponible del libro: "))

            conexion = Conexiones()
            conexion.abrir_conexion()
            conexion.mi_cursor.execute("""
                INSERT INTO Libros (ISBN, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (isbn, titulo, autor, genero, precio, fecha_ultimo_precio, cant_disponible))
            conexion.mi_conexion.commit()
            print("Libro cargado exitosamente.")
        except:
            print("Error al cargar el libro.")
        finally:
            conexion.cerrar_conexion()

    
    def modificar_precio_libro(self):
        try:
            libro_id = int(input("Ingrese el ID del libro a modificar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))

            conexion = Conexiones()
            conexion.abrir_conexion()
            libro = conexion.mi_cursor.execute("SELECT * FROM Libros WHERE ID = ?", (libro_id,)).fetchone()

            if libro:
                print("Información del libro:")
                print("ID:", libro[0])
                print("ISBN:", libro[1])
                print("Título:", libro[2])
                print("Autor:", libro[3])
                print("Género:", libro[4])
                print("Precio:", libro[5])
                print("Fecha último precio:", libro[6])
                print("Cantidad disponible:", libro[7])

                confirmacion = input("¿Desea modificar el precio? (s/n): ")
                if confirmacion.lower() == "s":
                    conexion.mi_cursor.execute("UPDATE Libros SET Precio = ? WHERE ID = ?", (nuevo_precio, libro_id))
                    conexion.mi_conexion.commit()
                    print("Precio del libro modificado exitosamente.")
                else:
                    print("Modificación del precio cancelada.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except:
            print("Error al modificar el precio del libro.")
        finally:
            conexion.cerrar_conexion()


class Conexiones():
    def __init__(self):
        self.mi_conexion = None
        self.mi_cursor = None

    def abrir_conexion(self):
        try:
            self.mi_conexion = sqlite3.connect("libreria.db")
            self.mi_cursor = self.mi_conexion.cursor()
        except:
            print("Error al abrir la conexión con la base de datos.")

    def cerrar_conexion(self):
        try:
            self.mi_cursor.close()
            self.mi_conexion.close()
        except:
            print("Error al cerrar la conexión con la base de datos.")
    
    





programa = ProgramaPrincipal()
programa.crear_tablas()
programa.menu()
