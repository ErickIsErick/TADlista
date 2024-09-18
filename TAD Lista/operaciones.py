class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.sig = None

class Lista:
    def __init__(self):
        self.head = None  
        self.ventana = None 

    def colocarVentPrimera(self):
        self.ventana = self.head

    #agregar un elemento después de la ventana
    def agregarDespuesVentana(self, elem):
        nuevo_nodo = Nodo(elem)
        if self.ventana is None:  # lista vacia porque si no la ventana esta afuera
            self.head = nuevo_nodo
            self.ventana = self.head
        else:
            nuevo_nodo.sig = self.ventana.sig
            self.ventana.sig = nuevo_nodo

    #eliminar el elemento en la ventana
    def eliminarVentana(self):
        if self.ventana is None or self.head is None:  # valida sii la lista está vacia o la ventana no apunta a nada
            print("no hay elementos para eliminar")
            return
        
        if self.ventana == self.head:  #valida si la ventana esta en la cabeza
            self.head = self.head.sig
            self.ventana = self.head
        else:
            actual = self.head
            while actual.sig != self.ventana:  #un while para encontrar el nodo anterior a la ventana
                actual = actual.sig
            actual.sig = self.ventana.sig  #aca tiene que saltar el nodo de la ventana
            self.ventana = actual.sig  #mover la ventana al siguiente nodo

    #avanzar la ventana
    def avanzarVentana(self):
        if self.ventana is not None and self.ventana.sig is not None:
            self.ventana = self.ventana.sig
        else:
            print("no se puede avanzar mas, la ventana esta en el final")

  
  
    def imprimirLista(self):
        actual = self.head
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.sig
        print("None")




#                      DEPURADOR                          #


lista = Lista()


lista.colocarVentPrimera()


lista.agregarDespuesVentana(10)
lista.agregarDespuesVentana(20)
lista.agregarDespuesVentana(30)


print("lista despues de agregar elementos:")
lista.imprimirLista()


print("avanzando la ventana...")
lista.avanzarVentana()

print("eliminando el elemento en la ventana...")
lista.eliminarVentana()

print("lista despues de eliminar:")
lista.imprimirLista()
