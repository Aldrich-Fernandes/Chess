import pygame
from support import getVector

class Movement:

    @staticmethod
    def BasicMove(pos, moveToPos, Type, colour): # Pawn, King, Horse
        if Type == "P":
            if colour == "White":
                movelist = (0,-75)
            else: movelist = (0,75)

            vector = tuple(map(lambda x,y : y-x, pos, moveToPos))
            if vector == movelist:
                return True
        elif Type == "K":
            movelist = [(75,75), (75,0), (0, 75)]
            if getVector(pos, moveToPos) in movelist:
                return True
        elif Type == "H":
            pass
        
        return False

    @staticmethod
    def StraightMove(pos, moveToPos):  #Rook, Queen
        vectorX, vectorY = getVector(pos, moveToPos)
        print(pos, (vectorX,vectorY))
        if vectorX == 0 or vectorY == 0:
            return True
        
        return False

    @staticmethod
    def DiagonalMove(pos, moveToPos): # Bishop, Queen
        vectorX, vectorY = getVector(pos, moveToPos)
        if vectorX == vectorY:
            return True
        
        return False
        
