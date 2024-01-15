import math
import random
import sys
import pygame
from random import uniform, choice


class Paddle:
    def __init__(self):
        self.len = 2
        self.bth = 60
        self.y = 226
        self.points = 0


class Ball:
    def __init__(self, win):
        self.v = [choice([-1, 1])*uniform(1.5, 2), choice([-1, 1])*uniform(1.5, 2)]
        # while self.v == [0, 0]:
        #     self.v = [choice([-1, 1])*uniform(1.5, 2), choice([-1, 1])*uniform(1.5, 2)]
        self.x = 512
        self.y = 256
        self.surface = win
        self.victory = 5
        self.winner = ""

    def reset(self):
        # erasing the previous ball
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x - 8, self.y - 8, 16, 16))
        self.v = [choice([-1, 1])*uniform(1.5, 2), choice([-1, 1])*uniform(1.5, 2)]
        self.x = 512
        self.y = 256
        # drawing the ball
        pygame.draw.rect(self.surface, (255, 255, 255), (self.x - 8, self.y - 8, 16, 16))
        pygame.display.flip()
        if not wait():
            sys.exit()

    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]

    def bounce(self):
        # checking if ball hits edge
        if self.y <= 0:
            self.v[1] = -self.v[1]
        if self.y >= 512:
            self.v[1] = -self.v[1]
        

# function to draw all items
def draw(win, colour, p1, p2, ball, font):
    # filling background with black
    win.fill((0, 0, 0))
    # drawing the middle dividing line
    pygame.draw.rect(win, colour, (510, 0, 4, 512))
    # drawing the first paddle
    pygame.draw.rect(win, colour, (7, p1.y, p1.len, p1.bth))
    # drawing the second paddle
    pygame.draw.rect(win, colour, (1012, p2.y, p2.len, p2.bth))
    # drawing the ball
    pygame.draw.rect(win, colour, (ball.x-8, ball.y-8, 16, 16))
    # displaying the score
    score1 = font.render(str(p1.points), 1, colour)
    score2 = font.render(str(p2.points), 1, colour)
    win.blit(score1, (512-score1.get_width()-20, 10))
    win.blit(score2, (512+20, 10))


def check(ball, p1, p2, win):
    # checking if ball hits top half of p1's paddle
    if ball.x-8 <= 9 and ball.x+8 >= 7 and ball.y+8 >= p1.y and ball.y-8 <= p1.y+30:
        ball.v[0] = -ball.v[0] + 0.1
        ball.v[1] = -abs(ball.v[1]) - 0.1
        ball.x = 18
    # checking if ball hits bottom half of p1's paddle
    if ball.x - 8 <= 9 and ball.x + 8 >= 7 and ball.y + 8 >= p1.y+31 and ball.y-8 <= p1.y+60:
        ball.v[0] = -ball.v[0] + 0.1
        ball.v[1] = abs(ball.v[1]) + 0.1
        ball.x = 18
    # checking if ball hits top half of p2's paddle
    if ball.x+8 >= 1012 and ball.x-8 <= 1014 and ball.y+8 >= p2.y and ball.y-8 <= p2.y+30:
        ball.v[0] = -ball.v[0] - 0.1
        ball.v[1] = -abs(ball.v[1]) - 0.1
        ball.x = 1005
    # checking if ball hits bottom half of p2's paddle
    if ball.x + 8 >= 1012 and ball.x - 8 <= 1014 and ball.y + 8 >= p2.y+31 and ball.y - 8 <= p2.y + 60:
        ball.v[0] = -ball.v[0] - 0.1
        ball.v[1] = abs(ball.v[1]) + 0.1
        ball.x = 1005

    # checking if a player scored
    if ball.x-8 <= 0:
        p2.points += 1
        font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
        draw(win, (255, 255, 255), p1, p2, ball, font)
        if p2.points == ball.victory:
            ball.winner = "p2"
            ball.x = 50
        else:
            ball.reset()
    if ball.x+8 >= 1024:
        p1.points += 1
        font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
        draw(win, (255, 255, 255), p1, p2, ball, font)
        if p1.points == ball.victory:
            ball.winner = "p1"
            ball.x = 0
        else:
            ball.reset()


def wait():
    # loop to wait for player to press any key
    while True:
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                return False
            # checking if any key is pressed
            if event.type == pygame.KEYDOWN:
                return True


