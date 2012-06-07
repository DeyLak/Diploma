__author__ = 'Yakovlev.Nikolay'
__date__ = '07.06.2012'


import LinearFilter
import Matrix

from PIL import Image

kernel = [[-1, 1],]

ImageToOperate = Image.open("Z:\Diplom\\test2.png")
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