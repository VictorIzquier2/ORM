import psycopg2 as bd
import sys
from logger_base import log

class Conexion:
  _DATABASE = 'orm'
  _USERNAME = 'postgres'
  _PASSWORD = 'admin'
  _DB_PORT = '5434'
  _HOST = '127.0.0.1'
  _conexion = None
  _cursor = None
  
  @classmethod
  def obtenerConexion(cls):
    # Si no existe una conexión previa a la BB.DD
    if cls._conexion is None:
      try:
        cls._conexion = bd.connect(user=cls._USERNAME, password=cls._PASSWORD, host=cls._HOST, port=cls._DB_PORT, database=cls._DATABASE)
        log.debug(f'Conexión a la BB.DD. realizada con éxito: {cls._conexion}')
        # Devolver la conexión
        return cls._conexion
      except Exception as e:
        log.error(f'Ocurrió un error durante la conexión: {e}, {type(e)}')
        # Cerrar el sistema
        sys.exit()
    else:
      # Si existe una conexión previa, devolverla
      return cls._conexion
    
  @classmethod
  def obtenerCursor(cls):
    # Si no hay abierto ningún cursor que apunte a las tablas
    if cls._cursor is None:
      try:
        cls._cursor = cls.obtenerConexion().cursor()
      except Exception as e:
        log.error(f'Ocurrió un error al obtener el cursor: {e}, {type(e)}')
        # Cerrar el sistema
        sys.exit()
    else:
      return cls._cursor
    
# Si este es el archivo que mandamos llamar, ejecutar pruebas:
if __name__ == '__main__':
  Conexion.obtenerConexion()
  Conexion.obtenerCursor()
      