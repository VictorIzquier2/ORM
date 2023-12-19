from logger_base import log

class Entidad:
  def __init__(self, posx=None, posy=None, radio=None, color=None, entidad=None):
    self.posx = posx
    self.posy = posy
    self.radio = radio
    self.color = color
    self.entidad = entidad
    
  def __str__(self):
    return f'Entidad: [Posición X: {self.posx}, Posición Y: {self.posy}, Radio: {self.radio} Color: {self.color}]'
  
if __name__ == '__main__':
  entidad1 = Entidad(497, 497, 30, 'gold', '')
  log.debug(entidad1)