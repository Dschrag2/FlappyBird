import pygame

#Loading in all images
def loadImages(FACTOR):
    # Loading and scaling background
    bg = pygame.image.load("./Images/bg.png")
    bg = pygame.transform.scale(bg,(bg.get_size()[0]*FACTOR, bg.get_size()[1]*FACTOR))

    # Getting screen size
    SCREEN_SIZE = (bg.get_size()[0],bg.get_size()[1])
    # Loading and scaling ground
    base = pygame.image.load("./Images/base.png")
    base = pygame.transform.scale(base,(base.get_size()[0]*FACTOR, base.get_size()[1]*FACTOR))
    baserect = base.get_rect(topleft = [0,bg.get_size()[1]-base.get_size()[1]])

    return bg,SCREEN_SIZE,base,baserect

def initIMGS(FACTOR):
    BIRD_IMGS = [pygame.image.load("./Images/bird1.png"),pygame.image.load("./Images/bird2.png"),pygame.image.load("./Images/bird3.png")]
    BIRD_IMGS[0] = pygame.transform.scale(BIRD_IMGS[0],(BIRD_IMGS[0].get_size()[0]*FACTOR, BIRD_IMGS[0].get_size()[1]*FACTOR))
    BIRD_IMGS[1] = pygame.transform.scale(BIRD_IMGS[1],(BIRD_IMGS[1].get_size()[0]*FACTOR, BIRD_IMGS[1].get_size()[1]*FACTOR))
    BIRD_IMGS[2] = pygame.transform.scale(BIRD_IMGS[2],(BIRD_IMGS[2].get_size()[0]*FACTOR, BIRD_IMGS[2].get_size()[1]*FACTOR))
    # PIPE_IMGS[0] is bottom pipe; PIPE_IMGS[1] is top pipe
    PIPE_IMGS = [pygame.image.load("./Images/pipe.png")] * 2
    PIPE_IMGS = [pygame.transform.scale(IMGS,(IMGS.get_size()[0]*FACTOR, IMGS.get_size()[1]*FACTOR)) for IMGS in PIPE_IMGS]
    PIPE_IMGS[1] = pygame.transform.flip(PIPE_IMGS[1],False,True)
    return BIRD_IMGS,PIPE_IMGS

def draw_text(SCREEN_SIZE,font,screen,score,gen,alive):
    text1 = font.render(f'Score: {score}', True, (0,0,0))
    text2 = font.render(f'Gen: {gen}',True, (0,0,0))
    text3 = font.render(f'Alive: {alive}', True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect2 = text1.get_rect()
    textRect3 = text1.get_rect()
    textRect1.topright = (SCREEN_SIZE[0]-25,0)
    textRect2.topleft = (0,0)
    textRect3.topleft = (0,25)
    screen.blit(text1,textRect1)
    screen.blit(text2,textRect2)
    screen.blit(text3,textRect3)

