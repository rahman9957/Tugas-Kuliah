import socket
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))

print("Alamat IP: 127.0.0.1")
print("Tanggal :", datetime.now().strftime("%d-%m-%Y"))
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
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] {client}: {message}")
