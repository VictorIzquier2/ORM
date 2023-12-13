import random
import math
from colores_basicos import COLORES_BASICOS

class Personas():
  contador_personas = 0
  personas = []
  
  @classmethod    
  def agregar_persona(cls, persona):
    Personas.contador_personas += 1
    cls.personas.append(persona) 
  
  def __str__(cls):
    personas_str = ''
    for persona in cls.personas:
      personas_str += persona.__str__()
    return f'''
    Personas: {personas_str}
    '''