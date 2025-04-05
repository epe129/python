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
# X = 400
# Y = 400

# create the display surface object
# of specific dimension (X,Y)
screen = pygame.display.set_mode((400,400))
# timer = pygame.time.Clock() 
# asettaa otsikon 
pygame.display.set_caption("asd")
# a = pygame.image.load("a.png")
# # ikkuna kuvakkeen muuntaminen
# pygame.display.set_icon(a) 

img = pygame.image.load("a.png").convert()

# creating list in which we will store
# the position of the circle 
# circle_positions = []
# d.fill(white)

# bg_active_color = white
# d.fill(white)
# # radius of the circle
# circle_radius = 60

# c = (255,255,255)
# antaa näytön normaalin koon
# x, y = n.get_size()

# custom user event to change color
# change_color = pygame.USEREVENT + 1

# custom user event to inflate defalte box
# ON_BOX = pygame.USEREVENT + 2

# create rectangle
# box = pygame.Rect((225, 225, 50, 50))
# grow = True


# vaihtaa väriä joka 500 ms
# pygame.time.set_timer(change_color, 500)

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

# pygame.draw.rect(d,black, pygame.Rect(30,30,60,60), 2, border_bottom_right_radius=5)
Käynnissä = True

# x,y = 0,0
# move_x,move_y = 0,0

# cliking = False
# right_cliking = False
# middle_clikcing = False


# Pelin silmukka niin kaun käynnissä kun peli suljetaan
while Käynnissä:
    mx, my = pygame.mouse.get_pos() ## hiiren x ja y koordinaatit
    paikka = [mx, my]
    # Tarkista tapahtuma, jos käyttäjä on työntänyt 
    # tapaus jonossa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Käynnissä = False
    
    # if event.type == MOUSEBUTTONDOWN:
    #     if event.button == 1:
    #         cliking = True
    #         img = pygame.image.load("p.png")
    #         pygame.display.update()  # update image


    #     if event.button == 3:
    #         middle_clikcing = middle_clikcing

    #         img = pygame.transform.scale(img, (100, 100))
    #         pygame.display.update()

    # if event.type == MOUSEBUTTONUP:
    #     if event.button == 1:
    #         cliking = False
    
    # screen.fill((255,255,255))

    # screen.blit(img, (paikka[0], paikka[1]))

    # if event.type == KEYDOWN:
    #     if event.key == K_LEFT:
    #         move_x = -0.3
    #     elif event.key == K_RIGHT:
    #         move_x = +0.3
    #     elif event.key == K_UP:
    #         move_y = -0.3
    #     elif event.key == K_DOWN:
    #         move_y = +0.3
        


    #     elif event.key == K_LCTRL:
    #         img = pygame.image.load("p.png")
    #         pygame.display.update()
    #     elif event.key == K_BACKSPACE:
    #         img = pygame.image.load("a.png")
    #         pygame.display.update()
        
    # if event.type == KEYUP:
    #     if event.key == K_LEFT:
    #         move_x = 0
    #     elif event.key == K_RIGHT:
    #         move_x = 0
    #     elif event.key == K_UP:
    #         move_y = 0
    #     elif event.key == K_DOWN:
    #         move_y = 0
    
    # x += move_x
    # y += move_y
    
    # screen.fill((255, 255, 255))
    
    # screen.blit(img, (x,y))


        # if event.type == change_color:
        #     if bg_active_color == green:
        #         d.fill(green)
        #         bg_active_color = white
        #     elif bg_active_color == white:
        #         d.fill(white)
        #         bg_active_color = green
        
        # if event.type == ON_BOX:
        #     if grow:
        #         box.inflate_ip(3,3)
        #         grow = box.width < 50
        #     else:
        #         box.inflate_ip(-3,-3)
        #         grow = box.width < 50
                
        # if box.collidepoint(pygame.mouse.get_pos()):
        #     pygame.event.post(pygame.event.Event(ON_BOX))

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         print("olet painanut oikeaa nuoli näppäintä")
        #     elif event.key == pygame.K_LEFT:
        #         print("olet painanut vasempaa nuoli näppäintä")
        #     elif event.key == pygame.K_UP:
        #         print("olet painanut ylöspäin nuoli näppäintä")

      
        # if event.type == pygame.QUIT:
        #     raise SystemExit
        # elif event.type == pygame.MOUSEMOTION:
        #     if event.rel[0] > 0:
        #         print("hiiri liikkuu oikealle")
        #     elif event.rel[1] > 0:
        #         print("hiiri liikkuu alas")
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 3:
        #         print("paino oikeaa hiirestä")
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     print("hiiri painike vapautettu")
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         print("painoit w:ta")
        #     elif event.key == pygame.K_s:
        #         print("painoit s:saa")
        #     elif event.key == pygame.K_a:
        #         print("painoit a:ta")
        #     elif event.key == pygame.K_d:
        #         print("painoit d:ta")
            
        # jos painaa x niin lopettaa
      
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

    # pygame.draw.rect(d, red, box)

    
    pygame.display.update()

    # timer.tick(30)

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