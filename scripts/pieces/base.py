from . import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, colour, pos, path):
        super().__init__()
        self._colour = colour
        self.__position = pos
        self.Type = None

        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.__position
    
    def getcolour(self):
        return self._colour
    
    def getPos(self):
        return self.__position
    
    def updatePos(self, movePos):
        self.__position = movePos
        self.rect.topleft = self.__position
    
    def validMove(self, TestVector, TrueVector): # tests if tile is valid 
        return False