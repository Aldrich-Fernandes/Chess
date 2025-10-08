from . import Piece, Movement

class Rook(Piece):
    def __init__(self, colour, pos, path):
        super().__init__(colour, pos, path)
    
    def validMove(self, TestVector, TrueVector):
        validMove = Movement.StraightMove(TestVector)
        return validMove