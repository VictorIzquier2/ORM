import random
from Entidad import Entidad


class Recogible(Entidad):
  contador_recogibles = 0
  lienzo = None
  
  @classmethod
  def recogible_random(cls, id_jugador):
    cls.contador_recogibles += 1
    id_recogible = cls.contador_recogibles
    id_jugador = id_jugador
    posx = random.randint(30,994)
    posy = random.randint(30, 994)
    color = "gold"
    return Recogible(id_recogible, id_jugador, posx, posy, color)
  
  def __init__(self, id_recogible=None, id_jugador=None, posx=None, posy=None, color=None):
    super().__init__(posx, posy, color)
    self.id_recogible = id_recogible
    self.id_jugador = id_jugador
    
  def __str__(self):
    return f'Recogible id: {self.id_recogible} [Id jugador: {self.id_jugador}, Posición X: {self.posx}, Posición Y: {self.posy}, Color: {self.color} ]'
    