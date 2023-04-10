import pygame
from movement import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, colour, pos, path):
        super().__init__()
        self._colour = colour
        self.__position = pos

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
    
    def validMove(self, moveToPos): # tests if tile is valid 
        return False

class Pawn(Piece):    
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type
    
    def validMove(self, moveToPos):
        validMove = Movement.BasicMove(self.getPos(), moveToPos, self.Type, self.getcolour())
        return validMove

class Horse(Piece):
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type

    def validMove(self, moveToPos):
        validMove = Movement.BasicMove(self.getPos(), moveToPos, self.Type, self.getcolour())
        return validMove

class Rook(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, moveToPos):
        validMove = Movement.StraightMove(self.getPos(), moveToPos)
        return validMove
        
class Bishop(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, moveToPos):
        validMove = Movement.DiagonalMove(self.getPos(), moveToPos)
        return validMove
        
class Queen(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, moveToPos):
        validMove = Movement.StraightMove(self.getPos(), moveToPos) or Movement.DiagonalMove(self.getPos(), moveToPos)
        return validMove
        
class King(Piece):
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type

    def validMove(self, moveToPos):
        validMove = Movement.BasicMove(self.getPos(), moveToPos, self.Type, self.getcolour())
        return validMove
        