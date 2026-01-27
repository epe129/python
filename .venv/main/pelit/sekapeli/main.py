import pygame
from number import main

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("game")

width = screen.get_width()

height = screen.get_height()

# colors
black = (0,0,0)
grey = (211, 211, 211)
white = (255, 255, 255)

font = pygame.font.SysFont('Corbel', 60)

otsikko = font.render('Play diffrent games' , True , black)

numeroPeli = font.render('QuestNumber' , True , black)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(white)
        
        mouse = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if 350 <= mouse[0] <= 350+400 and 300<= mouse[1] <= 300+40:
                main()
           
    screen.blit(otsikko, (300, 150))
    
    pygame.draw.rect(screen, grey,
                 [345, 290, 300, 60], 0, border_radius=10)
    screen.blit(numeroPeli, (350, 300))
    
    pygame.display.update()

pygame.quit()