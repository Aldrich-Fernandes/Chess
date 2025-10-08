from . import Piece, Movement

class Queen(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.StraightMove(TestVector) or Movement.DiagonalMove(TestVector)
        return validMove