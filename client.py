import socket

SERVER = "10.248.0.146"
PORT = 12345
FORMAT = 'utf-8'
ADDR = (SERVER,PORT)
HEADER = 128

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def sendData(msg):
    msg = msg.encode(FORMAT)
    messageLength = len(msg)
    send_length = str(messageLength).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)

while True:
    sendData(input())
