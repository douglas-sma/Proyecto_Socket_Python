import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind( ('localhost', 4200) )
servidor.listen(5)

while True:
    clientesocket, address = servidor.accept()
    print(f"Conexion desde {address} ha sido establecida")

    clientesocket.send(bytes("Bienvenido al servidor", "utf-8"))
    clientesocket.close()

