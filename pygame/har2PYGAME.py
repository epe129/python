# import pygame

# pygame.init()

# onko = pygame.get_init()

# print(onko)

import pygame
# tuomme pygame-moduulin
pygame.init()
# asetamme nöytön koon # pygame.RESIZABLE antaa koon muuntamisen luvan
n = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

# määrittää väri
color = "red"

# asettaa otsikon 
pygame.display.set_caption("asd")
a = pygame.image.load("a.png")
# ikkuna kuvakkeen muuntaminen
pygame.display.set_icon(a) 

c = (255,255,255)
# antaa näytön normaalin koon
# x, y = n.get_size()

# k = pygame.Surface.copy(n)

Käynnissä = True
# Pelin silmukka niin kaun käynnissä kun peli suljetaan
while Käynnissä:
    # Tarkista tapahtuma, jos käyttäjä on työntänyt 
    # tapaus jonossa
    for event in pygame.event.get():
        # jos painaa x niin lopettaa
        if event.type == pygame.QUIT:
            Käynnissä = False
    
    # piirtää ympyrän näytölle
    # pygame.draw.circle(n, (0,0,0), (300, 200), 75)
    
    # n.fill(color)
    # pygame.Surface.set_colorkey(a, [255,255,255])   
    n.blit(a,(100,100))
    # piirretään neliö
    pygame.draw.rect(n, c, pygame.Rect(20,20,40,40))
    
    # muuttaa pikseleiden kuvan muotoa
    # pygame.Surface.convert(n)
    # pygame.Surface.convert_alpha(n)
    

    pygame.display.update()

    # vaihtaa väriä sen mukaan mikä se on
    # if color == "red":
    #     color = "green"
    # else:
    #     color = "red" 


# print(x, y)