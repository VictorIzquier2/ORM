class Entidad:
  def __init__(self, posx=None, posy=None, color=None):
    self.posx = posx
    self.posy = posy
    self.color = color
    
  def __str__(self):
    return f'Entidad: [Posición X: {self.posx}, Posición Y: {self.posy}, Color: {self.color}]'