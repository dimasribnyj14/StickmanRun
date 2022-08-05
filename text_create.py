import pygame
import os
import save_settings as save
pygame.init()
class text:
    def __init__(self,x = None,y=None,name_font = None, text = None, color = None,size = None,aa=None):
        self.X = x
        self.Y = y
        self.SIZE = size
        self.NAME_FONT = name_font
        self.TEXT = text
        self.COLOR = color
        self.AA = aa
    def load_text(self,game):
        text_load = save.path()
        text_load = os.path.join(text_load, self.NAME_FONT)
        font = pygame.font.Font(self.NAME_FONT,self.SIZE)
        text = font.render(self.TEXT,self.AA,self.COLOR)
        game.blit(text,(self.X,self.Y))