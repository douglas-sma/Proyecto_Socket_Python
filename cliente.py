import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.connect(('localhost', 4200))

mensaje_completo = ''

while True:
    mensaje = servidor.recv(8)
    if len(mensaje) <= 0:
        break
    mensaje_completo += mensaje.decode("utf-8")

print(mensaje_completo)
