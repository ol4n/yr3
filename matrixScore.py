#Name: Olan Kelleher
#Student ID: 121472242
#Programme: CS1117
########################## Question 1 ############################################
def calculate_score (board):
    # Dictionary of symbols with their associated value
    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
    # Create an empty list to append the scores of each row to
    rowTotals = []
    # Create an empty list to append the scores of each column to
    colTotals = []
    '''Calculate the score per row and append it to the rowTotals list'''
    #Your code goes here
    # Gets each individual row in the matrix - board
    for row in board:
        # Create an empty list to append the value of each symbol to
        # Needs to be new empty list each time so in outer for loop
        singleRow = []
        # Gets each symbol in the individual row
        for symbol in row:
        # Variable val goes to dictionary and gets the value of the symbol during that iteration
            val = symbols[symbol]
            # Appends the value in val to the list for singleRow
            singleRow.append(val)
            # If the sum of singleRow is less than 0 (negative)
            # Sum takes all values in a list and adds them together
            if sum(singleRow) < 0:
                # Appends 0 to the rowTotals list
                rowTotals.append(0)
                # Otherwise
            else:
                # Get the sum of the values of singleRow and append to rowTotals
                rowTotals.append(sum(singleRow))
        '''Calculate the score per column and append it to the colTotals list'''
        #Your code goes here
        # For each column in the range of the length of a single list in the matrix
        # Range starts at 0, ends at the value of the length of the list but thats not included
        for col in range(len(board[0])):
            # Create an empty list to append each symbol from the column its iterating over
            singleCol = []
            # For each row in the range of the length of the matrix - board
            # Stays on each column and loops through the row e.g. (col 0, row 0), (col 0,row 1)...
            for row in range(len(board)):
                # The symbol is found by getting the index of the certain row and column its iterating over
                symbol = board[row][col]
                # Val goes to dictionary gets the value of the symbol and stores it in the variable
                val = symbols[symbol]
                # Appends the value in val to a list with all values in that column
                singleCol.append(val)
                # If the sum of all the values in singleCol is less than 0 (negative)
                if sum(singleCol) < 0:
                    # It appends 0 to the colTotals list
                    colTotals.append(0)
                # Otherwise
                else:
                    # Append the sum of all the values of a singleCol
                    colTotals.append(sum(singleCol))
                # Returns two lists - rowTotals and colTotals
                # The two lists contain the total value of the symbols in each row and in each column,
                # 0 if its a negative number
    return rowTotals, colTotals

rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X","O"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!",
"!!!"],
["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#",
"#"],
["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)

########################## Question 2 ############################################
def identifyPivot (L):
    #Your code goes here
    # Create two empty lists to compare the values to the left and to the right ofthe pivot
    leftList = []
    rightList = []
    # Num stores the first number of the list
    # Its the first number to be compared as it is impossible for it to be the pivot
    num = L[0]
    # Appends num to leftList to be compared
    leftList.append(num)
    # rightList becomes a copy of L
    rightList = L[:]
    # Removes num from rightList as it is to the left of any possible pivot
    # Remove - remove takes a value in its parameter and removes the first occurrence of the
    #value from the list
    rightList.remove(num)
    # i is to track the index of the pivot
    # i is set to one from the start as it will go through list L and needs to skip over first
    # value as it is impossible for that to be the pivot
    i = 1
    # while the number i is less than the length of the list L
    while i < len(L):
        # Pivot stores the number at the index of i in list L as the possible pivot point of the list
        pivot = L[i]
        # Remove pivot from rightList as it is not to be added with the values
        rightList.remove(pivot)
        # Now have two sub lists of L, one to the left of the potential pivot and one to the right
        # If the sum leftList does not equal to the sum of rightList
        if sum(leftList) != sum(rightList):
        # Append the number in pivot to the leftList as it is now no longer a potential pivot and
        #needs to be summed with the rest of the values to the left now
            leftList.append(pivot)
        # Increment the counter by 1
            i += 1
        # Otherwise if the sum of leftList and sum of rightList are equal
        elif sum(leftList) == sum(rightList):
        # Return the number stored in pivot
            return pivot
    # If the loop finishes e.g. it has got to the end of the list without finding a pivot, the pivot
    # becomes -1
    pivot = -1
    # returns pivot of -1
    return pivot
print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0
