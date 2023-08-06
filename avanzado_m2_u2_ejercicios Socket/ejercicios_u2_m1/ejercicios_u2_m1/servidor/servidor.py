import socket
"""
PASO 1 - Creamos objeto socket
PASO 2 - El método bind() se utiliza para asociar un socket a una dirección de servidor. 
         Se le pasa una dirección y un puerto.
PASO 3 - El método listen() pone al socket en modo servidor de escucha
PASO 4 - El método accept() acepta una conexión entrante (un cliente)
         El método accept() nos devuelve una conexión abierta entre 
         el servidor y el cliente, junto con la dirección del cliente.
PASO 5 - Funciones de envio y recepción de datos.
        Los datos de la conexión se leen con el método recv() 
        y se transmiten con el método sendall() o send().
PASO 6 - El método close () cierra la conexión
"""

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() #Esta es la IP del servidor
puerto = 456 #Puerto en el cual estoy escuchado 
print(host)

serversocket.bind((host, puerto)) 
serversocket.listen(3)
while True:
    #Inicia la conexión 
    clientsocket,address = serversocket.accept()
    print(type(address))
    # address es una tupla de dos valores
    print(0, '---', address[0])    #Dirección IP
    print(1, '---', address[1])    #Número de conexión

    print("Recibo la conexión desde: " + str(address[0]))
    #Mensaje Enviado
    mensaje = b'Hola Bienvenido a nuestro servidor' + b'\r\n'
    clientsocket.send(mensaje)
    clientsocket.close()
