import pygame, random

pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]

x = 410 
y = 440 

kuva = pygame.display.set_mode((500,500))
pygame.display.set_caption("Lumipalloja")

lumipallot = []
punaisetPallot = []

for c in range(70):
    q = random.randrange(0, 500)
    w = random.randrange(0, 500)
    lumipallot.append([q,w])

for punainen in range(22):
    d = random.randrange(0, 500)  # X-koordinaatti
    f = random.randrange(-800, -50)  # Y-koordinaatti yläpuolella
    liian_lahella = False
    for pallo in punaisetPallot:
        # Tarkistetaan, että uusi pallo ei ole liian lähellä muita palloja
        if abs(d - pallo[0]) < 50 and abs(f - pallo[1]) < 100:  # Vähintään 40 pikselin väli
            liian_lahella = True          
    if not liian_lahella:
        punaisetPallot.append([d, f])
        

kello = pygame.time.Clock()

loppu = False

while not loppu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loppu = True

    kuva.fill(BLACK)
    
    for c in range(len(lumipallot)):
        pygame.draw.circle(kuva, WHITE, lumipallot[c], 2)
        
        lumipallot[c][1] += 1

        if lumipallot[c][1] > 500:
            q = random.randrange(-800, -50)
            lumipallot[c][1] = q

            w = random.randrange(0, 500)
            lumipallot[c][0] = w
    
    for punainen in range(len(punaisetPallot)):
        pygame.draw.circle(kuva, RED, punaisetPallot[punainen], 20,20)
        
        punaisetPallot[punainen][1] += 1

        if punaisetPallot[punainen][1] > 500:
            d = random.randrange(-50, -10)
            punaisetPallot[punainen][1] = d

            f = random.randrange(0, 500)
            punaisetPallot[punainen][0] = f
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0:
        x -= 5
               
    if keys[pygame.K_RIGHT] and x < 500 - 50:
        x += 5
    
    for punainen in punaisetPallot:
        if x < punainen[0] + 20 and x + 50 > punainen[0] - 20 and y < punainen[1] + 20 and y + 50 > punainen[1] - 20:
            loppu = True
            break
        
   
    pygame.draw.rect(kuva, RED, pygame.Rect(x, y, 50, 50))
    pygame.display.update()
    
    kello.tick(100)

pygame.quit()