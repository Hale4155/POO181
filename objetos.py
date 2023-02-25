#1. importa la clase
from personaje import *

#2.solicitar atributos para el objeto 
print("")
print("### solicitud de datos del heroe ###")
espH=input("escribe el nombre de la especie del heroe: ")
nomH=input("escribe el nombre del heroe: ")
altH=float(input("escribe la altura del heroe: "))
cargaH=int(input("cuantas balas se recargaran al heroe: "))

print("")
print("### solicitud de datos del villano ###")
espV=input("escribe el nombre de la especie del villano: ")
nomV=input("escribe el nombre del villano: ")
altV=float(input("escribe la altura del villano: "))
cargaV=int(input("cuantas balas se recargaran al villano: "))
#3. creamos 2 objetos
heroe= Personaje(espH,nomH,altH)
villano= Personaje(espV,nomV,altV)

heroe.setnombre("Genji")
#4. acceder a sus atributos y metodos de cada obj

print("")
print("## Atributos y Metodos del heroe ##")
print("el personaje pertenece a la raza: "+ heroe.getespecie())
print("se llama: "+ heroe.getnombre())
print("mide: "+ str(heroe.getaltura()) + " metros")
print("")


print("metodos personaje")
heroe.correr(True)
heroe.lanzarGranada()
heroe.recargarArma(cargaH)

#ejemplo de lo que no se debe hacer 

# heroe.__pensar()


print("")
print("## Atributos y Metodos del villano ##")
print("el personaje pertenece a la raza: "+ villano.getespecie())
print("se llama: "+ villano.getnombre())
print("mide: "+ str(villano.getaltura()) + " metros")
print("")


print("metodos personaje")
heroe.correr(False)
heroe.lanzarGranada()
heroe.recargarArma(cargaV)

