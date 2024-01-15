import pygame
import time
from random import randrange

pygame.init()

sc_width = 530
sc_height = 480

win = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Shooter")

walkRight = [pygame.image.load('./images/R1.png'), pygame.image.load('./images/R2.png'),
             pygame.image.load('./images/R3.png'),
             pygame.image.load('./images/R4.png'), pygame.image.load('./images/R5.png'),
             pygame.image.load('./images/R6.png'),
             pygame.image.load('./images/R7.png'), pygame.image.load('./images/R8.png'),
             pygame.image.load('./images/R9.png')]
walkLeft = [pygame.image.load('./images/L1.png'), pygame.image.load('./images/L2.png'),
            pygame.image.load('./images/L3.png'),
            pygame.image.load('./images/L4.png'), pygame.image.load('./images/L5.png'),
            pygame.image.load('./images/L6.png'),
            pygame.image.load('./images/L7.png'), pygame.image.load('./images/L8.png'),
            pygame.image.load('./images/L9.png')]
bg = pygame.image.load('./images/bg.jpg')
char = pygame.image.load('./images/standing.png')

bulletSound = pygame.mixer.Sound("./audio/shoot.wav")
hitSound = pygame.mixer.Sound("./audio/hit.wav")

music = pygame.mixer.music.load("audio/bg.wav")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

score = 0


class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.lives = 3

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        font = pygame.font.SysFont("comicsans", 30, True)
        win.blit(font.render("Lives: " + str(self.lives), 1, (0, 150, 0)), (10, 20))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.lives -= 1
        self.isJump = 0
        self.jumpCount = 10
        self.x = 450
        self.y = 417
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-1 life', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        if self.lives == 0:
            text = font1.render('Game Over', 1, (230, 0, 0))
            win.blit(text, (250 - (text.get_width() / 2), 200))
            time.sleep(2)
            pygame.quit()


class Projectile():
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


class Enemy():
    walkRight = [pygame.image.load("./images/R1E.png"),
                 pygame.image.load("./images/R2E.png"),
                 pygame.image.load("./images/R3E.png"),
                 pygame.image.load("./images/R4E.png"),
                 pygame.image.load("./images/R5E.png"),
                 pygame.image.load("./images/R6E.png"),
                 pygame.image.load("./images/R7E.png"),
                 pygame.image.load("./images/R8E.png"),
                 pygame.image.load("./images/R9E.png"),
                 pygame.image.load("./images/R10E.png"),
                 pygame.image.load("./images/R11E.png")]

    walkLeft = [pygame.image.load("./images/L1E.png"),
                pygame.image.load("./images/L2E.png"),
                pygame.image.load("./images/L3E.png"),
                pygame.image.load("./images/L4E.png"),
                pygame.image.load("./images/L5E.png"),
                pygame.image.load("./images/L6E.png"),
                pygame.image.load("./images/L7E.png"),
                pygame.image.load("./images/L8E.png"),
                pygame.image.load("./images/L9E.png"),
                pygame.image.load("./images/L10E.png"),
                pygame.image.load("./images/L11E.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        global score
        if self.health - 1 > 0:
            self.health -= 1
        else:
            self.visible = False
            self.cool()
            score += 1

    def cool(self):
        i = 5
        while i > 5:
            time.sleep(2)
            i -= 1
        self.visible = True
        self.x = randrange(self.path[0], self.path[-1])
        self.y = 421
        self.health = 10


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 150, 0))
    win.blit(text, (390, 20))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont("comicsans", 30, True)
man = Player(250, 417, 64, 64)
goblin = Enemy(10, 421, 64, 64, 426)
shootcool = 0
bullets = []
running = True
while running:
    clock.tick(27)

    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[
        1] and goblin.visible:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()

    if shootcool > 0:
        shootcool += 1
    if shootcool > 5:
        shootcool = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1] and goblin.visible:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootcool == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(Projectile((man.x + man.width // 2), (man.y + man.width // 2), 6, (20, 20, 20), facing))
            bulletSound.play()

        shootcool = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < sc_width - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.standing = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= man.jumpCount * 2
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
