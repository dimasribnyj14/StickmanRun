import pygame
import json
import os
import save_settings as save
import sound_play as sound
import texture_show as image
import draw_paint as draw
import text_create as text
pygame.init()
def main_menu():
    fps = pygame.time.Clock()
    main = True
    main_music = sound.music("sound/main.wav")
    main_music.load()
    main_music.play()
    button = draw.draw(
        x = (save.config["width"]/1.25)//2,
        y = save.config["height"]//2,
        width = 130,
        height = 70,
        color = (23,30,69),
        border = 3,
        border_color = (20,53,63)
    )
    start_game = text.text(
        x = (save.config["width"]/1.25+30)//2,
        y = (save.config["height"]+25)//2,
        size = 50,
        name_font = "fonts/pixel_font.ttf",
        text = "Play",
        color = (20,65,75),
        aa = False
    )
    title_game = text.text(
        x = (save.config["width"]/2)//2,
        y = (save.config["height"]/2)//2-20,
        size = 50,
        name_font = "fonts/pixel_font.ttf",
        text = "Stickman Run",
        color = (200,100,0),
        aa = True
    )
    while main:
        game.fill(save.config["fill"])
        button.draw(game)
        start_game.load_text(game)
        title_game.load_text(game)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.RECT.collidepoint(pos):
                        main = False
                        error()
                        save.saves["levels":"error"]
        fps.tick(30)
        pygame.display.flip()