import socket
import os
class server:
    def __init__(self, host, port, devices, directory):
        self.host = host
        self.port = port
        self.devices = devices
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.devices)
        self.connections = []
        self.directory = directory
        self.name = "SERVER"
        self.version = "0.1v"
        print("NOOBSHER // SERVER // innitilized connection on {self.host}:{self.port} and awaiting {self.devices} devices to connect!")
    def print_server(self, module, message, prefix):
        match prefix:
            case 0:
                print("NOOBSHER{self.version} // {self.name} // {module} : {message}")
    def init_dir(self):
        created_dir = False
        found_dir = False
        if (not os.path.isdir(self.directory + "/server_main")):
            mkdir(self.directory + "/server_main")
            mkdir(self.directory + "/server_main/server_info")
            mkdir(self.directory + "/server_main/server_backups")
            mkdir(self.directory + "/server_main/seerver_main")
        else:
            if (not os.path.isdir(self.directory + "/server_main/server_info")):
                mkdir(self.directory + "/server_main/server_info")
            if (not os.path.isdir(self.directory + "/server_main/server_backups")):
                mkdir(self.directory + "/server_main/server_backups")
            if (not os.path.isdir(self.directory + "/server_main/seerver_main")):
                mkdir(self.directory + "/server_main/seerver_main")
        if (not os.path.isdir(self.directory + "/server_sessions")):
            mkdir(self.directory + "/server_session")
        if created_dir:
            self.print_server("FILE SYSTEM INNIT", "innitilized folder structure in {self.directory}", 0)
        elif found_dir:
            self.print_server("FILE SYSTEM INNIT", "repaired folder structure in {self.directory}", 0)
        else:
            self.print_server("FILE SYSTEM INNIT", "using folder structure in {self.directory}", 0)
        
    def later():


        for i in range(self.devices):
            conn = self.socket.accept()
            self.connections.append(conn)
            print ("Connected with client", i+1)
        
        fileno = 0
        idx = 0
        for conn in self.connections:
            idx += 1
            data = conn[0].recv(1024).decode()
            if not data:
                continue
            filename = 'output'+str(fileno)+'.txt'
            fileno = fileno + 1
            fo = open(filename, 'w')
            while data:
                if not data:
                    break
                else:
                    fo.write(data)
                    data = conn[0].recv(1024).decode()
            print("File transfer form {idx}, with file {filename}")
            fo.close()
        for conn in self.connections:
            conn[0].close()


    def test(self):
        print("Hello world!")


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