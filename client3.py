import socket

clientSocket = socket.socket()
print("Alamat IP Client: 127.0.0.1")

server_host = input("Masukkan alamat IP Server: ")
name = input("Masukkan username Client: ")

clientSocket.connect((server_host, 12345))
clientSocket.send(name.encode())

server_name = clientSocket.recv(1024).decode()
print(server_name, "telah bergabung...")

while True:
    message = input("Pesan: ")
    clientSocket.send(message.encode())
