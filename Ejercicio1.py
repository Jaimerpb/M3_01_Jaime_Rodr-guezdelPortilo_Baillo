#Creación:
#Crea una clase llamada Alumno que tenga los atributos nombre y nota
#Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
#Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota


class Alumno():       #Creamos la clase 'Alumno' 
    def __init__(self,nota,nombre): #Creamos el constructor de la clase, de parámetros nota y nombre
        self.nota=nota  #Declaramos que el atributo nota es igual al parámetro nota
        self.nombre=nombre   #Declaramos que el atributo nombre es igual al parámtero nombre
        print('El alumno se ha creado con éxito') #Añadir en el constructor un print para informar de que el alumno se ha creado con éxito.
    
    def Calificación(self): #Para saber si el alumno a aprobado o suspendido en base a su nota
        print("ALUMNO:{},NOTA:{}".format(self.nombre,self.nota))#Mostramos la nota y nombre dle alumno
        if self.nota<5 :    #Si el alumno saca una nota inferior a 5 indicamos que es un suspenso (mostrando un mensahe por pantalla) 
            print("El alumno:{} ha suspendido".format(self.nombre))
        else:  #El alumno saca una nota mayor igaul a 5,el alumno a aprobado.
            print("El alumno ha aprobado")


#Experimentación:
#Crea algunos alumnos
Alumno1=Alumno(8,"Jaime")
Alumno1.Calificación()
print(Alumno1)
Alumno2=Alumno(-1,"javier")
Alumno2.Calificación()
print(Alumno2)