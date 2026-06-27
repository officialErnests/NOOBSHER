from NOOBSHER import server as nb_server
server = nb_server("127.0.0.1", 8080, 2, "test/server")
server.init_dir()
server.test()
