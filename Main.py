# Example file showing a circle moving on screen
import pygame
import sys
import os
import neat
import Func
import BirdClass
import PipeClass

# Defining Variables
FPS = 30
FACTOR = 1.5
GEN = 0

# Loading all images
bg,SCREEN_SIZE,base,baserect = Func.loadImages(FACTOR)
Bird_Imgs,Pipe_IMGS = Func.initIMGS(FACTOR)

# pygame setup
pygame.init()
pygame.font.init()

def main(genomes, config):
    global GEN
    GEN += 1
    nets = []
    ge = []
    birds = []
    Pipes = []

    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(BirdClass.Bird(SCREEN_SIZE,Bird_Imgs))
        g.fitness = 0
        ge.append(g)


    # Initializing clock, screen, font, caption, score, etc.
    score = 0
    count = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    font = pygame.font.SysFont('timesnewroman',  30)
    pygame.display.set_caption('Flappy Bird')

    run = True
    while run:
        # Creating initial Pipe
        if len(Pipes) == 0:
            newPipe = PipeClass.Pipe(SCREEN_SIZE,Pipe_IMGS,baserect.height)
            Pipes.append(newPipe)

        clock.tick(FPS)
        count += 1
        rem = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Finding first pipe not yet passed
        pipe_ind = 0
        if len(birds) > 0:
            for x,pipe in enumerate(Pipes):
                if pipe.passed == False:
                    pipe_ind = x
                    break
        else:
            Pipes = []
            run = False
            break

        # Neural Net determining if bird jumps
        for x,bird in enumerate(birds):
            ge[x].fitness += 0.1
            output = nets[x].activate((bird.rect.y, abs(bird.rect.y - Pipes[pipe_ind].top), abs(bird.rect.y - Pipes[pipe_ind].bottom)))
            if output[0] > 0.5:
                bird.jump()

        # Creating new pipes every 50 ticks
        if count % 50 == 0:
            newPipe = PipeClass.Pipe(SCREEN_SIZE,Pipe_IMGS,baserect.height)
            Pipes.append(newPipe)

        # Moving Birds
        for x,bird in enumerate(birds):
            end = bird.move(baserect,Pipes)
            if (end):
                ge[x].fitness -= 1
                birds.pop(x)
                ge.pop(x)
                nets.pop(x)

        # Moving all Pipes and checking if pipes are off screen
        for Pipe in Pipes:
            passed = Pipe.move(SCREEN_SIZE[0]/3)
            if passed:
                score += 1
                for g in ge:
                    g.fitness += 5
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
        Func.draw_text(SCREEN_SIZE,font,screen,score,GEN,len(birds))
        for bird in birds:
            bird.display(screen)
        pygame.display.flip()


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)