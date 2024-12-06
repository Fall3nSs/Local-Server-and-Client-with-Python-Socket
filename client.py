import socket
import threading
import sys

HOST = "SERVERIP"
PORT = 12345
ADDR = (HOST,PORT)
HEADER = 128
DISCONNECT_MSG = "!DISC"
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendData():
    while True:
        message = input().encode(FORMAT)
        if message != DISCONNECT_MSG and message != '':
            msgLength = len(message)
            sendLength = str(msgLength).encode(FORMAT)
            sendLength += b' ' * (HEADER-len(sendLength))
            client.send(sendLength)
            client.send(message)
        elif message == DISCONNECT_MSG:
            SystemExit()

def receiveData():
    while True:
        messageLength = client.recv(HEADER).decode(FORMAT)
        if messageLength:
            messageLength = len(messageLength)
            message = client.recv(messageLength).decode(FORMAT)
            print(f"Client: {message}")

def start():
    sendThread = threading.Thread(target = sendData)
    receiveThread = threading.Thread(target = receiveData)
    sendThread.start()
    receiveThread.start()

start()        
