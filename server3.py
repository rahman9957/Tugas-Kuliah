import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))

print("Alamat IP: 127.0.0.1")
name = input("Masukkan Username Server: ")

serverSocket.listen()
msg, addrs = serverSocket.accept()
print("Menerima koneksi dari", addrs[0])
print("Connection Established dengan:", addrs[0])

client = msg.recv(1024).decode()
print(client + " sudah terhubung.")
msg.send(name.encode())

while True:
    message = msg.recv(1024).decode()
    print(client, ":", message)
