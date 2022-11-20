import numpy as np
from PIL import Image
from statistics import median
from image_processing_KB.utils import Yiq2Rgb_helping_methods as hm
from image_processing_KB.utils import histogram_stretching as hs
from image_processing_KB.utils import correlation as corr
from image_processing_KB.utils import hsb, kernels

def rgb2Yiq(image):
    imageCopy = np.zeros(image.shape)
    for i in range(len(image)):
        for j in range(len(image[0])):
            y =  (0.299*image[i][j][0])+(0.587*image[i][j][1])+(0.114*image[i][j][2])
            ii = (0.596*image[i][j][0])-(0.274*image[i][j][1])-(0.322*image[i][j][2])
            q =  (0.211*image[i][j][0])-(0.523*image[i][j][1])+(0.312*image[i][j][2])
            imageCopy[i][j][0], imageCopy[i][j][1], imageCopy[i][j][2] = round(y,2), round(ii,2), round(q,2)
    return imageCopy

def yiq2Rgb(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            r = image[i][j][0]+(0.956*image[i][j][1])+(0.621*image[i][j][2])
            g = image[i][j][0]-(0.272*image[i][j][1])-(0.647*image[i][j][2])
            b = image[i][j][0]-(1.106*image[i][j][1])+(1.703*image[i][j][2])
            image[i][j][0], image[i][j][1], image[i][j][2] = hm.__ajustYiq2Rgb(round(r)), hm.__ajustYiq2Rgb(round(g)), hm.__ajustYiq2Rgb(round(b))
    return image.astype(int)

def rgbNegative(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
          for k in range(len(image[0][0])):
            image[i][j][k] =  255-image[i][j][k]
    return image

def yNegative(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
          for k in range(len(image[0][0])):
            image[i][j][0] =  255-image[i][j][0]
    return image

def correlation(imageArray, m, n, kernel, offset, zeroPadding):
    if m < 1 or n < 1: raise ValueError("Invalid m x n value")
    imageCopy = imageArray.copy()
    
    auxArr1 = [i for i in range(m)]
    auxArr2 = [i for i in range(n)]
    pivot = [round(median(auxArr1)),round(median(auxArr2))]

    if kernel == "sobelV" or kernel == "sobelH":
      m, n = 3, 3
      pivot = [1, 1]

    if zeroPadding:
        up = pivot[0]
        down = m-pivot[0]-1
        left = pivot[1]
        right = n-pivot[1]-1

        zerosRow = [[0, 0, 0] for _ in range(len(imageCopy[0]))]
        zerosColumn = [0, 0, 0] #pixel is always 1x3

        for _ in range(up): imageCopy = np.insert(imageCopy, 0, zerosRow, axis=0)
        for _ in range(down): imageCopy = np.insert(imageCopy, len(imageCopy), zerosRow, axis=0)
        for _ in range(left): imageCopy = np.insert(imageCopy, 0, zerosColumn, axis=1)
        for _ in range(right): imageCopy = np.insert(imageCopy, len(imageCopy[0]), zerosColumn, axis=1)
    else:
        if m > len(imageCopy) or n > len(imageCopy[0]): raise ValueError("Invalid m x n value")
    
    dividedRows = [corr.rowDivider(i,n) for i in imageCopy.tolist()]
    dividedColumns = corr.columnDivider(imageCopy, m)
    imageWindows = corr.windowMaker(dividedRows,dividedColumns)

    result = []
    if kernel == "box":
        for i in imageWindows:
            result.append(kernels.box(i))
    elif kernel == "mediana":
        for i in imageWindows:
            result.append(kernels.mediana(i))
    elif kernel == "sobelV":
        for i in imageWindows:
            result.append(kernels.sobelV(i))
    elif kernel == "sobelH":
        for i in imageWindows:
            result.append(kernels.sobelH(i))
    else:
        raise ValueError("Invalid kernel")

    result = list(corr.grouper(result,len(dividedRows[0]))) #Os kernels retornam uma lista 1D. Grouper converte isso para uma lista 2D (imagem)

    if kernel == "sobelV" or kernel == "sobelH":
        result = np.abs(result)
        histR = hs.getComponent(result,0)#red=0,green=1,blue=2
        histG = hs.getComponent(result,1)
        histB = hs.getComponent(result,2)

        expR = hs.histExp(histR, min(histR), max(histR))
        expG = hs.histExp(histG, min(histG), max(histG))
        expB = hs.histExp(histB, min(histB), max(histB))

        result = hs.setComponent(result, expR, 0)
        result = hs.setComponent(result, expG, 1)
        result = hs.setComponent(result, expB, 2)

    result = np.array(result)+offset
    result[result > 255] = 255
    result[result < 0] = 0
    return result

def rgb2hsb(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            image[i][j] = hsb.__rgb2hsbConverter(image[i][j][0], image[i][j][1], image[i][j][2])
    return image

def hsb2rgb(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            image[i][j] = hsb.__hsb2rgbConverter(image[i][j][0], image[i][j][1], image[i][j][2])
    return image

def setSaturation(image, sat_value=0.5):
    HSVimage = rgb2hsb(image) #Converts the input image to HSB
    imageSat = hs.getComponent(HSVimage,1) #Get the saturation value of all pixels
    imageSat = [i*sat_value for i in imageSat] #Changes the saturation. 0.6 = 60% of the original saturation
    HSVimage = hs.setComponent(HSVimage, imageSat, 1) #The HSB image pixels recieves the new S values
    HSVimage = hsb2rgb(HSVimage) #Converts back to RGB
    return HSVimage

def open(path):
    return np.array(Image.open(path))