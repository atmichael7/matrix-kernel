def rebuildMatrix(inputMatrix):
    # the matrix is required to be uniform in length
    inputHeight = len(inputMatrix)
    inputLength = len(inputMatrix[0])

    # build empty matrix of same size + 2 on each x and y for buffer
    tempMatrix = [ [0 for y in range(inputLength+2)] for x in range(inputHeight+2) ]

    # build left and right buffer zones & copy original data
    for currRow in range(inputHeight):
        for currIndex in range(inputLength):
            tempMatrix[currRow+1][currIndex+1] = inputMatrix[currRow][currIndex]

    return tempMatrix