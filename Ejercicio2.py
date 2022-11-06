#CREACIÓN:
#Copia el ejercicio anterior y realicemos una modificación:
#Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. 
#Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:
#def __str__(self): return "Lo que quiero mostrar"
#Este método nos sirve para imprimir por pantalla la información de un objeto, 
#si tenemos un objeto alumno1 creado y realizamos print(alumno1), 
#Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

class Alumno:
    def __init__(self,nota,nombre): 
        self.nota=nota 
        self.nombre=nombre   
        print('El alumno se ha creado con éxito') 
    
    def Calificación(self): 
        print("ALUMNO:{},NOTA:{}".format(self.nombre,self.nota))
        if self.nota<5 :    
            print("El alumno:{} ha suspendido".format(self.nombre))
        else:  
            print("El alumno ha aprobado")
    def __str__(self):               #para representar los objetos como una cadena, para mostrar por pantalla 
        return "Nombre:{},Nota:{}".format(self.nombre,self.nota)









 