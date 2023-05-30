import socket
from threading import Thread


def sending(csoc):
    while csoc:
        msg = input()
        try:
            csoc.sendall(msg.encode("utf-8"))
        except socket.error:
            print("closed")
            break


def receving(csoc):
    while csoc:
        try:
            b = csoc.recv(1024)
            print(b.decode('utf-8'))
        except socket.error:
            print("closed")
            break


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(("", 8000))
soc.listen()

clients = []
cnt = 0

while True:
    c_socket, addr = soc.accept()
    clients.append(c_socket)
    c_socket.sendall(b"Hello from server")
    Thread(target=sending, args=(clients[cnt],)).start()
    Thread(target=receving, args=(clients[cnt],)).start()
    cnt += 1
