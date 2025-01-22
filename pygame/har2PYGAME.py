# import pygame

# pygame.init()

# onko = pygame.get_init()

# print(onko)

import pygame

import sys

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

# c = (255,255,255)
# antaa näytön normaalin koon
# x, y = n.get_size()

# k = pygame.Surface.copy(n)

# kuvapinnan asettaminen näytön pinnalle 
# # tehdään valkoinen värillinen osa pinnasta 
# # läpinäkyvänä
# pygame.Surface.set_colorkey(a, [255,255,255])

# asettaa kuinka hyvin kuva näkyy 0 läpinäkyvä 
pygame.Surface.set_alpha(a, 1)

# tulostaa väriavaimen arvon surfacesta
# print(pygame.Surface.get_colorkey(a))
# print(pygame.Surface.get_alpha(a))

# pygame.time.wait(5000)

def drawingfucntion(x,y,width,height):

    # creating rectangle using the draw.rect() method
    pygame.draw.rect(n, (0,0,255), [x , y, width, height])

    # calculation the center of the circle
    circle_x = width/2 + x
    circle_y = height/2 + y

    # calculating the radius of the circle
    if height < width:
        radius = height/2
    else:
        radius = width/2

    # drawing the circle
    pygame.draw.circle(n, (0,255,0), [circle_x, circle_y], radius)


Käynnissä = True
# Pelin silmukka niin kaun käynnissä kun peli suljetaan
while Käynnissä:
    # Tarkista tapahtuma, jos käyttäjä on työntänyt 
    # tapaus jonossa
    for event in pygame.event.get():
        # jos painaa x niin lopettaa
        if event.type == pygame.QUIT:
            Käynnissä = False
    n.fill((255,255,255))

    drawingfucntion(50,200,500,200)

    # piirtää ympyrän näytölle
    # pygame.draw.circle(n, (0,0,0), (300, 200), 75)
    
    # n.fill(color)
    # pygame.Surface.set_colorkey(a, [255,255,255])   
    # n.blit(a,(100,100))
    # piirretään neliö
    # pygame.draw.rect(n, c, pygame.Rect(20,20,40,40))
    
    # muuttaa pikseleiden kuvan muotoa
    # pygame.Surface.convert(n)
    # pygame.Surface.convert_alpha(n)
    # 

    # käyttää draw.rect moduulia
    # piirtämään hahmotellun suorakulmion
    # [100,100,350,100] paikka ja koko
    # 2 reunojen paksuus
    # pygame.draw.rect(n, (0,0,255), [100,100,350,100],0)

    # piirretääm ympyrä käyttäen draw.rect toimintoa
    # pygame.draw.circle(n, (0,255,0),[300,300], 170, 0)

    # piirretään monikulmio draw.polugon()

    # pygame.draw.polygon(n, [255,0,0],[[300,300], [100,100], [100,300]], 1)

    # piirretään viiva
    # pygame.draw.line(n, (0,0,0), [100,300],[300,300], 1)

    # pygame.draw.rect(n, (0,0,255), [50,200,400,200])
    # pygame.draw.circle(n, (0,255,0), [250,300], 50)

    # rl = [pygame.Rect(50,100,500,200),
    #       pygame.Rect(70,120,460,160),
    #       pygame.Rect(90,140,420,120),
    #       pygame.Rect(110,160,380,80),
    #       pygame.Rect(130,190,340,40),
    # ] 

    # color = [(0,0,0),
    #          (255,255,255),
    #          (0,0,255),
    #          (0,255,0),
    #          (255,0,0),
    #          ]
    
    # color_var = 0

    # for r in rl:

    #     pygame.draw.rect(n, color[color_var],r)

    #     color_var += 1

    
    pygame.display.update()

    # vaihtaa väriä sen mukaan mikä se on
    # if color == "red":
    #     color = "green"
    # else:
    #     color = "red" 


# print(x, y)