import threading
import socket

PORT = 3030
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handleClient(con, addr):
    pass


def start():
    pass


print("[STARTING] ...")
start()
