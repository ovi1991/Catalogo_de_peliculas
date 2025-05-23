import os


class ServiciosPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'


    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')


    def listar_peliculas(self):
        try:
            with open(self.nombre_archivo, 'r', encoding= 'utf-8') as archivo:
                print('---Listado de peliculas:---')
                for linea in archivo:
                    print(linea.strip())
        except Exception as e:
            print(f'Error al listar las peliculas: {e}')
        return []
    
    def eliminar_pelicula(self):
        os.remove(self.nombre_archivo)
        print(f'Archivo {self.nombre_archivo} eliminado.')
        return []

        
