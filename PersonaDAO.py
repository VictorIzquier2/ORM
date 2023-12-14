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
  _COMPROBAR = 'SELECT EXISTS(SELECT 1 FROM jugadores)'
  _EXISTE_REGISTRO = 'SELECT EXISTS(SELECT 1 FROM jugadores WHERE id_jugador=%s)'
  _INSERTAR = 'INSERT INTO jugadores(id_jugador, posx, posy, radio, direccion, color, entidad, energia, afiliacion, entidad_energia, entidad_afiliacion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
  _ACTUALIZAR = 'UPDATE jugadores SET posx=%s, posy=%s, radio=%s, direccion=%s, color=%s, entidad=%s, energia=%s, afiliacion=%s, entidad_energia=%s, entidad_afiliacion=%s WHERE id_jugador=%s'
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
          persona = Persona(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10])
          Personas.agregar_persona(persona)
        return Personas.personas
      
  @classmethod
  def insertar(cls, p):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (p.id_jugador, p.posx, p.posy, p.radio, p.direccion, p.color, p.entidad, p.energia, p.afiliacion, p.entidad_energia, p.entidad_afiliacion)
        cursor.execute(cls._INSERTAR, valores)
        log.debug(f'Persona insertada: {p}')
        return cursor.rowcount
      
  @classmethod
  def actualizar(cls, p):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (p.posx, p.posy, p.radio, p.direccion, p.color, p.entidad, p.energia, p.afiliacion, p.entidad_energia, p.entidad_afiliacion, p.id_jugador)
        cursor.execute(cls._ACTUALIZAR, valores)
        log.debug(f'Persona actualizada: {p}')  
        return cursor.rowcount
      
  @classmethod
  def eliminar(cls, p):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (p.id_jugador,)
        cursor.execute(cls._ELIMINAR, valores)
        log.debug(f'Objeto eliminado: {p}')
        return cursor.rowcount
      
  @classmethod
  def comprobar(cls):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        cursor.execute(cls._COMPROBAR)
        comprobacion = cursor.fetchone()[0]
        return comprobacion
      
  @classmethod
  def existe_registro(cls, p):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor: 
        cursor.execute(cls._EXISTE_REGISTRO, (p.id_jugador,))
        return cursor.fetchone()[0]
# Pruebas
if __name__ == '__main__':
  # Insertar un registro
  '''persona1 = Persona(id_jugador=1, posx=512, posy=512, radio=30, direccion=90, color='blue', entidad='')
  personas_insertadas = PersonaDAO.insertar(persona1)
  log.debug(f'Personas insertadas: {personas_insertadas}')'''
  
  # Actualizar un registro
  ''' persona1 = Persona(1, 256, 256, 30, 90, 'red', '')
  personas_actualizadas = PersonaDAO.actualizar(persona1)
  log.debug(f'Personas actualizadas: {personas_actualizadas}')'''
  
  # Eliminar un registro
  '''persona1 = Persona(id_jugador=1)
  personas_eliminadas = PersonaDAO.eliminar(persona1)
  log.debug(f'Personas eliminadas: {personas_eliminadas}')'''
  
  # Seleccionar personas
  ''' personas = PersonaDAO.seleccionar()
  for persona in personas:
    log.debug(persona)'''
      
        
  