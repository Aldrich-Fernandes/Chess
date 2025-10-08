from . import Piece, Movement

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