import pygame
import time
import random
# ottaa käyttön fontin
pygame.font.init()

#NÄYTÖN KOKO
WIDTH, HEIGHT = 1000, 800
#ASETTAA NÄYTÖN KOOKSI WIDHT JA HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#ASETTAA OTSIKON
pygame.display.set_caption("väistelypeli")
#Pelaaja
PLAYER_WIDHT = 40
PLAYER_HEIGHT = 60
# liikkuvuus
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGT = 20
# määrittää fontin koon- ja tyylin
FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars):
    # asettaa taustan laita aina ekaksi muuten yli kirjottaaa kaikki muut väri määritykset
    WIN.fill("white")
    
    #  piirtää fontin ruudulle
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    # piirttä tekstin ylä kulmaan
    WIN.blit(time_text, (10, 10))

    # piirtää pelaajan ja antaa sen värin
    pygame.draw.rect(WIN, "black", player)

    for star in stars:
        pygame.draw.rect(WIN, "black", star)

    pygame.display.update()
    
def game_over():
    lost_text = FONT.render("YOU LOST", 1, "black")
    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
    pygame.display.flip()   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                pygame.display.flip()               
# pää funtkio
def main():
    run = True
    # määrittää missä pelaaja on
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDHT, PLAYER_HEIGHT)
    # määrittää ajan
    clock = pygame.time.Clock()
    # ottaa nykyisen ajan
    start_time = time.time()
    # ensimmäinen ammus lisätään 2000 millisekunnissa
    elapsed_time = 2000
    # kertoo milloin pitäisi lisätä lisää ammuksia
    star_count = 0
    # sisältää kaikki ammukset jotka piirretään näytölle
    stars = []

    STAR_VEL = 5

    hit = False
    star_add_increment = 2000
    while run:
        # määrittää maksimi määrän kuvia sekunnissa ja kertoo kauan kulunut viimeisestä ammuksen luonnista
        star_count += clock.tick(60)
        # antaa ajan milloin peli alkoi
        elapsed_time = time.time() - start_time 
        # kun tulee 2000 millisekuntia täyteen niin lisätään ammus
        if star_count > star_add_increment:
            # kuinka monta ammusta luodaan näytölle
            for _ in range(40):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGT, STAR_WIDTH, STAR_HEIGT)
                stars.append(star)
            
            star_add_increment  = max(200, star_add_increment - 50)
            star_count = 0


        # tarkistaa onko x sää painettu jos on peli suljetaan
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
                
        # voi painaa näppäimiä
        keys = pygame.key.get_pressed()
        # jos painaa vasentanuolinäppäintä niin liikkuu vasemmalle
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        # jos painaa oikeaanuolinäppäintä niin liikkuu oikealle
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        # liikuttaa ammuksia
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            game_over()
            
            
            

        draw(player, elapsed_time, stars)
    

if __name__ == "__main__":
    main()
