board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
computer = computer2 = player = ' '
def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True 
    return False 

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter 
        printBoard(board)
        if checkWin():
            if letter == computer:
                print("Computer1 wins!")
                exit()
            elif letter == player:
                print("Player wins!")
                exit()
            else:
                print("Computer2 wins")
                exit()
        if checkDraw():
            print("Draw!")
            exit() 
        return 
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return    
def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 
def playerMove():
    position = int(input("Enter a position: "))
    insertLetter(player, position)
    return 
def compMove(mark1,mark2):
    bestScore = -2
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = mark1
            score = minimax(board,mark1,mark2,False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(mark1, bestMove)
    return
def minimax(board,mark1,mark2, isMaximizing):
    if checkWhichMarkWon(mark1):
        return 1 
    elif checkWhichMarkWon(mark2):
        return -1 
    elif checkDraw():
        return 0    
    if isMaximizing:
        bestScore = -2
        for key in board.keys():
            if board[key] == ' ':
                board[key] = mark1 
                score = minimax(board,mark1,mark2, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 2
        for key in board.keys():
            if board[key] == ' ':
                board[key] = mark2
                score = minimax(board,mark1,mark2, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore
def Value(mark,position):
    dem = 0
    if ((board[1] == board[2] or board[2] == ' ') and (board[1] == board[3] or board[3] == ' ') and board[1] == mark) or ((board[1] == board[2] or board[1] == ' ') and (board[2] == board[3] or board[3] == ' ') and board[2] == mark) or  ((board[1] == board[3] or board[1] == ' ') and (board[2] == board[3] or board[2] == ' ') and board[3] == mark):
        dem += 1
    if ((board[1] == board[4] or board[4] == ' ') and (board[1] == board[7] or board[7] == ' ') and board[1] == mark) or ((board[1] == board[4] or board[1] == ' ') and (board[4] == board[7] or board[7] == ' ') and board[4] == mark ) or ((board[1] == board[7] or board[1] == ' ') and (board[4] == board[7] or board[4] == ' ') and board[7] == mark):
        dem += 1
    if ((board[1] == board[5] or board[5] == ' ') and (board[1] == board[9] or board[9] == ' ') and board[1] == mark) or ((board[1] == board[5] or board[1] == ' ') and (board[5] == board[9] or board[9] == ' ') and board[5] == mark) or ((board[1] == board[9] or board[1] == ' ') and (board[5] == board[9] or board[5] == ' ') and board[9] == mark):
        dem += 1
    if ((board[2] == board[5] or board[5] == ' ') and (board[2] == board[8] or board[8] == ' ') and board[2] == mark) or ((board[2] == board[5] or board[2] == ' ') and (board[8] == board[5] or board[8] == ' ') and board[5] == mark) or ((board[2] == board[8] or board[2] == ' ') and (board[5] == board[8] or board[5] == ' ') and board[8] == mark):
        dem += 1
    if ((board[3] == board[6] or board[6] == ' ') and (board[9] == board[3] or board[9] == ' ') and board[3] == mark) or ((board[3] == board[6] or board[3] == ' ') and (board[6] == board[9] or board[9] == ' ') and board[6] == mark) or ((board[3] == board[9] or board[3] == ' ') and (board[6] == board[9] or board[6] == ' ') and board[9] == mark):
        dem += 1
    if ((board[3] == board[5] or board[5] == ' ') and (board[3] == board[7] or board[7] == ' ') and board[3] == mark) or ((board[7] == board[5] or board[7] == ' ') and (board[3] == board[5] or board[3] == ' ') and board[5] == mark) or ((board[7] == board[5] or board[5] == ' ') and (board[7] == board[3] or board[3] == ' ') and board[7] == mark):
        dem += 1
    if ((board[4] == board[5] or board[5] == ' ') and (board[4] == board[6] or board[6] == ' ') and board[4] == mark) or ((board[4] == board[5] or board[4] == ' ') and (board[5] == board[6] or board[6] == ' ') and board[5] == mark) or ((board[4] == board[6] or board[4] == ' ') and (board[5] == board[6] or board[5] == ' ') and board[6] == mark):
        dem += 1
    if ((board[7] == board[8] or board[8] == ' ') and (board[7] == board[9] or board[9] == ' ') and board[7] == mark) or ((board[7] == board[8] or board[7] == ' ') and (board[8] == board[9] or board[9] == ' ') and board[8] == mark) or ((board[7] == board[9] or board[7] == ' ') and (board[8] == board[9] or board[8] == ' ') and board[9] == mark):
        dem += 1
    return dem
def useHauristic():
    max = -1
    index = 0
    for i in board.keys():
        if board[i] != ' ':
            continue
        if board[i] == ' ':
            board[i] = computer2
            x = Value(computer2,i)
            board[i] = ' '
        if x > max:
            max = x
            index = i
    print(max)
    insertLetter(computer2,index)
x = int(input("Nhap lua chon: 1.Player Vs Com 2.Com(H) Vs Com(M) 3.Com(M) vs Com(H): "))
if x==1:
    player = 'X'
    computer = 'O'
    while not checkWin():
        playerMove()
        compMove(computer,player)
elif x==2:
    computer2 = 'X'
    computer = 'O'
    while not checkWin():
        useHauristic()
        compMove(computer,computer2)
else:
    computer = 'X'
    computer2 = 'O'
    while not checkWin():
        compMove(computer,computer2)
        useHauristic()
