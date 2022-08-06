import os
import pygame
import save_settings as save
pygame.init()
class image:
    def __init__(self,x = None, y = None, width = None, height = None, name_img = None):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMG = name_img
        self.IMAGE = None
        self.COUNT = 5
        self.SPEED = 0
        self.DIRECTIONx = "Right"
        self.DIRECTIONy = "Up"
        self.RECT = pygame.Rect(self.X,self.Y,self.WIDTH,self.HEIGHT)
        if self.NAME_IMG:
            self.load_texture()
    def load_texture(self,directionx=False,directiony=False):
        path_img = save.path()
        path_img = os.path.join(path_img, self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE,directionx,directiony)
    def show(self,game):
        game.blit(self.IMAGE,(self.X,self.Y))
    def animation_rain(self):
        self.SPEED += 1
        if self.SPEED % 2 == 0:
            if self.COUNT == 5:
                self.COUNT = 1
            self.NAME_IMG = f"texture/rain/{self.COUNT}.png"
            self.directionx()
            self.COUNT += 1
    def animation(self):
        self.SPEED += 1
        if self.SPEED % 4 == 0:
            if self.COUNT == 6:
                self.COUNT = 1
            else:
                self.COUNT += 1
                print(self.NAME_IMG)
                self.NAME_IMG = f"texture/stickman/walk/{self.COUNT}.png"
                self.directionx()
                #self.load_texture()
            
    def directionx(self):
        if self.DIRECTIONx == "Right":
            self.load_texture()
        else:
            self.load_texture(True)
    def directiony(self):
        if self.DIRECTIONy == "Down":
            self.load_texture()
        else:
            self.load_texture(directionx=False,directiony = True)
    def move(self,speed):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if self.X+5 + self.WIDTH <= save.config["width"]:
                self.X += speed
                self.DIRECTIONx = "Right"
            # else:
            #     print("right")
                self.animation()
            else:
                self.NAME_IMG = "texture/stickman/idle/idle.png"
                self.directionx()
        #else:
            #self.NAME_IMG = "texture/stickman/idle/idle.png"
            #self.directionx()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if self.X != 0:
                self.X -= speed
                self.DIRECTIONx = "Left"
                self.animation()

            else:
                self.NAME_IMG = "texture/stickman/idle/idle.png"
                self.directionx()
        #else:
            #self.NAME_IMG = "texture/stickman/idle/idle.png"
            #self.directionx()
    def gravity(self,speed):
        if not self.Y == 400:
            self.Y += speed
    def jump(self,speed):
        key = pygame.key.get_pressed()
        time = save.config["height"]
        if key[pygame.K_w] or key[pygame.K_SPACE]:
            if self.Y != 0 and time != 0:
                time -= 1
                self.Y -= speed