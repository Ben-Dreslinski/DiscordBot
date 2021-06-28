from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from array import *
import random
import datetime

class Bingo():
    possibleSquares = [] # TODO: add events here as strings separated by commas: ['X does Y', 'Z does W'] etc
                         # will have to accomodate for running off of square using \n

    eventBoard = [
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""]
                   ]
    stateBoard = [
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]
                   ]

    startTime = 0
    rowDone = -1
    colDone = -1
    leftDiagDone = -1
    rightDiagDone = -1

    def __init__(self):
        random.shuffle(self.possibleSquares)
        k = 0
        for i in range(0, 5):
            for j in range(0, 5):
                self.eventBoard[i][j] = self.possibleSquares[k]
                k += 1
        
        self.createBoard()
        self.startTime = datetime.datetime.now()

    def createBoard(self):
        img = Image.open('lib/bingo/BINGOtemplatepng.png')
        d1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype("arial.ttf", 32)

        for i in range(0, 5):
                for j in range(0, 5):
                    if (i == 2 and j == 2):
                        d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue

                    d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
        
        img.save('lib/bingo/BINGOedit.png')

    def populateBoard(self):
        img = Image.open('lib/bingo/BINGOtemplatepng.png')
        d1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype("arial.ttf", 32)

        for i in range(0, 5):
            for j in range(0, 5):
                if (i == 2 and j == 2 and self.leftDiagDone != 1 and self.rightDiagDone != 1 and self.rowDone < 0 and self.colDone < 0):
                    d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                    continue

                if (self.stateBoard[j][i] == 0):
                    d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
                elif (self.rowDone > -1 or self.colDone > -1 or self.leftDiagDone > -1 or self.rightDiagDone > -1):
                    if (self.leftDiagDone > 0):
                        if (i == 2 and j == 2):
                            d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (255, 255, 0))
                        elif (i == j):
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 255, 0))
                        else:
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
                    elif (self.rightDiagDone > 0):
                        if (i == 2 and j ==2):
                            d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (255, 255, 0))
                        elif ((j == 0 and i == 4) or (j == 1 and i == 3) or (j == 3 and i == 1) or (j == 4 and i == 0)):
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 255, 0))
                        else:
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
                    elif ((self.rowDone > -1) or (self.colDone > -1)):
                        if ((self.rowDone == j) or (self.colDone == i)):
                            if (i == 2 and j == 2):
                                d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (255, 255, 0))
                            else:
                                d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 255, 0))
                        elif (i == 2 and j == 2):
                            d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        else:
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
                    else:
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
                else:
                    d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
    
        img.save('lib/bingo/BINGOedit.png')

    def reset(self):
        self.eventBoard = [
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""],
                   ["", "", "", "", ""]
                   ]
        self.stateBoard = [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                    ]

        self.startTime = 0
        self.rowDone = -1
        self.colDone = -1
        self.leftDiagDone = -1
        self.rightDiagDone = -1
        self.__init__()

    def getStartTime(self):
        return (self.startTime).strftime("%H:%M:%S")
    
    def getStartDate(self):
        return (self.startTime).strftime("%m/%d/%Y")

    def getCol(self, letter: str):
        if (letter.upper() == 'B'):
            col = 0
        elif (letter.upper() == 'I'):
            col = 1
        elif (letter.upper() == 'N'):
            col = 2
        elif (letter.upper() == 'G'):
            col = 3
        elif (letter.upper() == 'O'):
            col = 4
        
        return col

    def getBoardEvents(self):
        return self.eventBoard

    def getBoardStates(self):
        return self.stateBoard

    def colSum(self, col: int):
        count = 0
        for i in range(0, 5):
            count += self.stateBoard[i][col]
        
        return count
    
    def rowSum(self, row: int):
        count = 0
        for i in range(0, 5):
            count += self.stateBoard[row][i]
        
        return count
    
    def leftDiagSum(self):
        return (self.stateBoard[0][0] + self.stateBoard[1][1] + self.stateBoard[2][2] + self.stateBoard[3][3]
            + self.stateBoard[4][4])
    
    def rightDiagSum(self):
        return (self.stateBoard[0][4] + self.stateBoard[1][3] + self.stateBoard[2][2] + self.stateBoard[3][1]
            + self.stateBoard[4][0])

    def greenUpdate(self, letter: str, square: int):
        if (letter.upper() == "N" and square == 3):
            return -1

        col = self.getCol(letter)
        row = square - 1

        if (self.stateBoard[row][col] == 1):
            return 0

        self.stateBoard[row][col] = 1
        
        if (self.rowSum(row) == 5):
            self.rowDone = row
        
        if (self.colSum(col) == 5):
            self.colDone = col
        
        if (self.leftDiagSum() == 5):
            self.leftDiagDone = 1
        
        if (self.rightDiagSum() == 5):
            self.rightDiagDone = 1

        self.populateBoard()
        return 1
    
    def redUpdate(self, letter: str, square: int):
        if (letter.upper() == "N" and square == 3):
            return -1
        
        col = self.getCol(letter)
        row = square - 1

        if (self.stateBoard[row][col] == 0):
            return 0

        self.stateBoard[row][col] = 0

        if (self.rowSum(row) != 5):
            self.rowDone = -1
        
        if (self.colSum(col) != 5):
            self.colDone = -1
        
        if (self.leftDiagSum() != 5):
            self.leftDiagDone = -1
        
        if (self.rightDiagSum() != 5):
            self.rightDiagDone = -1

        self.populateBoard()
        return 1
    
    # debugging functions

    def printEvents(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.eventBoard[i][j])
    
    def printStates(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.stateBoard[i][j])

board = Bingo()
board.printEvents()