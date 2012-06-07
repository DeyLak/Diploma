'''Operations with linear filter: applying'''

__author__ = 'Yakovlev.Nikolay'
__date__ = '05.06.2012'
#import random


def ApplyLinearFilter(argMatrixInput, argMarixKernel):

# Defines empty output Matrix.
    MatrixOutput = [[0 for i in range(len(argMatrixInput[0]) - len(argMarixKernel[0]) + 1)] for j in range(len(argMatrixInput) - len(argMarixKernel) + 1)]

# Convolute
    for y in range(len(argMatrixInput) - len(argMarixKernel) + 1):
        for x in range(len(argMatrixInput[0]) - len(argMarixKernel[0]) + 1):
            Sum = 0
            MaxValueForNormalization = 0.0 # Keep max value for later normalization
            for i in range(len(argMarixKernel)): # Rows of kernel
                for j in range(len(argMarixKernel[0])): # Columns of kernel
                    Sum += argMatrixInput[y + i][x + j] * argMarixKernel[i][j]
                    if Sum > MaxValueForNormalization:
                        MaxValueForNormalization = float(Sum)
            MatrixOutput[y][x] = Sum

    return MatrixOutput