import pygame
import json
import os
import save_settings as save
import sound_play as sound
import texture_show as image
import draw_paint as draw
import text_create as text
pygame.init()
def scene():
    fps = pygame.time.Clock()
    main = True
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
        fps.tick(30)
        pygame.display.flip()