import socket
from threading import Thread

# A simple clinet for a chat application. Run this along with server.py

def sending(csoc):
    while csoc:
        msg = input()
        if msg == "exit":
            break
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
        except:
            print("closed")
            break


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# soc.connect(("192.168.187.208", 8000))
soc.connect(("127.0.0.1", 8000))
b = soc.recv(1024)
print(b.decode("utf-8"))

Thread(target=sending, args=(soc,)).start()
Thread(target=receving, args=(soc,)).start()

soc.close()
