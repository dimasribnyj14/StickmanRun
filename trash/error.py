import pygame
import json
import os
import save_settings as save
import sound_play as sound
import texture_show as image
import draw_paint as draw
import text_create as text
pygame.init()
def error():
    fps = pygame.time.Clock()
    main = True
    error_thinking = image.image(
        x = 500,
        y = 170,
        width = 100,
        height = 300,
        name_img = "texture/stickman/error.png"
    )
    blit = pygame.Rect(0,0,save.config["width"],save.config["height"])
    error_thinking.load_texture()
    error = text.text(
        x = 0,
        y = 120,
        size = 30,
        name_font = "fonts/pixel_font.ttf",
        text = f"Error: Map {save.saves['levels']} has no found",
        color = (0,0,0),
        aa = True
    )
    recommend = text.text(
        x = 0,
        y = 50,
        size = 30,
        name_font = "fonts/pixel_font.ttf",
        text = "Click everywhere to go Menu.",
        color = (0,0,0),
        aa = True
    )
    while main:
        game.fill((255,255,255))
        error.load_text(game)
        recommend.load_text(game)
        error_thinking.show(game)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if blit.colliderect(blit):
                        main = False
                        main_menu()
        fps.tick(30)
        pygame.display.flip()