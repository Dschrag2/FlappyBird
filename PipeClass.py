import pygame
import random

class Pipe:
    def __init__(self,SCREEN_SIZE,Pipe_IMGS,baseSize):
        self.velo = 5
        self.middle = random.randint(int(0.2*(SCREEN_SIZE[1]-baseSize)),int(0.8*(SCREEN_SIZE[1]-baseSize)))
        self.gap = 0.25 * (SCREEN_SIZE[1] - baseSize)
        self.IMGS = Pipe_IMGS
        self.size = self.IMGS[0].get_size() # (52,320)
        self.basesize = baseSize
        self.toprect = self.IMGS[1].get_rect(bottomleft = [SCREEN_SIZE[0], self.middle - self.gap/2])
        self.bottomrect = self.IMGS[0].get_rect(topleft = [SCREEN_SIZE[0], self.middle + self.gap/2])

    def display(self,screen):
        screen.blit(self.IMGS[0],self.bottomrect)
        screen.blit(self.IMGS[1],self.toprect)

    def move(self):
        self.toprect.x -= self.velo
        self.bottomrect.x -= self.velo