# Display matrix file 
from dispMatrix import goThruMatrix # goThruMatrix(dimension, matrixName)

# Rebuild matrix that adds a buffer of zeros on the left, top, right, and bottom sides of array
from modifyMatrix import rebuildMatrix  # rebuildMatrix(inputMatrix)

# Reduces the modified matrix to get rid of buffer zones 
from reduceMatrix import reduceMatrix # reduceMatrix(inputMatrix)

# Makes an empty matrix that matches the size of the inputted 2d array
from makeEmptyMatrix import makeEmptyMatrix # makeEmptyMatrix(inputMatrix)


def kernalApplication(kernel, inputMatrix):
    kernelHeight = len(kernel)
    kernelLength = len(kernel[0])

    #debug_ct = 0

    w_inputMatrix = rebuildMatrix(inputMatrix)
    outputMatrix = makeEmptyMatrix(w_inputMatrix)

    inputHeight = len(w_inputMatrix)
    inputLength = len(w_inputMatrix[0])

    goThruMatrix(2, w_inputMatrix)
    goThruMatrix(2, outputMatrix)
    #print("Debug! ----> H{}, L{}".format(inputHeight, inputLength))

    # go through row of input matrix
    for currRow in range(1, inputHeight-1):
        # go through each index of the current row of the input matrix
        for currIndex in range(1, inputLength-1):
            # now need to do running summation
            # Set summation to zero since we will be starting here on each index for the input matrix
            summation = 0
            # the row count needs to be set to 1
            # this is because the row above will need to be considered in order to match the index of the kernel and its respective value
            # so the row count for the input index will be subtracted by the row count
            #   while the kernel will not need to be subtracted 
            rowCount = 1

            # when the row count is supposed to be 


            # loop to go through rows of the kernel
            for kernelRow in range(kernelHeight):
                indexCount = 1
                # loop that goes through each index of the kernel 
                for kernelIndex in range(kernelLength):
                    # add the current index of input matrix corresponding to the kernal index 
                    # this will be multiplied by the index of the kernel so if its zero it wont have an effect
                    summation = summation + ((w_inputMatrix[currRow-rowCount][currIndex-indexCount]) * (kernel[kernelRow][kernelIndex]))
                    #print("Rc:{},iC:{}.. cI{} -> {} = {} + ({} * {})".format(rowCount, indexCount, currIndex, summation, summation, 
                    # w_inputMatrix[currRow-rowCount][currIndex-indexCount], kernel[kernelRow][kernelIndex]))
                    #print("Current SUM --> {}".format(summation))
                    indexCount -= 1
                    #debug_ct += 1

                rowCount -= 1
            # summation is done with kernel cross reference
            outputMatrix[currRow][currIndex] = summation
            #print("Total sum: {}".format(summation))
    
    return(reduceMatrix(outputMatrix))