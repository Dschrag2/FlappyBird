import pygame
import sys

class Bird:
    def __init__(self,SCREEN_SIZE,IMGS):
        self.x = SCREEN_SIZE[0]/3
        self.y = SCREEN_SIZE[1]/3
        self.velo = 0
        self.accel = 1.2
        self.tick_count = 0
        self.IMGS = IMGS
        self.rect = self.IMGS[0].get_rect(topleft = [self.x, self.y])
        self.screensize = SCREEN_SIZE
        self.rect.y = self.y

    def jump(self):
        self.velo = -12
        self.tick_count = 0

    def move(self,baserect,Pipes):
        self.tick_count += 1
        self.velo = self.velo + self.accel
        self.rect = self.rect.move([0,self.velo])

        #Checking if bird hits ceiling
        if self.rect.y <= 0:
            self.rect.y = 0
            self.velo = 0

        #Checking for collisions between bird and ground
        if self.rect.colliderect(baserect):
            self.rect.y = self.screensize[1] - baserect.height - self.rect.height
            return True

        for pipe in Pipes:
            if self.rect.colliderect(pipe.toprect) or self.rect.colliderect(pipe.bottomrect):
                return True
        return False

    def display(self,screen):
        if self.velo == 0:
            screen.blit(self.IMGS[0],self.rect)
        elif self.tick_count % 15 < 5:
            screen.blit(self.IMGS[0],self.rect)
        elif self.tick_count % 15 >= 5 and self.tick_count % 15 < 10:
            screen.blit(self.IMGS[1],self.rect)
        elif self.tick_count % 15 >= 10:
            screen.blit(self.IMGS[2],self.rect)
