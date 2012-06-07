__author__ = 'Yakovlev.Nikolay'
__date__ = '07.06.2012'

import socket
import  time
import cPickle

from PIL import Image

Host = "localhost"
Port = 8021

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))
while True:
    ImagePath = raw_input("Please, enter the image address, or 'exit': ")
    if ImagePath == "exit":
        break
    ImageToOperate = Image.open(ImagePath)
    ImageToOperate.show()

    FileToSaveImage = open(str(time.time()), "w")

    NewDumpObject = cPickle.Pickler(FileToSaveImage)
    NewDumpObject.dump(ImageToOperate)

    s.send(FileToSaveImage.name)
    #result = s.recv(1024)
    #print result
s.close()