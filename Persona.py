import random
import math
from colores_basicos import COLORES_BASICOS
from Personas import Personas
from Recogibles import Recogibles
from Entidad import Entidad
from logger_base import log

class Persona(Entidad):
  lienzo = None
  
  @classmethod
  def jugador_random(cls):
    id_jugador = Personas.contador_personas + 1
    posx = random.randint(30, 994)
    posy = random.randint(30, 994)
    radio = 30
    direccion = random.randint(0,360)
    color = random.choice(COLORES_BASICOS)
    entidad = ""
    energia = 100
    afiliacion = 0
    entidad_energia = ""
    entidad_afiliacion = ""
    inventario = []
    return Persona(id_jugador, posx, posy,radio, direccion, color, entidad, energia, afiliacion, entidad_energia, entidad_afiliacion, inventario)
  
  def __init__(self, id_jugador=None, posx=None, posy=None, radio=None, direccion=None, color=None, entidad=None, energia=None, afiliacion=None, entidad_energia=None, entidad_afiliacion=None, inventario=None):
    super().__init__(posx, posy, radio, color, entidad)
    self.id_jugador = id_jugador
    self.direccion = direccion
    self.energia = energia
    self.afiliacion = afiliacion
    self.entidad_energia = entidad_energia
    self.entidad_afiliacion = entidad_afiliacion
    self.inventario = inventario
    
  def dibuja(self):
    self.entidad = self.lienzo.create_oval(
      self.posx-self.radio/2,
      self.posy-self.radio/2,
      self.posx+self.radio/2,
      self.posy+self.radio/2, 
      fill=self.color
      )
    self.entidad_energia = self.lienzo.create_rectangle(
      self.posx-self.radio/2,
      self.posy-self.radio/2-10,
      self.posx+self.radio/2,
      self.posy-self.radio/2-8,
      fill="green"
      )
    self.entidad_afiliacion = self.lienzo.create_rectangle(
      self.posx-self.radio/2,
      self.posy-self.radio/2-16,
      self.posx+self.radio/2,
      self.posy-self.radio/2-14,
      fill="blue"
    )
  def mueve(self):
    self.colisiona()
    Persona.lienzo.move(
      self.entidad,
      math.cos(self.direccion),
      math.sin(self.direccion)
      )
    anchura_energia = (self.energia/100) * self.radio
    Persona.lienzo.coords(
      self.entidad_energia,
      self.posx - self.radio/2,
      self.posy - self.radio/2 - 10,
      self.posx - self.radio/2 + anchura_energia,
      self.posy - self.radio/2 - 8
    )
    anchura_afiliacion = (self.afiliacion/100) * self.radio
    Persona.lienzo.coords(
      self.entidad_afiliacion,
      self.posx - self.radio/2,
      self.posy - self.radio/2 - 16,
      self.posx - self.radio/2 + anchura_afiliacion,
      self.posy - self.radio/2 - 14
    )
    self.posx += math.cos(self.direccion)
    self.posy += math.sin(self.direccion)
    
  def eliminar(self):
    if self.entidad:
      Persona.lienzo.delete(self.entidad)
      
    if self.entidad_energia:
      Persona.lienzo.delete(self.entidad_energia)
      
    if self.entidad_afiliacion:
      Persona.lienzo.delete(self.entidad_afiliacion)
    
  def aDiccionario(self):
    return {
      "id_jugador": self.id_jugador,
      "posx": self.posx,
      "posy": self.posy,
      "radio": self.radio,
      "direccion": self.direccion,
      "color": self.color,
      "entidad": self.entidad,
      "energia": self.energia,
      "afiliacion": self.afiliacion,
      "entidad_energia": self.entidad_energia,
      "entidad_afiliacion": self.entidad_afiliacion,
      "inventario": self.inventario
    }
    
  def cambiaColor(self, nuevo_color):
    self.color = nuevo_color
    Persona.lienzo.itemconfig(self.entidad, fill=nuevo_color)
    
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
          
          # Si los colores de ambos coinciden aumenta la afiliación hasta 100
          if self.color == otraPersona.color:
            if self.afiliacion < 100:
              self.afiliacion += 25
            if otraPersona.afiliacion < 100:
              otraPersona.afiliacion += 25

          # Si los colores de ambos no coinciden, disminuye la energía hasta 0
          # Si la energía llega a 0 los objetos se destruyen
          else:
            if self.energia > 0:
              self.energia -= 25           
            if otraPersona.energia > 0:
              otraPersona.energia -= 25
              
          # Separar los objetos
          entrelazamiento = self.radio - distancia
          self.posx -= math.cos(self.direccion) * entrelazamiento
          self.posy -= math.sin(self.direccion) * entrelazamiento
          otraPersona.posx += math.cos(otraPersona.direccion) * entrelazamiento
          otraPersona.posy += math.sin(otraPersona.direccion) * entrelazamiento
          
          # Cambiar el color de las personas
          nuevoColor = random.choice(COLORES_BASICOS)
          if self.afiliacion < 100:
            self.cambiaColor(nuevoColor)
          if otraPersona.afiliacion < 100:
            otraPersona.cambiaColor(nuevoColor)
                
    for recogible in Recogibles.recogibles:
      if recogible != self:
        distancia = math.sqrt((recogible.posx - self.posx)**2 + (recogible.posy - self.posy)**2)
        if distancia < self.radio:
          if recogible.id_jugador == None:
            recogible.id_jugador = self.id_jugador
          self.inventario.append(recogible.aDiccionario())
          self.energia = 100
            
        
if __name__ == '__main__':
  persona1 = Persona(1, 497, 497, 30, 180, 'white', '', 100, 0, '', '', [])
  persona2 = Persona.jugador_random()
  log.debug(persona1)
  log.debug(persona2)
  log.debug(persona1.aDiccionario())
  log.debug(persona2.aDiccionario())