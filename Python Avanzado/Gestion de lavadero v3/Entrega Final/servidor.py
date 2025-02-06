import socket
import datetime

archivo_log = open("log.txt", "a")
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


servidor_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # Creando socket TCP

HOST = "localhost"
PORT = 8080

servidor_socket.bind((HOST, PORT))
servidor_socket.listen(1)

print("Servidor escuchando a puerto ", PORT)

archivo_log.write(
    f"{fecha_actual} - Servidor inicado. Conectado a puerto " + str(PORT) + ".\n"
)

cliente_socket, addr = servidor_socket.accept()  # Conexion recibida desde el cliente
print("Conexión establecida con ", addr)

try:
    while True:
        mensaje = cliente_socket.recv(
            1024
        )  # Recibiendo datos del cliente en max 1024 bytes
        if not mensaje:
            print("Cliente desconectado.")
            break
        print("Cliente: ", mensaje.decode())
        with open("log.txt", "a") as archivo_log:
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo_log.write(f"{fecha_actual} - {mensaje.decode()}.\n")

except Exception as e:
    print(e)
    with open(
        "log.txt", "a"
    ) as archivo_log:  # Creamos registro en log en caso de que el programa se cierre.
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo_log.write(f"{fecha_actual} - Se cerro el programa debido a un error.\n")

finally:
    cliente_socket.close()
    servidor_socket.close()
    print("Conexión cerrada.")
    with open("log.txt", "a") as archivo_log:
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo_log.write(f"{fecha_actual} - Programa cerrado.\n")
