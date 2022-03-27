#client.py
from cgi import print_arguments
from posixpath import split
from queue import Queue
import threading
import socket
from time import sleep
import re
name = input("Choose your nickname : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_q = Queue()
port_q = Queue()

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
my_socket.connect((host, port))

conned = my_socket.recv(1024).decode()
print(conned)

name_send = my_socket.send(name.encode())
#This part of the code will just be definitions of the chat bots


# funker
def send_msg():
    while True: 
        message_to_send = input()
       
        my_socket.send(message_to_send.encode())
        if message_to_send == "exit":
            my_socket.close()

test2 = Queue()

def recv1():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        test = re.findall(r'\w+', message)
        res = [test[-1]]
        test2.put(res)

if name == "Stian":
    message = "Hei, mitt navn er Stian, jeg blir gjerne med på " + verb
    my_socket.send(message.encode())
    sleep(5)
    message = "Ok, du er teit"
    my_socket.send(message.encode())

def thread_starter():
    recv = threading.Thread(target=recv1)
    recv.start()

    send = threading.Thread(target=send_msg)           
    send.start()
    
thread_starter()
