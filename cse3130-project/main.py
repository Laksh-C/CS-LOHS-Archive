# main.py
"""
title: Main Program Code
author: Laksh Chopra
date-created: 09/02/24
"""

### IMPORTS
import pygame
from box import Box
from random import randrange
from playing_field import Window
from playing_field import Text

pygame.init()


# Defining all objects used to render the playing field-#####################################
#############################################################################################
#############################################################################################
WINDOW = Window("Brick Breaker", 800, 600, 30)
LIVES = 0
BRICK_BREAKER_TEXT = Text("BRICK BREAKER!!!")
BRICK_BREAKER_TEXT.setTextSize(40)
BRICK_BREAKER_TEXT.setTextFont("varsity_regular.ttf")
TITLE_BOX = Box(WINDOW.getWidth(), 40)
TITLE_BOX.setColor((110, 110, 110))
BRICK_BREAKER_TEXT.setPOS(WINDOW.getWidth() // 2 - BRICK_BREAKER_TEXT.getWidth() // 2, -4)
FLASHING_COLOR = [140, 3, 252]
BRICK_SPACING = 11.6777777777

PADDLE = Box(150, 20)
PADDLE.setSpeed(10)
PADDLE.setPOS(
    WINDOW.getWidth() // 2 - PADDLE.getWidth() // 2,
    500
)
PADDLE.setColor((255, 89, 89))

HELLO = Text("Press SPACE to start!")
HELLO.setPOS(
    WINDOW.getWidth() // 2 - HELLO.getWidth() // 2,
    420
)

PADDLE_RIGHT = Box(PADDLE.getWidth()/2, 20)
PADDLE_RIGHT.setSpeed(10)
PADDLE_RIGHT.setPOS(
    WINDOW.getWidth()//2,
    500
)
PADDLE_RIGHT.setColor((52, 122, 235))

BALL = Box(15, 15)
BALL.setSpeed(5)
BALL.setPOS(
    WINDOW.getWidth() //2 - BALL.getWidth() // 2,
    460
)

GAME_OVER_TEXT = Text("GAME OVER :(")
GAME_OVER_TEXT.setTextSize(60)
GAME_OVER_TEXT.setTextFont("varsity_regular.ttf")
GAME_OVER_TEXT.setPOS(
    WINDOW.getWidth()//2 - GAME_OVER_TEXT.getWidth()//2,
    WINDOW.getHeight()//2 - GAME_OVER_TEXT.getHeight() //2
)

YOU_WIN_TEXT = Text("YOU WIN!!!")
YOU_WIN_TEXT.setTextSize(60)
YOU_WIN_TEXT.setTextFont("varsity_regular.ttf")
YOU_WIN_TEXT.setPOS(
    WINDOW.getWidth()//2 - YOU_WIN_TEXT.getWidth()//2,
    WINDOW.getHeight()//2 - YOU_WIN_TEXT.getHeight()//2
)
#############################################################################################
#############################################################################################

# Rendering the layout of the level one for bricks ##########################################
BRICK_ROW1 = []
BRICK_ROW2 = []
BRICK_ROW3 = []
BRICK_ROW4 = []
BRICK_ROW5 = []
BRICK_ROW6 = []

LONG_ROWS = [BRICK_ROW1, BRICK_ROW3, BRICK_ROW5]
SHORT_ROWS = [BRICK_ROW2, BRICK_ROW4, BRICK_ROW6]

for j in range(3):
    for i in range(7):
        LONG_ROWS[j].append(Box(90, 40))
        LONG_ROWS[j][i].setColor((randrange(50, 220), randrange(50, 220), randrange(50, 220)))

for j in range(3):
    for i in range(6):
        SHORT_ROWS[j].append(Box(90, 40))
        SHORT_ROWS[j][i].setColor((randrange(50, 220), randrange(50, 220), randrange(50, 220)))

for i in range(3):
    for j in range(7):
        if j == 0:
            if i==0:
                LONG_ROWS[0][0].setPOS(50, 80)
            elif i == 1:
                LONG_ROWS[1][0].setPOS(50, 160+2*BRICK_SPACING)
            elif i==2:
                LONG_ROWS[2][0].setPOS(50, 240+4*BRICK_SPACING)
        else:
            LONG_ROWS[i][j].setPOS(
                LONG_ROWS[i][j-1].getX() + LONG_ROWS[i][j].getWidth() + BRICK_SPACING,
                LONG_ROWS[i][j-1].getY()
            )

for i in range(3):
    for j in range(6):
        if j == 0:
            if i==0:
                SHORT_ROWS[0][0].setPOS(95+BRICK_SPACING/2, 120+BRICK_SPACING)
            elif i == 1:
                SHORT_ROWS[1][0].setPOS(95+BRICK_SPACING/2, 200+3*BRICK_SPACING)
            elif i==2:
                SHORT_ROWS[2][0].setPOS(95+BRICK_SPACING/2, 280 + 5*BRICK_SPACING)
        else:
            SHORT_ROWS[i][j].setPOS(
                SHORT_ROWS[i][j - 1].getX() + SHORT_ROWS[i][j].getWidth() + BRICK_SPACING,
                SHORT_ROWS[i][j - 1].getY()
            )
BRICKS = BRICK_ROW1 + BRICK_ROW2 + BRICK_ROW3 + BRICK_ROW4 + BRICK_ROW5 + BRICK_ROW6
DELETED_BRICK_COUNT = 0
#############################################################################################
#############################################################################################

# Rendering the layout of the level one for bricks ##########################################
BRICK_ROW1_LEVEL2 = []
BRICK_ROW2_LEVEL2 = []
BRICK_ROW3_LEVEL2 = []
BRICK_ROW4_LEVEL2 = []
BRICK_ROW5_LEVEL2 = []
BRICK_ROW6_LEVEL2 = []

FULL_ROWS_LEVEL2 = [BRICK_ROW1_LEVEL2, BRICK_ROW6_LEVEL2]
SHORT_ROWS_LEVEL2 = [BRICK_ROW2_LEVEL2, BRICK_ROW3_LEVEL2, BRICK_ROW4_LEVEL2, BRICK_ROW5_LEVEL2]

for i in range(2):
    for j in range(7):
        FULL_ROWS_LEVEL2[i].append(Box(90, 40))
        FULL_ROWS_LEVEL2[i][j].setColor((randrange(50, 220), randrange(50, 220), randrange(50, 220)))

for i in range(4):
    for j in range(7):
        SHORT_ROWS_LEVEL2[i].append(Box(90, 40))
        SHORT_ROWS_LEVEL2[i][j].setColor((randrange(50, 220), randrange(50, 220), randrange(50, 220)))

for i in range(2):
    for j in range(7):
        if j==0:
            if i==0:
                FULL_ROWS_LEVEL2[0][0].setPOS(50, 80)
            elif i == 1:
                FULL_ROWS_LEVEL2[1][0].setPOS(50, 240+4*BRICK_SPACING)
        else:
            FULL_ROWS_LEVEL2[i][j].setPOS(
                FULL_ROWS_LEVEL2[i][j-1].getX() + FULL_ROWS_LEVEL2[i][j].getWidth() + BRICK_SPACING,
                FULL_ROWS_LEVEL2[i][j-1].getY()
            )

for i in range(4):
    for j in range(7):
        if j==0:
            if i==0:
                SHORT_ROWS_LEVEL2[0][0].setPOS(50, 120+BRICK_SPACING)
            elif i==1:
                SHORT_ROWS_LEVEL2[1][0].setPOS(50, 160+2*BRICK_SPACING)
            elif i==2:
                SHORT_ROWS_LEVEL2[2][0].setPOS(50, 200+3*BRICK_SPACING)
            elif i==3:
                SHORT_ROWS_LEVEL2[3][0].setPOS(50, 240+4*BRICK_SPACING)
        else:
            SHORT_ROWS_LEVEL2[i][j].setPOS(
                SHORT_ROWS_LEVEL2[i][j-1].getX() + SHORT_ROWS_LEVEL2[i][j].getWidth() + BRICK_SPACING,
                SHORT_ROWS_LEVEL2[i][j-1].getY()
            )

for i in range(4):
    del SHORT_ROWS_LEVEL2[i][5]
    del SHORT_ROWS_LEVEL2[i][3]
    del SHORT_ROWS_LEVEL2[i][1]

LEVEL_2_BRICKS = BRICK_ROW1_LEVEL2 + BRICK_ROW2_LEVEL2 + BRICK_ROW3_LEVEL2 + BRICK_ROW4_LEVEL2 + BRICK_ROW5_LEVEL2 + BRICK_ROW6_LEVEL2
# Game Function Variables
START = False
GAME_OVER = False
LEVEL1 = True
Level2 = False

if __name__ == "__main__":
    while True:
        #Blitting/rendering
        LIVES = PADDLE.getLivesRemaining()
        SCORE_TEXT = Text(f"LIVES: {LIVES}")
        SCORE_TEXT.setTextSize(30)
        SCORE_TEXT.setTextColor((0, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        BRICK_BREAKER_TEXT.pulseTextColor(FLASHING_COLOR, [randrange(10)/10, randrange(10)/10, randrange(10)/10])
        WINDOW.getSurface().blit(TITLE_BOX.getSurface(), (0, 0))
        WINDOW.getSurface().blit(SCORE_TEXT.getSurface(), (10, 2.5))
        WINDOW.getSurface().blit(BRICK_BREAKER_TEXT.getSurface(), BRICK_BREAKER_TEXT.getPOS())
        WINDOW.getSurface().blit(HELLO.getSurface(), HELLO.getPOS())
        PADDLE.ADmove(PRESSED_KEYS)
        WINDOW.getSurface().blit(PADDLE.getSurface(), PADDLE.getPOS())
        WINDOW.getSurface().blit(PADDLE_RIGHT.getSurface(), ((PADDLE.getX()+PADDLE_RIGHT.getWidth()), PADDLE.getY()))

        #Blitting all Bricks
        for i in range(len(BRICKS)):
            WINDOW.getSurface().blit(BRICKS[i].getSurface(), BRICKS[i].getPOS())

##################################
####--- MAIN PROGRAM CODE ---#####
##################################

        ### INPUTS ###
        if PRESSED_KEYS[pygame.K_SPACE] == 1:
            HELLO.setPOS(-10000, -10000)        # when start is pressed, make the hello text disappear
            START = True
        if not START:       # if the game is not in start mode, reappear the hello text
            HELLO.setPOS(
                WINDOW.getWidth() // 2 - HELLO.getWidth() // 2,
                420
            )

        ### PROCESSING ###
        if START:
            BALL.bounceWindow()
            if (BALL.getY()+BALL.getHeight()) > PADDLE.getY() and BALL.isCollision(PADDLE.getSurface(), PADDLE.getPOS()):
                if BALL.getX() >= (PADDLE.getX()+75):
                    if BALL.getXDIR() == 1:
                        pass
                    else:
                        BALL.setXDIR(1)
                else:
                    if BALL.getXDIR() == -1:
                        pass
                    else:
                        BALL.setXDIR(-1)
                BALL.setYDIR(-1)
            if BALL.getY()+BALL.getHeight() == WINDOW.getHeight():
                START = False
                PADDLE.loseLife()
                BALL.setPOS(
                    WINDOW.getWidth() // 2 - BALL.getWidth() // 2,
                    460
                )
                BALL.setYDIR(1)
                PADDLE.setPOS(
                    WINDOW.getWidth() // 2 - PADDLE.getWidth() // 2,
                    500
                )
            if PADDLE.getLivesRemaining()==0:
                GAME_OVER = True

            # Ball Collision Logic
            for i in range(len(BRICKS)):
                if BALL.isCollision(BRICKS[i].getSurface(), BRICKS[i].getPOS()) \
                        and BALL.getY() < (BRICKS[i].getY() + 41) and BALL.getY() > (BRICKS[i].getY() + 36) \
                        and (BALL.getX() + BALL.getWidth()) > BRICKS[i].getX() \
                        and BALL.getX() < (BRICKS[i].getX() + 90):
                    BRICKS[i].setPOS(-1000, -1000)
                    DELETED_BRICK_COUNT += 1
                    BALL.setYDIR(1)
                if BALL.isCollision(BRICKS[i].getSurface(), BRICKS[i].getPOS()) \
                        and (BALL.getY() + BALL.getHeight()) > BRICKS[i].getY() and (
                        BALL.getY() + BALL.getHeight()) < (BRICKS[i].getY() + 5) \
                        and (BALL.getX() + BALL.getWidth()) > BRICKS[i].getX() \
                        and BALL.getX() < (BRICKS[i].getX() + 90):
                    BRICKS[i].setPOS(-1000, -1000)
                    DELETED_BRICK_COUNT += 1
                    BALL.setYDIR(-1)
                if BALL.isCollision(BRICKS[i].getSurface(), BRICKS[i].getPOS()) \
                        and (BALL.getX()) < (BRICKS[i].getX() + 91) and (BALL.getX()) > (BRICKS[i].getX() + 86) \
                        and (BALL.getY() + BALL.getHeight()) > BRICKS[i].getY() \
                        and (BALL.getY()) < (BRICKS[i].getY() + 40):
                    BRICKS[i].setPOS(-1000, -1000)
                    DELETED_BRICK_COUNT += 1
                    BALL.setXDIR(1)
                if BALL.isCollision(BRICKS[i].getSurface(), BRICKS[i].getPOS()) \
                        and (BALL.getX() + BALL.getWidth()) > BRICKS[i].getX() and (
                        BALL.getX() + BALL.getWidth()) < (BRICKS[i].getX() + 5) \
                        and (BALL.getX() + BALL.getWidth()) > BRICKS[i].getX() \
                        and BALL.getX() < (BRICKS[i].getX() + 90):
                    BRICKS[i].setPOS(-1000, -1000)
                    DELETED_BRICK_COUNT += 1
                    BALL.setXDIR(-1)

        ### OUTPUTS ###
        if GAME_OVER == True:
            GAME_OVER_TEXT.pulseTextColor(FLASHING_COLOR, [randrange(10)/10, randrange(10)/10, randrange(10)/10])
            WINDOW.getSurface().blit(GAME_OVER_TEXT.getSurface(), GAME_OVER_TEXT.getPOS())
            for i in range(len(BRICKS)):
                BRICKS[i].setPOS(-2000, -2000)
            HELLO.setPOS(-1000, -1000)
            BALL.setPOS(-1000, -1000)
            PADDLE.setPOS(-1000, -1000)
            PADDLE_RIGHT.setPOS(-1000,-1000)

        if DELETED_BRICK_COUNT == 39:
            LEVEL1 = False
            Level2 = True
            DELETED_BRICK_COUNT = 0
            BRICKS = LEVEL_2_BRICKS
            BALL.setPOS(
                WINDOW.getWidth() // 2 - BALL.getWidth() // 2,
                460
            )

        if DELETED_BRICK_COUNT == 30 and Level2:
            BALL.setPOS(-1000, -1000)
            PADDLE.setPOS(-1000, -1000)
            PADDLE_RIGHT.setPOS(-1000, -1000)
            YOU_WIN_TEXT.pulseTextColor(FLASHING_COLOR, [randrange(10)/10, randrange(10)/10, randrange(10)/10])
            WINDOW.getSurface().blit(YOU_WIN_TEXT.getSurface(), YOU_WIN_TEXT.getPOS())


        WINDOW.updateFrame()