# Example file showing a circle moving on screen
import pygame
import sys
import Func
import BirdClass
import PipeClass

# Defining Variables
FPS = 30
FACTOR = 1.5
count = 0
Pipes = []

# Creating a clock object
clock = pygame.time.Clock()

# Loading all images
bg,SCREEN_SIZE,base,baserect = Func.loadImages(FACTOR)
Bird_Imgs,Pipe_IMGS = Func.initIMGS(FACTOR)

# Initializing screen Surface
screen = pygame.display.set_mode(SCREEN_SIZE)

# Creating Bird
Birdie = BirdClass.Bird(SCREEN_SIZE,Bird_Imgs)

# Intializing Text
font,text,textRect = Func.Text(Birdie)

# pygame setup
pygame.init()

while True:
    count += 1
    rem = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if count % 45 == 0:
        newPipe = PipeClass.Pipe(SCREEN_SIZE,Pipe_IMGS,baserect.height)
        Pipes.append(newPipe)

    # Checking for spacebar presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        Birdie.jump()

    # Moving Birds
    Birdie.move(baserect)

    # Moving all Pipes and checking if pipes are off screen
    for Pipe in Pipes:
        Pipe.move()
        if Pipe.toprect.x < -1*Pipe.toprect.width:
            rem.append(Pipe)

    # Removing off screen Pipes
    for Pipe in rem:
        Pipes.remove(Pipe)
        del Pipe

    # Copying everything to screen
    screen.blit(bg,(0,0))
    for Pipe in Pipes:
        Pipe.display(screen)
    screen.blit(base,baserect)
    Func.draw_text(Birdie.velo,font,screen,textRect)
    Birdie.display(screen)

    pygame.display.flip()
    clock.tick(FPS)