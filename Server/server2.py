#server.py



import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5000
ADDRESS = "127.0.0.1"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))       

def listen():
    i=1
    while i <= 10:
        print ("listen kjører")
        my_socket.listen()
        conn, addr = my_socket.accept()
        broadcast_list.append(conn)
        print(f"kjører")
        
        

    i = 1
    while i <= 10:
        print ("msg kjører")
        conn = listen()
        message = conn.recv(1024).decode()
        if message:
            print(f"Received message: " + message)
            broadcast(message)
        
         

def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")


listen_thread = threading.Thread(target=listen)

listen_thread.start()