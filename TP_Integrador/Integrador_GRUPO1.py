import sqlite3
import math
import datetime
from datetime import date

today = date.today()
today = today.strftime("%Y-%m-%d")

class ProgramaPrincipal():

    def estandarizar_fecha(self, fecha): #Si el día es menor a 10 lo estandarizo, sino lo devuelvo sin modificar
        fecha = str(fecha)
        if len(fecha) == 1:
            fecha = '0' + fecha
            return fecha
        else:
            return fecha

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
            respuesta = int(input("Ingrese una opción del menú: "))
            if respuesta == 1:
                self.cargar_libros()
            if respuesta == 2:
                self.modificar_precio_libro()
            if respuesta == 3:
                self.borrar_libro()
            if respuesta == 4:
                self.cargar_disponibilidad()
            if respuesta == 5:
                print("Como desea ordenar los libros? 1- ID 2- Autor 3- Titulo")
                rta = int(input("Ingrese una opcion: "))
                if rta == 1:
                    self.mostrar_libros("ID") #muestro libros ordenados por ID
                elif rta == 2:
                    self.mostrar_libros("Autor") #muestro libros ordenados por autor
                elif rta == 3:
                    self.mostrar_libros("Titulo") #muestro libros ordenados por título
                else:
                    print("Opcion incorrecta")
            if respuesta == 6:
                self.realizar_venta()
            if respuesta == 7:
                self.actualizar_precios() #REVISAR FECHA_ACTUAL (NO ESTÁ PEDIDA AL USUARIO)
            if respuesta == 8:
                self.mostrar_registros_anteriores()
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
                    ISBN INTEGER UNIQUE,
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
                    ISBN INTEGER UNIQUE,
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


    def cargar_libros(self): #opcion 1
        try:
            isbn = int(input("Ingrese el ISBN del libro: "))
            while len(str(isbn)) != 10 or not isinstance(isbn, int):
                print("ERROR! El ISBN debe ser un numero de 10 digitos")
                isbn = int(input("Ingrese el ISBN del libro: "))

            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            
            while autor.isdigit():
                print("ERROR! Ingrese un nombre de autor valido")
                autor = input("Ingrese el autor del libro: ")

            genero = input("Ingrese el género del libro: ")
            
            while genero.isdigit():
                print("ERROR! Ingrese un genero valido")
                genero = input("Ingrese el género del libro: ")

            precio = float(input("Ingrese el precio del libro: "))

            while precio < 1: #validacion
                print("ERROR! El precio debe ser mayor o igual a 1")
                precio = float(input("Ingrese el precio del libro: "))
            precio = round(precio, 2)

            dia_ultimo_precio = int(input("Ingrese el día del último precio (DD): "))

            while not isinstance(dia_ultimo_precio, int) or dia_ultimo_precio < 1 or dia_ultimo_precio > 31:
                print("ERROR! Ingrese un dia correcto")
                dia_ultimo_precio = int(input("Ingrese el dia del último precio (DD): "))

            dia_ultimo_precio = self.estandarizar_fecha(dia_ultimo_precio)

            mes_ultimo_precio = int(input("Ingrese el mes del último precio (MM): "))

            while not isinstance(mes_ultimo_precio, int) or mes_ultimo_precio < 1 or mes_ultimo_precio > 12:
                print("ERROR! Ingrese un mes correcto")
                mes_ultimo_precio = int(input("Ingrese el mes del último precio (MM): "))

            mes_ultimo_precio = self.estandarizar_fecha(mes_ultimo_precio)

            anio_ultimo_precio = int(input("Ingrese el año del último precio (AAAA): "))

            while len(str(anio_ultimo_precio)) != 4 or not isinstance(anio_ultimo_precio, int):
                print("ERROR! Ingrese un año correcto")
                anio_ultimo_precio = int(input("Ingrese el año del último precio (AAAA): "))

                anio_ultimo_precio = str(anio_ultimo_precio)

            fecha_ultimo_precio = f"{anio_ultimo_precio}-{mes_ultimo_precio}-{dia_ultimo_precio}"

            cant_disponible = int(input("Ingrese la cantidad disponible del libro: "))

            while cant_disponible < 1 or not isinstance(cant_disponible, int): #validacion
                print("ERROR! La cantidad debe ser mayor a 0")
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

    
    def modificar_precio_libro(self): #opcion 2
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
            
    def borrar_libro(self): #opcion 3
        try:
            libro_id = int(input("Ingrese el ID del libro a borrar: "))

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

                confirmacion = input("¿Desea borrar el libro? (s/n): ")
                if confirmacion.lower() == "s":
                    conexion.mi_cursor.execute("DELETE FROM Libros WHERE ID = ?", (libro_id,))
                    conexion.mi_conexion.commit()
                    print("Libro borrado exitosamente.")
                else:
                    print("Borrado del libro cancelado.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except:
            print("Error al borrar el libro.")
        finally:
            conexion.cerrar_conexion()        

    def cargar_disponibilidad(self): #opcion 4
        try:
            libro_id = int(input("Ingrese el ID del libro: "))
            incremento_cant = int(input("Ingrese el incremento de cantidad disponible: "))
            while incremento_cant < 1: #validacion
                print("ERROR! La cantidad debe ser mayor a 0")
                incremento_cant = int(input("Ingrese el incremento de cantidad disponible: "))

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

                confirmacion = input("¿Desea incrementar la cantidad disponible? (s/n): ")
                if confirmacion.lower() == "s":
                    nueva_cant = libro[7] + incremento_cant
                    conexion.mi_cursor.execute("UPDATE Libros SET CantDisponible = ? WHERE ID = ?", (nueva_cant, libro_id))
                    conexion.mi_conexion.commit()
                    print("Cantidad disponible del libro actualizada exitosamente.")
                else:
                    print("Actualización de la cantidad disponible cancelada.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except:
            print("Error al cargar la disponibilidad del libro.")
        finally:
            conexion.cerrar_conexion()

    def mostrar_libros(self, orden: str): #opcion 5
        try:
            conexion = Conexiones()
            conexion.abrir_conexion()
            libros = conexion.mi_cursor.execute(f"SELECT * FROM Libros ORDER BY {orden}").fetchall()
            if libros:
                print(f"Listado de Libros ordenados por {orden}:")
                for libro in libros:
                    print("ID:", libro[0])
                    print("ISBN:", libro[1])
                    print("Título:", libro[2])
                    print("Autor:", libro[3])
                    print("Género:", libro[4])
                    print("Precio:", libro[5])
                    print("Fecha último precio:", libro[6])
                    print("Cantidad disponible:", libro[7])
                    print("------------------------")
            else:
                print("No hay libros para mostrar.")
        except:
            print("Error al mostrar los libros.")
        finally:
            conexion.cerrar_conexion()

    def realizar_venta(self): #opcion 6
        try:
            libro_id = int(input("Ingrese el ID del libro vendido: "))
            cantidad = int(input("Ingrese la cantidad vendida: "))
            
            fecha_venta = today #La fecha de venta es la fecha de hoy, cuando se realiza esta venta

            conexion = Conexiones()
            conexion.abrir_conexion()
            libro = conexion.mi_cursor.execute("SELECT * FROM Libros WHERE ID = ?", (libro_id,)).fetchone()

            if libro:
                if cantidad <= libro[7]:
                    print("Información del libro vendido:")
                    print("ID:", libro[0])
                    print("ISBN:", libro[1])
                    print("Título:", libro[2])
                    print("Autor:", libro[3])
                    print("Género:", libro[4])
                    print("Precio:", libro[5])
                    print("Fecha último precio:", libro[6])
                    print("Cantidad disponible:", libro[7])

                    confirmacion = input("¿Desea registrar la venta? (s/n): ")
                    if confirmacion.lower() == "s":
                        nueva_cant = libro[7] - cantidad
                        conexion.mi_cursor.execute("INSERT INTO Ventas (LibroID, Cantidad, FechaVenta) VALUES (?, ?, ?)",
                                                    (libro_id, cantidad, fecha_venta))
                        conexion.mi_cursor.execute("UPDATE Libros SET CantDisponible = ? WHERE ID = ?", (nueva_cant, libro_id))
                        conexion.mi_conexion.commit()
                        print("Venta registrada exitosamente.")
                    else:
                        print("Registro de la venta cancelado.")
                else:
                    print("No hay suficiente cantidad disponible del libro.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except:
            print("Error al realizar la venta.")
        finally:
            conexion.cerrar_conexion()

    def actualizar_precios(self): #opcion 7
        try:
            porcentaje_aumento = float(input("Ingrese el porcentaje de aumento de precios: "))

            conexion = Conexiones()
            conexion.abrir_conexion()
            libros = conexion.mi_cursor.execute("SELECT * FROM Libros").fetchall()

            if libros:
                print("Precios antes de la actualización:")
                for libro in libros:
                    print("ID:", libro[0])
                    print("ISBN:", libro[1])
                    print("Título:", libro[2])
                    print("Autor:", libro[3])
                    print("Género:", libro[4])
                    print("Precio:", libro[5])
                    print("Fecha último precio:", libro[6])
                    print("Cantidad disponible:", libro[7])
                    print("------------------------")

                confirmacion = input("¿Desea actualizar los precios? (s/n): ")
                if confirmacion.lower() == "s":
                    for libro in libros:
                        conexion.mi_cursor.execute("""
                            INSERT INTO historico_libros (ISBN, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """, (libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]))
                        nuevo_precio = libro[5] + libro[5] * porcentaje_aumento / 100
                        conexion.mi_cursor.execute("UPDATE Libros SET Precio = ?, FechaUltimoPrecio = ? WHERE ID = ?", (nuevo_precio, today, libro[0]))
                    conexion.mi_conexion.commit()
                    print("Precios actualizados exitosamente.")
                else:
                    print("Actualización de precios cancelada.")
            else:
                print("No hay libros para actualizar.")
        except:
            print("Error al actualizar los precios.")
        finally:
            conexion.cerrar_conexion()

    def mostrar_registros_anteriores(self): #opcion 8
        try:
            dia_limite = int(input("Ingrese el día de la fecha limite de busqueda (DD): "))

            while not isinstance(dia_limite, int) or dia_limite < 1 or dia_limite > 31:
                print("ERROR! Ingrese un dia correcto")
                dia_limite = int(input("Ingrese el dia de la fecha limite de busqueda (DD): "))

            dia_limite = self.estandarizar_fecha(dia_limite)

            mes_limite = int(input("Ingrese el mes de la fecha limite de busqueda (MM): "))

            while not isinstance(mes_limite, int) or mes_limite < 1 or mes_limite > 12:
                print("ERROR! Ingrese un mes correcto")
                mes_limite = int(input("Ingrese el mes de la fecha limite de busqueda (MM): "))

            mes_limite = self.estandarizar_fecha(mes_limite)

            anio_limite = int(input("Ingrese el año de la fecha limite de busqueda (AAAA): "))

            while len(str(anio_limite)) != 4 or not isinstance(anio_limite, int):
                print("ERROR! Ingrese un año correcto")
                anio_limite = int(input("Ingrese el año de la fecha limite de busqueda (AAAA): "))

            anio_limite = str(anio_limite)

            fecha_limite = f"{anio_limite}-{mes_limite}-{dia_limite}"

            conexion = Conexiones()
            conexion.abrir_conexion()
            registros = conexion.mi_cursor.execute("SELECT * FROM Libros WHERE FechaUltimoPrecio < ?", (fecha_limite,)).fetchall()
            

            if registros:
                print("Registros anteriores a la fecha límite:")
                for registro in registros:
                    print("ID:", registro[0])
                    print("ISBN:", registro[1])
                    print("Título:", registro[2])
                    print("Autor:", registro[3])
                    print("Género:", registro[4])
                    print("Precio:", registro[5])
                    print("Fecha último precio:", registro[6])
                    print("Cantidad disponible:", registro[7])
                    print("------------------------")
            else:
                print("No hay registros anteriores a la fecha límite.")
        except:
            print("Error al mostrar los registros anteriores.")
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