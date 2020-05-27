def table(positionsList):
    print("\n\t   Tic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| {} || {} || {} ||".format(positionsList[0], positionsList[1], positionsList[2]))
    print("\t|| {} || {} || {} ||".format(positionsList[3], positionsList[4], positionsList[5]))
    print("\t|| {} || {} || {} ||".format(positionsList[6], positionsList[7], positionsList[8]))
    print("\t~~~~~~~~~~~~~~~~~")

def playerMove(playerLetter, positionsList):
    while True:
        playerPos = int(input("{}: Where would you like to place your piece (1-9): ".format(playerLetter)))
        if playerPos > 0 and playerPos < 10:
            if positionsList[playerPos - 1] == "_":
                return playerPos
            else:
                print("That position is already chosen. Try another spot.")
        else:
            print("That is not a right option. Try a number between (1-9).")

def placePlayerTable(playerLetter, playerPos, positionsList):
    positionsList[playerPos - 1] = playerLetter

def winner(pLet, posList):
    return ((posList[0] == pLet and posList[1] == pLet and posList[2] == pLet) or
            (posList[3] == pLet and posList[4] == pLet and posList[5] == pLet) or
            (posList[6] == pLet and posList[7] == pLet and posList[8] == pLet) or
            (posList[0] == pLet and posList[3] == pLet and posList[6] == pLet) or
            (posList[1] == pLet and posList[4] == pLet and posList[7] == pLet) or
            (posList[2] == pLet and posList[5] == pLet and posList[8] == pLet) or
            (posList[0] == pLet and posList[4] == pLet and posList[8] == pLet) or
            (posList[2] == pLet and posList[4] == pLet and posList[6] == pLet))

listGame = ["_"]*9
exampleTab = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player1 = "X"
player2 = "O"
table(exampleTab)
table(listGame)

while True:
    #player 1
    move = playerMove(player1, listGame)
    placePlayerTable(player1, move, listGame)
    table(exampleTab)
    table(listGame)
    if winner(player1, listGame):
        print("Player 1 wins!")
        break
    elif "_" not in listGame:
        print("Was a tie!")
        break
    #player 2
    move = playerMove(player2, listGame)
    placePlayerTable(player2, move, listGame)
    table(exampleTab)
    table(listGame)
    if winner(player2, listGame):
        print("Player 2 wins!")
        break