def options(win, ball):
    show = True
    while show:
        # loading the font
        font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
        # rendering the text
        text = font.render("Score to win:", True, (255, 255, 255))
        plus = font.render(" + ", True, (255, 255, 255))
        val = font.render(str(ball.victory), True, (255, 255, 255))
        sub = font.render(" - ", True, (255, 255, 255))
        back = font.render("<- Go Back(esc)", True, (255, 255, 255))
        # x and y coordinates of plus button
        plusx = (1024 - plus.get_width()) // 2 + 140
        plusy = (512 - plus.get_height()) // 2 - 20
        # x and y coordinates of subtract button
        subx = (1024 - sub.get_width()) // 2 + 140
        suby = (512 - sub.get_height()) // 2 + 20
        # x and y coordinates of back button
        backx = 5
        backy = 5
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if plusx <= position[0] <= plusx + plus.get_width() and \
                        plusy <= position[1] <= plusy + plus.get_height():
                    ball.victory += 1
                if subx <= position[0] <= subx + sub.get_width() and \
                        suby <= position[1] <= suby + sub.get_height() and ball.victory > 1:
                    ball.victory -= 1
                if backx <= position[0] <= backx + back.get_width() and \
                        backy <= position[1] <= backy + back.get_height():
                    show = False

        # displaying the text and buttons
        win.blit(text, ((1024 - text.get_width()) // 2 - 10, (512 - text.get_height()) // 2))
        win.blit(plus, (plusx, plusy))
        win.blit(val, ((1024 - val.get_width()) // 2 + 142, (512 - val.get_height()) // 2))
        win.blit(sub, (subx, suby))
        win.blit(back, (backx, backy))
        pygame.display.flip()
        win.fill([0, 0, 0])


# function to display the title screen
def title(win, ball):
    # initializing the font
    font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
    titlefont = pygame.font.Font("./fonts/ArcadeFont.TTF", 40)
    # displaying the title screen
    titletext = titlefont.render("PONG", True, (255, 255, 255))
    opt = font.render("Help and Options", True, (255, 255, 255))
    text = font.render("Start Game", True, (255, 255, 255))
    win.blit(titletext, ((1024 - titletext.get_width()) // 2, ((512 - titletext.get_height()) // 2) - 60))
    win.blit(opt, ((1024 - opt.get_width()) // 2, (512 - opt.get_height()) // 2))
    win.blit(text, ((1024 - text.get_width()) // 2, ((512 - text.get_height()) // 2) + 50))
    pygame.display.flip()
    for event in pygame.event.get():
        # checking whether program is to be exited
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            optx = (1024 - opt.get_width()) // 2
            opty = (512 - opt.get_height()) // 2
            startx = (1024 - text.get_width()) // 2
            starty = ((512 - text.get_height()) // 2) + 50
            if optx <= position[0] <= optx+opt.get_width() and \
                    opty <= position[1] <= opty + opt.get_height():
                options(win, ball)
            if startx <= position[0] <= startx+text.get_width() and \
                    starty <= position[1] <= starty + text.get_height():
                return True


def end(ball, win):
    while True:
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)
        restart = font.render("Press SPACE to play again", True, (255, 255, 255))
        if ball.winner == "p1":
            text = font.render("Player 1 is the Winner!", True, (255, 255, 255))
        else:
            text = font.render("Player 2 is the Winner!", True, (255, 255, 255))
        win.blit(text, ((1024 - text.get_width()) // 2, ((512 - text.get_height()) // 2)))
        win.blit(restart, ((1024 - restart.get_width()) // 2, ((512 - restart.get_height()) // 2)+50))
        pygame.display.flip()


def main():
    # initializing the game modules
    pygame.init()
    # setting window icon
    icon = pygame.image.load('icons/icon.ico')
    pygame.display.set_icon(icon)
    # Creating the game window
    win = pygame.display.set_mode((1024, 512))
    # setting the title of the window
    pygame.display.set_caption("Pong")
    # creating the 2 player objects and ball object
    p1 = Paddle()
    p2 = Paddle()
    ball = Ball(win)

    # initializing the font
    font = pygame.font.Font("./fonts/ArcadeFont.TTF", 20)

    # loading the title screen
    while True:
        if title(win, ball):
            break

    # running stores what is returned by wait() function
    running = True
    # main loop
    while running:
        if ball.winner != "":
            break
        draw(win, (255, 255, 255), p1, p2, ball, font)
        # checking if ball needs to change direction
        ball.bounce()
        check(ball, p1, p2, win)
        # moving the ball
        ball.move()
        for event in pygame.event.get():
            # checking whether program is to be exited
            if event.type == pygame.QUIT:
                running = False

        # key is list of all keys being pressed at the moment
        key = pygame.key.get_pressed()
        # Movement of player 1
        if key[pygame.K_w] and p1.y > 8:
            p1.y -= 3
        if key[pygame.K_s] and p1.y < 444:
            p1.y += 3

        # Movement of player 2
        if key[pygame.K_UP] and p2.y > 8:
            p2.y -= 3
        if key[pygame.K_DOWN] and p2.y < 444:
            p2.y += 3

        # Updating the game window
        pygame.display.flip()
        #  setting the game clock
        pygame.time.delay(4)
    end(ball, win)


main()
