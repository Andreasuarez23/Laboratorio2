class Emisor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)

    def enviar_mensaje(self, receptor): #funcion que envia el mensaje
        if receptor.distancia <= 1:
            print(f"Mensaje entregado de {self.nombre} a {receptor.nombre}")
        else:
            print(f"El receptor {receptor.nombre} está demasiado lejos para recibir el mensaje.")


    def recibir_mensaje(self, mensaje, receptor):
        print(f"Receptor {self.nombre} recibe mensaje '{mensaje}' de emisor {receptor.nombre}")


class Receptor:
    def __init__(self, nombre, distancia):  #tiene como atributo la distancia en el que se encuentra el receptor
        self.nombre = nombre
        self.distancia = distancia
        
    def recibir_mensaje(self, mensaje, emisor):
        print(f"Receptor {self.nombre} recibe mensaje '{mensaje}' de emisor {emisor.nombre}")


# Crear nodos
emisores = [Emisor(i) for i in range(0, 5)]


# Definir vecinos para cada nodo (topología mesh)
emisores[0].agregar_vecino(emisores[1])
emisores[0].agregar_vecino(emisores[2])
emisores[0].agregar_vecino(emisores[3])

emisores[1].agregar_vecino(emisores[0])
emisores[1].agregar_vecino(emisores[2])
emisores[1].agregar_vecino(emisores[4])

emisores[2].agregar_vecino(emisores[0])
emisores[2].agregar_vecino(emisores[1])
emisores[2].agregar_vecino(emisores[3])
emisores[2].agregar_vecino(emisores[4])

emisores[3].agregar_vecino(emisores[0])
emisores[3].agregar_vecino(emisores[2])
emisores[3].agregar_vecino(emisores[4])

emisores[4].agregar_vecino(emisores[1])
emisores[4].agregar_vecino(emisores[2])
emisores[4].agregar_vecino(emisores[3])

# Envío de mensajes entre nodos
emisores[0].enviar_mensaje("Hola", emisores[1])
emisores[2].enviar_mensaje("Hola", emisores[4])
emisores[3].enviar_mensaje("Hola", emisores[1])