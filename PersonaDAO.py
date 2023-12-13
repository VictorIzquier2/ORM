from Conexion import Conexion
from Persona import Persona
from Personas import Personas
from logger_base import log

class PersonaDAO:
  '''
  DAO( Data Access Object)
  Patrón que consiste en separar por completo la lógica del programa de la lógica para acceder a los datos
  '''
  
  _SELECCIONAR = 'SELECT * FROM jugadores ORDER BY id_jugador'
  _INSERTAR = 'INSERT INTO jugadores(posx, posy, radio, direccion, color, entidad) VALUES(%s, %s, %s, %s, %s, %s)'
  _ACTUALIZAR = 'UPDATE jugadores SET posx=%s, posy=%s, radio=%s, direccion=%s, color=%s, entidad=%s WHERE id_jugador=%s'
  _ELIMINAR  = 'DELETE FROM jugadores WHERE id_jugador=%s'
  
  @classmethod
  def seleccionar(cls):
    # Al usar with tanto la conexión como el cursor se cierran automáticamente
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        # El cursor ejecuta la sentencia _SELECCIONAR
        cursor.execute(cls._SELECCIONAR)
        # Se consiguen todos los registros de la BB.DD. con un fetchall()
        registros_jugadores = cursor.fetchall()
        for registro in registros_jugadores:
          # A través de las posiciones dentro del registro se accede a los campos de Persona
          persona = Persona.paraDB(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
          Personas.agregar_persona(persona)
        return Personas.personas
      
  @classmethod
  def insertar(cls, persona):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (persona.posx, persona.posy, persona.radio, persona.direccion, persona.color, persona.entidad)
        cursor.execute(cls._INSERTAR, valores)
        log.debug(f'Persona insertada: {persona}')
        return cursor.rowcount
      
  @classmethod
  def actualizar(cls, persona):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (persona.posx, persona.posy, persona.radio, persona.direccion, persona.color, persona.entidad, persona.id_jugador)
        cursor.execute(cls._ACTUALIZAR, valores)
        log.debug(f'Persona actualizada: {persona}')  
        return cursor.rowcount
      
  @classmethod
  def eliminar(cls, persona):
    with Conexion.obtenerConexion():
      with Conexion.obtenerCursor() as cursor:
        valores = (persona.id_persona,)
        cursor.execute(cls._ELIMINAR, valores)
        log.debug(f'Objeto eliminado: {persona}')
        return cursor.rowcount
      
# Pruebas
if __name__ == '__main__':
  # Insertar un registro
  ''' persona1 = Persona.paraDB(posx=512, posy=512, radio=30, direccion=90, color='blue', entidad='')
  personas_insertadas = PersonaDAO.insertar(persona1)
  log.debug(f'Personas insertadas: {personas_insertadas}')'''
  
  # Seleccionar personas
  personas = PersonaDAO.seleccionar()
  for persona in personas:
    log.debug(persona)
      
        
  