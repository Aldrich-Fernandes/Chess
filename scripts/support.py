def getSquareCord(pos): 
    posX = (pos[0]//75)*75
    posY = (pos[1]//75)*75
    return (posX, posY)

def checkAtPos(pieceList, pos):
    for piece in pieceList:
        if piece.getPos() == pos:
            return True
    return False

def getVector(pos, moveToPos):
    vector =  tuple(map(lambda x,y : abs(y-x), pos, moveToPos))
    print(vector)
    return vector