#client.py
from multiprocessing.connection import wait
import threading
import _thread
import socket
from time import sleep
name = input("Choose your nickname : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 5000
my_socket.connect((host, port))

#This part of the code will just be definitions of the chat bots

class thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i=0
        while i<=10:
            message = my_socket.recv(1024).decode()
            print(message)

# funker
def send_msg():
    while True: 
        message_to_send = input()
        message_navn = name + ": " + message_to_send
        my_socket.send(message_navn.encode())

if name == "Stian":
    message = "Hei, mitt navn er Stian"
    my_socket.send(message.encode())
    sleep(5)
    message = "Ok, du er teit"
    my_socket.send(message.encode())
else:
    recv = thread()
    recv.start()
    #funker
    send_msg()

           
           
     

