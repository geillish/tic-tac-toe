#########################################
def TicTacToe():
	board = [['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']]
	
	win_flag = False
	user_flag = False
	winner = ""
	player1_symbol = "z"
	
	player1_name = input("Hey player 1, what is your name?\n")
	print()
	player2_name = input("Hi player 2, what is your name?\n")
	print()
	
	while player1_symbol != "x" and player1_symbol != "o":
		player1_symbol = input(f"{player1_name} Are you x or o?\n").lower()
		if player1_symbol == "x":
			player2_symbol = "o"
		else:
			player2_symbol = "x"
		
	print()
	
	print(f"{player1_name} you are {player1_symbol}")
	print(f"{player2_name} you are {player2_symbol}")
	
	while not win_flag:
		print()
		
		#print the board
		print(board[0])
		print(board[1])
		print(board[2])
		
		#player 1 turn
		while user_flag == False:
			print()
			user_row = int(input(f"{player1_name} please give me a row: \n"))-1
			user_col = int(input(f"{player1_name} please give me a column: \n"))-1
			if board[user_row][user_col] == "-":
				board = player_move(user_row,user_col,player1_symbol,board)
				user_flag = True
			else:
				print()
				print("That space is occupado - try again.")
		user_flag = False
		print()
		
		win_flag = check3inRow(board, player1_symbol)
		if win_flag == True:
			print(f"You won {player1_name}!\n")
			break
		win_flag = check3inColumn(board, player1_symbol)
		if win_flag == True:
			print(f"You won {player1_name}!\n")
			break
		
		win_flag = check3inDiag(board, player1_symbol)
		if win_flag == True:
			print(f"You won {player1_name}!\n")
			break
		
		
		#print the board
		print(board[0])
		print(board[1])
		print(board[2])
		
		print()
		
		#player 2 turn
		while user_flag == False:
			print()
			user_row = int(input(f"{player2_name} please give me a row: \n"))-1
			user_col = int(input(f"{player2_name} please give me a column: \n"))-1
			if board[user_row][user_col] == "-":
				board = player_move(user_row,user_col,player2_symbol,board)
				user_flag = True
			else:
				print()
				print("That space is occupado - try again.")
		user_flag = False
		
		win_flag = check3inRow(board, player2_symbol)
		if win_flag == True:
			print(f"You won {player2_name}!\n")
			break
		win_flag = check3inColumn(board, player2_symbol)
		if win_flag == True:
			print(f"You won {player2_name}!\n")
			break
		win_flag = check3inDiag(board, player2_symbol)
		if win_flag == True:
			print(f"You won {player2_name}!\n")

	print()
	
	print(board[0])
	print(board[1])
	print(board[2])

#########################################
def player_move(row, col, symbol, board):
	change_row = board[row]
	change_row[col] = symbol
	board[row] = change_row
	return board


#########################################
def check3inRow(board, symbol):
  for row in range(0,2):
  	if board[row][0] == board[row][1] == board[row][2] == symbol:
  		return True


#########################################
def check3inColumn(board, symbol):
  for col in range(0,2):
  	if board[0][col] == board[1][col] == board[2][col] == symbol:
  		return True
  		

#########################################
def check3inDiag(board, symbol):
  for col in range(0,2):
  	if board[0][0] == board[1][1] == board[2][2] == symbol:
  		return True
  	elif board[0][2] == board[1][1] == board[2][0] == symbol:
  		return True


#########################################
TicTacToe()
