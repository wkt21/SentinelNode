#!/usr/bin/env python3
import socket

HOST = "0.0.0.0"
PORT = 22

while True:
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    conn.send(b"Fake SSH Service\n")
    conn.close()
