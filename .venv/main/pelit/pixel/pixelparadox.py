import pygame
from pygame.locals import *

pygame.init()

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

running = True

player = pygame.image.load("player2.png").convert()

player_SIZE = (150, 150)

player = pygame.transform.scale(player, player_SIZE)

x, y = 0, 0
move_x, move_y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == KEYDOWN:
        if event.key == K_LEFT:  
            move_x = -0.3 
            print("pressed LEFT")
        elif event.key == K_RIGHT:  
            move_x = +0.3  
            print("pressed RIGHT")
        elif event.key == K_UP: 
            move_y = -0.3  
            print("pressed UP")
        elif event.key == K_DOWN: 
            move_y = +0.3  
            print("pressed DOWN")
    
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 1000 - player_SIZE[0]:
        x = 1000 - player_SIZE[0]
    if y > 800 - player_SIZE[1]:
        y = 800 - player_SIZE[1]

    print(f"move_x: {x}, move_y: {y}")

    if event.type == KEYUP:
        if event.key == K_LEFT:
            move_x = 0  
        elif event.key == K_RIGHT:  
            move_x = 0  
        elif event.key == K_UP: 
            move_y = 0  
        elif event.key == K_DOWN:  
            move_y = 0  
    x += move_x
    y += move_y    
    screen.fill((255, 255, 255))
    screen.blit(player, (x, y))
    pygame.display.update()
pygame.quit()