
def makeEmptyMatrix(inputMatrix):
    # the matrix is required to be uniform in length
    inputHeight = len(inputMatrix)
    inputLength = len(inputMatrix[0])

    # build empty matrix of same size + 2 on each x and y for buffer
    tempMatrix = [ [0 for y in range(inputLength)] for x in range(inputHeight) ]

    return tempMatrix