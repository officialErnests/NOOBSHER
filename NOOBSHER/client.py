import socket
import os
from time import localtime, strftime
from datetime import datetime
class client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

        while True:
            input()
            try:
                fi = open("data_folder/really_cool.txt", 'r')
                data = fi.read()
                if not data:
                    break
                while data:
                    self.socket.send(str(data).encode())
                    data = fi.read()
                fi.close()
            except IOError:
                print("invalid file")