import socket
from datetime import datetime

# Buat socket TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke semua alamat IP di komputer ini
serverSocket.bind(("0.0.0.0", 12345))

serverSocket.listen(1)

print("======================================")
print("   SERVER SIAP DIJALANKAN (TCP CHAT)")
print("======================================")
print("Tanggal :", datetime.now().strftime("%d-%m-%Y"))
print("IP Server:", socket.gethostbyname(socket.gethostname()))
print("Port     : 12345")
print("--------------------------------------")

# Tunggu koneksi dari client
conn, addr = serverSocket.accept()
print("Terhubung dengan:", addr[0])

# Pertukaran nama
client_name = conn.recv(1024).decode()
server_name = input("Masukkan nama Server: ")
conn.send(server_name.encode())

print(f"{client_name} telah bergabung pada {datetime.now().strftime('%H:%M:%S')}")
print("--------------------------------------")

while True:
    # Terima pesan dari client
    pesan = conn.recv(1024).decode()
    if not pesan:
        print("Koneksi client terputus.")
        break

    waktu_terima = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu_terima}] {client_name}: {pesan}")

    # Kirim balasan ke client
    balasan = input("Balas ke client: ")
    waktu_kirim = datetime.now().strftime("%H:%M:%S")
    conn.send(f"[{waktu_kirim}] {server_name}: {balasan}".encode())

conn.close()
serverSocket.close()
