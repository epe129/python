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

# Näppäinkomennot
KEY_COMMANDS = [
    "Nuoli ylös: Kävele pohjoiseen",
    "Nuoli alas: Kävele etelään",
    "Nuoli vasen: Kävele länteen",
    "Nuoli oikea: Kävele itään",
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
            elif event.key == pygame.K_UP:  # Kävele pohjoiseen
                result = self.game.process_command("kävele pohjoinen")
                print(result)
            elif event.key == pygame.K_DOWN:  # Kävele etelään
                result = self.game.process_command("kävele etelä")
                print(result)
            elif event.key == pygame.K_LEFT:  # Kävele länteen
                result = self.game.process_command("kävele länsi")
                print(result)
            elif event.key == pygame.K_RIGHT:  # Kävele itään
                result = self.game.process_command("kävele itä")
                print(result)
            elif event.key == pygame.K_SPACE:  # Poimi esine
                room = self.game.rooms[self.game.player.current_room]
                if room.items:
                    result = self.game.process_command(f"poimi {room.items[0]}")
                    print(result)

    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            self.draw_room()
            self.draw_inventory()
            self.draw_key_commands()

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