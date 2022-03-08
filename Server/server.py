import socket

Host = "127.0.0.1"
Port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print (f"Connected by {addr}")
        while True:
            msg = b"Dette funker"
            conn.send(msg)
        