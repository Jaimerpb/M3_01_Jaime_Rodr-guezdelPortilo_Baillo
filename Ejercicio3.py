#Creación:
#Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
#Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
#Crea el método __str__ para visualizar por pantalla la información de los productos.


class producto():    #Creamos la clase 'producto'
    def __init__(self,codigo,nombre,precio,tipo):  #constructor y propiedades.
        self.codigo=codigo #Declaramos los atributos 
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo 
    def __str__(self): #Para mostrar la información de los productos(def __str__)
        return ("El codigo de {} es {}, es del tipo {} y su precio es {}".format(self.nombre,self.codigo,self.tipo,self.precio ))
#Probando:
Producto1=producto('72093485', 'lata de COcacola',0.65, 'bebidas')
print(Producto1)
Producto2=producto('9134875092','chanclas',3 ,'prendas')
print(Producto2)














