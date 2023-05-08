import pygame
import sys
import random

pygame.init()

# length of side of game window
window_len = 525
# creates the game window and sets the title to "Space Invaders"
win = pygame.display.set_mode((window_len, window_len))
pygame.display.set_caption("Space Invaders")
# sets icon to icon.icn
icon = pygame.image.load('./images/icon.icn')
pygame.display.set_icon(icon)
# saves RGB values of colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
neon_green = (57, 255, 20)
blue = (0, 0, 255)
# loads the images of aliens and spaceship and resizes them to 30x25 pixels
spaceship_img = pygame.transform.scale(pygame.image.load(r'./images/spaceship.png'), (30, 25))
sfx_img = pygame.transform.scale(pygame.image.load(r'./images/sfx_on.png'), (40, 35))
# Loading sounds
shoot = pygame.mixer.Sound("./sounds/shoot.wav")
shoot.set_volume(0.1)
hit = pygame.mixer.Sound("./sounds/invaderkilled.wav")
hit.set_volume(0.1)
shiphit = pygame.mixer.Sound("./sounds/hit.wav")
shiphit.set_volume(0.5)
death = pygame.mixer.Sound("./sounds/explosion.wav")
fanfare = pygame.mixer.Sound("./sounds/victory.wav")
fanfare.set_volume(0.5)
countdown1 = pygame.mixer.Sound("./sounds/countdown1.wav")
countdown1.set_volume(0.5)
countdown2 = pygame.mixer.Sound("./sounds/countdown2.wav")
countdown2.set_volume(0.5)
pygame.mixer.music.load("./sounds/bg.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
mute = False
sfx = False


class Spaceship:
    def __init__(self):
        # sets default value of x value of spaceship to centre of screen
        self.x = (window_len / 2) - 15
        self.score = 0
        self.lives = 3

    # function to draw spaceship
    def draw(self):
        win.blit(spaceship_img, (self.x, 460))

    def hit(self, row):
        if row == 0:
            self.score += 30
        elif row in [1, 2]:
            self.score += 20
        else:
            self.score += 10


class Aliens:
    def __init__(self):
        # saves whether the aliens moved down in the previous loop or not
        self.down = 0
        # amount to be moved at a time by aliens
        self.increment = 0.5
        # stores the number of times move function has been called, in order to add sufficient delay
        self.count = 0
        # stores which sprite to use (1 is first, -1 is second)
        self.sprite = 1
        # list of existing aliens
        self.alienli = [list(range(0, 11)) for x in range(0, 5)]

        # loading images of aliens
        self.alien_img = pygame.transform.scale(pygame.image.load(r'./images/alien.png'), (30, 25))
        self.alien_img2 = pygame.transform.scale(pygame.image.load(r'./images/alien2.png'), (30, 25))

        self.boltli = []

    # function to move aliens
    def move(self):
        global run
        if self.count == 25:
            # condition to choose which sprite to use
            if abs(self.sprite) != self.sprite or self.sprite == 0:
                self.alien_img = pygame.transform.scale(pygame.image.load(r'./images/alien.png'), (30, 25))
                self.alien_img2 = pygame.transform.scale(pygame.image.load(r'./images/alien2.png'), (30, 25))
                self.sprite = 1
            else:
                self.alien_img = pygame.transform.scale(pygame.image.load(r'./images/alien2.png'), (30, 25))
                self.alien_img2 = pygame.transform.scale(pygame.image.load(r'./images/alien.png'), (30, 25))
                self.sprite = -1

            # condition on whether to move aliens down or not
            if (max([i[-1] for i in self.alienli if len(i) > 0]) >= (520 / 35) - 1 or (
                    min([i[0] for i in self.alienli if len(i) > 0]) == 0 and len(
                    self.alienli) != 5)) and self.down == 0:
                self.alienli.insert(0, [])
                self.increment = -self.increment
                self.down = 1
            else:
                self.down = 0
                for i in self.alienli:
                    for j in range(0, len(i)):
                        x = i[j]
                        i.insert(j, x + self.increment)
                        i.pop(j + 1)

            if len(aliens.alienli) * 25 + 55 >= 420:
                ship.lives = 0
                run = False

            self.count = 0
        self.count += 1
        self.draw()

    # function to draw the aliens
    def draw(self):
        li = [len(x) for x in self.alienli if len(x) > 0]
        maximum = max(li)
        row = [x for x in self.alienli if len(x) == maximum][0]
        canshoot = True
        for i, k in enumerate(self.alienli):
            for j in k:
                if k.index(j) % 2 == 0:
                    win.blit(self.alien_img, (j * 35, (i * 25) + 55))
                else:
                    win.blit(self.alien_img2, (j * 35, (i * 25) + 55))
                if k == row:
                    if random.randrange(0, 100) == 5 and len(self.boltli) == 0 and canshoot:
                        self.boltli.append(Bullet(x=(j * 35) + 15, y=(i * 25) + 55, shape="bolt", facing=-1))
                        canshoot = False


class Bullet:
    def __init__(self, x, y=455, shape="rect", facing=1):
        self.x = x - 1
        self.y = y
        self.shape = shape
        self.facing = facing
        self.move()

    def move(self):
        global barriers
        global bullets
        self.y -= 10 * self.facing
        if self.shape == "rect":
            for i in barriers:
                for j in range(0, len(i.barrierli)):
                    if bullets:
                        for k in i.barrierli[j]:
                            barriery = i.y + 5 * j
                            barrierx = i.x + 5 * k
                            if barriery <= self.y <= barriery + 5 and barrierx <= self.x <= barrierx + 5:
                                bullets.clear()
                                i.barrierli[j].remove(k)
                    else:
                        break
        else:
            for i in aliens.boltli:
                if i.y >= 500:
                    aliens.boltli.remove(i)
                elif 495 >= i.y >= 470 and ship.x + 30 >= i.x >= ship.x:
                    shiphit.play()
                    for j in range(0, 10):
                        pygame.draw.rect(win, black, (int(ship.x), 460, 32, 25))
                        pygame.display.flip()
                        pygame.time.delay(10)
                        ship.draw()
                        pygame.display.flip()
                        pygame.time.delay(10)
                    aliens.boltli.remove(i)
                    ship.lives -= 1

            for bolt in aliens.boltli:
                for i in barriers:
                    for j in range(0, len(i.barrierli)):
                        for k in i.barrierli[j]:
                            barriery = i.y + 5 * j
                            barrierx = i.x + 5 * k
                            if barriery <= bolt.y + 10 <= barriery + 5 and barrierx <= bolt.x <= barrierx + 5:
                                aliens.boltli.remove(bolt)
                                i.barrierli[j].remove(k)
                                break
                        if bolt not in aliens.boltli:
                            break
                    if bolt not in aliens.boltli:
                        break
        self.draw()

    def draw(self):
        if self.shape == "rect":
            pygame.draw.rect(win, yellow, (self.x, self.y, 3, 10))
        else:
            pygame.draw.rect(win, red, (self.x, self.y, 3, 10))


class Barrier:
    def __init__(self, x):
        self.x = x
        self.y = 405
        self.barrierli = []
        for i in range(0, 5):
            self.barrierli.append([j for j in range(0, 10)])

    def draw(self):
        for i, k in enumerate(self.barrierli):
            for j in k:
                pygame.draw.rect(win, neon_green, (self.x + 5 * j, self.y + 5 * i, 4, 4))


def mutesfx():
    if sfx:
        shoot.set_volume(0)
        hit.set_volume(0)
        shiphit.set_volume(0)
        death.set_volume(0)
        fanfare.set_volume(0)
        countdown1.set_volume(0)
        countdown2.set_volume(0)
    else:
        shoot.set_volume(0.1)
        hit.set_volume(0.1)
        shiphit.set_volume(0.2)
        death.set_volume(1)
        fanfare.set_volume(0.5)
        countdown1.set_volume(0.5)
        countdown2.set_volume(0.5)


def mutemusic():
    if mute:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(0.4)


def instructions():
    win.fill(black)
    title = font1.render("How To Play", True, yellow)
    movement = font2.render("Use the left and right arrow", True, white)
    movement2 = font2.render("keys to move.", True, white)
    shoot = font2.render("Press the spacebar to shoot.", True, white)
    goal1 = font2.render("Your goal is to kill the aliens", True, white)
    goal2 = font2.render("before they reach your spaceship.", True, white)
    defence1 = font2.render("You can use the green squares", True, white)
    defence2 = font2.render("as shields.", True, white)
    warning1 = font2.render("Be careful because the aliens", True, white)
    warning2 = font2.render("can shoot back and you have ", True, white)
    warning3 = font2.render("only 3 extra ships!", True, white)
    ending1 = font2.render("Let's see if you have what", True, white)
    ending2 = font2.render("it takes to save your", True, white)
    ending3 = font2.render("planet from an alien invasion!", True, white)
    txtcolour = white
    back = font2.render("<-- Back(shortcut: esc)", True, txtcolour)
    win.blit(title, ((525 - title.get_width()) // 2, 15))
    win.blit(movement, ((525 - movement.get_width()) // 2, 60))
    win.blit(movement2, ((525 - movement2.get_width()) // 2, 80))
    win.blit(shoot, ((525 - shoot.get_width()) // 2, 115))
    win.blit(goal1, ((525 - goal1.get_width()) // 2, 150))
    win.blit(goal2, ((525 - goal2.get_width()) // 2, 170))
    win.blit(defence1, ((525 - defence1.get_width()) // 2, 205))
    win.blit(defence2, ((525 - defence2.get_width()) // 2, 225))
    win.blit(warning1, ((525 - warning1.get_width()) // 2, 260))
    win.blit(warning2, ((525 - warning2.get_width()) // 2, 280))
    win.blit(warning3, ((525 - warning3.get_width()) // 2, 300))
    win.blit(ending1, ((525 - ending1.get_width()) // 2, 335))
    win.blit(ending2, ((525 - ending2.get_width()) // 2, 355))
    win.blit(ending3, ((525 - ending3.get_width()) // 2, 375))
    leave = False
    while not leave:
        back = font2.render("<-- Back(shortcut: esc)", True, txtcolour)
        win.blit(back, (10, 500))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    leave = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                textx = 10
                texty = 500
                if textx <= position[0] <= textx + back.get_width() and texty + 14 >= position[1] >= texty:
                    leave = True
            if not event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                textx = 10
                texty = 500
                if textx <= position[0] <= textx + back.get_width() and texty + 14 >= position[1] >= texty:
                    txtcolour = blue
                else:
                    txtcolour = white


def pause():
    pass


def end():
    running = True
    resume = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_SPACE:
                    resume = True
                    running = False
    if resume:
        main()
    else:
        sys.exit()


def main():
    global bullets, mute, run, ship, aliens, sfx
    ct = 3
    # creating spaceship and alien objects
    ship = Spaceship()
    aliens = Aliens()
    # loop for countdown
    for i in range(800, 50, -1):
        win.fill(black)
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # checking if program is to be exited
                if key[pygame.K_q]:
                    sys.exit()
                if key[pygame.K_m]:
                    mute = not mute
                    mutemusic()
                if key[pygame.K_n]:
                    sfx = not sfx
                    mutesfx()
        if i % 200 == 0:
            # displaying either GO or number
            if ct == 0:
                numtxt = font1.render("GO", True, green)
                countdown2.play()
            else:
                numtxt = font1.render(str(ct), True, white)
                countdown1.play()
            ct -= 1

        win.blit(numtxt, (525 // 2 - numtxt.get_width() // 2, 250))
        pygame.display.flip()
        pygame.time.delay(5)

    bullets = []
    victory = False
    barrier1 = Barrier(x=73)
    barrier2 = Barrier(x=186)
    barrier3 = Barrier(x=299)
    barrier4 = Barrier(x=412)
    barriers = [barrier1, barrier2, barrier3, barrier4]

    # main loop
    while run:
        win.fill(black)
        # displaying the score and remaining lives of the person
        scoretxt = font2.render("Score: " + str(ship.score), True, white)
        lifetxt = font2.render("Remaining Ships:", True, white)
        menutxt = font2.render("Options(esc)", True, white)
        win.blit(scoretxt, (5, 5))
        win.blit(lifetxt, (5, 500))
        pygame.draw.rect(win, white, (0, 30, window_len, 2))
        pygame.draw.rect(win, white, (0, 490, window_len, 2))
        lifex = lifetxt.get_width() + 3
        # drawing images for remaining ships
        for i in range(0, ship.lives):
            win.blit(pygame.transform.scale(spaceship_img, (18, 15)), (lifex, 500))
            lifex += 20
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                run = False
            # Checking if a key is pressed
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # toggling muting of the music
                if key[pygame.K_m]:
                    mute = not mute
                    mutemusic()
                #  toggling muting of sound effects
                if key[pygame.K_n]:
                    sfx = not sfx
                    mutesfx()
        for i in barriers:
            i.draw()
        ship.draw()
        aliens.move()
        # key is list of all keys being pressed at the moment
        key = pygame.key.get_pressed()

        # moving the ship left
        if key[pygame.K_LEFT] and ship.x > 5:
            ship.x -= 3

        # moving the ship right
        if key[pygame.K_RIGHT] and ship.x < window_len - 35:
            ship.x += 3

        if key[pygame.K_SPACE] and len(bullets) == 0:
            shoot.play()
            bullet = Bullet(x=ship.x + 15)
            bullets.append(bullet)

        if len(bullets) == 1:
            bullet.move()
            if bullet.y <= 15:
                bullets.clear()
            for i in range(len(aliens.alienli) - 1, -1, -1):
                alieny = (i * 25) + 55
                li = aliens.alienli[i]
                for j in range(0, len(li)):
                    if li[j] * 35 <= bullet.x <= li[j] * 35 + 30 and alieny + 25 >= bullet.y >= alieny:
                        hit.play()
                        bullets = []
                        li.pop(j)
                        aliens.alienli[i] = li
                        ship.hit(aliens.alienli[-5:].index(li))
                        break
                if not bullets:
                    break
        boolli = []
        for i in aliens.alienli:
            if len(i) == 0:
                boolli.append(False)
            else:
                boolli.append(True)
        if not any(boolli):
            victory = True
            break
        if aliens.boltli:
            for i in aliens.boltli:
                i.move()

        if ship.lives <= 0:
            run = False
        win.blit(menutxt, (520 - (menutxt.get_width()), 5))

        # loop to remove last list in alienli if it is empty
        while not aliens.alienli[-1]:
            aliens.alienli.pop()

        # refreshes the game window
        pygame.display.flip()
        # sets delay in loop for smooth running
        pygame.time.delay(20)

    running = False
    if victory:
        fanfare.play()
        win.fill(black)
        over = font1.render("YOU WON!", True, green)
        again = font1.render("PRESS SPACE TO PLAY AGAIN", True, green)
        win.blit(over, ((525 - over.get_width()) // 2, 250))
        win.blit(again, ((525 - again.get_width()) // 2, 280))
        pygame.display.update()
        running = True
        end()
    if ship.lives <= 0:
        pygame.time.delay(120)
        death.play()
        win.fill(black)
        over = font1.render("GAME OVER", True, red)
        again = font1.render("PRESS SPACE TO PLAY AGAIN", True, red)
        win.blit(over, ((525 - over.get_width()) // 2, 250))
        win.blit(again, ((525 - again.get_width()) // 2, 280))
        pygame.display.update()
        running = True
        end()


# creating spaceship and alien objects
ship = Spaceship()
aliens = Aliens()
run = False
font1 = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
font2 = pygame.font.Font("./fonts/ArcadeFont.TTF", 14)
colour = white
bullets = []
victory = False
barrier1 = Barrier(x=73)
barrier2 = Barrier(x=186)
barrier3 = Barrier(x=299)
barrier4 = Barrier(x=412)
barriers = [barrier1, barrier2, barrier3, barrier4]

while not run:
    win.fill(black)
    text1 = font1.render("SPACE INVADERS", True, yellow)
    text2 = font1.render("Press Q to quit", True, white)
    text3 = font1.render("Press Space to start", True, white)
    text4 = font1.render("How to Play", True, colour)
    win.blit(text1, ((525 - text1.get_width()) // 2, 175))
    win.blit(text2, ((525 - text2.get_width()) // 2, 225))
    win.blit(text3, ((525 - text3.get_width()) // 2, 275))
    win.blit(text4, ((525 - text4.get_width()) // 2, 325))
    pygame.display.flip()
    for event in pygame.event.get():
        # checking whether program is to be exited
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            # checking if program is to be exited
            if key[pygame.K_q]:
                sys.exit()
            # Checks when to start the game
            if key[pygame.K_SPACE]:
                run = True
                main()
                break
            if key[pygame.K_m]:
                mute = not mute
                mutemusic()
            if key[pygame.K_n]:
                sfx = not sfx
                mutesfx()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            textx = (525 - text4.get_width()) // 2
            texty = 325
            if textx <= position[0] <= textx + text4.get_width() and texty + 20 >= position[1] >= texty:
                instructions()
        if not event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            textx = (525 - text4.get_width()) // 2
            texty = 325
            if textx <= position[0] <= textx + text4.get_width() and texty + 20 >= position[1] >= texty:
                colour = blue
            else:
                colour = white
