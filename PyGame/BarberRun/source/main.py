import random
import pygame


class Player:
    def __init__(self):
        self.health = 4
        self.score = 0
        self.sprites = []
        self.setImage()
        self.image_count = 0
        self.x = 80
        self.y = 500
        self.isJump = False
        self.jump_velocity = 70
        self.invulnerability = 70

    def draw(self):
        win.blit(self.sprites[self.image_count // 15], (self.x, self.y))

        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites)*15:
            self.image_count += 1
        else:
            self.image_count = 0

    def setImage(self):
        self.sprites = [pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man1.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man2.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man3.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man4.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man5.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man6.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man7.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man8.png'), (92, 120))]


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
    spawn = True
    def __init__(self, y, image):
        # placeholder image
        self.image = image
        self.x = 1000
        self.y = y
        self.x_velocity = 3
        self.y_velocity = 0
        self.damage = 1

    def move(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity


class Razor(Enemies):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (83, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (83, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/razor2.png'), (83, 140))]
        self.image_count = 0

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.image = self.sprites[1]
            self.image_count = 0


class Scissors(Enemies):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)),
                             pygame.transform.scale(pygame.image.load('../images/enemies/scissors2.png'), (245, 140))]
        self.image_count = 0
        self.x_velocity = 4

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.image = self.sprites[1]
            self.image_count = 0

class Blade(Enemies):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/blade.png'), (60, 76)))
        self.x_velocity = 5
        self.image_count = 0

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = pygame.transform.rotate(self.image, 90)
            self.image_count = 0


class Barber(Enemies):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber2.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber3.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber4.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber5.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber6.png'), (88, 140))]
        self.image_count = 0
        self.x_velocity = 2.2
        self.damage = 2

    def draw(self):
        win.blit(self.sprites[self.image_count // 20], (self.x, self.y))

        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites) * 20:
            self.image_count += 1
        else:
            self.image_count = 0


def death():
    print("ded :(")


def checkCollision(player, enemies):
    for enemy in enemies:
        if player.invulnerability > 0:
            break
        if (enemy.x+20 < player.x < enemy.x + enemy.image.get_width() or enemy.x+20 < player.x+92 < enemy.x + enemy.image.get_width()) and (enemy.y < player.y < enemy.y + enemy.image.get_height() or enemy.y < player.y + 120< enemy.y + enemy.image.get_height()):
            if player.health > 1:
                player.health -= enemy.damage
                if player.health < 1:
                    player.health = 1
                    death()
                player.setImage()
            else:
                death()
            player.invulnerability = 100
            break


def redrawGameWindow(player, background, enemies, font):
    win.fill((151, 123, 89))
    background.draw()
    health = font.render(f"Health: {player.health}", 1, (45, 56, 56))
    win.blit(health, (18, 18))
    for enemy in enemies:
        enemy.draw()
    player.draw()
    pygame.display.update()


def main():
    font = pygame.font.Font("../fonts/ArcadeFont.ttf", 20)
    background = Background()
    clock = pygame.time.Clock()
    running = True
    player = Player()
    enemy_types = [Razor, Scissors, Barber]
    enemies = []
    # main loop
    while running:
        clock.tick(250)
        if Enemies.spawn:
            index = random.randint(0, len(enemy_types)-1)
            y = 480
            if index == 1:
                y = random.randrange(50, 340)
            enemies.append(enemy_types[index](y))
            Enemies.spawn = False
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
            if player.jump_velocity < -70:
                player.isJump = False
                player.jump_velocity = 70
            else:
                player.y -= player.jump_velocity*0.1
                player.jump_velocity -= 1

        for enemy in enemies:
            enemy.move()
            if enemy.x < -enemy.image.get_width():
                enemies.remove(enemy)
                del enemy
                Enemies.spawn = True

        if player.invulnerability > 0:
            player.invulnerability -= 1
        else:
            checkCollision(player, enemies)

        redrawGameWindow(player, background, enemies, font)


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
