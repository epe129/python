import pygame
from number import main

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("game")

width = screen.get_width()

height = screen.get_height()

# white black
black = (0,0,0)

white = (255, 255, 255)

smallfont = pygame.font.SysFont('Corbel',35)

text = smallfont.render('QuestNumber' , True , black)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(white)
        
        mouse = pygame.mouse.get_pos()

        posotion_y = width/2-50
        posotion_x = height/3
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if posotion_y <= mouse[0] <= posotion_y+140 and posotion_x <= mouse[1] <= posotion_x+20:
                main()
           
    
    screen.blit(text , (posotion_y,posotion_x))
    
    pygame.display.update()

        

pygame.quit()