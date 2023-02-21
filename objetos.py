#1. importa la clase
from personaje import *

#2. instanciar un objeto
heroe= Personaje()

#3. acceder a sus atributos
print("Atributos del personaje")
print("el personaje pertenece a la raza: "+ heroe.especie)
print("se llama: "+ heroe.nombre)
print("mide: "+ str(heroe.altura) + " metros")


print("metodos personaje")
heroe.correr(True)
heroe.lanzarGranada()
heroe.recargarArma(68)