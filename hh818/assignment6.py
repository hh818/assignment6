'''
Created on Mar 30, 2015

@author: ds-ga-1007
'''
if __name__ == "__main__":
    import numpy as np
    import assignment6Functions 
    import matplotlib.pyplot as plt
    
    #########################
    #Question 1
    #########################
    originalArray1 = (np.arange(1, 16).reshape(3,5)).transpose()
    print originalArray1
    
    #Q1. a.
    print assignment6Functions.getArrayRows(originalArray1, 1, 3)
    
    #Q1. b.
    print assignment6Functions.getArrayCol(originalArray1, 1)
    
    #Q1. c.
    print assignment6Functions.getArrayRecSection(originalArray1, 1, 4, 0, 3)
    
    #Q1. d.
    print assignment6Functions.getArrayBetween(originalArray1, 2, 11)
    
    #########################
    #Question 2
    #########################
    originalArray2 = np.arange(25).reshape(5 ,5)
    divideBy = np.array([1., 5, 10, 15, 20])
    print assignment6Functions.divideArrayByArray(originalArray2, divideBy)
    
    #########################
    #Question 3
    #########################
    originalArray3 = np.random.rand(10, 3)
    columnIndex = assignment6Functions.findClosest(originalArray3, 0.5)
    rowIndex = np.arange(10)
    print originalArray3[rowIndex, columnIndex]
    
    #########################
    #Question 4
    #########################
    N_max = 50
    some_threshold = 50.
    
    mask = assignment6Functions.mandelbrotIteration(N_max, some_threshold, 601, 401)
    
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')