import pygame

# Käytetään pygame-moduulin käynnistämiseen
pygame.init()

# luodaan väri
color = (255,255,255)

# kuvan paikka
paikka = (0,0)

# asetetaan näytön koko
näyttö = pygame.display.set_mode((500, 500))

# asetetaan otsikko
pygame.display.set_caption("Otsikko")

# laitetaan kuva näytölle
kuva = pygame.image.load("p.png")

sulje = False

while not sulje:
    # asetetaan näytön väri musta
    näyttö.fill(color)
    # asetetaan kuva näytölle 
    näyttö.blit(kuva, paikka)

    # tyhjentää tapahtuma jonon jotta peli pysyy päällä
    for event in pygame.event.get():
        # jos painat x ylhäältä peli suljetaan
        if event.type == pygame.QUIT:
            sulje = True
    # päivittää ruudun    
    pygame.display.update()


# JÄIT KOHTAAN Suorakulmiolaatikko Pygame-ikkunassa: