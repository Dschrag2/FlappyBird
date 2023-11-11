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
score = 0
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
font,textRect = Func.Text(Birdie)
font2,textRect2 = Func.finalText(SCREEN_SIZE)

# pygame setup
pygame.init()

# Setting window title
pygame.display.set_caption('Flappy Bird')

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
    end = Birdie.move(baserect,Pipes)
    if (end):
        break

    # Moving all Pipes and checking if pipes are off screen
    for Pipe in Pipes:
        Pipe.move(Birdie)
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
    Func.draw_text(Birdie.score,font,screen,textRect)
    Birdie.display(screen)
 
    pygame.display.flip()
    clock.tick(FPS)

# Post death screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(bg,(0,0))
    for Pipe in Pipes:
        Pipe.display(screen)
    screen.blit(base,baserect)
    Func.draw_text(Birdie.score,font,screen,textRect)
    Birdie.display(screen)
    Func.draw_finalText(font2,screen,textRect2)

    pygame.display.flip()
    clock.tick(FPS)