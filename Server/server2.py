#server.py




from queue import Queue

import socket
import threading
from tkinter import Y


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Welcome to S354418's server. Follow the instructions below")
print("To write a message to the users, just type in the command line")
print("To get help just type --help")
print("Please follow the instructions to start the server, enjoy!")
print("Do you wanna define the IP and Port yourself? Y/N")

test = Queue()

def auto():
    kult = input(str("Y/N: "))
    if kult == "Y":
        print("Choose the host ip address: ")
        host = input(str("IP address: "))

        print("Choose the host port: ")
        port = int (input(str("Port: ")))
        
        

    elif kult == "N":
        print("Set host to localhost and port to 5000")
        host = "127.0.0.1"
        port = 5000
        
    else:
        print("Please enter either Y or N")
        auto()

auto()

broadcast_list = []

print("Starting Server...")
my_socket.bind((host, port))       

#Back-end for listning og recv av packets

ok = Queue()
e = threading.Event()


def listen_ok():
    i= 0
    while i <=10:
        
        my_socket.listen()
        conn, addr = my_socket.accept()
        conned = "Connected to the Server! This is your addr"
        conn.send(conned.encode())
        broadcast_list.append(conn)
        ok.put(conn)
        e.set()
        
def msg():
    i = 1
    test = ok.get()
    while i <= 10:
        message = test.recv(1024).decode()
        if message == "hei: bye": 
            my_socket.close()
            break
        else:
            print(f"Received message: " + message)
            broadcast(message)

#Mangler FIKS
def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())

def meld():
    i = 0
    while i <= 10:
        hei = input(str("Skriv noe:"))
        message = "Host: " + hei
        broadcast(message)
    
def thread_starter():
    listen_thread = threading.Thread(target=listen_ok)
    listen_thread.daemon = True
    listen_thread.setDaemon(True)
    listen_thread.start()

    send_meld = threading.Thread(target=meld)
    send_meld.start()

    while 1 < 10:
        e.wait()
        msg_thread = threading.Thread(target=msg)
        msg_thread.daemon = True
        msg_thread.setDaemon(True)
        msg_thread.start()
        
thread_starter()
 

print("Thread manager started...")
print("Listening for new connections...")
print("Message listening is active...")
print("Server started")

#Mangler

#A good program will check if clients are 
#still connected before trying to interact with them. If they're not, or if you decide that they're 
#taking too long to respond, you can remove them from the list of connections. 

#You are free to decide when and how to disconnect the clients (you can
#even kick them out if they misbehave) and how to gracefully terminate the program. 

#Make a "bot" that takes its response from the command line. That way you
#or other users can interact with the bots and make the dialogue more interesting.

#Don't nag your users. It's sometimes nice to let the user add choices and
#options, but your defaults should work well without user interaction. Don't make them fill out 
#forms. 

