import socket

clientSocket = socket.socket()
ip_client = socket.gethostbyname(socket.gethostname())
print("Alamat IP Client:", ip_client)

server_host = input("Masukkan alamat IP Server: ")
server_port = int(input("Masukkan Port Server: "))
name = input("Masukkan username Client: ")

clientSocket.connect((server_host, server_port))
clientSocket.send(name.encode())

server_name = clientSocket.recv(1024).decode()
print(server_name, "telah bergabung...")

while True:
    message = input("Pesan: ")
    clientSocket.send(message.encode())
