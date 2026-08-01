import pygame

pygame.init()

screen = pygame.display.set_mode((2000, 1000))
pygame.display.set_caption("Click the Circle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(f"Mouse clicked at: {mouse_pos}")

pygame.quit()
