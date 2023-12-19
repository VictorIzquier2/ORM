import tkinter as tk
import tkinter.messagebox as msgbox
import json
from Persona import Persona
from Personas import Personas
from PersonaDAO import PersonaDAO
from Recogible import Recogible
from Recogibles import Recogibles
from RecogibleDAO import RecogibleDAO

def guardarPersonas():
  # Guardar archivo json
  for persona in Personas.personas:
    cadena = json.dumps([persona.aDiccionario() for persona in Personas.personas])
    with open("jugadores.json", 'w', encoding='utf8') as archivo:
      archivo.write(cadena)
      
  for recogible in Recogibles.recogibles:
    cadena = json.dumps([recogible.aDiccionario() for recogible in Recogibles.recogibles])
    with open("recogibles.json", "w", encoding='utf8') as archivo:
      archivo.write(cadena)
        
  with open("jugadores.json", 'r', encoding='utf8') as archivo:
    jugadores = json.load(archivo)
    if not PersonaDAO.comprobar():
      for jugador in jugadores:
        id_jugador = jugador['id_jugador']
        posx = jugador['posx']
        posy = jugador['posy']
        radio = jugador['radio']
        direccion = jugador['direccion']
        color = jugador['color']
        entidad = jugador['entidad']
        energia = jugador['energia']
        afiliacion = jugador['afiliacion']
        entidad_energia = jugador['entidad_energia']
        entidad_afiliacion = jugador['entidad_afiliacion']
        inventario = jugador['inventario']
        persona = Persona(id_jugador, posx, posy, radio, direccion, color, entidad, energia, afiliacion, entidad_energia, entidad_afiliacion, inventario)
        PersonaDAO.insertar(persona)   
    else:
      for jugador in jugadores:
        id_jugador = jugador['id_jugador']
        posx = jugador['posx']
        posy = jugador['posy']
        radio = jugador['radio']
        direccion = jugador['direccion']
        color = jugador['color']
        entidad = jugador['entidad']
        energia = jugador['energia']
        afiliacion = jugador['afiliacion']
        entidad_energia = jugador['entidad_energia']
        entidad_afiliacion = jugador['entidad_afiliacion']
        inventario = jugador['inventario']
        persona = Persona(id_jugador, posx, posy, radio, direccion, color, entidad, energia, afiliacion, entidad_energia, entidad_afiliacion, inventario)
        PersonaDAO.actualizar(persona)
        
  with open("recogibles.json", 'r', encoding='utf8') as archivo:
    recogibles = json.load(archivo)
    if not RecogibleDAO.comprobar():
      for recogible in recogibles:
        id_recogible = recogible['id_recogible']
        id_jugador = recogible['id_jugador']
        posx = recogible['posx']
        posy =recogible['posy']
        radio = recogible['radio']
        color = recogible['color']
        entidad = recogible['entidad']
        recogible = Recogible(id_recogible, id_jugador, posx, posy, radio, color, entidad)
        RecogibleDAO.insertar(recogible)   
    else:
      for recogible in recogibles:
        id_recogible = recogible['id_recogible']
        id_jugador = recogible['id_jugador']
        posx = recogible['posx']
        posy = recogible['posy']
        radio = recogible['radio']
        color = recogible['color']
        entidad = recogible['entidad']
        recogible = Recogible(id_recogible, id_jugador, posx, posy, radio, color, entidad)
        RecogibleDAO.actualizar(recogible)
          
def mostrar_mensaje_ganador(color_ganador):
  ventana_mensaje = tk.Toplevel(raiz)
  ventana_mensaje.title("Fin del juego")
  ventana_mensaje.geometry("400x100")
  
  tk.Label(ventana_mensaje, text=f'Ganó el equipo de color {color_ganador}', font=("Helvetica, 12")).pack(pady=20)
  
  boton_cerrar = tk.Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
  boton_cerrar.pack(pady=10)
    
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
    
  with open("recogibles.json", "r") as carga2:
    cargado2 = carga2.read()
  
  if cargado: # Nos aseguramos que el contenido del archivo no está vacío  
    cargadolista = json.loads(cargado)
    for elemento in cargadolista:
      Persona.lienzo = lienzo
      persona = Persona.jugador_random()
      persona.__dict__.update(elemento)
      Personas.agregar_persona(persona)
  else:
    print("El archivo está vacío. Se crearán nuevas personas")
    
  if cargado2:
    cargadolista2 = json.loads(cargado2)
    for elemento in cargadolista2:
      Recogible.lienzo = lienzo
      recogible = Recogible.recogible_random()
      recogible.__dict__.update(elemento)
      Recogibles.agregar_recogible(recogible)
  else:
    print("El archivo está vacío. Se crearán nuevos recogibles")
    
except FileNotFoundError as FNFE:
  print(f"Error: Archivo no encontrado: {FNFE}")
except json.JSONDecodeError as JDE:
  print(f"Error al decodificar JSON. El archivo puede estar corrupto o mal construido: {JDE}")
except Exception as e:
  print(f"Hubo un error: {e}, {type(e)}")

# En la coleccion instancio personas en el caso de que no existan
if Personas.contador_personas == 0:
  npersonas = 5
  for i in range(0, npersonas):
    Persona.lienzo = lienzo
    persona = Persona.jugador_random()
    
    Personas.agregar_persona(persona)
    
if Recogibles.contador_recogibles == 0:
  nrecogibles = 3
  for i in range(0, nrecogibles):
    Recogible.lienzo = lienzo
    recogible = Recogible.recogible_random()
    
    Recogibles.agregar_recogible(recogible)

# Para cada persona pintarlas en la pantalla
for persona in Personas.personas:
  if persona.energia > 0:
    persona.dibuja()
    
for recogible in Recogibles.recogibles:
  print(recogible)
  if recogible.id_jugador == None:
    recogible.dibuja()

contador = 0
# creo un bucle repetitivo
def bucle():
  colores_activos = {persona.color for persona in Personas.personas if persona.energia > 0}
  
  if len(colores_activos) == 1:
    color_ganador = colores_activos.pop()
    mostrar_mensaje_ganador(color_ganador)
    return
  
  # para cada persona en la coleccion
  personas_a_eliminar = []
  for persona in Personas.personas:
    if persona.energia > 0:
      persona.mueve()
    else:
      persona.eliminar()
      personas_a_eliminar.append(persona)
      
  for persona in personas_a_eliminar:
    Personas.eliminar_persona(persona.id_jugador)
    if PersonaDAO.existe_registro(persona):
      PersonaDAO.eliminar(persona)
      
  recogibles_a_eliminar = []
  for recogible in Recogibles.recogibles:
    if recogible.id_jugador !=None:
      recogible.eliminar()
      recogibles_a_eliminar.append(recogible)
      
  for recogible in recogibles_a_eliminar:
    Recogibles.eliminar_recogible(recogible)
    if RecogibleDAO.existe_registro(recogible):
      RecogibleDAO.eliminar(recogible)      
  
  raiz.after(5, bucle)    
  
bucle()

raiz.mainloop()