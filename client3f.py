import socket
from datetime import datetime

# Buat socket TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("======================================")
print("     CLIENT SIAP DIJALANKAN (TCP CHAT)")
print("======================================")

# Masukkan alamat IP server dan port
server_ip = input("Masukkan alamat IP Server: ")
server_port = 12345

# Koneksi ke server
clientSocket.connect((server_ip, server_port))

# Pertukaran nama
client_name = input("Masukkan nama Client: ")
clientSocket.send(client_name.encode())

server_name = clientSocket.recv(1024).decode()
print(f"Tersambung dengan {server_name}")
print("--------------------------------------")

while True:
    # Kirim pesan ke server
    pesan = input("Kirim pesan: ")
    waktu_kirim = datetime.now().strftime("%H:%M:%S")
    clientSocket.send(f"[{waktu_kirim}] {client_name}: {pesan}".encode())

    # Terima balasan dari server
    balasan = clientSocket.recv(1024).decode()
    if not balasan:
        print("Koneksi server terputus.")
        break

    waktu_terima = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu_terima}] {balasan}")

clientSocket.close()
