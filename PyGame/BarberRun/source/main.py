import pygame
import time
from random import randrange

pygame.init()

sc_width = 530
sc_height = 480

win = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Barber Run")

man = [pygame.image.load('../images/man1.png'), pygame.image.load('../images/man2.png'),
             pygame.image.load('../images/man3.png'),
             pygame.image.load('../images/man4.png'), pygame.image.load('../images/man5.png'),
             pygame.image.load('../images/man6.png'),
             pygame.image.load('../images/man7.png'), pygame.image.load('../images/man8.png')]
#
# bulletSound = pygame.mixer.Sound("./audio/shoot.wav")
# hitSound = pygame.mixer.Sound("./audio/hit.wav")
#
# music = pygame.mixer.music.load("audio/bg.wav")
# pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
count = 0
muspos = -.5

def redrawGameWindow():
    global count, muspos
    win.fill([0, 0, 0])
    win.blit(man[count], (0, 0))
    win.blit(mustache, (19+muspos, 19+muspos))
    if count%2 == 0:
        muspos = -muspos
    if count+1 < len(man):
        count += 1
    else:
        count = 0
    pygame.display.update()


# mainloop
font = pygame.font.SysFont("comicsans", 30, True)
shootcool = 0
bullets = []
running = True
while running:
    clock.tick(10)

    redrawGameWindow()

pygame.quit()
