def isValid(x, y, board,n):
#check if (x,y) lies on the board
	if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
		return True
	return False

#function to print the board if solution exists
def printSolution(n, board):

	for i in range(n):
		for j in range(n):
			print(board[i][j]+1, end=' ')
		print()


def solve(n,r,c):

	# Board matrix
	board = [[-1 for i in range(n)]for i in range(n)]

	# xmove and ymove define next move of Knight.
	# xmove is for next value of x coordinate
	xmove = [2, 1, -1, -2, -2, -1, 1, 2]
	ymove = [1, 2, 2, 1, -1, -2, -2, -1]

	# Initialising the first block i.e the block where our knight starts
	board[r-1][c-1] = 0

	pos = 1

	# Check if solution exists or not
	if(not solveUtil(n, board, r-1, c-1, xmove, ymove, pos)):
		print("Solution does not exist :(")
		stk=2
		stk=int(stk)
		return stk
	else:
    
		printSolution(n, board)
		return  board


#recursive function to implement backtracking
def solveUtil(n, board, xcurr, ycurr, xmove, ymove, pos):
	if(pos == n*n):
		return True

	# try all next moves from the current  x, y
	for i in range(8):
		xnew = xcurr + xmove[i]
		ynew = ycurr + ymove[i]
		if(isValid(xnew, ynew, board,n)):
			board[xnew][ynew] = pos
			if(solveUtil(n, board, xnew, ynew, xmove, ymove, pos+1)): 
				return True

			#backtrack
			board[xnew][ynew] = -1
	return False

#driver function
if __name__ == "__main__":
    solve(n,r,c)  
