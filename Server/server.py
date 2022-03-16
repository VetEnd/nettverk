from email import message
from math import degrees
from select import select
import socket, time
import sys
from _thread import *

#Host = "127.0.0.1"
#Port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.bind((Host, Port))
s.bind(('127.0.0.1', 5000))
print ("Bind success")

s.listen(10)

list_clients= []

def client_thread(conn, addr) :
    

    while True:
        try:
            message = s.recv(2048)
            if message:
                print ("<"+ addr[0] +">" + message)

                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for clients in list_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                remove (clients)

def remove(connection):
    if connection in list_clients:
            list_clients.remove(connection)

while True:
    conn, addr = s.accept()
    list_clients.append(conn)
    print (addr[0] + " connected")

    start_new_thread(client_thread, (conn,addr))

conn.close()
s.close()

  #  print ("hei")

   # data, addr = s.accept()

   # print("Connection from ", addr)

   # msg_send = "Hello! You are connected to the server!".encode('utf-8')
   # data.send(msg_send)     

   # while True:
    #    some_msg = data.recv(1024).decode('utf-8')
    #    print("message from client: " + some_msg)

    #    if some_msg == "bye":
    #        break

    #    response_msg = input("Write something to the client: ")
    #    msg_send = response_msg.encode('utf-8')
    #    data.send(msg_send)
    #    print("Client is responding")

    #msg_send = "Bye recived, connection ended.".encode('utf-8')