def getComponent(matrix, color):
    aux = []
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        aux.append(matrix[i][j][color])
    return aux

def setComponent(matrix, expHist, color):
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        matrix[i][j][color] = expHist[0]
        expHist.pop(0)
    return matrix

def histExp(hist, rMin, rMax):
    expandedHist = []
    for i in hist:
        expandedHist.append(round(((i-rMin)/(rMax-rMin))*255))
    return expandedHist
