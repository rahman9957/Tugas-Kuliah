import socket



socketClient = socket.socket( socket.AF_INET,socket.SOCK_DGRAM)

socketClient.connect(("127.0.0.1", 12345))



while True:

    a = input(str('message>>'))

    b = str.encode(a)

    socketClient.send(b)

    break

