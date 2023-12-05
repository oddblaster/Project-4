import pygame, sys
from constants import*
from board import Board
def main():
    print("HELLO WORLD!")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    
    screen.fill("White")

    start_title_font = pygame.font.Font(None,100)
    button_start_font = pygame.font.Font(None,70)
    button_quit_font = pygame.font.Font(None,70)

    title_surface = start_title_font.render("Sudukou",0,"Red")
    title_rectangle = title_surface.get_rect(center=(600//2,600//2-150))

    
    
    start_text = button_start_font.render("Start",0,(255,255,255))
    quit_text = button_quit_font.render("Quit",0,(255,255,255))

    print( start_text.get_size()[0])
 
    start_surface = pygame.Surface(start_text.get_size())
    start_surface.fill((0,0,0))
    start_rect = start_surface.get_rect()
    
    screen.blit(title_surface, title_rectangle)
    start_surface.blit(start_text,(10,10))
    

    newboard = Board(600,600,screen,"Hard")
    
    #newboard.draw()

    chip_font = pygame.font.Font(None,100)
    chip_num = chip_font.render('x',0,"Black")
    

    rect = chip_num.get_rect(center=(300,300))

    screen.blit(chip_num, rect) 

    pygame.display.set_caption("Sudoku")

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(f"Keyboard: {newboard.click(x,y)}")
        pygame.display.update()