import socket
"""
PASO 1 - Creamos objeto socket
PASO 2 (OPCIONAL) - El método bind() se utiliza para asociar un socket a una dirección de servidor. 
         Se le pasa una dirección y un puerto.
PASO 3 - El método connect() fija una conexión remota
PASO 4 - Funciones de envio y recepción de datos.
        Después que la conexión esté establecida, 
        la información puede ser enviada con el método sendall() 
        y recibida con el método recv(), igual que el servidor.
PASO 5 - El método close () cierra la conexión
"""

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.56.1'
#host = socket.gethostname() #esta es la dirección ip del servidor.
puerto = 456
clientsocket.connect((host, puerto)) 
mensaje = clientsocket.recv(1024)
clientsocket.close()
print(mensaje.decode('ascii'))