import pygame

pygame.init()

pygame.display.set_caption("Kissa")
pygame.display.set_mode((550,550))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           game = False
           
    pygame.display.update()

pygame.QUIT()