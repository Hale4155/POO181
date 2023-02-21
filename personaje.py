
class Personaje:
    
    #atributos del personaje 
    
    especie = "humano"
    nombre = "genji"
    altura = 1.90
    
    #metodos personaje 
    
    def correr(self,status):
        if(status):
            print("el personaje "+ self.nombre + " esta corriendo")
        else:
         print("el personaje "+ self.nombre + " se detuvo")
         
    def lanzarGranada(self):
        print("se lanzo granada ") 
    def recargarArma(self, municiones):
        cargador= 5
        cargador=cargador+municiones
        print("el arma tiene ahora "+ str(cargador) +" balas")        
     