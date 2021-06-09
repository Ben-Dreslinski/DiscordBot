from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from array import *
import random
import datetime

class Bingo():
    possibleSquares = ['Dragoon types\nin #forums\nor says a\nhistorical fact', 'One of the surf\nservers needs\na restart',
                   'Someone\nmakes a\nresignation\npost on\nthe forums', 'Someones\ncomplaining in\nthe shoutbox\non the forums',
                   'Alt evader\ngets banned', 'Scammer gets\nbanned from\ndiscord', 'Main discord\nannouncement',
                   'GFL-Wide\nserver issues in\nmultiple games', 'Dragoon makes\nan anime\nreference',
                   'Someone with a\nDaBaby pic\njoins one of\nthe discords', 'Frenzy actually\nresponds to\na dm',
                   'Discord rule\n9 report', 'GFX request\nis completed', 'Mod team\napplication\ngets accepted',
                   'Petr says\nsomething\ndebatable or\ncomplains over\nsomething', 'Infra mentions\na girl', 'Roy goes\non a\nbreak',
                   'New surf\nvideo on\nGFL Surf\nchannel', 'One of the\nGFL discords\ngets raided', 'Someone pings\nfurry Alexis\ninstead of\ncool Alexis', 
                   'Infra gets\npinged while\nasleep', 'Infra says\n"basically"', 'Carlbot says\n"actually" in\nsurf discord', 'Someone gets\ncaught in 4k', 'Someone with\n2+ roles\ngets another',
                   'Someone gets\naround a\nfilter', 'More than\n5 people in\nmain vc', '15 posts on\nthe forums\nwithin 24 hrs', 'A bug on the\nforums gets\nreported', 
                   'Someone hits\n30x using slots', 'CWRP hits\n80 players', 'A rust server\nhits 100 pop', 'Surf hits 100\nplayers', 'GFL twitter\nposts a\ntweet', 
                   'Someone brings\nup veganism', 'There is a\ndebate in\n#politics', '3 hours and\nno messages\nin main\n#general', 'Someone posts\nskribble.io or\ngarticphone\nlink',
                   'Someone posts\na metal song', 'Someone posts\na rap song', 'Someone posts\na country song', 'Someone is\ncomplaining \nabout their\nparents', 'Someone posts\ntheir own\nartwork in\nmain #art',
                   'Someone asks if\nmember is free', 'More than\n$200 donated\nin 1 day', 'More than\n$50 donated\nfrom 1 person', 'Someone asks\nabout a\ndead server', 'Someone brings\nup alcohol', 
                   'NSFW ban\nin discord', 'NSFW ban\nfrom in-game\nspray', 'Prop-hunt hits\n45 players', '2fort hits\n33 players', 'Hightower hits\n33 players', 'TTT Anarchy\nhits 33 pop',
                   'Dark rp\nis up', 'Squad is up', 'More than 2\nposts in last\ncomments wins', 'More than 2\nposts in last\nquote wins', 'More than 20\npeople join\nrust in 1 day',
                   'More than 20\npeople join\nmain in 1 day', 'Someone says\nstepbro or\nstepsis', 'Someone says\nsus outside\nof AH',
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

    startTime = 0

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
                    if (i == 2 and j == 2):
                        d1.text((i*243, j*200 + 200), 'Free space', font=myFont, fill = (0, 255, 0))
                        continue
                    if (self.stateBoard[j][i] == 0):
                        d1.text((i*243, j*200 + 200), self.eventBoard[i][j], font=myFont, fill = (255, 0, 0))
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

    def greenUpdate(self, letter: str, square: int):
        col = self.getCol(letter)
        row = self.getRow(square)

        self.stateBoard[row][col] = 1
        print(self.eventBoard[col][row])
        self.printStates()

        count = 0
        for i in range(0, 5):
            count += self.stateBoard[i][0]
        
        # if (count == 5):
        #     print("Bingo")

        self.populateBoard(col, row)
    
    def redUpdate(self, letter: str, square: int):
        col = self.getCol(letter)
        row = self.getRow(square)

        self.stateBoard[row][col] = 0
        print(self.eventBoard[col][row])
        self.printStates()
        self.populateBoard(col, row)


        
        

board = Bingo()
board.printEvents()