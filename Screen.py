import pygame
'''
screen class holds everything graphics related to the sudoku project

It contains the Functions: 
--> __init__(): creates a new blank screen 
--> ButtonEventCheck(): checks if anything has been pressed, it will return the name of the pressed button or the row and column of the grid if a grid is pressed
--> FindCenter(object): Finds the center of the given rect, probably do not need to use for anything else other then what its already used for.
--> ClearScreen(): makes the screen blank
--> StartScreen(): displays the starting screen with the buttons easy, medium, and hard
--> GameScreen(): creates the game screen (the grid) and the buttons Restart, Reset and Exit 
--> displayNums(nums,playernums): Displays the numbers onto the GameScreen Grid.
the function above takes in two parameters, each should be a 9x9 2D array with integers.
one parameter should contain the numbers set there by the game.
the second parameter should contain the numbers set there by the player.
-->WinningScreen(): Displays the winning screen and the button Exit
--> LosingScreen(): Displays the losing screen and the restart button
'''

class Screen:
    def __init__(self):
        #below initializes the screen
        pygame.init()
        pygame.event.get()

        #below sets screen attributes line screen and buttons
        pygame.display.set_caption('Sudoku') #makes screen name
        self.screen = pygame.display.set_mode((700,800))
        self.screen.fill("white")

        self.easyButton = pygame.Rect(0, 0, 0, 0)
        self.mediumButton = pygame.Rect(0, 0, 0, 0)
        self.hardButton = pygame.Rect(0, 0, 0, 0)
        self.resetButton = pygame.Rect(0, 0, 0, 0)
        self.restartButton = pygame.Rect(0, 0, 0, 0)
        self.exitButton = pygame.Rect(0, 0, 0, 0)
        self.gameScreenDisplay = False


        #below updates screen
        pygame.display.update()

    def ButtonEventCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if self.easyButton.collidepoint(position):
                    return("easy")
                if self.mediumButton.collidepoint(position):
                    return("medium")
                if self.hardButton.collidepoint(position):
                    return("hard")
                if self.restartButton.collidepoint(position):
                    return("Restart")
                if self.resetButton.collidepoint(position):
                    return("reset")
                if self.exitButton.collidepoint(position):
                    return("Exit")
                if self.gameScreenDisplay:
                    square_size = self.screen.get_rect().width / 9
                    #pygame.Rect(WordLocation[0]-5, WordLocation[1]-5,medium.get_rect().width+10,medium.get_rect().height+10)
                    col = (position[0]//square_size)
                    row =  (position[1]//square_size)
                    square = pygame.Rect(col*square_size, row*square_size, square_size+2, square_size+2)
                    pygame.draw.rect(self.screen, "red", square, 4)
                    return(int(col),int(row))
            pygame.display.update()

    def ClearScreen(self):
        self.screen.fill("white")
        self.easyButton = pygame.Rect(0,0,0,0)
        self.mediumButton = pygame.Rect(0,0,0,0)
        self.hardButton = pygame.Rect(0,0,0,0)
        self.resetButton = pygame.Rect(0, 0, 0, 0)
        self.restartButton = pygame.Rect(0, 0, 0, 0)
        self.exitButton = pygame.Rect(0, 0, 0, 0)
        self.gameScreenDisplay = False
        pygame.display.update()

    def FindCenter(self,object): #intends to find cords that would place object in center screen
        Screencenter = self.screen.get_rect().center
        objectcenter = object.get_rect().center
        x = Screencenter[0] - objectcenter[0]
        y = Screencenter[1] - objectcenter[1]
        return(x,y) #needs to return a tuple to work


    def StartScreen(self):
        #below finds center of screen to be used later
        Screencenter = self.screen.get_rect().center #returns center x,y as tuple

        #below sets text attributes -----------------------------------------------
        font = pygame.font.SysFont('Arial', 40)

        #below creates different text elements used

        WelcomeTo = font.render('Welcome To', False, "black")
        WordLocation = self.FindCenter(WelcomeTo)
        WordLocation = (WordLocation[0],WordLocation[1] - 150) #Moves Word location for WelcomeTo slightly up from center
        self.screen.blit(WelcomeTo, (WordLocation)) #draws words on image at center given

        #Below makes rainbow letters
        font.set_bold(True)
        letters = [
            font.render('S', False, "Red",),
            font.render('u', False, "Blue"),
            font.render('d', False, "Yellow"),
            font.render('o', False, "Orange"),
            font.render('k', False, "Green"),
            font.render('u', False, "Purple"),
            font.render('!', False, "Red"),
            font.render('!', False, "green"),
            font.render('!', False, "brown")]
        WordLocation = self.FindCenter(letters[0])
        WordLocation = (WordLocation[0]-60,WordLocation[1] - 110)
        for letter in letters:
            self.screen.blit(letter, WordLocation)
            WordLocation = (WordLocation[0] + letter.get_width(),WordLocation[1])


        font = pygame.font.SysFont('Arial', 28)

        GameMode = font.render('Please Select A Game Mode:', False, "black")
        WordLocation = self.FindCenter(GameMode)
        WordLocation = (WordLocation[0],WordLocation[1]-50)
        self.screen.blit(GameMode, (WordLocation))

        #the Words Easy Medium and Hard also need buttons so below also initializes buttons with the words

        #below is easy
        easy = font.render('Easy', False, "black")
        WordLocation = self.FindCenter(easy)
        WordLocation = (WordLocation[0]-100, WordLocation[1]+10)

        self.easyButton = pygame.Rect(WordLocation[0]-5, WordLocation[1]-5,easy.get_rect().width+10,easy.get_rect().height+10)

        pygame.draw.rect(self.screen, "Green", self.easyButton, 50)
        self.screen.blit(easy, (WordLocation))

        #below is medium
        medium = font.render('Medium', False, "black")
        WordLocation = self.FindCenter(medium)
        WordLocation = (WordLocation[0], WordLocation[1] + 10)

        self.mediumButton = pygame.Rect(WordLocation[0]-5, WordLocation[1]-5,medium.get_rect().width+10,medium.get_rect().height+10)

        pygame.draw.rect(self.screen, "Orange", self.mediumButton, 50)
        self.screen.blit(medium, (WordLocation))

        #below is hard
        hard = font.render('Hard', False, "black")
        WordLocation = self.FindCenter(hard)
        WordLocation = (WordLocation[0] + 100, WordLocation[1] + 10)

        self.hardButton = pygame.Rect(WordLocation[0]-5, WordLocation[1]-5,hard.get_rect().width+10,hard.get_rect().height+10)

        pygame.draw.rect(self.screen, "Red", self.hardButton, 50)
        self.screen.blit(hard, (WordLocation))
        # below updates the screen
        pygame.display.update()

    def GameScreen(self):
        self.gameScreenDisplay = True #This makes it so when they press on screen it does soemthing in button event thing
        #Below will draw columns n stuff
        screenWidth = self.screen.get_rect().width
        screenHeight = self.screen.get_rect().height

        #below draws the three thick columns and rows
        square_size = screenWidth // 3
        for i in range(1, 4):
            pygame.draw.line(self.screen, "black", (i * square_size, 0), (i * square_size, screenHeight), 4)
            pygame.draw.line(self.screen, "black", (0, i * square_size), (screenWidth, i * square_size), 4)

        #below draws the nine cols and rows with thin lines
        square_size = screenWidth  / 9
        for i in range(10):  # 10 lines to create 9 spaces
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * square_size), (screenWidth, i * square_size), 1)
            pygame.draw.line(self.screen, (0, 0, 0), (i * square_size, 0), (i * square_size, screenHeight-square_size), 1)

        #so :/ I couldnt figure out how to get the lines to not draw into the bottom so I have what's below to visually fix that
        whiteRect = pygame.Rect((0,screenHeight-square_size-20),(screenWidth,square_size+21))
        pygame.draw.rect(self.screen, "White", whiteRect, 50)

        #Below creates and displays the buttons:
        font = pygame.font.SysFont('Arial', 32)

        #below is the Reset Button
        Reset = font.render('Reset', False, "black")
        WordLocation = self.FindCenter(Reset)
        WordLocation = (WordLocation[0]-150,WordLocation[1] + 350)  # Moves Word location for WelcomeTo slightly up from center
        self.resetButton = pygame.Rect(WordLocation[0] - 5, WordLocation[1] - 5, Reset.get_rect().width + 10,Reset.get_rect().height + 10)

        pygame.draw.rect(self.screen, "lightblue", self.resetButton, 50)
        self.screen.blit(Reset, (WordLocation))

        #Below is the Restart Button
        Restart = font.render('Restart', False, "black")
        WordLocation = self.FindCenter(Restart)
        WordLocation = (WordLocation[0],WordLocation[1] + 350)  # Moves Word location for WelcomeTo slightly up from center
        self.restartButton = pygame.Rect(WordLocation[0] - 5, WordLocation[1] - 5, Restart.get_rect().width + 10,Restart.get_rect().height + 10)

        pygame.draw.rect(self.screen, "lightblue", self.restartButton, 50)
        self.screen.blit(Restart, (WordLocation))

        #Below is the Exit Button
        exit = font.render('Exit', False, "black")
        WordLocation = self.FindCenter(exit)
        WordLocation = (WordLocation[0] + 150,WordLocation[1] + 350)  # Moves Word location for WelcomeTo slightly up from center
        self.exitButton = pygame.Rect(WordLocation[0] - 5, WordLocation[1] - 5, exit.get_rect().width + 10,exit.get_rect().height + 10)

        pygame.draw.rect(self.screen, "lightblue", self.exitButton, 50)
        self.screen.blit(exit, (WordLocation))

        #Below updates the screen
        pygame.display.update()

    def displayNums(self,nums,playernums): #nums expects to be a 9x9 2D array of numbers, and same with playernums
        font = pygame.font.SysFont('Arial', 38) #initialized font

        # renderedNums = []
        square_size = self.screen.get_rect().width  / 9 #This is legit same as square size used in prev function
        WordLocation = (square_size-(square_size/2),square_size-square_size/2)
        for col in nums:
            # renderedNums.append[[]]
            for num in col:
                if num != 0:
                    renderedNum = font.render(str(num), False, "black")
                    WordWidth = renderedNum.get_rect().width / 2
                    Wordheight = renderedNum.get_rect().height / 2
                    self.screen.blit(renderedNum, (WordLocation[0]-WordWidth,WordLocation[1]-Wordheight))
                WordLocation = (WordLocation[0]+square_size,WordLocation[1])
            WordLocation = (square_size-(square_size/2), WordLocation[1]+square_size)

        #below is for teh player numbers to be typed in gray
        square_size = self.screen.get_rect().width / 9  # This is legit same as square size used in prev function
        WordLocation = (square_size - (square_size / 2), square_size - square_size / 2)
        for col in playernums:
            for num in col:
                if num != 0:
                    renderedNum = font.render(str(num), False, (90,90,90))
                    WordWidth = renderedNum.get_rect().width / 2
                    Wordheight = renderedNum.get_rect().height / 2
                    self.screen.blit(renderedNum, (WordLocation[0]-WordWidth,WordLocation[1]-Wordheight))
                WordLocation = (WordLocation[0]+square_size,WordLocation[1])
            WordLocation = (square_size-(square_size/2), WordLocation[1]+square_size)

        pygame.display.update()

    def WinningScreen(self):
        font = pygame.font.SysFont('Arial', 40)

        # below creates different text elements used

        GameWon = font.render('Game Won :3', False, "black")
        WordLocation = self.FindCenter(GameWon)
        WordLocation = (WordLocation[0],WordLocation[1] - 150)  # Moves Word location for WelcomeTo slightly up from center
        self.screen.blit(GameWon, (WordLocation))  # draws words on image at center given

        # Below is the Exit Button
        exit = font.render('Exit', False, "black")
        WordLocation = self.FindCenter(exit)
        WordLocation = (WordLocation[0],WordLocation[1])  # Moves Word location for WelcomeTo slightly up from center
        self.exitButton = pygame.Rect(WordLocation[0] - 5, WordLocation[1] - 5, exit.get_rect().width + 10,exit.get_rect().height + 10)

        pygame.draw.rect(self.screen, "lightblue", self.exitButton, 50)
        self.screen.blit(exit, (WordLocation))

        pygame.display.update()

    def LosingScreen(self):
        font = pygame.font.SysFont('Arial', 40)

        # below creates different text elements used

        GameOver = font.render('Game Over :c', False, "black")
        WordLocation = self.FindCenter(GameOver)
        WordLocation = (WordLocation[0], WordLocation[1] - 150)  # Moves Word location for WelcomeTo slightly up from center
        self.screen.blit(GameOver, (WordLocation))  # draws words on image at center given

        # Below is the Restart Button
        Restart = font.render('Restart', False, "black")
        WordLocation = self.FindCenter(Restart)
        WordLocation = (WordLocation[0], WordLocation[1])  # Moves Word location for WelcomeTo slightly up from center
        self.restartButton = pygame.Rect(WordLocation[0] - 5, WordLocation[1] - 5, Restart.get_rect().width + 10,Restart.get_rect().height + 10)

        pygame.draw.rect(self.screen, "lightblue", self.restartButton, 50)
        self.screen.blit(Restart, (WordLocation))

        pygame.display.update()