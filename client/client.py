import socket #Imports the libary for socket'
import sys

Host = sys.argv[1]
temp = sys.argv[2]
Port = int(temp)

Bot_name = sys.argv [3]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect ((Host, Port))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print (f"Receviced {data!r}")