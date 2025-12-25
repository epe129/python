import pygame

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Guest the number")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit Pygame
    pygame.quit()
