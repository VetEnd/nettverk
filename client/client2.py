#client.py
import threading
import _thread
import socket
nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()
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
        my_socket.send(message_to_send.encode())

recv = thread()
recv.start()

#funker
send_msg()

           
           
     

