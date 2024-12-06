import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER,PORT)
HEADER = 128
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISC"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []

def broadcast(message, sender_conn):
    for conn in connections:
        if conn != sender_conn: 
            conn.send(message)

def handleClient(conn,addr):
    print(f"[CONNECTION] {addr} connected!")
    connections.append(conn)
    connected = True
    while connected:
        data_length = conn.recv(HEADER).decode(FORMAT)
        if data_length:
            broadcast(data_length.encode(FORMAT), conn)
            data_length = len(data_length)
            data = conn.recv(data_length).decode(FORMAT)
            if data == DISCONNECT_MSG:
                print(f"{addr} disconnected from the server!")
                connected = False
                connections.remove(conn)
                conn.close()
            else:    
                broadcast(data.encode(FORMAT), conn)
                print(data)


def start():
    server.listen()
    print(f"[LISTENING] Server started to listening on {SERVER}!")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handleClient, args = (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("Server is starting...")
start()
