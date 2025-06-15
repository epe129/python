import pygame
import sys
import os
from game_engine import Game

# Lisää projektin juurihakemisto moduulipolkuun
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Pygame asetukset
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Värit
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Esineiden kuvat
ITEM_IMAGES = {
    "avain": "assets/sprites/key.png",
    "kirja": "assets/sprites/kirja.png",
    "kolikko": "assets/sprites/coin.png"
}

# Kuvien koko
IMAGE_SIZE = (50, 50)

# Hahmon kuva
PLAYER_IMAGE = "assets/sprites/peliukkeli.png"
PLAYER_SIZE = (80, 80)  # Skaalataan hahmo hieman suuremmaksi

# Näppäinkomennot
KEY_COMMANDS = [
    "Nuoli ylös: Liiku ylös",
    "Nuoli alas: Liiku alas",
    "Nuoli vasen: Liiku vasemmalle",
    "Nuoli oikea: Liiku oikealle",
    "Välilyönti: Poimi esine",
    "S: Tallenna peli",
    "H: Näytä ohjeet",
    "Q: Lopeta peli"
]

class VisualGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Seikkailupeli")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Käytä oletusfonttia
        self.small_font = pygame.font.Font(None, 24)  # Pienempi fontti näppäinkomennoille
        self.game = Game()
        self.running = True

        # Lataa ja skaalaa kuvat
        self.item_images = {item: pygame.transform.scale(pygame.image.load(path), IMAGE_SIZE) for item, path in ITEM_IMAGES.items()}
        self.player_image = pygame.transform.scale(pygame.image.load(PLAYER_IMAGE), PLAYER_SIZE)  # Lataa ja skaalaa hahmon kuva

        # Pelaajan sijainti (aloitetaan huoneen keskeltä)
        self.player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE[0] // 2
        self.player_y = SCREEN_HEIGHT // 2 - PLAYER_SIZE[1] // 2
        self.player_speed = 5  # Pelaajan liikkumisnopeus

    def draw_text(self, text, x, y, color=BLACK, font=None):
        if font is None:
            font = self.font
        rendered_text = font.render(text, True, color)
        self.screen.blit(rendered_text, (x, y))

    def draw_room(self):
        room = self.game.rooms[self.game.player.current_room]
        self.draw_text(f"Huone: {room.name}", 20, 20)
        self.draw_text(room.description, 20, 60)

        # Piirrä esineet kuvina
        max_items_per_row = SCREEN_WIDTH // (IMAGE_SIZE[0] + 20)  # Maksimimäärä esineitä per rivi
        for i, item in enumerate(room.items):
            if item in self.item_images:
                row = i // max_items_per_row  # Laske rivi
                col = i % max_items_per_row  # Laske sarake
                x = 20 + col * (IMAGE_SIZE[0] + 20)  # X-sijainti
                y = 150 + row * (IMAGE_SIZE[1] + 40)  # Y-sijainti
                self.screen.blit(self.item_images[item], (x, y))
                self.draw_text(item, x, y + IMAGE_SIZE[1] + 10, BLACK)

    def draw_doors(self):
        room = self.game.rooms[self.game.player.current_room]
        door_color = (0, 0, 255)  # Sininen ovi
        locked_door_color = (255, 0, 0)  # Punainen lukittu ovi

        # Piirrä ovet huoneen reunoille
        for direction, next_room in room.exits.items():
            if direction == "pohjoinen":
                color = locked_door_color if direction in room.locked_exits else door_color
                pygame.draw.rect(self.screen, color, (SCREEN_WIDTH // 2 - 50, 0, 100, 20))
            elif direction == "etelä":
                color = locked_door_color if direction in room.locked_exits else door_color
                pygame.draw.rect(self.screen, color, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 20, 100, 20))
            elif direction == "itä":
                color = locked_door_color if direction in room.locked_exits else door_color
                pygame.draw.rect(self.screen, color, (SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 50, 20, 100))
            elif direction == "länsi":
                color = locked_door_color if direction in room.locked_exits else door_color
                pygame.draw.rect(self.screen, color, (0, SCREEN_HEIGHT // 2 - 50, 20, 100))

    def draw_player(self):
        # Piirrä pelaajan hahmo
        self.screen.blit(self.player_image, (self.player_x, self.player_y))

    def draw_inventory(self):
        inventory_text = f"Tavarat: {', '.join(self.game.player.inventory) if self.game.player.inventory else 'Ei mitään'}"
        self.draw_text(inventory_text, 20, SCREEN_HEIGHT - 120)

    def draw_key_commands(self):
        # Näytä näppäinkomennot ruudun oikeassa reunassa ja hieman alempana
        x_offset = SCREEN_WIDTH - 250  # Sijoita oikeaan reunaan
        y_offset = 150  # Aloita hieman alempaa
        for i, command in enumerate(KEY_COMMANDS):
            self.draw_text(command, x_offset, y_offset + i * 25, BLACK, font=self.small_font)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Lopeta peli
                self.running = False
            elif event.key == pygame.K_h:  # Näytä ohjeet
                print(self.game.process_command("komennot"))
            elif event.key == pygame.K_s:  # Tallenna peli
                self.game.save()
                print("Peli tallennettu.")
            elif event.key == pygame.K_SPACE:  # Poimi esine
                room = self.game.rooms[self.game.player.current_room]
                if room.items:
                    result = self.game.process_command(f"poimi {room.items[0]}")
                    print(result)

    def update_player_position(self, keys):
        # Liikuta pelaajaa nuolinäppäimillä
        if keys[pygame.K_UP]:
            self.player_y -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_y += self.player_speed
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed

        # Tarkista, ylittääkö hahmo ruudun reunan ja vaihda huonetta
        if self.player_x < 0:  # Vasen reuna
            self.player_x = SCREEN_WIDTH - PLAYER_SIZE[0]
            print(self.game.process_command("kävele länsi"))
        elif self.player_x + PLAYER_SIZE[0] > SCREEN_WIDTH:  # Oikea reuna
            self.player_x = 0
            print(self.game.process_command("kävele itä"))
        elif self.player_y < 0:  # Yläreuna
            self.player_y = SCREEN_HEIGHT - PLAYER_SIZE[1]
            print(self.game.process_command("kävele pohjoinen"))
        elif self.player_y + PLAYER_SIZE[1] > SCREEN_HEIGHT:  # Alareuna
            self.player_y = 0
            print(self.game.process_command("kävele etelä"))

    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            self.draw_room()
            self.draw_player()
            self.draw_inventory()
            self.draw_key_commands()
            self.draw_doors()  # Piirrä ovet

            keys = pygame.key.get_pressed()
            self.update_player_position(keys)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_input(event)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    visual_game = VisualGame()
    visual_game.run()