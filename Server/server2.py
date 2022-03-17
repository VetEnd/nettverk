#server.py




import socket
import threading


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5000
ADDRESS = "127.0.0.1"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))       

#Back-end for listning og recv av packets
def thread_starter():
    listen_thread = threading.Thread(target=listen_ok)
    listen_thread.start()


def listen_ok():
    i= 0
    while i <=10:
        print ("listen kjører")
        my_socket.listen()
        conn, addr = my_socket.accept()
        broadcast_list.append(conn)
        msg_thread = threading.Thread(target=msg, args=(conn, ))
        msg_thread.start()

def msg(conn):
    i = 1
    while i <= 10:
        print ("msg kjører")
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

#Input fra server og ut
def meld():
    i = 0
    while i <= 10:
        hei = input(str("Skriv noe:"))
        message = "Host: " + hei
        broadcast(message)
meld()