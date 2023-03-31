from piece import *
from os import system
import pygame, sys

class Board:
    def __init__(self, screen):
        self.__columns = 8
        self.__rows = 8
        self.__gameOver = False

        self.blackPieces = pygame.sprite.Group()
        self.whitePieces = pygame.sprite.Group()
        self.__setUp()
        self.screen = screen

    def getWidth(self):
        return self.__columns
    
    def getHeight(self):
        return self.__rows
    
    def gameOver(self):
        return self.__gameOver

    def movePiece(self, piece, startPos, endPos): # attempts the move, if relaying if it is valid or not 
        pass

    def __takePiece(): # Displays a message if a piece is taken (gameOver = True if king is taken)
        pass

    def __upgradePiece(): # replaces the pawn with a queen.
        pass

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
                    piece = Pawn("White", (pos), r"Assets\PawnW.png", "P", 1)
                elif lable == "R":
                    piece = Rook("White", (pos), r"Assets\RookW.png", "R", 7)
                elif lable == "H":
                    piece = Horse("White", (pos), r"Assets\HorseW.png", "H", 3)
                elif lable == "B":
                    piece = Bishop("White", (pos), r"Assets\BishopW.png", "B", 7)
                elif lable == "Q":
                    piece = Queen("White", (pos), r"Assets\QueenW.png", "Q", 7)
                elif lable == "K":
                    piece = King("White", (pos), r"Assets\KingW.png", "K", 1)
                elif lable == "p":
                    piece = Pawn("Black", (pos), r"Assets\PawnB.png", "P", 1)
                elif lable == "r":
                    piece = Rook("Black", (pos), r"Assets\RookB.png", "R", 7)
                elif lable == "h":
                    piece = Horse("Black", (pos), r"Assets\HorseB.png", "H", 3)
                elif lable == "b":
                    piece = Bishop("Black", (pos), r"Assets\BishopB.png", "B", 7)
                elif lable == "q":
                    piece = Queen("Black", (pos), r"Assets\QueenB.png", "Q", 7)
                elif lable == "k":
                    piece = King("Black", (pos), r"Assets\KingB.png", "K", 1)
                else:
                    piece = None
                
                board[y][x] = piece
                if piece != None:
                    if piece.getcolour() == "White":
                        self.whitePieces.add(piece)
                    else:
                        self.blackPieces.add(piece)
        return board    
    
    def checkAtPos(self, pieceList, pos):
        for piece in pieceList:
            if piece.getPos() == pos:
                return True
            
        return False
        
    def run(self, player):
        self.whitePieces.draw(self.screen)
        self.blackPieces.draw(self.screen)
        pygame.display.update()

        if player.getColour() == "White":
            pieceList = self.whitePieces
        else:
            pieceList = self.blackPieces
        choosenPiece = None
        moveToPos = None

        while choosenPiece == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = getSquareCord(pygame.mouse.get_pos())
                    choosenPiece = player.choosePiece(pos, pieceList)
        
        while moveToPos == None:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    moveToPos = getSquareCord(pygame.mouse.get_pos())
                    if not self.checkAtPos(pieceList, moveToPos):
                        if choosenPiece.validMove(moveToPos): # checks if the piece is able to move to the position

                            choosenPiece.updatePos(moveToPos)

def getSquareCord(pos): #Test
    posX = (pos[0]//75)*75
    posY = (pos[1]//75)*75
    return (posX, posY)