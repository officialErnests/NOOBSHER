import socket
import os
from time import localtime, strftime
from datetime import datetime
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
        self.files = {}
        self.log = None
        self.temp_log = ""
        self.log_crash = False
        self.exited = False
        
        self.is_migration_needed = False
        self.print_server("SERVER", f"innitilized connection on {self.host}:{self.port} and awaiting {self.devices} devices to connect!", 1)
    def close(self):
        self.log.close()
    def print_server(self, module, message, prefix):
        t_time = datetime.now()
        match prefix:
            case 0:
                t_message = f"NOOBSHER-{self.version} // {self.name} -={t_time}=- // {module} : {message}"
            case 1:
                t_message = f"NOOBSHER-{self.version} !! {self.name} -={t_time}=- !! {module} : {message}"
            case 2:
                t_message = f"NOOBSHER-{self.version} XX {self.name} -={t_time}=- XX {module} : {message}"
            case 3:
                t_message = f"NOOBSHER-{self.version} [FATAL] {self.name} -={t_time}=- [FATAL] {module} : {message}"
        print(t_message)
        if self.log: 
            try:
                if self.temp_log:
                    self.log.write(self.temp_log)
                    self.temp_log = ""
                self.log.write("\n" + t_message)
            except:
                self.log.close()
                self.log = None
                self.log_crash = True
                self.print_server("PRINTER", "Failed to write to log file", 2)
        elif not self.log_crash: self.temp_log += "\n" + t_message
    def is_exited(self, name) -> bool:
        if self.exited: 
            self.print_server(name, "EXITED", 3)
            return False
    def init_dir(self) -> bool:
        function_system = "FILE SYSTEM INIT"
        if self.is_exited(function_system): return False

        #Creates folder structure
        try: 
            self.init_dir_folders(function_system)
        except:
            self.print_server(function_system, "File system failed to initilize", 3)
            self.exit()
            return False
        
        try:
            self.init_dir_logs(function_system)
        except:
            self.print_server(function_system, f"log file failed to create nor find", 2)
        
        created_file = True
        found_file = True

        # try:
        #     self.init_dir_files
        # except:
        
        self.print_server(function_system, "directories has been inited", 0)
        return True
    def init_dir_folders(self, function_system):
        self.files = {}
        function_system += " >> FOLDER INIT"
        if self.is_exited(function_system): return False
        main_dir_checker = ""
        found_dir = True
        for main_dir_iter in self.directory.split("/"):
            if (not os.path.isdir(main_dir_iter)):
                found_dir = False
                os.mkdir(main_dir_iter)
                self.print_server(function_system, f"innitilized root folder, {main_dir_iter}, as it wasn't found", 0)
            main_dir_checker += main_dir_iter
        if found_dir:
            self.print_server(function_system, f"found root folder, {self.directory}!", 1)
        else:
            self.print_server(function_system, f"created root folder, {self.directory}!", 0)

        found_dir = True
        if (not os.path.isdir(self.directory)):
            self.print_server(function_system, f"innitilizing folder structure in {self.directory}", 1)
            os.mkdir(self.directory + "/server_main")
            self.files["main"] = self.directory + "/server_main"
            os.mkdir(self.files["main"] + "/server_info")
            os.mkdir(self.files["main"] + "/seerver_main")
            os.mkdir(self.files["main"] + "/server_backups")
            os.mkdir(self.files["main"] + "/server_session")
            self.files["meta"] = self.files["main"] + "/server_info"
            self.files["server"] = self.files["main"] + "/server_main"
            self.files["backups"] = self.files["main"] + "/server_backups"
            self.files["sessions"] = self.files["main"] + "/server_session"
            os.mkdir(self.files["meta"] + "/server_logs")
            self.files["logs"] = self.files["meta"] + "/server_logs"
        else:
            self.files["main"] = self.directory + "/server_main"
            if (not os.path.isdir(self.files["main"] + "/server_info")): os.mkdir(self.files["main"] + "/server_info"); found_dir = False
            if (not os.path.isdir(self.files["main"] + "/seerver_main")): os.mkdir(self.files["main"] + "/seerver_main"); found_dir = False
            if (not os.path.isdir(self.files["main"] + "/server_backups")): os.mkdir(self.files["main"] + "/server_backups"); found_dir = False
            if (not os.path.isdir(self.files["main"] + "/server_session")): os.mkdir(self.files["main"] + "/server_session"); found_dir = False
            self.files["meta"] = self.files["main"] + "/server_info"
            self.files["server"] = self.files["main"] + "/server_main"
            self.files["backups"] = self.files["main"] + "/server_backups"
            self.files["sessions"] = self.files["main"] + "/server_session"
            if (not os.path.isdir(self.files["meta"] + "/server_logs")): os.mkdir(self.files["meta"] + "/server_logs"); found_dir = False
            self.files["logs"] = self.files["meta"] + "/server_logs"
        if not found_dir:
            self.print_server(function_system, f"repaired folder structure in {self.directory}", 1)
        else:
            self.print_server(function_system, f"using folder structure in {self.directory}", 0)
    def init_dir_logs(self, function_system):
        if self.is_exited(function_system): return False
        log_file_name = self.files["logs"] + "/log_" + strftime("%y-%m-%d_%H-%M-%S", localtime()) + ".txt"
        function_system += " >> LOGS INIT"
        if (not os.path.exists(log_file_name)):
            self.log = open(log_file_name, "x")
            self.print_server(function_system, f"created new log file at {log_file_name}", 0)
        else:
            self.log = open(log_file_name, "a")
            self.print_server(function_system, f"log file already existed at {log_file_name}", 1)
    def init_dir_files(self, function_system):
        if self.is_exited(function_system): return False
        function_system += " >> FILES INIT"

        file_created = True
        file_found = True
        file_name = self.files["logs"] + "/config.txt"
        if not os.path.exists(file_name):
            file_found = False
            self.print_server(function_system, f"config file found, loading data", 1)
            with open(file_name, "x") as f: 
                for line in f:
                    self.init_dir_files_check_conf(function_system, line)

        else: 
            file_created = False

        return (file_created, file_found)
    def init_dir_files_check_conf(self, function_system, text:str) -> bool:
        if self.is_exited(function_system): return False
        splits = text.split("//")
        match splits[0].strip():
            case "version":
                if (splits[1] == self.version):
                    self.print_server(function_system, f"Version great {self.version}", 0)
                else:
                    self.print_server(function_system, f"Version not compatable! (server:{splits[1]} programm:{self.version}) please use migration, otherwise some settings may not save or there might be miscompatabilities...", 4)
                    self.is_migration_needed = True

        return False
    def isMigrationNeeded(self) -> bool:
        function_system = "Migration"
        if self.is_exited(function_system): return False
        return self.is_migration_needed
    def exit(self):
        if self.log: 
            self.print_server("EXITER", "closing log file", 0)
            self.log.close()
        else:
            self.print_server("EXITER", "no log file to close", 0)
        self.exited = True


    # def later():


    #     for i in range(self.devices):
    #         conn = self.socket.accept()
    #         self.connections.append(conn)
    #         print ("Connected with client", i+1)
        
    #     fileno = 0
    #     idx = 0
    #     for conn in self.connections:
    #         idx += 1
    #         data = conn[0].recv(1024).decode()
    #         if not data:
    #             continue
    #         filename = 'output'+str(fileno)+'.txt'
    #         fileno = fileno + 1
    #         fo = open(filename, 'w')
    #         while data:
    #             if not data:
    #                 break
    #             else:
    #                 fo.write(data)
    #                 data = conn[0].recv(1024).decode()
    #         print("File transfer form {idx}, with file {filename}")
    #         fo.close()
    #     for conn in self.connections:
    #         conn[0].close()


    def test(self):
        print("Hello world!")

