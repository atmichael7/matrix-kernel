def reduceMatrix(inputMatrix):
    inputHeight = len(inputMatrix)
    inputLength = len(inputMatrix[0])

    tempMatrix = [ [0 for y in range(inputLength-2)] for x in range(inputHeight-2)]

    for currRow in range(1, inputHeight-1):
        for currIndex in range(1, inputLength-1):
            tempMatrix[currRow-1][currIndex-1] = inputMatrix[currRow][currIndex]

    return tempMatrix