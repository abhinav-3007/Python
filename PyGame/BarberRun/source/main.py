import random

import pygame
import time
from random import randrange


class Player:
    def __init__(self):
        self.health = 4
        self.score = 0
        self.sprites = [pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man1.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man2.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man3.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man4.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man5.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man6.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man7.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man8.png'), (92, 120))]

        self.image_count = 0
        self.x = 80
        self.y = 500
        self.isJump = False
        self.jump_velocity = 40

    def draw(self):
        win.blit(self.sprites[self.image_count // 15], (self.x, self.y))

        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites)*15:
            self.image_count += 1
        else:
            self.image_count = 0


class Background:
    def __init__(self):
        self.image_width = 662
        self.image = pygame.transform.scale(pygame.image.load('../images/bg.png'), (self.image_width, 600))
        self.x = 0
        self.y = 50
    
    def draw(self):
        win.blit(self.image, (self.x, self.y))
        win.blit(self.image, (self.x + self.image_width, self.y))
        win.blit(self.image, (self.x + self.image_width*2, self.y))
        if self.x+1 <= -self.image_width:
            self.x = 0
        else:
            self.x -= 2


class Enemies:
    image_options = [pygame.transform.scale(pygame.image.load(f'../images/enemies/razor.png'), (42, 120))]
    no_of_options = len(image_options)

    def __init__(self, x, y):
        self.enemy_type = random.randint(1, Enemies.no_of_options)
        self.image = Enemies.image_options[self.enemy_type-1]
        self.x = x
        self.y = y
        self.incline = 20
        self.incline_count = 0

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image = pygame.transform.rotate(Enemies.image_options[self.enemy_type-1], self.incline)
        self.incline_count += 1
        if self.incline_count == 40:
            self.incline = -self.incline
            self.incline_count = 0


def redrawGameWindow(player, background, enemies):
    win.fill((151, 123, 89))
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    pygame.display.update()


def main():
    font = pygame.font.SysFont("comicsans", 30, True)
    background = Background()
    clock = pygame.time.Clock()
    running = True
    player = Player()
    enemies = [Enemies(0, 0)]
    # main loop
    while running:
        clock.tick(150)

        # condition to quit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # making the player jump if UP key is pressed
        if not player.isJump:
            if keys[pygame.K_UP]:
                player.isJump = True
        else:
            if player.jump_velocity < -40:
                player.isJump = False
                player.jump_velocity = 40
            else:
                player.y -= player.jump_velocity*0.5
                player.jump_velocity -= 1

        redrawGameWindow(player, background, enemies)


if __name__ == '__main__':
    pygame.init()

    sc_width = 1000
    sc_height = 650

    # initializing game window
    win = pygame.display.set_mode((sc_width, sc_height))
    pygame.display.set_caption("Barber Run")

    # calling main loop
    main()

    pygame.quit()
