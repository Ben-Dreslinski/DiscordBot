from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from array import *
import random

class Bingo():
    possibleSquares = ['Dragoon types\nin #forums\nor says a\nhistorical fact', 'One of the surf\nservers needs\na restart',
                   'Someone\nmakes a\nresignation\npost on\nthe forums', 'Someones\ncomplaining in\nthe shoutbox\non the forums',
                   'Alt evader\ngets banned', 'Scammer gets\nbanned from\ndiscord', 'Main discord\nannouncement',
                   'GFL-Wide\nserver issues in\nmultiple games', 'Dragoon makes\nan anime\nreference',
                   'Someone with a\nDaBaby pic\njoins one of\nthe discords', 'Frenzy actually\nresponds to\na dm',
                   'Discord rule\n9 report', 'GFX request\nis completed', 'Mod team\napplication\ngets accepted',
                   'Petr says\nsomething\ndebatable or\ncomplains over\nsomething', 'Infra mentions\na girl', 'Roy goes\non a\nbreak',
                   'New surf\nvideo on\nGFL Surf\nchannel',
                   'One of the\nGFL discords\ngets raided', 'Someone pings\nfurry Alexis\ninstead of\ncool Alexis', 'Infra gets\npinged while\nasleep',
                   'Infra says\n"basically"', 'Carlbot says\n"actually" in\nsurf discord', 'Someone gets\ncaught in 4k', 'Someone with\n2+ roles\ngets another'
                   ]

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

    def __init__(self):
        random.shuffle(self.possibleSquares)
        k = 0
        for i in range(0, 5):
            for j in range(0, 5):
                self.eventBoard[i][j] = self.possibleSquares[k]
                k += 1
        
        self.populateBoard()

    def populateBoard(self, row=-1, col=-1):
        if (row > -1):
            img = Image.open('lib/bingo/BINGOtemplatepng.png')
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype("arial.ttf", 32)
            for i in range(0, 5):
                for j in range(0, 5):
                    if (i == row and col == j):
                        d1.text((i*242, j*200 + 200), self.eventBoard[row][col], font=myFont, fill = (0, 255, 0))
                        continue
                    if (i == 2 and j == 2):
                        d1.text((i*242, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue
                    if (self.stateBoard[j][i] == 0):
                        d1.text((i*242, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
                    else:
                        d1.text((i*242, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
        else:
            img = Image.open('lib/bingo/BINGOtemplatepng.png')
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype("arial.ttf", 32)
            for i in range(0, 5):
                for j in range(0, 5):

                    if (i == 2 and j == 2):
                        d1.text((i*242, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue
                    
                    if (self.stateBoard[row][col] == 0):
                        d1.text((i*242, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
                    else:
                        d1.text((i*242, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (0, 255, 0))
    
        img.save('lib/bingo/BINGOedit.png')

    def getCol(self, letter: str):
        col = 0
        if (letter == "B"):
            col = 0
        elif (letter == "I"):
            col = 1
        elif (letter == "N"):
            col = 2
        elif (letter == "G"):
            col = 3
        elif (letter == "O"):
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

    def updatesquare(self, letter: str, square: int):
        col = self.getCol(letter)
        row = self.getRow(square)

        self.stateBoard[row][col] = 1
        self.populateBoard(col, row)


        
        

board = Bingo()
board.printEvents()