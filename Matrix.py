'''Operationswith matricies: outputing, converting frow image to matrix'''

__author__ = 'Yakovlev.Nikolay'
__date__ = '05.06.2012'

# Prints a Matrix
def OutputMatrix(argMatrix):
    for Rows in range(len(argMatrix)):
        s = ""
        for Columns in range(len(argMatrix[0])):
            s += "%4d " %(argMatrix[Rows][Columns])
        print s

def ImageToMatrix(argImage):
# Defines empty output Matrix.
    MatrixOutput = [[0 for i in range(argImage.size[0])] for j in range(argImage.size[1])]

    for x in xrange(argImage.size[0]):
        for y in xrange(argImage.size[1]):
            MatrixOutput[x][y] = argImage.load()[x,y]
    return MatrixOutput