from . import Piece, Movement

class Horse(Piece):
    def __init__(self, colour, pos, path, Type):
        super().__init__(colour, pos, path)
        self.Type = Type

    def validMove(self, TestVector, TrueVector):
        validMove = Movement.BasicMove(self.Type, self.getcolour(), TestVector, TrueVector)
        return validMove