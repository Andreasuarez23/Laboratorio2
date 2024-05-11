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

class Emisor:
    def __init__(self, nombre):
        self.nombre = nombre
        
        

    def enviar_mensaje(self, receptor): #funcion que envia el mensaje
        if receptor.distancia <= 1:
            print(f"Mensaje entregado de {self.nombre} a {receptor.nombre}")
        else:
            print(f"El receptor {receptor.nombre} está demasiado lejos para recibir el mensaje.")


class Receptor:
    def __init__(self, nombre, distancia):  #tiene como atributo la distancia en el que se encuentra el receptor
        self.nombre = nombre
        self.distancia = distancia

#enviar mensaje
emisor_a = Emisor("A")
receptor_b= Receptor("B",distancia=1)
receptor_c= Receptor("C",distancia=2)
emisor_a.enviar_mensaje(receptor_b)
emisor_a.enviar_mensaje(receptor_c)