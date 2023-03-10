import pygame
from Package.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED,WHITE
from Package.board import Board
from Package.game import Game
from minimax.algorithm import minimax
pygame.font.init()
FPS=60

WIN = pygame.display.set_mode((WIDTH+300,HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x,y=pos
    row =y //SQUARE_SIZE
    col =x //SQUARE_SIZE  
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    game=Game(WIN)
   
    while run:
        clock.tick(FPS)
        if game.turn==WHITE:
            value,new_board = minimax(game.get_board(),3,WHITE,game)
            game.ai_move(new_board)

        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
            if event.type== pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)

        
        game.update()
            
    pygame.quit()

main()