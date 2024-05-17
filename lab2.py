"""Segundo ejercicio de programación
1. Dados las siguientes topologías de red vistas en clase:
a. Mesh
b. Star
c. Bus.
2. Implemente un programa en Python que modele una de ellas según la asignación dada a su equipo.
3. Cada uno de estos modelos tiene respetar la topología asignada y cumplir con el siguiente protocolo de
comunicación:
a. Mesh: Dado un emisor A y un receptor B, el mensaje debe ser entregado si B esta como maximo a un
vecino de distancia. Caso contrario , el mensaje no se entrega pero se indica en pantalla que este es el
caso."""

#Integrantes del grupo: Mijal Nuñez - Andrea Suarez
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)

    def enviar_mensaje(self, mensaje, receptor):
        if receptor in self.vecinos:
            print(f"Nodo {self.nombre} envía mensaje '{mensaje}' a Nodo {receptor.nombre}")
            receptor.recibir_mensaje(mensaje, self)
        else:
            print(f"El receptor {receptor.nombre} está demasiado lejos para recibir el mensaje '{mensaje}'.")

    def recibir_mensaje(self, mensaje, emisor):
        print(f"Nodo {self.nombre} recibe mensaje '{mensaje}' de Nodo {emisor.nombre}")


# Crear nodos
nodos = {
    "A": Nodo("A"),
    "B": Nodo("B"),
    "C": Nodo("C"),
    "D": Nodo("D"),
    "E": Nodo("E")
}

# Definir vecinos para cada nodo (topología mesh)
nodos["A"].agregar_vecino(nodos["B"])
nodos["A"].agregar_vecino(nodos["C"])
nodos["A"].agregar_vecino(nodos["D"])

nodos["B"].agregar_vecino(nodos["A"])
nodos["B"].agregar_vecino(nodos["C"])
nodos["B"].agregar_vecino(nodos["E"])

nodos["C"].agregar_vecino(nodos["A"])
nodos["C"].agregar_vecino(nodos["B"])
nodos["C"].agregar_vecino(nodos["D"])
nodos["C"].agregar_vecino(nodos["E"])

nodos["D"].agregar_vecino(nodos["A"])
nodos["D"].agregar_vecino(nodos["C"])
nodos["D"].agregar_vecino(nodos["E"])

nodos["E"].agregar_vecino(nodos["B"])
nodos["E"].agregar_vecino(nodos["C"])
nodos["E"].agregar_vecino(nodos["D"])

# Envío de mensajes entre nodos
nodos["A"].enviar_mensaje("Hola", nodos["B"])
nodos["C"].enviar_mensaje("Hola", nodos["E"])
nodos["D"].enviar_mensaje("Hola", nodos["B"])
nodos["A"].enviar_mensaje("Hola", nodos["E"]) 
nodos["B"].enviar_mensaje("Hola",nodos["E"])
nodos["E"].enviar_mensaje("Hola",nodos["D"])


