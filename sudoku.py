# Algorithm

# Starting with an incomplete board:
#     Find some empty space
#     Attempt to place the digits 1-9 in that space
#     Check if that digit is valid in the current spot based on the current board
#      a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
#     b. If it is not valid, reset the square you just filled and go back to the previous step.
#     Once the board is full by the definition of this algorithm we have found a solution.

#here the zeros reprensent empty spaces
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#backtracking function. we call this function from inside of itself (recursively)
def solve(bo): # this is the base case of our recursion
    find = find_empty(bo)
    if not find:
        return True# this actually means we've found the solution
    else:
        row, col = find

    for i in range(1,10):#we're going to insert values 1-9 to find the solution
        if valid(bo, i, (row, col)):# we're going to check if the solution is valid
            bo[row][col] = i#if so then this plugs in the valid value/number into our board

            if solve(bo):#we recursively try to finish the solution by calling solve on the new board with the newly added value
                return True

            bo[row][col] = 0 #if the value isn't valid we need to backtrack find a new one until we find the solution

    return False

# check if the board is valid
def valid(bo, num, pos): #3 parameters
    # Check row (we loop through every single column in the given row)
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: #first we check each element in the row to see if it's the number that was inserted, we also say to ignore the actual position we're inserting the number into
            return False

    # Check column
    for i in range(len(bo)):# we loop through all rows 0-8 and check if our current x value is equal to the same number we inserted
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box (3x3 box)
    box_x = pos[1] // 3 # we need to use integer division to check which box we're in
    box_y = pos[0] // 3#these values will give us 0, 1 or 2 (upper row (0), middle row(1), last row(2))

    for i in range(box_y*3, box_y*3 + 3): #loop through all 9 elements in the box. We need to mulitply the box number by three to get the index
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False# if a duplicate number has been found

    return True


#print board out to see it visually
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#here we find the empty spaces
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)#board before solution
solve(board)
print("___________________")
print_board(board)#board with the solution

#backtracking is very efficient. Better than a naive solution that is very slow