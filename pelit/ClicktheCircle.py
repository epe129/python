import random
import pygame


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Circle")

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 32)


def new_circle():
    radius = 30
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    return x, y, radius


circle_x, circle_y, circle_r = new_circle()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5

            if distance <= circle_r:
                score += 1
                circle_x, circle_y, circle_r = new_circle()

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), circle_r)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()
