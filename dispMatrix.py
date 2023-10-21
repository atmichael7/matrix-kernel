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