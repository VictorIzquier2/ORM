import random
import math
from colores_basicos import COLORES_BASICOS
from Personas import Personas

class Persona:
  def __init__(self, lienzo):
    self.lienzo = lienzo
    self.posx = random.randint(30, 994)
    self.posy = random.randint(30, 994)
    self.radio = 30
    self.direccion = random.randint(0,360)
    self.color = "blue"
    self.entidad = ""
    
  @classmethod
  def paraDB(cls, cadena):
    id_jugador, posx, posy, radio, direccion, color, entidad = cadena.split(',')
    return cls(int(id_jugador), int(posx), int(posy), int(radio), int(direccion), color, entidad)
    
  def dibuja(self):
    self.entidad = self.lienzo.create_oval(
      self.posx-self.radio/2,
      self.posy-self.radio/2,
      self.posx+self.radio/2,
      self.posy+self.radio/2, 
      fill=self.color
      )
  def mueve(self):
    self.colisiona()
    self.lienzo.move(
      self.entidad,
      math.cos(self.direccion),
      math.sin(self.direccion)
      )
    self.posx += math.cos(self.direccion)
    self.posy += math.sin(self.direccion)
    
  def aDiccionario(self):
    return {
      "posx": self.posx,
      "posy": self.posy,
      "radio": self.radio,
      "direccion": self.direccion,
      "color": self.color
    }
    
  def cambiaColor(self, nuevo_color):
    self.color = nuevo_color
    self.lienzo.itemconfig(self.entidad, fill=nuevo_color)
    
  def colisiona(self):
    if self.posx - self.radio/2 < 0 or self.posx + self.radio/2 > 1024 or self.posy - self.radio/2 < 0 or self.posy + self.radio/2 > 1024:
        self.direccion += 180

    for otraPersona in Personas.personas:
        if otraPersona != self:
            distancia = math.sqrt((otraPersona.posx - self.posx)**2 + (otraPersona.posy - self.posy)**2)
            if distancia < self.radio:
                # Calcular el ángulo de colisión y ajustar la dirección
                # (Opcional: puedes mejorar este cálculo para un efecto más realista)
                self.direccion += 180
                otraPersona.direccion += 180

                # Separar los objetos
                entrelazamiento = self.radio - distancia
                self.posx -= math.cos(self.direccion) * entrelazamiento
                self.posy -= math.sin(self.direccion) * entrelazamiento
                otraPersona.posx += math.cos(otraPersona.direccion) * entrelazamiento
                otraPersona.posy += math.sin(otraPersona.direccion) * entrelazamiento
                
                # Cambiar el color de las personas
                nuevoColor = random.choice(COLORES_BASICOS)
                self.cambiaColor(nuevoColor)
                otraPersona.cambiaColor(nuevoColor)