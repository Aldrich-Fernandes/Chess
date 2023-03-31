import pygame
from movement import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, colour, pos, path, Type, maxMove):
        super().__init__()
        self._colour = colour
        self.__position = pos
        self.__maxMove = maxMove
        self.Type = Type

        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.__position
    
    def getMaxMoves(self):
        return self.__maxMove
    
    def getcolour(self):
        return self._colour
    
    def getPos(self):
        return self.__position
    
    def updatePos(self, movePos):
        self.__position = movePos
        self.rect.topleft = self.__position
    
    def validMove(self): # tests if tile is valid 
        pass


class Pawn(Piece):    
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, moveToPos):
        validMove = BasicMovement()

class Horse(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)

class Rook(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
        

class Bishop(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
        

class Queen(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
        

class King(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
        