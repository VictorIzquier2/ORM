import tkinter as tk
import random
import math

class Persona:
  def __init__(self):
    self.posx = random.randint(0,1024)
    self.posy = random.randint(0,1024)
    self.radio = 30
    self.direccion = random.randint(0,360)
    self.color = "blue"
    self.entidad = ""
    
  def dibuja(self):
    self.entidad = lienzo.create_oval(
      self.posx-self.radio/2,
      self.posy-self.radio/2,
      self.posx+self.radio/2,
      self.posy+self.radio/2, 
      fill=self.color
      )
  def mueve(self):
    lienzo.move(
      self.entidad,
      math.cos(self.direccion),
      math.sin(self.direccion)
      )
    
# instanciar ventana tkinter    
raiz = tk.Tk()

# instanciar un lienzo en la ventana tkinter
lienzo = tk.Canvas(width=1024, height=1024)
lienzo.pack()

# instanciación de la clase Persona
personas = []
npersonas = 20

# En la coleccion instancio personas
for i in range(0, npersonas):
  personas.append(Persona())

# Para cada persona pintarlas en la pantalla
for persona in personas:
  persona.dibuja()
  
# creo un bucle repetitivo
def bucle():
  # para ada persona en la coleccion
  for persona in personas:
    persona.mueve()
  raiz.after(10, bucle)
  
bucle()

raiz.mainloop()