from colores_basicos import COLORES_BASICOS
from logging import log

class Personas():
  contador_personas = 0
  personas = []
 
  @classmethod    
  def agregar_persona(cls, persona):
    Personas.contador_personas += 1
    cls.personas.append(persona)
    
  @classmethod
  def eliminar_persona(cls, id_jugador):
    for persona in cls.personas:
      if persona.id_jugador == id_jugador:
        indice = cls.personas.index(persona)
        cls.personas.pop(indice)
    Personas.contador_personas -=1
  
  def __str__(cls):
    personas_str = ''
    for persona in cls.personas:
      personas_str += persona.__str__()
    return f'''
    Personas: {personas_str}
    '''
