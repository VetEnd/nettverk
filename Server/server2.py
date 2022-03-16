#server.py
from email import message
import re
import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5000
ADDRESS = "127.0.0.1"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))



def listen():
    i = 0
    while i < 10:
        my_socket.listen()
        conn, addr = my_socket.accept()
        broadcast_list.append(conn)
        print(f"kjører")

def msg(conn):
    i=0
    while i < 9:
        message = conn.recv(1024).decode()
        if message:
            print(f"Received message: " + message)
            broadcast(message)
        else:
            print(f" disconnected : " + conn)
        return  

def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")




ok = threading.Thread(listen)
ok.start()
