import pygame
from movement import *

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
    
class Pawn(Piece):    
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type
        self.FirstMove = True
    
    def validMove(self, TestVector, TrueVector, isAttacking):
        validMove = Movement.BasicMove(self.Type, self.getcolour(), TestVector, TrueVector, self.FirstMove, isAttacking)
        if self.FirstMove and validMove:
            self.FirstMove = False
        return validMove

class Horse(Piece):
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type

    def validMove(self, TestVector, TrueVector):
        validMove = Movement.BasicMove(self.Type, self.getcolour(), TestVector, TrueVector)
        return validMove

class Rook(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.StraightMove(TestVector)
        return validMove
        
class Bishop(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.DiagonalMove(TestVector)
        return validMove
        
class Queen(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.StraightMove(TestVector) or Movement.DiagonalMove(TestVector)
        return validMove
        
class King(Piece):
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type

    def validMove(self, TestVector, TrueVector):
        validMove = Movement.BasicMove(self.Type, self.getcolour(), TestVector, TrueVector)
        return validMove