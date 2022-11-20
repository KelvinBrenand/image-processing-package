from statistics import median
import numpy as np
def box(matrix): #Box m x n em RGB
    tot_sumR, tot_sumG, tot_sumB = 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tot_sumR += matrix[i][j][0]
            tot_sumG += matrix[i][j][1]
            tot_sumB += matrix[i][j][2]
    return [tot_sumR // (len(matrix)*len(matrix[0])), tot_sumG // (len(matrix)*len(matrix[0])), tot_sumB // (len(matrix)*len(matrix[0]))]

def mediana(matrix): #Median m x n in RGB
    RArray, GArray, BArray = [], [], []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            RArray.append(matrix[i][j][0])
            GArray.append(matrix[i][j][1])
            BArray.append(matrix[i][j][2])
    RArray.sort()
    GArray.sort()
    BArray.sort()
    return [round(median(RArray)), round(median(GArray)), round(median(BArray))]

def sobelV(matrix):#matrix must be np array. Sobel is 3x3
    matrixCopy = np.array(matrix.copy())
    
    #BANDA R
    matrixCopy[0][0][0] = -1*matrixCopy[0][0][0]
    matrixCopy[0][1][0] = 0
    matrixCopy[1][0][0] = -2*matrixCopy[1][0][0]
    matrixCopy[1][1][0] = 0
    matrixCopy[1][2][0] = 2*matrixCopy[1][2][0]
    matrixCopy[2][0][0] = -1*matrixCopy[2][0][0]
    matrixCopy[2][1][0] = 0
    
    #BANDA G
    matrixCopy[0][0][1] = -1*matrixCopy[0][0][1]
    matrixCopy[0][1][1] = 0
    matrixCopy[1][0][1] = -2*matrixCopy[1][0][1]
    matrixCopy[1][1][1] = 0
    matrixCopy[1][2][1] = 2*matrixCopy[1][2][1]
    matrixCopy[2][0][1] = -1*matrixCopy[2][0][1]
    matrixCopy[2][1][1] = 0
    
    #BANDA B
    matrixCopy[0][0][2] = -1*matrixCopy[0][0][2]
    matrixCopy[0][1][2] = 0
    matrixCopy[1][0][2] = -2*matrixCopy[1][0][2]
    matrixCopy[1][1][2] = 0
    matrixCopy[1][2][2] = 2*matrixCopy[1][2][2]
    matrixCopy[2][0][2] = -1*matrixCopy[2][0][2]
    matrixCopy[2][1][2] = 0
    return [np.sum(matrixCopy[:,:,0]),np.sum(matrixCopy[:,:,1]),np.sum(matrixCopy[:,:,2])]

def sobelH(matrix):#matrix must be np array. Sobel is 3x3
    matrixCopy = np.array(matrix.copy())
    
    #BANDA R
    matrixCopy[0][0][0] = -1*matrixCopy[0][0][0]
    matrixCopy[0][1][0] = -2*matrixCopy[0][1][0]
    matrixCopy[0][2][0] = -1*matrixCopy[0][2][0]
    matrixCopy[1][0][0] = 0
    matrixCopy[1][1][0] = 0
    matrixCopy[1][2][0] = 0
    matrixCopy[2][1][0] = 2*matrixCopy[2][1][0]
    
    #BANDA G
    matrixCopy[0][0][1] = -1*matrixCopy[0][0][1]
    matrixCopy[0][1][1] = -2*matrixCopy[0][1][1]
    matrixCopy[0][2][1] = -1*matrixCopy[0][2][1]
    matrixCopy[1][0][1] = 0
    matrixCopy[1][1][1] = 0
    matrixCopy[1][2][1] = 0
    matrixCopy[2][1][1] = 2*matrixCopy[2][1][1]
    
    #BANDA B
    matrixCopy[0][0][2] = -1*matrixCopy[0][0][2]
    matrixCopy[0][1][2] = -2*matrixCopy[0][1][2]
    matrixCopy[0][2][2] = -1*matrixCopy[0][2][2]
    matrixCopy[1][0][2] = 0
    matrixCopy[1][1][2] = 0
    matrixCopy[1][2][2] = 0
    matrixCopy[2][1][2] = 2*matrixCopy[2][1][2]
    return [np.sum(matrixCopy[:,:,0]),np.sum(matrixCopy[:,:,1]),np.sum(matrixCopy[:,:,2])]