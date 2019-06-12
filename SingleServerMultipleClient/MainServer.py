import socket
import time 
import sys

s = socket.socket()
host = socket.gethostname()
print("Server will start on host :",host)
port =8080
s.bind((host, port))
print("Server done binding to host and port successfully")
s.listen(1)
print("Waiting for 2 connections...")
conn, addr = s.accept()
print("Client one has connected")
conn.send("Welcome to the Server".encode())
print("Waiting for 1 connections...")
conn1, addr1 = s.accept()
print("Client two has connected")
conn1.send("Welcome to the server".encode())

while 1:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    conn1.send(message)
    print("Message has been sent...")
    recv_message = conn.recv(1024)
    print("Client :", recv_message.decode())
    conn1.send(recv_message)    
    recv_message1 = conn1.recv(1024) 
    print("Client :", recv_message1.decode())
    conn.send(recv_message1)