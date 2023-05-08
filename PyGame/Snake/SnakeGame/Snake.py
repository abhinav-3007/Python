import pygame
import random
import sys

pygame.init()

win = pygame.display.set_mode((525, 525))
pygame.display.set_caption("Snake")
icon = pygame.image.load(r'./icons/icon.icn')
pygame.display.set_icon(icon)

grid_ct = 21
grid_w = 25
grid_h = 25
mute = False
sfx = False


class Snake:
    def __init__(self):
        self.pos = [[10, 10]]
        self.score = 0
        self.dir = ["", 0]

    def add(self):
        global speed
        global highscore
        speed -= 0.5
        x = self.pos[0][0]
        y = self.pos[0][1]
        self.score += 1
        if self.dir[0] == "x":
            self.pos.append([x - self.dir[1], y])
        elif self.dir[0] == "y":
            self.pos.append([x, y - self.dir[1]])
        if highscore < snake.score:
            highscore = snake.score

    @staticmethod
    def turn():
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and snake.dir[0] != "x":
            snake.dir = ["x", -1]
        if key[pygame.K_RIGHT] and snake.dir[0] != "x":
            snake.dir = ["x", 1]
        if key[pygame.K_UP] and snake.dir[0] != "y":
            snake.dir = ["y", -1]
        if key[pygame.K_DOWN] and snake.dir[0] != "y":
            snake.dir = ["y", 1]

    def move(self):
        x = self.pos[0][0]
        y = self.pos[0][1]
        if x > 0 and x * grid_w + grid_w < 525 and y > 0 and y * grid_h + grid_h < 525:
            if self.dir[0] == "x":
                x = x + self.dir[1]
            elif self.dir[0] == "y":
                y = y + self.dir[1]
            self.pos.pop()
            self.pos.insert(0, [x, y])
        else:
            self.die()

    def draw(self):
        for i in self.pos:
            x = self.pos.index(i)
            if x != 0:
                pygame.draw.rect(win, (0, 0, 225), (self.pos[x][0] * grid_w, self.pos[x][1] * grid_h, grid_w, grid_h))
                pygame.draw.rect(win, (0, 0, 150), (self.pos[x][0] * grid_w, self.pos[x][1] * grid_h, grid_w, grid_h),
                                 1)
            else:
                pygame.draw.rect(win, (0, 0, 150), (self.pos[x][0] * grid_w, self.pos[x][1] * grid_h, grid_w, grid_h))

    @staticmethod
    def die():
        die.play()
        s = pygame.Surface((1000, 750))
        s.set_alpha(128)
        s.fill((128, 128, 128))
        win.blit(s, (0, 0))
        font = pygame.font.SysFont("comicsansms", 35, True)
        text1 = font.render("You Died! Your score was: " + str(snake.score), 1, (128, 10, 10))
        text2 = font.render("Press Q to quit", 1, (128, 10, 10))
        text3 = font.render("Press Space to play again", 1, (128, 10, 10))
        win.blit(text1, ((525 - text1.get_width()) // 2, 200))
        win.blit(text2, ((525 - text2.get_width()) // 2, 250))
        win.blit(text3, ((525 - text3.get_width()) // 2, 300))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main()
                    if event.key == pygame.K_q:
                        running = False
        pygame.quit()
        sys.exit(0)


class Food:
    def __init__(self):
        self.x = random.randrange(1, 19)
        self.y = random.randrange(1, 19)

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x * grid_w, self.y * grid_h, grid_w, grid_h))

    def eat(self):
        while True:
            x1 = random.randrange(1, 19)
            y1 = random.randrange(1, 19)
            if [x1, y1] not in snake.pos and [x1, y1] != [self.x, self.y]:
                self.x = x1
                self.y = y1
                break


def draw():
    for y in range(0, grid_ct):
        for x in range(0, grid_ct):
            if x == 0 or y == 0 or x == 20 or y == 20:
                pygame.draw.rect(win, (0, 50, 0), (x * grid_w, y * grid_h, grid_w, grid_h))
            elif (x + y) % 2 == 0:
                pygame.draw.rect(win, (0, 150, 0), (x * grid_w, y * grid_h, grid_w, grid_h))
            else:
                pygame.draw.rect(win, (0, 255, 0), (x * grid_w, y * grid_h, grid_w, grid_h))
    font = pygame.font.SysFont("comicsansms", 15, True)
    text1 = font.render("Score: " + str(snake.score), 1, (200, 200, 200))
    text2 = font.render("High Score: " + str(highscore), 1, (200, 200, 200))
    win.blit(text1, (3, 3))
    win.blit(text2, (522 - (text2.get_width()), 3))

    if mute:
        music_icn = pygame.transform.scale(pygame.image.load(r'./icons/music_off.png'), (35, 25))
    else:
        music_icn = pygame.transform.scale(pygame.image.load(r'./icons/music_on.png'), (30, 25))

    if sfx:
        sfx_icn = pygame.transform.scale(pygame.image.load(r'./icons/sfx_off.png'), (40, 35))
    else:
        sfx_icn = pygame.transform.scale(pygame.image.load(r'./icons/sfx_on.png'), (40, 35))

    shortcut1 = font.render("(Shortcut: A)", 1, (200, 200, 200))
    shortcut2 = font.render("(Shortcut: S)", 1, (200, 200, 200))
    win.blit(music_icn, (0, 500))
    win.blit(sfx_icn, (488 - (shortcut2.get_width() + 5), 495))

    win.blit(shortcut1, (40, 500))
    win.blit(shortcut2, (488 - (shortcut2.get_width()) + 35, 500))
    food.draw()
    snake.draw()
    pygame.display.flip()


def main():
    global speed
    global mute
    global sfx
    run = True
    speed = 80
    snake.__init__()
    food.__init__()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_a]:
                    mute = not mute
                elif key[pygame.K_s]:
                    sfx = not sfx
                else:
                    snake.turn()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] <= 150 and position[1] >= 495:
                    mute = not mute
                elif position[0] >= 375 and position[1] >= 500:
                    sfx = not sfx

        draw()
        snake.move()
        if snake.pos[0][0] == food.x and snake.pos[0][1] == food.y:
            chomp.play()
            food.eat()
            snake.add()
        head = snake.pos[0]
        if head in snake.pos[1:]:
            snake.die()
        if mute:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        if sfx:
            chomp.set_volume(0)
            die.set_volume(0)
        else:
            chomp.set_volume(1)
            die.set_volume(1)
        pygame.time.delay(int(speed))


snake = Snake()
food = Food()

highscore = 0
speed = 100

chomp = pygame.mixer.Sound("./sounds/chomp.wav")
die = pygame.mixer.Sound("./sounds/die.wav")
pygame.mixer.music.load("./sounds/bg.wav")
pygame.mixer.music.play(-1)

main()

pygame.quit()
