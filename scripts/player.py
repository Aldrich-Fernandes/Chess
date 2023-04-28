class Player():
    def __init__(self, colour): 
        self._colour = colour # "black" or "white"

    def getColour(self): 
        return self._colour
    
    def choosePiece(self, mousePos, pieceList):
        for piece in pieceList:
            if piece.getPos() == mousePos:
                choosenPiece = piece
                return choosenPiece        

    def __getPos(): # checks if the location is valid and makes the move
        pass