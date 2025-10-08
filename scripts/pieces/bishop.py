from . import Piece, Movement

class Bishop(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.DiagonalMove(TestVector)
        return validMove