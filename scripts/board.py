from piece import *
import pygame, sys


class Board:
    def __init__(self, screen):
        self.__gameOver = False

        self.blackPieces = pygame.sprite.Group()
        self.whitePieces = pygame.sprite.Group()
        self.allPieces = pygame.sprite.Group()

        self.__setUp()
        self.screen = screen

    #SUPPORT METHODS        
    def getSquareCord(self, pos): 
        posX = (pos[0]//75)*75
        posY = (pos[1]//75)*75
        return (posX, posY)

    def checkAtPos(self, pieceList, pos):
        for piece in pieceList:
            if piece.getPos() == pos:
                return True
        return False

    def checkType(self, pos):
        for piece in self.allPieces:
            if piece.getPos() == pos:
                if piece.Type == "H":
                    return "H"
                elif piece.Type == "P":
                    return "P"
        return None
    
    def getDirectionalVector(self, TrueVector):
        dirX = TrueVector[0]
        dirY = TrueVector[1]

        x,y = 0,0
        if dirX < 0:
            x = -75
        elif dirX > 0:
            x = 75
        if dirY < 0:
            y = -75
        elif dirY > 0:
            y = 75
        
        return x,y

    def getVector(self, pos, moveToPos):
        TestVector = tuple(map(lambda x,y : abs(y-x), pos, moveToPos)) # to check if in line with piece movment
        TrueVector = tuple(map(lambda x,y : y-x, pos, moveToPos))
        return TestVector, TrueVector

    def addVectorToPos(self, pos, vector):
        return tuple(map(lambda x,y : x+y, pos, vector))

    #BOARD INTERACTIONS
    def __setUp(self): # sets up board with all piece in its staring position
        board = [
            ["r","h","b","q","k","b","h","r"],
            ["p","p","p","p","p","p","p","p"],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            ["P","P","P","P","P","P","P","P"],
            ["R","H","B","Q","K","B","H","R"],
        ]

        for y in range(len(board)):
            for x, lable in enumerate(board[y]):
                pos = x*75 ,y*75

                if lable == "P":
                    piece = Pawn("White", (pos), r"Assets\PawnW.png", "P")
                elif lable == "R":
                    piece = Rook("White", (pos), r"Assets\RookW.png")
                elif lable == "H":
                    piece = Horse("White", (pos), r"Assets\HorseW.png", "H")
                elif lable == "B":
                    piece = Bishop("White", (pos), r"Assets\BishopW.png")
                elif lable == "Q":
                    piece = Queen("White", (pos), r"Assets\QueenW.png")
                elif lable == "K":
                    piece = King("White", (pos), r"Assets\KingW.png", "K")

                elif lable == "p":
                    piece = Pawn("Black", (pos), r"Assets\PawnB.png", "P")
                elif lable == "r":
                    piece = Rook("Black", (pos), r"Assets\RookB.png")
                elif lable == "h":
                    piece = Horse("Black", (pos), r"Assets\HorseB.png", "H")
                elif lable == "b":
                    piece = Bishop("Black", (pos), r"Assets\BishopB.png")
                elif lable == "q":
                    piece = Queen("Black", (pos), r"Assets\QueenB.png")
                elif lable == "k":
                    piece = King("Black", (pos), r"Assets\KingB.png", "K")
                else:
                    piece = None
                
                if piece != None:
                    if piece.getcolour() == "White":
                        self.whitePieces.add(piece)
                    else:
                        self.blackPieces.add(piece)
                    self.allPieces.add(piece)
  
    def validPath(self, PiecePos, moveToPos, TrueVector):
        dirX, dirY = self.getDirectionalVector((TrueVector))
        posX, posY = PiecePos
        
        while (posX, posY) != moveToPos: # infinite loop breaks game
            posX += dirX 
            posY += dirY 
            if ((posX, posY) == moveToPos or self.checkType(PiecePos) == "H") and self.checkType(PiecePos) != "P":
                return True
                
            if self.checkAtPos(self.allPieces, (posX, posY)): #checks the journey
                print("Obsticle")
                return False
        return False
            
    def gameOver(self):
        return self.__gameOver
    
    def __takePiece(self, colour, pos): # Displays a message if a piece is taken (gameOver = True if king is taken)
        if colour == "White":
            if self.checkAtPos(self.blackPieces, pos):
                for piece in self.blackPieces:
                    if piece.getPos() == pos:
                        if piece.Type == "K":
                            self.__gameOver = True
                        piece.kill()
                        return None
            else:
                return None
        else:
            if self.checkAtPos(self.whitePieces, pos):
                for piece in self.whitePieces:
                    if piece.getPos() == pos:
                        if piece.Type == "K":
                            self.__gameOver = True
                        piece.kill()
                        return None
            else:
                return None

    def __upgradePiece(self, piece): # replaces the pawn with a queen.
        if piece.Type == "P":
            if piece.getcolour() == "White" and piece.getPos()[1] == 0:
                pos = piece.getPos()
                piece.kill()
                newPiece = Queen("White", (pos), r"Assets\QueenW.png")
                self.whitePieces.add(newPiece)
                self.allPieces.add(newPiece)
            elif piece.getcolour() == "Black" and piece.getPos()[1] == 525:
                pos = piece.getPos()
                piece.kill()
                newPiece = Queen("White", (pos), r"Assets\QueenB.png")
                self.blackPieces.add(newPiece)
                self.allPieces.add(newPiece)

    #MOVING PIECES
    def getChoosenPiece(self, player, pieceList):
        choosenPiece = None
        while choosenPiece == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.getSquareCord(pygame.mouse.get_pos())
                    choosenPiece = player.choosePiece(pos, pieceList)                   
                    
        return choosenPiece
    
    def getMoveTo(self, choosenPiece, pieceList):
        moveToPos = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    moveToPos = self.getSquareCord(pygame.mouse.get_pos())
                    TestVector, TrueVector = self.getVector(choosenPiece.getPos(), moveToPos)

                    if not self.checkAtPos(pieceList, moveToPos): # check if own piece at the pos
                        if choosenPiece.Type == "P":
                            if choosenPiece.getcolour() == "White":
                                enemyList = self.blackPieces
                            else:
                                enemyList = self.whitePieces
                                                        
                            if self.checkAtPos(enemyList, moveToPos):
                                isAttacking = True
                            else:
                                isAttacking = False
                            
                            if choosenPiece.validMove(TestVector, TrueVector, isAttacking):
                                return moveToPos
                            
                        elif choosenPiece.validMove(TestVector, TrueVector): # checks if the piece is able to move to the positio
                            if self.validPath(choosenPiece.getPos(), moveToPos, TrueVector):
                                return moveToPos
                            else:
                                print("Another piece in the way")
                                return None
                        else:
                            print("Invalid square")
                            return None
                    else:
                        print("Square occupied")
                        return None

    #MAIN GAME LOOP
    def run(self, player):
        self.whitePieces.draw(self.screen)
        self.blackPieces.draw(self.screen)
        pygame.display.update()

        if player.getColour() == "White":
            pieceList = self.whitePieces
        else:
            pieceList = self.blackPieces

        choosenPiece, moveToPos = None, None

        while choosenPiece == None or moveToPos == None:
            choosenPiece = self.getChoosenPiece(player, pieceList) #chooses only your own piece
            moveToPos = self.getMoveTo(choosenPiece, pieceList)#pos that  is not on own piece and is a valid move
        choosenPiece.updatePos(moveToPos)

        self.__takePiece(player.getColour(), moveToPos)
        self.__upgradePiece(choosenPiece)