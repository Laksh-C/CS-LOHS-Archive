# player_sprite.py in f_santa
"""
title: Composite player sprite
author: Laksh Chopra
date-created: 17/01/24
"""
import pygame
from box import Box
from image_sprite import ImageSprite
from my_sprite import MySprite

class Player(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__IMAGE = ImageSprite(IMAGE_FILE, False)
        self.__HIT_BOX = Box(self.__IMAGE.getWidth()//2, self.__IMAGE.getHeight()//2)

        self.__HIT_BOX.setPOS(
            self.getX() + self.__IMAGE.getWidth()//2 - self.__HIT_BOX.getWidth()//2,
            self.getY() + self.__IMAGE.getHeight()//2 - self.__HIT_BOX.getHeight()//2
        )
        self._SURFACE = self.__IMAGE.getSurface()
        """self.__HAND_HIT_BOX = Box(20, 20)
        self.__HAND_HIT_BOX.setPOS(
            self.getX() + self.__IMAGE.getWidth()  - self.__HAND_HIT_BOX.getWidth(),
            self.getY() + self.__IMAGE.getHeight() - self.__HAND_HIT_BOX.getHeight()
        )"""


    # --- MODIFIER METHODS --- #
    def setX(self, X):
        MySprite.setX(self, X)
        self.__IMAGE.setX(X)
        self.__HIT_BOX.setX(
            self.getX() + self.__IMAGE.getWidth() // 2 - self.__HIT_BOX.getWidth() // 2
        )

    def setY(self, Y):
        MySprite.setY(self, Y)
        self.__IMAGE.setY(Y)
        self.__HIT_BOX.setY(
            self.getY() + self.__IMAGE.getHeight() // 2 - self.__HIT_BOX.getHeight() // 2
        )

    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def setScale(self, SCALE_X, SCALE_Y = 0):
        self.__IMAGE.setScale(SCALE_X, SCALE_Y)
        self.__HIT_BOX = Box(self.__IMAGE.getWidth()//2, self.__IMAGE.getHeight()//2)
        self._SURFACE = self.__IMAGE.getSurface()
        self.setPOS(self.getX(), self.getY())


    def WASDmove(self, KEY_PRESSES):
        MySprite.WASDmove(self, KEY_PRESSES)
        self.__IMAGE.WASDmove(KEY_PRESSES)
        self.setPOS(self.getX(), self.getY())


    # --- ACCESSOR METHODS --- #
    def getSurface(self):
        return self.__IMAGE.getSurface()

    def getHitBox(self):
        return self.__HIT_BOX.getSurface()

    def getHitBoxPOS(self):
        return self.__HIT_BOX.getPOS()

    def isCollision(self, SURFACE, POS):
        return self.__HIT_BOX.isCollision(SURFACE, POS)

    def getHandHitBox(self):
        return self.__HAND_HIT_BOX.getSurface()

    def getHandHitBoxPos(self):
        return self.__HAND_HIT_BOX.getPOS()


if __name__ == "__main__":
    from window import Window
    from random import randrange
    pygame.init()

    WINDOW = Window("Composite Sprites")
    PLAYER = Player("media/santa.png")
    TREE = Player("media/tree.png")
    ORNAMENT = Player("media/decoration1.png")

    PLAYER.setScale(0.5)
    PLAYER.setPOS(100,100)


    ORNAMENT.setScale(0.05)
    ORNAMENT.setPOS(
        randrange(WINDOW.getWidth()-ORNAMENT.getWidth()),
        randrange(WINDOW.getHeight()-ORNAMENT.getHeight())
    )

    TREE.setScale(0.13)
    TREE.setPOS(
        WINDOW.getWidth() // 2 - TREE.getWidth() // 2,
        WINDOW.getHeight() // 2 - TREE.getHeight() // 2
    )

    GIFT_1 = Player("media/gift1.png")
    GIFT_1.setScale(0.24)
    GIFT_1.setPOS(
        randrange(WINDOW.getWidth()-GIFT_1.getWidth()),
        randrange(WINDOW.getWidth()-GIFT_1.getHeight())
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        PRESSED_KEYS = pygame.key.get_pressed()
        PLAYER.WASDmove(PRESSED_KEYS)
        if PLAYER.isCollision(GIFT_1.getHitBox(), GIFT_1.getHitBoxPOS()):
            GIFT_1.WASDmove(PRESSED_KEYS)
            print("HIT!")

        if PLAYER.isCollision(ORNAMENT.getHitBox(), ORNAMENT.getHitBoxPOS()):
            ORNAMENT.WASDmove(PRESSED_KEYS)
            print("Ornament Moved!")



        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TREE.getSurface(), TREE.getPOS())
        WINDOW.getSurface().blit(ORNAMENT.getSurface(), ORNAMENT.getPOS())
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.getSurface().blit(GIFT_1.getSurface(), GIFT_1.getPOS())
        #WINDOW.getSurface().blit(PLAYER.getHandHitBox(), PLAYER.getHandHitBoxPos())
        #WINDOW.getSurface().blit(PLAYER.getHitBox(), PLAYER.getHitBoxPOS())
        #WINDOW.getSurface().blit(GIFT_1.getHitBox(), GIFT_1.getHitBoxPOS())
        #WINDOW.getSurface().blit(ORNAMENT.getHitBox(), ORNAMENT.getHitBoxPOS())
        #WINDOW.getSurface().blit(TREE.getHitBox(), TREE.getHitBoxPOS())
        WINDOW.updateFrame()



