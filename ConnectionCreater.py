__author__ = 'Yakovlev.Nikolay'
__date__ = '06.06.2012'

import threading
import LinearFilter
import Matrix
import cPickle

from PIL import Image

kernel = [[-1, 1],]

class Connection(threading.Thread):
    def __init__(self, User, Address):
        self.User = User
        self.Address = Address
        threading.Thread.__init__(self)

    def run (self):
        while True:
            Buffer = self.User.recv(1024)

            FileToLoad = open(Buffer, "r")

            NewLoadedObject = cPickle.Unpickler(FileToLoad)

            ImageToOperate = NewLoadedObject.load()
            ImageToOperate = Image.open(Buffer)
            ImageToOperate.show()
            ImageToOperate = ImageToOperate.convert("L")
            ImageToOperate.show()

            PixelsMatrix = Matrix.ImageToMatrix(ImageToOperate)

            Result = LinearFilter.ApplyLinearFilter(PixelsMatrix, kernel)

            print "Input"
            Matrix.OutputMatrix(PixelsMatrix)
            print ""
            print ""
            print "Kernel"
            Matrix.OutputMatrix(kernel)
            print ""
            print ""
            print "Output"
            Matrix.OutputMatrix(Result)
        self.sock.close()
