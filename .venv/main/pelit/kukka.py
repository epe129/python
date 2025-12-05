import pygame
from math import sin, cos, radians

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("kukka")

screen.fill((255,255,255))

def drawRhodoneaCurve(n, koko):
    pisteet = []
    for i in range(0, 361):
        r = koko * sin(radians(n*i))

        x = r * cos(radians(i))
        y = r * sin(radians(i))

        list.append(pisteet, (400 / 2 + x, 400 / 2 + y))
    
    pygame.draw.lines(screen, (0,0,0), False, pisteet, 1)

peli = True
while peli:
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            peli = False   
  
    def drawPattern():
        drawRhodoneaCurve(12, 200)
    drawPattern()

    pygame.display.update() 

pygame.QUIT()