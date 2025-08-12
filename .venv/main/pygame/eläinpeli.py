# Create a virtual pet that the player can take care of. 
# The pet has stats like hunger, happiness, and energy, which change over time. 
# The player can feed, play with, or let the pet rest to keep it happy and healthy.

# Features:
# Stats Management: The pet's stats (hunger, happiness, energy) decrease over time.
# Player Actions: The player can perform actions like feeding, playing, or letting the pet sleep to improve its stats.
# Win/Lose Conditions: If the pet's stats drop too low, it becomes unhappy or "runs away." If the player keeps the pet happy for a certain time, they win.
# Customization: Let the player name their pet or choose its type (e.g., dog, cat, dragon).
# This project is fun, interactive, and can be expanded with animations or a graphical interface later!

import pygame

pygame.init()

pygame.display.set_caption("Kissa")
pygame.display.set_mode((550,550))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           game = False
           
    pygame.display.update()

pygame.QUIT()