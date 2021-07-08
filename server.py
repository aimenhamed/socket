import threading
import socket

HEADER = 64
PORT = 3030
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SERVER}.")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}.")


print("[STARTING] ...")
start()
