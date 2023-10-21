matrix = [[0, 0, 1, 1, 1],
          [0, 0, 1, 1, 1],
          [0, 0, 1, 1, 1]]

result = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

x_dir_outline = [[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]]

x_dir_kernel = [[1, 0, 1],
                [1, 0, 1],
                [1, 0, 1]]

y_dir_kernel = [[1, 1, 1],
                [0, 0, 0],
                [1, 1, 1]]


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


def reduceMatrix(inputMatrix):
    inputHeight = len(inputMatrix)
    inputLength = len(inputMatrix[0])

    tempMatrix = [ [0 for y in range(inputLength-2)] for x in range(inputHeight-2)]

    for currRow in range(1, inputHeight-1):
        for currIndex in range(1, inputLength-1):
            tempMatrix[currRow-1][currIndex-1] = inputMatrix[currRow][currIndex]

    return tempMatrix


def makeEmptyMatrix(inputMatrix):
    # the matrix is required to be uniform in length
    inputHeight = len(inputMatrix)
    inputLength = len(inputMatrix[0])

    # build empty matrix of same size + 2 on each x and y for buffer
    tempMatrix = [ [0 for y in range(inputLength)] for x in range(inputHeight) ]

    return tempMatrix


def goThruMatrix(dimensions, matrix):
    if dimensions == 1:
        print("Row 1: ", end="")
        for curr_index in range(len(matrix)):
            print(matrix[curr_index], end=", ")
    
    elif dimensions == 2:
        for curr_row in range(len(matrix)): # goes through each row index
            amount_of_columns = len(matrix[curr_row])
            print("Row {}: ".format(curr_row+1), end="")
            
            for curr_col in range(amount_of_columns):
                print(matrix[curr_row][curr_col], end=", ")
                
            print("")
                
    else: # dimensions == 3 
        for curr_row in range(len(matrix)): # goes through each row 
            amount_of_columns = len(matrix[curr_row]) # gather how many entries are in the current row
            print("Row {}: ".format(curr_row))
            
            for curr_col in range(amount_of_columns):
                amount_of_entries = len(matrix[curr_row][curr_col])
                print("Entry {}: ".format(curr_col+1)) # wording here is ambiguous, this is listing each column, but each column has sub entries 
                
                for curr_entry in range(amount_of_entries):
                    print(matrix[curr_row][curr_col][curr_entry], end=", ")
                    
                print("")
            
            print("")

    print("")
 

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
                    #print("Rc:{},iC:{}.. cI{} -> {} = {} + ({} * {})".format(rowCount, indexCount, currIndex, summation, summation, w_inputMatrix[currRow-rowCount][currIndex-indexCount], kernel[kernelRow][kernelIndex]))
                    #print("Current SUM --> {}".format(summation))
                    indexCount -= 1
                    #debug_ct += 1

                rowCount -= 1
            # summation is done with kernel cross reference
            outputMatrix[currRow][currIndex] = summation
            #print("Total sum: {}".format(summation))
    
    return(reduceMatrix(outputMatrix))

result = kernalApplication(x_dir_kernel, matrix)

goThruMatrix(2, result)
