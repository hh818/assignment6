'''
Created on Mar 30, 2015

@author: ds-ga-1007
'''
import numpy as np

###########################
#Question 1
###########################
def getArrayRows(originalArray, row1, row2):
    '''get a new array containing the specified rows of the original array'''
    array1a = originalArray[[row1, row2]]
    return array1a

def getArrayCol(originalArray, col1):
    '''b. a new array containing the specified column of the original array'''
    array1b = originalArray[:, col1]
    return array1b

def getArrayRecSection(originalArray, row1, row2, col1, col2):
    '''c. a new array b/w [row1,col1] and [row2,col2]'''
    array1c = originalArray[row1:row2, col1:col2]
    return array1c

def getArrayBetween(originalArray, int1, int2):
    '''d. a new array of values b/w int1 and int2'''
    array1d = originalArray.copy().transpose()
    return array1d.ravel()[int1:int2]

###########################
#Question 2
###########################
def divideArrayByArray(array1, array2):
    '''divide each column of an array element wise with another array'''
    tempArray = array1.transpose()/array2
    result = tempArray.transpose()
    return result

###########################
#Question 3
###########################
def findClosest(array, value):
    '''return the columns in array that corresponds to the number closest to value in each row'''
    columns = (np.abs(array-value).argsort())[:, 0]
    return columns

###########################
#Question 4
###########################
def mandelbrotIteration(N_max, some_threshold, nx, ny):
    #construct grid
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    
    c = x[:,np.newaxis] + 1j*y[np.newaxis, :]
    
    z = c
    
    for v in range(N_max):
        z = z**2 + c

    mask = (abs(z) < some_threshold)
    
    return mask