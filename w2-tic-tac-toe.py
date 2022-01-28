#Assignment: Week 1, tic tac toe, Steven Buechele

def showGameboard(slotNum):
    print(slotNum[0] + '|' + slotNum[1] + '|' + slotNum[2])
    print('-+-+-')
    print(slotNum[3] + '|' + slotNum[4] + '|' + slotNum[5])
    print('-+-+-')
    print(slotNum[6] + '|' + slotNum[7] + '|' + slotNum[8])
    print('\n')

def gameBoard(slotNum, current):
    goodInput = False

    while goodInput == False:
        showGameboard(slotNum)
        #Ask current player to enter a number
        print('Player ' + current + ', select an available slot: ')
        numSelect = input()        

        match numSelect:
            case '1':
                if slotNum[0] == '1':
                    slotNum[0] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')

            case '2':
                if slotNum[1] == '2':
                    slotNum[1] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '3':
                if slotNum[2] == '3':
                    slotNum[2] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '4':
                if slotNum[3] == '4':
                    slotNum[3] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '5':
                if slotNum[4] == '5':
                    slotNum[4] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '6':
                if slotNum[5] == '6':
                    slotNum[5] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '7':
                if slotNum[6] == '7':
                    slotNum[6] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '8':
                if slotNum[7] == '8':
                    slotNum[7] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case '9':
                if slotNum[8] == '9':
                    slotNum[8] = current
                    return slotNum
                else:
                    print('Slot ' + numSelect + ' is filled.')
            case _:
                print('Slot ' + numSelect + ' is not a valid option.')
        
    return slotNum

def main():

    #Tic tac toe:
    #Create player 'O' and player 'X'
    playx = 'X'
    playo = 'O'

    #create var for current player
    current = playx

    #create slot array
    slotNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


    countRound = 0

    runGame = True
    while runGame == True:
        #Fill slot with 'X' or 'O' depending on which player selected it
        #Using match/case method to input numbers
        #if slot is already filled, <0, or >9 notify the player
        #   and ask same player to enter new number    
        slotNum = gameBoard(slotNum, current)

        countRound += 1

        #check if 3 in row
        if slotNum[0] == slotNum[1] == slotNum[2]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[3] == slotNum[4] == slotNum[5]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[6] == slotNum[7] == slotNum[8]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[0] == slotNum[3] == slotNum[6]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[1] == slotNum[4] == slotNum[7]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[2] == slotNum[5] == slotNum[8]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[0] == slotNum[4] == slotNum[8]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False
        elif slotNum[2] == slotNum[4] == slotNum[6]:
            showGameboard(slotNum)
            print('Player ' + current + ' wins')
            runGame = False

        if countRound >= 9:
            showGameboard(slotNum)
            print("It's a draw")
            runGame = False
    

        #change 'current' to other player
        if current == 'O':
            current = 'X'
        else:
            current = 'O'

if __name__ == '__main__':
    main()
