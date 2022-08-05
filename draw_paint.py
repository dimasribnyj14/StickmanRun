import pygame
import texture_show as image
pygame.init()
class draw(image.image):
    def __init__(self,x,y,width,height,color = None, border = None,border_color = None):
        super().__init__(x, y, width, height)
        self.X_one = x
        self.Y_one = y
        self.WIDTH_one = width
        self.HEIGHT_one = height
        self.COLOR = color
        self.BORDER = border
        self.BORDER_COLOR = border_color
        self.DRAW = None
        self.RECT = pygame.Rect(self.X_one,self.Y_one,self.WIDTH_one,self.HEIGHT_one)
    def draw(self,game):
        pygame.draw.rect(game,self.COLOR,self.RECT)
        pygame.draw.rect(game,self.BORDER_COLOR,self.RECT,self.BORDER)