from Conexion import Conexion
from Recogible import Recogible
from logger_base import log
import json

class RecogibleDAO:
   
  _SELECCIONAR = 'SELECT * FROM recogibles ORDER BY id_jugador'
  _COMPROBAR = 'SELECT EXISTS(SELECT 1 FROM recogibles)'
  _EXISTE_REGISTRO = 'SELECT EXISTS(SELECT 1 FROM recogibles WHERE id_recogible=%s)'
  _INSERTAR = 'INSERT INTO recogibles(id_recogible, id_jugador, posx, posy, color) VALUES(%s, %s, %s, %s, %s)'
  _ACTUALIZAR = 'UPDATE recogibles SET id_jugador=%s, posx=%s, posy=%s, color=%s WHERE id_recogible=%s'
  _ELIMINAR  = 'DELETE FROM recogibles WHERE id_recogible=%s'
  _ELIMINAR_DE_JUGADOR = 'DELETE FROM recogibles WHERE id_jugador=%s'
  
  @classmethod
  def seleccionar(cls):
    # Al usar with tanto la conexión como el cursor se cierran automáticamente
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        # El cursor ejecuta la sentencia _SELECCIONAR
        cursor.execute(cls._SELECCIONAR)
        # Se consiguen todos los registros de la BB.DD. con un fetchall()
        registros_recogibles = cursor.fetchall()
        recogibles = []
        for registro in registros_recogibles:
          # A través de las posiciones dentro del registro se accede a los campos de Persona
          recogible = Recogible(registro[0], registro[1], registro[2], registro[3], registro[4])
          recogibles.append(recogible)
        return recogibles
      
  @classmethod
  def insertar(cls, r):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (r.id_recogible, r.id_jugador, r.posx, r.posy, r.color)
        cursor.execute(cls._INSERTAR, valores)
        log.debug(f'Recogible insertado: {r}')
        return cursor.rowcount
      
  @classmethod
  def actualizar(cls, r):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (r.id_jugador, r.posx, r.posy, r.color, r.id_recogible)
        cursor.execute(cls._ACTUALIZAR, valores)
        log.debug(f'Recogible actualizado: {r}')  
        return cursor.rowcount
      
  @classmethod
  def eliminar(cls, r):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        valores = (r.id_recogible,)
        cursor.execute(cls._ELIMINAR, valores)
        log.debug(f'Recogible eliminado: {r}')
        return cursor.rowcount
  
  @classmethod
  def eliminar(cls, p):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        inventario_json = json.dumps(p.inventario)
        valores = (p.id_jugador,)
        cursor.execute(cls._ELIMINAR_DE_JUGADOR, valores)
        log.debug(f'Recogibles eliminados: {inventario_json}')
      
  @classmethod
  def comprobar(cls):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor:
        cursor.execute(cls._COMPROBAR)
        comprobacion = cursor.fetchone()[0]
        return comprobacion
      
  @classmethod
  def existe_registro(cls, r):
    with Conexion.obtenerConexion() as conexion:
      with conexion.cursor() as cursor: 
        cursor.execute(cls._EXISTE_REGISTRO, (r.id_recogible,))
        return cursor.fetchone()[0]
# Pruebas
if __name__ == '__main__':
  # Insertar un registro
  '''recogible1 = Recogible(id_recogible=1, id_jugador=1, posx=512, posy=512, color='blue')
  recogible_insertado = RecogibleDAO.insertar(recogible1)
  log.debug(f'Recogible insertado: {recogible_insertado}')'''
  
  # Actualizar un registro
  ''' recogible1 = Recogible(1, 1, 256, 256, 'red')
  recogible_actualizado = RecogibleDAO.actualizar(recogible1)
  log.debug(f'Recogible actualizado: {recogible_actualizado}')'''
  
  # Eliminar un registro
  '''recogible1 = Recogible(id_recogible=1)
  recogible_eliminado = RecogibleDAO.eliminar(recogible1)
  log.debug(f'Recogible eliminado: {recogible_eliminado}')'''
  
  # Seleccionar personas
  ''' recogibles = RecogibleDAO.seleccionar()
  for recogible in recogibles:
    log.debug(recogible)'''
      