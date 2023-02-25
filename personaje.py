
class Personaje:
    
    #creamos al constructor
    def __init__(self, esp,nom,alt):
         self.__especie = esp
         self.__nombre = nom
         self.__altura = alt
    
    #metodos personaje 
    
    def correr(self,status):
        if(status):
            print("el personaje "+ self.__nombre + " esta corriendo")
        else:
         print("el personaje "+ self.__nombre + " se detuvo")
         
    def lanzarGranada(self):
        print("se lanzo granada ") 
    def recargarArma(self, municiones):
        cargador= 5
        cargador=cargador+municiones
        print("el arma tiene ahora "+ str(cargador) +" balas")  
        
        #ejemplo de metodo privado
        
    def __pensar(self):
        print("estoy pensando.....")    
     
    #declaramos los Getters y Setters de los atributos privados 
             
    def getespecie(self):
        return self.__especie
    
    def setespecie(self,esp):
        self.__especie=esp
    
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nom):
        self.__nombre=nom
        
    def getaltura(self):
        return self.__altura
    
    def setaltura(self,alt):
        self.__especie=alt
            
            
         