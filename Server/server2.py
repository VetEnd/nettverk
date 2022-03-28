#server.py
from http import client
from multiprocessing.connection import Client, wait
from queue import Queue
import socket
import threading
from time import sleep
from tkinter import Y
import sys
import os


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Welcome to S354418's server. Follow the instructions below")
print("To write a message to the users, just type in the command line")
print("To get help just type --help")
print("Please follow the instructions to start the server, enjoy!")
print("Do you wanna define the IP and Port yourself? Y/N")

host_q = Queue()
port_q = Queue()
#or "y" or "Yes" or "YEs" or "YES" or "yes" or "yEs" or "yeS" or "YeS"
# or "n" or "NO" or "No" or "no" or "nO"
def check():
    check_input = input(str("Y/N: "))
    if check_input == "Y":
        print("Choose the host ip address: ")
        host_input = input(str("IP address: "))
        port_q.put(host_input)

        print("Choose the host port: ")
        port_input = int (input(str("Port: ")))
        port_q.put(port_input)
    elif check_input == "N":
        print("Set host to localhost and port to 5000")
        host = "127.0.0.1"
        port = 5000
        host_q.put(host)
        port_q.put(port)
    else:
        print("Please enter either Y or N")
        check()

check()


broadcast_list = []
name_list = []

host = host_q.get()
port = port_q.get()

print("Starting Server...")
my_socket.bind((host, port))       

#Back-end for listning og recv av packets

ok = Queue()
e = threading.Event()
name_q = Queue()

def listen_ok():
    i= 0
    while i <=10:
        my_socket.listen()
        conn, addr = my_socket.accept()
        conned = "Connected to the Server!"
        conn.send(conned.encode())
        broadcast_list.append(conn)
        name = conn.recv(1024).decode()
        name_q.put(name)
       
        ok.put(conn)
        e.set()
        
def msg():
    
    i = 1
    test = ok.get()
    name = name_q.get()
    while i <= 10:
        try:
            message = test.recv(1024).decode()
            send_message = name +": " + message
            print(f"Received message: " + send_message)
            broadcast(send_message)
        except socket.error:
            print("Client timedout")
            break
            
        
#Mangler FIKS
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)

def meld():
    i = 0
    while i <= 10:
        hei = input(str("Skriv noe:"))
        if hei == "--help":
            print("Liste med kommandoer (Kick, exit restart?)")
        elif hei =="--kick":
            print("Which of these would you like to kick?")
            print(name_list)
            print("The next line you write will kick the person")
            kick_client = input(str(""))
        elif hei == "--exit":
            print("Kicking all clients, and shuting down")
            message = "Server is shutting down you, will be disconnected automaticlly"
            broadcast(message)
            
            message = "--exit"
            broadcast(message)
            sleep(5)
            print("All clients kicked")
            print("Shuting down..")
            os._exit(1)
        
        else:
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

#Funker halveis, mulig Timeout ville vært bedre
#A good program will check if clients are 
#still connected before trying to interact with them. If they're not, or if you decide that they're 
#taking too long to respond, you can remove them from the list of connections. 

#Funker halveis fullfører hvis man får tid

 #(you can even kick them out if they misbehave) and how to gracefully terminate the program. 

