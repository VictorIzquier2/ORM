class Recogibles():
  contador_recogibles = 0
  recogibles = []
  
  @classmethod
  def agregar_recogible(cls, recogible):
    Recogibles.contador_recogibles +=1
    cls.recogibles.append(recogible)
    
  @classmethod
  def eliminar_recogible(cls, id_recogible):
    for recogible in cls.recogibles:
      if recogible.id_recogible == id_recogible:
        indice = cls.recogibles.index(recogible)
        cls.recogibles.pop(indice)
    Recogibles.contador_recogibles -= 1
    
  def __str__(cls):
    recogibles_str = ''
    for recogible in cls.recogibles:
      recogibles_str += recogible.__str__()
    return f'''
    Recogibles: {recogibles_str}
    '''