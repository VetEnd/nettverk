#server.py




import socket
import threading


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Welcome to S354418's server. Follow the instructions below")
print("To write a message to the users, just type in the command line")
print("To get help just type --help")
print("Please follow the instructions to start the server, enjoy!")

print("Choose the host ip address: ")
host = input(str("IP address: "))

print("Choose the host port: ")
port = int (input(str("Port: ")))

broadcast_list = []

print("Starting Server...")
my_socket.bind((host, port))       

#Back-end for listning og recv av packets
def thread_starter():
    listen_thread = threading.Thread(target=listen_ok)
    listen_thread.start()


def listen_ok():
    i= 0
    while i <=10:
        my_socket.listen()
        conn, addr = my_socket.accept()
        conned = "Connected to the Server! This is your addr"
        conn.send(conned.encode())
        broadcast_list.append(conn)
        msg_thread = threading.Thread(target=msg, args=(conn, ))
        msg_thread.start()

def msg(conn):
    i = 1
    while i <= 10:
        message = conn.recv(1024).decode()
        if message == "hei: bye": 
            my_socket.close()
            break
        else:
            print(f"Received message: " + message)
            broadcast(message)

def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())
    

thread_starter()
print("Thread manager started...")
print("Listening for new connections...")
print("Message listening is active...")
print("Server started")

#Input fra server og ut
def meld():
    i = 0
    while i <= 10:
        hei = input(str("Skriv noe:"))
        message = "Host: " + hei
        broadcast(message)
meld()