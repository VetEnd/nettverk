#client.py
from asyncio.windows_events import NULL
import socket
import threading
nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 5000
my_socket.connect((host, port))

def recv_thread():
     message = my_socket.recv(1024).decode()
     print(message)

thread_receive = threading.Thread(target=recv_thread)




while True: 
        message_to_send = input()
        my_socket.send(message_to_send.encode())
        thread_receive.start()
    
           
           
     

