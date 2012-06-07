'''Main function'''

__author__ = 'Yakovlev.Nikolay'
__date__ = '05.06.2012'


import ConnectionCreater


import socket

Host = "localhost"
Port = 8021

NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
NewSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
NewSocket.bind((Host, Port))
NewSocket.listen(5)
while True:
    User, Address = NewSocket.accept()
    ConnectionCreater.Connection(User, Address).start()

