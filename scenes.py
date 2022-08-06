import pygame
import save_settings as save
import sound_play as sound
import texture_show as image
import draw_paint as draw
import text_create as text
import maps
pygame.init()
name = pygame.display.set_caption(save.config["name"])
if save.config["fullscreen"] == 1:
    game = pygame.display.set_mode((save.config["width"],save.config["height"]),pygame.FULLSCREEN)
else:
    game = pygame.display.set_mode((save.config["width"],save.config["height"]))
def scene():
    fps = pygame.time.Clock()
    main = True
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
        fps.tick(30)
        pygame.display.flip()
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
        text = "Click everywhere to leave.",
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
                        save.saves["levels"] = "main_menu"
                        save.create_Json("saves.json",save.saves)
                        main = False
        fps.tick(30)
        pygame.display.flip()
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
        text = f"{save.config['name']}",
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
                        firstlevel()
                        save.saves["levels"] = "first_level"
                        save.create_Json("saves.json",save.saves)
        fps.tick(30)
        pygame.display.flip()
def firstlevel():
    fps = pygame.time.Clock()
    main = True
    #main_music = sound.music("sound/main.wav")
    #main_music.load()
    #main_music.play_loop()
    rain = sound.music("sound/rain.wav")
    rain.load()
    rain.play_loop()
    sky = image.image(
        x = 0,
        y = 0,
        width = save.config["width"],
        height = save.config["height"],
        name_img = ("texture/sky/sky_rain.png")
    )
    tutorial = image.image(
        x = 70,
        y = 100,
        width = 205,
        height = 106,
        name_img = ("texture/tutorial.png")
    )
    stickman = image.image(
        x = 20,
        y = 400,
        width = 30,
        height = 50,
        name_img = ("texture/stickman/idle/idle.png")
    )
    rain = image.image(
        x = 0,
        y = 0,
        width = save.config["width"],
        height = save.config["height"],
        name_img = ("texture/rain/1.png")
    )
    time_tutorial = 0
    while main:
        sky.show(game)
        rain.show(game)
        time_tutorial += 1
        if time_tutorial <= 100:
            tutorial.show(game)
        rain.animation_rain()
        stickman.show(game)
        stickman.move(2)
        stickman.gravity(5)
        #stickman.jump(3)
        for le in maps.list_create_map_lvl1:
            le.show(game)
        if stickman.X == 600:
            main = False
            firstlevel_n1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                save.saves["levels"] = "main_menu"
                save.create_Json("saves.json",save.saves)
        fps.tick(30)
        pygame.display.flip()
def firstlevel_n1():
    fps = pygame.time.Clock()
    main = True
    #main_music = sound.music("sound/main.wav")
    #main_music.load()
    #main_music.play_loop()
    rain_sound = sound.music("sound/rain.wav")
    rain_sound.load()
    rain_sound.play_loop()
    sky = image.image(
        x = 0,
        y = 0,
        width = save.config["width"],
        height = save.config["height"],
        name_img = ("texture/sky/sky_rain.png")
    )
    stickman = image.image(
        x = 20,
        y = 400,
        width = 30,
        height = 50,
        name_img = ("texture/stickman/idle/idle.png")
    )
    rain = image.image(
        x = 0,
        y = 0,
        width = save.config["width"],
        height = save.config["height"],
        name_img = ("texture/rain/1.png")
    )
    while main:
        sky.show(game)
        rain.show(game)
        rain.animation_rain()
        stickman.show(game)
        stickman.move(2)
        stickman.gravity(5)
        #stickman.jump(3)
        for le in maps.list_create_map_lvl1n1:
            le.show(game)
        if stickman.X == 400:
            main = False
            rain_sound.stop()
            main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                save.saves["levels"] = "main_menu"
                save.create_Json("saves.json",save.saves)
        fps.tick(30)
        pygame.display.flip()