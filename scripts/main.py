import pygame, sys
from board import Board
from player import Player


pygame.init()
Clock = pygame.time.Clock()

BoardWidth = 600
BoardHight = 600
screen = pygame.display.set_mode((BoardWidth, BoardHight))
background = pygame.image.load(r"Assets\Board.png")
pygame.display.set_caption("Chess")

Board = Board(screen)

Player1 = Player("White")
Player2 = Player("Black")
Players = [Player1, Player2]
turn = 2

while not Board.gameOver():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #Test
    
    screen.blit(background, (0,0))

    player = Players[turn % 2]
    print(f"{player.getColour()}'s turn")
    Board.run(player)
    turn += 1

    Clock.tick(60)