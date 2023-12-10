import random
import math
from colores_basicos import COLORES_BASICOS

class Personas():
  contador_personas = 0
  
  def __init__(self, personas):
    self._personas = list(personas)
    
  @property
  def personas(self):
    return self._personas
  
  @personas.setter
  def personas(self, personas):
    self.personas = personas
    
  def agregar_persona(self, persona):
    Personas.contador_personas += 1
    self.personas.append(persona)  
  
  def __str__(self):
    personas_str = ''
    for persona in self.personas:
      personas_str += persona.__str__()
    return f'''
    Personas: {personas_str}
    '''