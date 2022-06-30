import pygame 
from abstractCharacter import AbstractCharacter

# background image move with player
class Backgroundimage(AbstractCharacter):
    def __init__(self, x, y):
        self.image = pygame.image.load('bg.jpg')
        self.pos = [x, y]
        self.to = [0, 0]

    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y

    # player can't escape from map
    def update(self, dt, screen):
        width, height = screen.get_size()
        phw = self.image.get_width() / 2
        phh = self.image.get_height() / 2
        self.pos[0] = self.pos[0] + dt * self.to[0]
        self.pos[1] = self.pos[1] + dt * self.to[1]
        self.pos[0] = min(max(self.pos[0], width - self.image.get_width()), 0)
        self.pos[1] = min(max(self.pos[1], height - self.image.get_height()), 0)
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos[0],self.pos[1]))
