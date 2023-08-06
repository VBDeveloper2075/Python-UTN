import socket
import sys
import binascii

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################333
mi_valor = 0x00003EF5
print(type(mi_valor))
packed_data = bytearray()
packed_data += mi_valor.to_bytes(4, "big")
mensaje = packed_data

sock.sendto(mensaje, (HOST, PORT))
received = sock.recvfrom(1024)

print(received)
# ===== ENVIO Y RECEPCIÓN DE DATOS =================
# print(binascii.hexlify(mensaje).decode("utf-8"))
# print("Sent:     {}".format(data))
# print("Received: {}".format(received))
# print(binascii.hexlify(received[0]).decode("utf-8"))
# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
