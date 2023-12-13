import tkinter as tk
import json
from Persona import Persona
from Personas import Personas 


def guardarPersonas():
  cadena = json.dumps([persona.aDiccionario() for persona in Personas.personas])
  with open("jugadores.json", 'w') as archivo:
    archivo.write(cadena)
    
# instanciar ventana tkinter    
raiz = tk.Tk()

marcoSuperior = tk.Frame(raiz)
marcoSuperior.pack(side=tk.TOP, fill=tk.X)

marcoPrincipal = tk.Frame(raiz)
marcoPrincipal.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# Boton de guardar
boton = tk.Button(marcoSuperior, text="Guardar", command=guardarPersonas)
boton.pack(side=tk.LEFT)

# instanciar un lienzo en la ventana tkinter
lienzo = tk.Canvas(marcoPrincipal, width=1024, height=1024)
lienzo.pack()

# Cargar personas desde el disco 
try:
  with open("jugadores.json", "r") as carga:
    cargado = carga.read()
  
  if cargado: # Nos aseguramos que el contenido del archivo no está vacío  
    cargadolista = json.loads(cargado)
    for elemento in cargadolista:
      persona = Persona(lienzo)
      persona.__dict__.update(elemento)
      Personas.agregar_persona(persona)
  else:
    print("El archivo está vacío. Se crearán nuevas personas")
except FileNotFoundError as FNFE:
  print(f"Error: Archivo no encontrado: {FNFE}")
except json.JSONDecodeError as JDE:
  print(f"Error al decodificar JSON. El archivo puede estar corrupto o mal construido: {JDE}")
except Exception as e:
  print(f"Hubo un error: {e}, {type(e)}")

# En la coleccion instancio personas en el caso de que no existan
if Personas.contador_personas == 0:
  npersonas = 25
  for i in range(0, npersonas):
    Personas.agregar_persona(Persona(lienzo))

# Para cada persona pintarlas en la pantalla
for persona in Personas.personas:
  persona.dibuja()
  
# creo un bucle repetitivo
def bucle():
  # para ada persona en la coleccion
  for persona in Personas.personas:
    persona.mueve()
  raiz.after(10, bucle)    
  
bucle()

raiz.mainloop()