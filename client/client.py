
from concurrent.futures import thread
import socket #Imports the libary for socket'
import sys
import _thread
import threading

Host = input(str("IP addresse:"))

Port = 5000

name = input(str("Please enter your username: "))


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect ((Host, Port))

print ("Connect to server")

def send_thread():
    while True:
        message = input()
        if message:
            message_name = name + " : " + message
            conn.send(message.encode())

def recv_thread():
    while True:
        message = conn.recv(1024).decode()
        print (message)

threading.Thread(target=send_thread).start()
threading.Thread(target=recv_thread).start()
