# import pygame

# pygame.init()

# onko = pygame.get_init()

# print(onko)

import pygame
from pygame.locals import *

# import sys

# tuomme pygame-moduulin
pygame.init()
# asetamme nöytön koon # pygame.RESIZABLE antaa koon muuntamisen luvan
# n = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

# määrittää väri
# color = (0,0,255)

white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
black = (0,0,0)
red = (255,0,0)

# assingning values to x and y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension (X,Y)
d = pygame.display.set_mode((X,Y))

# asettaa otsikon 
pygame.display.set_caption("asd")
# a = pygame.image.load("a.png")
# # ikkuna kuvakkeen muuntaminen
# pygame.display.set_icon(a) 

# creating list in which we will store
# the position of the circle 
# circle_positions = []
d.fill(white)

# # radius of the circle
# circle_radius = 60

# c = (255,255,255)
# antaa näytön normaalin koon
# x, y = n.get_size()

# k = pygame.Surface.copy(n)

# kuvapinnan asettaminen näytön pinnalle 
# # tehdään valkoinen värillinen osa pinnasta 
# # läpinäkyvänä
# pygame.Surface.set_colorkey(a, [255,255,255])

# asettaa kuinka hyvin kuva näkyy 0 läpinäkyvä 
# pygame.Surface.set_alpha(a, 1)

# tulostaa väriavaimen arvon surfacesta
# print(pygame.Surface.get_colorkey(a))
# print(pygame.Surface.get_alpha(a))

# pygame.time.wait(5000)

# def drawingfucntion(x,y,width,height):

#     # creating rectangle using the draw.rect() method
#     pygame.draw.rect(n, (0,0,255), [x , y, width, height])

#     # calculation the center of the circle
#     circle_x = width/2 + x
#     circle_y = height/2 + y

#     # calculating the radius of the circle
#     if height < width:
#         radius = height/2
#     else:
#         radius = width/2

#     # drawing the circle
#     pygame.draw.circle(n, (0,255,0), [circle_x, circle_y], radius)

# draw a polygon using draw.polygon()
# method of pygame
# pygame.draw.polygon(surfare, color, pointlist, thickness)
# thickness of line parameter is optinal
# pygame.draw.polygon(d, blue, [(146,0),(291,106),(236,277),(0,106)])

# # draw a line using draw.line()
# # method of pygame.
# # pygame,draw.line(surface,color, start point, end point, thickness)
# pygame.draw.line(d, green, (60,300), (120, 300), 4)

# # draw a circle using draw.circle()
# # method of pygame
# # pygame.draw.circle(surface, color, center point, raidus, thickness)
# pygame.draw.circle(d, green, (300, 50), 20, 1)

# # draw a ellipse using draw.ellipse()
# # method of pygame
# # pygame.draw.ellipse(surface, color, bounding rectangle, thickness)
# pygame.draw.ellipse(d, black, (150,300,100,50))

# # draw a rectangle using draw.rect()
# # method of pygame
# # pygame.draw.rect(surface, color, rectangle, tuple, thickness)
# # thickness of line parameter is optimal
# pygame.draw.rect(d, black, (150, 300, 100, 50))

pygame.draw.rect(d,black, pygame.Rect(30,30,60,60), 2, border_bottom_right_radius=5)
Käynnissä = True
# Pelin silmukka niin kaun käynnissä kun peli suljetaan
while Käynnissä:
    # Tarkista tapahtuma, jos käyttäjä on työntänyt 
    # tapaus jonossa
    for event in pygame.event.get():
        # jos painaa x niin lopettaa
        if event.type == pygame.QUIT:
            Käynnissä = False

        # if the type of the evnt is MOUSEBUTTONDOWN
        # then storing the current position
        # elif event.type == MOUSEBUTTONDOWN:
        #     position = event.pos
        #     circle_positions.append(position)

        # # using for loop to itarete
        # over the circle_postions
        # list
    # for position in circle_positions:
    #     #drawing the circle
    #     pygame.draw.circle(n, color, position, circle_radius)
  
    # n.fill((255,255,255))

    
    pygame.display.update()

    # drawingfucntion(50,200,500,200)

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

    
    # vaihtaa väriä sen mukaan mikä se on
    # if color == "red":
    #     color = "green"
    # else:
    #     color = "red" 


# print(x, y)