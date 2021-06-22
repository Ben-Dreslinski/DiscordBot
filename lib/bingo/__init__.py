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
    diagDone = -1

    def __init__(self):
        random.shuffle(self.possibleSquares)
        k = 0
        for i in range(0, 5):
            for j in range(0, 5):
                self.eventBoard[i][j] = self.possibleSquares[k]
                k += 1
        
        self.populateBoard()
        self.startTime = datetime.datetime.now()

    def populateBoard(self, row=-1, col=-1):
        img = Image.open('lib/bingo/BINGOtemplatepng.png')
        d1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype("arial.ttf", 32)

        if (row > -1):
            for i in range(0, 5):
                for j in range(0, 5):
                    if (i == 2 and j == 2 and self.diagDone != 1 and self.rowDone < 0 and self.colDone < 0):
                        d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue

                    if (self.stateBoard[j][i] == 0):
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
                    elif (self.rowDone > -1 or self.colDone > -1 or self.diagDone > -1):
                        if (self.diagDone > 0 and i == 2 and j == 2):
                            d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (255, 255, 0))
                        elif ((self.rowDone == j) or (self.colDone == i)):
                            if (i == 2 and j == 2):
                                d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (255, 255, 0))
                            else:
                                d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 255, 0))
                        else:
                            d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
                    else:
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
        else:
            for i in range(0, 5):
                for j in range(0, 5):
                    if (i == 2 and j == 2):
                        d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue

                    if (self.stateBoard[row][col] == 0):
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
                    else:
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
    
        img.save('lib/bingo/BINGOedit.png')

    def getStartTime(self):
        return (self.startTime).strftime("%H:%M:%S")
    
    def getStartDate(self):
        return (self.startTime).strftime("%m/%d/%Y")

    def getCol(self, letter: str):
        if (letter == "B" or letter == 'b'):
            col = 0
        elif (letter == "I" or letter == 'i'):
            col = 1
        elif (letter == "N" or letter == 'n'):
            col = 2
        elif (letter == "G" or letter == 'g'):
            col = 3
        elif (letter == "O" or letter == 'o'):
            col = 4
        
        return col
    
    def getRow(self, square: int):
        square = int(square)
        if (square == 1):
            row = 0
        elif (square == 2):
            row = 1
        elif (square == 3):
            row = 2
        elif (square == 4):
            row = 3
        elif (square == 5):
            row = 4
        
        return row

    def getBoardEvents(self):
        return self.eventBoard

    def getBoardStates(self):
        return self.stateBoard
    
    def printEvents(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.eventBoard[i][j])
    
    def printStates(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.stateBoard[i][j])

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
    
    def diagonalSum(self):
        return (self.stateBoard[0][0] + self.stateBoard[1][1] + self.stateBoard[2][2] + self.stateBoard[3][3]
            + self.stateBoard[4][4])

    def greenUpdate(self, letter: str, square: int):
        if (letter == "N" and square == 3):
            return -1

        col = self.getCol(letter)
        row = self.getRow(square)

        if (self.stateBoard[row][col] == 1):
            return 0

        self.stateBoard[row][col] = 1
        
        if (self.rowSum(row) == 5):
            self.rowDone = row
        
        if (self.colSum(col) == 5):
            self.colDone = col
        
        if (self.diagonalSum() == 5):
            self.diagDone = 1

        self.populateBoard(col, row)
        return 1
    
    def redUpdate(self, letter: str, square: int):
        if (letter == "N" and square == 3):
            return -1
        
        col = self.getCol(letter)
        row = self.getRow(square)

        if (self.stateBoard[row][col] == 0):
            return 0

        self.stateBoard[row][col] = 0

        if (self.rowSum(row) != 5):
            self.rowDone = -1
        
        if (self.colSum(col) != 5):
            self.colDone = -1
        
        if (self.diagonalSum() == 5):
            self.diagDone = -1

        self.populateBoard(col, row)
        return 1

board = Bingo()
board.printEvents()