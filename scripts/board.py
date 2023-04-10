from piece import *
from support import getSquareCord, checkAtPos
import pygame, sys

class Board:
    def __init__(self, screen):
        self.__gameOver = False

        self.blackPieces = pygame.sprite.Group()
        self.whitePieces = pygame.sprite.Group()
        self.__setUp()
        self.screen = screen


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

    
    def gameOver(self):
        return self.__gameOver
    
    def __takePiece(): # Displays a message if a piece is taken (gameOver = True if king is taken)
        pass

    def __upgradePiece(): # replaces the pawn with a queen.
        pass

    def getChoosenPiece(self, player, pieceList):
        choosenPiece = None
        while choosenPiece == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = getSquareCord(pygame.mouse.get_pos())
                    choosenPiece = player.choosePiece(pos, pieceList)
        return choosenPiece
    
    def getMoveTo(self, choosenPiece, pieceList):
        moveToPos = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    moveToPos = getSquareCord(pygame.mouse.get_pos())
                    if not checkAtPos(pieceList, moveToPos): # check if own piece at the pos
                        if choosenPiece.validMove(moveToPos): # checks if the piece is able to move to the position
                            return moveToPos
                        else:
                            print("Invalid square")
                            return None
                    else:
                        print("Square occupied")
                        return None
           
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
            moveToPos = self.getMoveTo(choosenPiece, pieceList)#pos that  is not on own piece 
        choosenPiece.updatePos(moveToPos)
        
        
                


