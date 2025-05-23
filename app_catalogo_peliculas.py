from peliculas import Pelicula
from servicio_peliculas import ServiciosPeliculas


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicios_peliculas = ServiciosPeliculas()


    def mostrar_menu(self):
        print('---Menu de Catalogo de Peliculas---')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar pelicula
                2. Listar peliculas
                3. Eliminar peliculas
                4. Salir''')
                opcion = int(input('Seleccione una opcion (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Ingrese el nombre de la pelicula:')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicios_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicios_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicios_peliculas.eliminar_pelicula()
                elif opcion == 4:
                    print('Saliendo del programa...')
                    break
                else:
                    print('Error: Opcion no valida. Introduce un valor  entre 1 y 4.')
                

            except ValueError:
                print('Error: Opcion no valida. Intente nuevamente.')
            except Exception as e:
                print(f'Error inesperado: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()
