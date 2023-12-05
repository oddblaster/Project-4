import pygame, sys
from board import Board


WIDTH = 600
HEIGHT = 600
def main():
    print("HELLO WORLD!")
class Button:
    def __init__(self,x,y,text_size, text=''):

        self.x = x
        self.y = y
        self.text = text
        self.text_size = text_size

    def draw(self):
        button_font = pygame.font.Font(None,self.text_size)

        button_text = button_font.render(self.text,0,(0,0,255))

        frame_size = [i + 20 for i in button_text.get_size()]
        button_surface = pygame.Surface(frame_size)
        button_surface.fill("Orange")


        button_surface.blit(button_text,(10,10))
        button_rect = button_surface.get_rect(center = (self.x,self.y))

        screen.blit(button_surface, button_rect)



  
    


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH ,HEIGHT))
    
    screen.fill("White")

    start_title_font = pygame.font.Font(None,100)
    button_start_font = pygame.font.Font(None,70)
    button_quit_font = pygame.font.Font(None,70)

    title_surface = start_title_font.render("Sudoku",0,"Red")
    title_rectangle = title_surface.get_rect(center=(WIDTH//2, HEIGHT//2-150))

    
    quit_text = button_quit_font.render("Quit",0,(255,255,255))


    start = Button(WIDTH//2,HEIGHT//2 + 50,70,"Start")
    exit = Button(WIDTH//2,HEIGHT//2 + 150,70,"Exit")
    start.draw()
    exit.draw()

    chip_font = pygame.font.Font(None,100)
    chip_num = chip_font.render('x',0,"Black")
    
   
   
    rect = chip_num.get_rect(center=(300,300))
    
    pygame.display.set_caption("Sudoku")

    screen.blit(title_surface, title_rectangle)


    #loser = button()
    in_game = False
    in_menu = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and in_menu == True:

                if event.pos[1] < 383 and event.pos[1] > 316:
                    if event.pos[0] > 231 and event.pos[0] < 365: 
                        screen.fill("White")
                        in_menu = False

                elif event.pos[1] < 483 and event.pos[1] > 417:
                    if event.pos[0] < 357 and event.pos[0] > 243:
                        sys.exit()
            elif in_menu == False:
                easy_button = Button(WIDTH//2,HEIGHT//3,70,"EASY")
                medium_button = Button(WIDTH//2,HEIGHT//3+100,70,"MEDIUM")
                hard_button = Button(WIDTH//2,HEIGHT//3+200,70,"HARD")

                easy_button.draw()
                medium_button.draw()
                hard_button.draw()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[1] < 233 and event.pos[1] > 166:
                        if event.pos[0] > 190 and event.pos[0] < 292:
                            in_game = True
                            screen.fill("White")
                            newboard = Board(600,600,screen,"Easy")
                    elif event.pos[1] < 268 and event.pos[1] > 335:
                        if event.pos[0] > 193 and event.pos[0] < 289: 
                            in_game = True
                            screen.fill("White")
                            newboard = Board(600,600,screen,"Medium")
                    elif event.pos[1] < 434 and event.pos[1] > 368:
                        if event.pos[0] > 220 and event.pos[0] < 381: 
                            in_game = True
                            screen.fill("White")
                            newboard = Board(600,600,screen,"Hard")
                while in_game == True:
                    newboard.draw()

                #print(f"Keyboard: {newboard.click(x,y)}")
        pygame.display.update()