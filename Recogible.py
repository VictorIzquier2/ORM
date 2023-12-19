import random
from Entidad import Entidad
from logger_base import log
from Recogibles import Recogibles

class Recogible(Entidad):
  lienzo = None
  
  @classmethod
  def recogible_random(cls):
    Recogibles.contador_recogibles += 1
    id_recogible = Recogibles.contador_recogibles
    id_jugador = None
    posx = random.randint(30, 994)
    posy = random.randint(30, 994)
    radio = 30
    color = "black"
    entidad = ""
    return Recogible(id_recogible, id_jugador, posx, posy, radio, color, entidad)
  
  def __init__(self, id_recogible=None, id_jugador=None, posx=None, posy=None, radio=None, color=None, entidad=None):
    super().__init__(posx, posy, radio, color, entidad)
    self.id_recogible = id_recogible
    self.id_jugador = id_jugador
    
  def dibuja(self):
    self.entidad = self.lienzo.create_oval(
      self.posx-self.radio/2,
      self.posy-self.radio/2, 
      self.posx+self.radio/2, 
      self.posy+self.radio/2, 
      fill=self.color
    )
    
  def __str__(self):
    return f'Recogible id: {self.id_recogible} [Id jugador: {self.id_jugador}, Posición X: {self.posx}, Posición Y: {self.posy}, Radio: {self.radio}, Color: {self.color}, Entidad: {self.entidad} ]'
  
  def eliminar(self):
    if self.entidad:
      Recogible.lienzo.delete(self.entidad)
      
  def aDiccionario(self):
    return {
      "id_recogible": self.id_recogible,
      "id_jugador": self.id_jugador,
      "posx": self.posx,
      "posy": self.posy,
      "radio": self.radio,
      "color": self.color,
      "entidad": self.entidad
    }
      
if __name__ == '__main__':
  recogible1 = Recogible(1, 1, 497, 497, 30, "black", "")
  recogible2 = Recogible.recogible_random()
  log.debug(recogible1)
  log.debug(recogible2)
      

    