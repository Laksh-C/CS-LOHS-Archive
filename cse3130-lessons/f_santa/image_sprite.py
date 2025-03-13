# image_sprite.py in f_santa
"""
title: image Sprite class
author: Laksh Chopra
date-created: 15/1/24
"""

from my_sprite import MySprite
import pygame

class ImageSprite(MySprite):
    def __init__(self, IMAGE_FILE, LOOKING_RIGHT=True):
        MySprite.__init__(self)
        self.__FILE_NAME = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_NAME).convert_alpha()
        self.__LOOKING_RIGHT = LOOKING_RIGHT # Looking to the left



    # MODIFIER METHOD
    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Adjust the scale of the image
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE,(self._SURFACE.get_width() * SCALE_X,
                                              self._SURFACE.get_height()*SCALE_Y)
)

    def WASDmove(self, KEY_PRESSES):
        # polymorphism to flip the image if necessary
        MySprite.WASDmove(self, KEY_PRESSES)
        if  KEY_PRESSES[pygame.K_d] == 1 and self.__LOOKING_RIGHT is False:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__LOOKING_RIGHT = True
        if KEY_PRESSES[pygame.K_a] == 1 and self.__LOOKING_RIGHT is True:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__LOOKING_RIGHT = False




if __name__ == "__main__":
    from window import Window
    pygame.init()
    from random import randrange

    WINDOW = Window("Santa")
    SANTA = ImageSprite("media/santa.png", False)
    SANTA.setScale(0.5)
    GIFT_1 = ImageSprite("media/gift1.png", False)
    GIFT_1.setScale(0.25)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEYS_PRESSED = pygame.key.get_pressed()
        SANTA.WASDmove(KEYS_PRESSED)

        if GIFT_1.isCollision(SANTA.getSurface(), SANTA.getPOS()):
            GIFT_1.setPOS(
                randrange(WINDOW.getWidth()-GIFT_1.getSurface().get_width()),
                randrange(WINDOW.getHeight()-GIFT_1.getSurface().get_height())
            )

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(SANTA.getSurface(), SANTA.getPOS())
        WINDOW.getSurface().blit(GIFT_1.getSurface(), GIFT_1.getPOS())
        WINDOW.updateFrame()
