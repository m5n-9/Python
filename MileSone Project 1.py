import json


XO={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
plays = 0

def printBoard():
    print ('         |       |')
    print ('   ',XO['1'],'   |  ',XO['2'],'  |    ',XO['3'])
    print ('___________________________')
    print ('         |       |')
    print ('   ',XO['4'],'   |  ',XO['5'],'  |    ',XO['6'])
    print ('___________________________')
    print ('         |       |')
    print ('   ',XO['7'],'   |  ',XO['8'],'  |    ',XO['9'])

def gamePlay(choices):
    choice= input("Select a number to make your move :")
    XO[choice]=choices
    printBoard()

def checkWinner():
    global plays
    if (XO['1'], XO['2'], XO['3']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['1'], XO['5'], XO['9']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['1'], XO['4'], XO['7']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['2'], XO['5'], XO['8']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['3'], XO['6'], XO['9']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['3'], XO['5'], XO['7']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['4'], XO['5'], XO['6']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['7'], XO['8'], XO['9']) ==('X','X','X'):
        print ("Player one wins")
        exit()
    elif (XO['1'], XO['2'], XO['3']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['1'], XO['5'], XO['9']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['1'], XO['4'], XO['7']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['2'], XO['5'], XO['8']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['3'], XO['6'], XO['9']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['3'], XO['5'], XO['7']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['4'], XO['5'], XO['6']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (XO['7'], XO['8'], XO['9']) ==('O','O','O'):
        print ("Player two wins")
        exit()
    elif (plays == 9): 
        print ("No one wins")

def gameEnd():
    #1
    global plays
    printBoard()
    print ("First player's move")
    gamePlay('X')
    plays = plays + 1
    #2
    print ("Second player's move")
    gamePlay('O')
    plays=plays+1
    #3
    print ("First player's move")
    gamePlay('X')
    plays=plays+1
    #4
    print ("Second player's move")
    gamePlay('O')
    plays=plays+1
    #5
    print ("First player's move")
    gamePlay('X')
    checkWinner()
    plays=plays+1
    #6
    print ("Second player's move")
    gamePlay('O')
    checkWinner()
    plays=plays+1
    #7
    print ("First player's move")
    gamePlay('X')
    checkWinner()
    plays=plays+1
    #8
    print ("Second player's move")
    gamePlay('O')
    checkWinner()
    plays=plays+1
    #9
    print ("First player's move")
    gamePlay('X')
    checkWinner()
    plays=plays+1



gameEnd()


exit()