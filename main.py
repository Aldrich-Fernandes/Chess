import pygame, sys
from scripts.board import Board
from scripts.player import Player

pygame.init()
Clock = pygame.time.Clock() #Test update

BoardWidth = 600
BoardHight = 600
screen = pygame.display.set_mode((BoardWidth, BoardHight))
background = pygame.image.load(r"Assets/Board.png")
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
    Board.run(player)
        
    turn += 1
    Clock.tick(60)

print(f"{player.getColour()} WINS!!")


