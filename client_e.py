import socket
from datetime import datetime

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = input("Masukkan alamat IP Server: ")
server_port = int(input("Masukkan Port Server: "))

clientSocket.connect((server_ip, server_port))

client_name = input("Masukkan nama Client: ")
clientSocket.send(client_name.encode())

server_name = clientSocket.recv(1024).decode()
print(f"Tersambung dengan {server_name}")
print("------------------------------------")

while True:
    pesan = input("Kirim pesan: ")
    waktu_kirim = datetime.now().strftime("%H:%M:%S")
    clientSocket.send(f"[{waktu_kirim}] {client_name}: {pesan}".encode())

    balasan = clientSocket.recv(1024).decode()
    waktu_terima = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu_terima}] {balasan}")
