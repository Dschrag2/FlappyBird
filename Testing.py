# Example file showing a circle moving on screen
import pygame
import sys

FPS = 30
FACTOR = 1.5
VELO = 0
ACCEL = 1.3

#Creating a clock object
clock = pygame.time.Clock()

# pygame setup
pygame.init()

# Loading and scaling background
bg = pygame.image.load("./Images/bg.png")
bg = pygame.transform.scale(bg,(bg.get_size()[0]*FACTOR, bg.get_size()[1]*FACTOR))

# Getting screen size
SCREEN_SIZE = (bg.get_size()[0],bg.get_size()[1])

# Loading and scaling ground
base = pygame.image.load("./Images/base.png")
base = pygame.transform.scale(base,(base.get_size()[0]*FACTOR, base.get_size()[1]*FACTOR))
baserect = base.get_rect(topleft = [0,bg.get_size()[1]-base.get_size()[1]])

# Loading and scaling bird1
bird1 = pygame.image.load("./Images/bird1.png")
bird1 = pygame.transform.scale(bird1,(bird1.get_size()[0]*FACTOR,bird1.get_size()[1]*FACTOR))
bird1rect = bird1.get_rect(topright = [bg.get_size()[0]/2, bg.get_size()[1]*1/3])

# Initializing screen Surface
screen = pygame.display.set_mode(SCREEN_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        VELO = -15

    bird1rect = bird1rect.move([0,VELO])
    #Checking if bird hits ceiling
    if bird1rect.y <= 0:
        bird1rect.y = 0
        VELO = 0

    #Checking for collisions between bird and ground
    if bird1rect.colliderect(baserect):
        VELO = 0
        bird1rect.y = bg.get_size()[1] - baserect.height - bird1rect.height

    #Copying bg to screen
    screen.blit(bg,(0,0))
    screen.blit(base,baserect)
    
    screen.blit(bird1,bird1rect)
    pygame.display.flip()
    VELO = VELO + ACCEL
    clock.tick(FPS)