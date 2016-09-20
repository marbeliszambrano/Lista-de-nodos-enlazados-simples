# Lista-de-nodos-enlazados-simples
class Nodo:
    def __init__(self,valor):
        self.info = valor
        self.sig = None

class Lista:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__actual = None
        self.__n = 0
        self.__pos = 0

    def insertar_inicio(self,valor):
        nodo = Nodo(valor)
        nodo.sig = self.__primero
        self.__primero = nodo
        self.__actual = nodo
        if (self.__ultimo == None):
            self.__ultimo = nodo
        self.__n = self.__n+1
        self.__pos = 0

    def insertar_ultimo(self,valor):
        nodo = Nodo(valor)
        if(self.__ultimo == None):
            self.__primero = nodo
        else:
            self.__ultimo.sig = nodo
        self.__ultimo = nodo
        self.__actual = nodo
        self.__n = self.__n+1
        self.__pos = self.__n-1

    def insertar_actual(self,valor):
        if(self.__n==0):
            self.insertar_inicio(valor)
            return
        if(self.__actual==self.__ultimo):
            self.insertar_ultimo(valor)
            return
        nodo = Nodo(valor)
        nodo.sig = self.__actual.sig
        self.__actual.sig = nodo
        self.__actual = nodo
        self.__n =self.__n+1
        self.__pos = self.__pos+1

    def pos_actual(self,pos):
        if (self.__n == 0):
            return 
        nodo = self.__primero
        for i in range(self.__n):
            if(i==pos):
                self.__actual = nodo
                return " el actual esta en la posicion",pos
        return "la posicion no existe"

    def buscar_elem(self,valor): 
        if (self.__n == 0):
            return 
        nodo = self.__primero
        for i in range(self.__n):
            if (nodo.info == valor):
                return ("el numero"),valor,(" si se encuentra")
            nodo = nodo.sig
        return " el valor no se encuentra en la lista"
        
    def eliminar_primero(self):
        if(self.__primero == None):
            return
        nodo = self.__primero
        if(self.__actual == nodo):
            self.__actual == nodo.sig
        self.__primero = nodo.sig
        self.__n = self.__n-1
        self.__pos = self.__pos-1
        del nodo
        if(self.__n == 0):
            self.__ultimo=None
            self.__actual= None
            
    def mostrar(self):
        nodo = self.__primero
        for i in range(self.__n):
            print nodo.info
            nodo=nodo.sig
            
l= Lista()
l.insertar_actual(5)
l.insertar_actual(10)
l.insertar_actual(15)
l.insertar_actual(20)
l.insertar_inicio(25)
l.insertar_actual(30)
l.insertar_ultimo(35)

l.mostrar()

m=l.pos_actual(6)
print m

n=l.buscar_elem(60)
print n

l.eliminar_primero()   
l.eliminar_primero()
l.eliminar_primero()
l.mostrar()
        
