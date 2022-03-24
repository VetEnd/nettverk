#client.py
from cgi import print_arguments
import threading
import socket
from time import sleep
name = input("Choose your nickname : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def start():
    print("Type inn IP address: ")
    host = input(str("IP address: "))

    print("Type inn port")
    port = int (input(str("Port: ")))

    print("Connecting to server")
    my_socket.connect((host, port))

    conned = my_socket.recv(1024).decode()
    print(conned)

    name_send = my_socket.send(name.encode())
#This part of the code will just be definitions of the chat bots
start()
def recv1():
    i=0
    while i<=10:
        message = my_socket.recv(1024).decode()
        print(message)

# funker
def send_msg():
    while True: 
        message_to_send = input()
        message_navn = message_to_send
        my_socket.send(message_navn.encode())
        if message_to_send == "exit":
            my_socket.close()

if name == "Stian":
    message = "Hei, mitt navn er Stian"
    my_socket.send(message.encode())
    sleep(5)
    message = "Ok, du er teit"
    my_socket.send(message.encode())
else:
    
    #funker
    send_msg()

def thread_starter():
    recv = threading.Thread(target=recv1)
    recv.daemon = True
    recv.start

    send = threading.Thread(target=send_msg)           
    send.daemon = True
    

