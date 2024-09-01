import random
import pygame


class Player:
    def __init__(self):
        self.health = 4
        self.score = 0
        self.image = pygame.transform.scale(pygame.image.load(f'../images/level_4/man1.png'), (92, 120))
        self.injured = pygame.transform.scale(
            pygame.image.load(f'../images/level_4/man_hit.png'), (92, 120))
        self.healed = pygame.transform.scale(
            pygame.image.load(f'../images/level_4/man_healed.png'), (92, 120))
        self.sprites = []
        self.attack_sprites = []
        self.setImage()
        self.image_count = 0
        self.x = 80
        self.y = 500
        self.isJump = False
        self.jump_velocity = 70
        self.invulnerability = 0
        self.hit_countdown = 0
        self.attack_countdown = 40
        self.attack_cooldown = 0
        self.hitbox = pygame.Rect(self.x + 20, self.y, 62, 120)
        self.attack_hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())
        self.sound = pygame.mixer.Sound('../audio/whip.wav')
        with open('72105103104328399111114101.BHAENS', mode='rb') as high_score:
            self.high_score = int.from_bytes(high_score.read(), byteorder='big')
        self.dead = False
        self.pause = False
        self.start = False
        self.instructions = False

    def draw(self):
        self.image = self.sprites[self.image_count // 15]
        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites)*15:
            self.image_count += 1
        else:
            self.image_count = 0

        if self.attack_countdown < 40:
            if self.health > 1:
                image_index = min(self.attack_countdown//10, len(self.attack_sprites)-1)
                self.image = self.attack_sprites[image_index]
            self.attack_countdown += 1
            self.attack_cooldown = 400

        if self.hit_countdown > 0:
            self.image = self.injured
            self.hit_countdown = max(0, self.hit_countdown - 1)
        elif self.hit_countdown < 0:
            self.image = self.healed
            self.hit_countdown = min(0, self.hit_countdown + 1)
        self.hitbox = pygame.Rect(self.x + 20, self.y, 62, 120)
        self.attack_hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())
        win.blit(self.image, (self.x, self.y))

    def setImage(self):
        # loading the images for the player
        self.sprites = [pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man1.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man2.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man3.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man4.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man5.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man6.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man7.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.health}/man8.png'), (92, 120))]
        self.attack_sprites.clear()
        # loading the images for when the player attacks
        for i in range(2, self.health+1):
            length = 176 if i == 2 else 318 if i == 3 else 459
            self.attack_sprites.append(
                pygame.transform.scale(pygame.image.load(f'../images/level_{i}/man_shooting.png'), (length, 120)))
        # loading image for when player is hit
        self.injured = pygame.transform.scale(
            pygame.image.load(f'../images/level_{self.health}/man_hit.png'), (92, 120))
        # loading image for when player is healed
        self.healed = pygame.transform.scale(
            pygame.image.load(f'../images/level_{self.health}/man_healed.png'), (92, 120))


class Background:
    def __init__(self):
        self.image_width = 662
        self.image = pygame.transform.scale(pygame.image.load('../images/bg.png'), (self.image_width, 600))
        self.x = 0
        self.y = 50
        self.velocity = 1.5
    
    def draw(self, move):
        win.blit(self.image, (self.x, self.y))
        win.blit(self.image, (self.x + self.image_width, self.y))
        win.blit(self.image, (self.x + self.image_width*2, self.y))
        if move:
            if self.x+self.velocity <= -self.image_width:
                self.x = 0
            else:
                self.x -= self.velocity


class Character:
    spawn = True
    x_velocity = 3
    def __init__(self, y, image):
        # placeholder image
        self.image = image
        self.x = 1000
        self.y = y
        self.y_velocity = 0
        self.damage = 1
        self.hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())

    def move(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
        self.hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())


class GrowthSerum(Character):
    x_velocity = 1.5
    def __init__(self, x, y, regen_amount, height):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/growth_serum.png'), (int(round(0.5625*height)), height)))
        self.x = x
        self.damage = -regen_amount
        self.image_count = 0
        self.sound = pygame.mixer.Sound('../audio/growth_serum.wav')

    def move(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.y += 5
        elif self.image_count == 80:
            self.y -= 5
            self.image_count = 0


class Razor(Character):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (83, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (83, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/razor2.png'), (83, 140))]
        self.image_count = 0
        self.sound = pygame.mixer.Sound('../audio/razor.wav')

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.image = self.sprites[1]
            self.image_count = 0


class Scissors(Character):
    x_velocity = 5
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)),
                             pygame.transform.scale(pygame.image.load('../images/enemies/scissors2.png'), (245, 140))]
        self.image_count = 40
        self.damage = 2
        self.sound = pygame.mixer.Sound("../audio/scissor.wav")

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.sound.play()
            self.image = self.sprites[1]
            self.image_count = 0


class Blade(Character):
    x_velocity = 7
    def __init__(self, x, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/blade.png'), (60, 76)))
        self.x = x
        self.damage = 1
        self.image_count = 0
        self.sound = pygame.mixer.Sound('../audio/blade_hit.wav')

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = pygame.transform.rotate(self.image, 90)
            self.image_count = 0


class Barber(Character):
    x_velocity = 2
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber2.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber3.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber4.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber5.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber6.png'), (88, 140))]
        self.image_count = 0
        self.throw_count = 250
        self.throw_limit = 250
        self.throw_sound = pygame.mixer.Sound('../audio/blade_throw.wav')
        self.sound = pygame.mixer.Sound('../audio/blade_hit.wav')

    def draw(self):
        win.blit(self.sprites[self.image_count // 20], (self.x, self.y))
        # iterating through various barber sprites
        if self.image_count + 1 < len(self.sprites) * 20:
            self.image_count += 1
        else:
            self.image_count = 0


def countdown(player, background, characters, font):
    for i in range(3, 0, -1):
        redrawGameWindow(player, background, characters, font, False)
        counter = font.render(f"{i}", 1, (255, 255, 255))
        win.blit(counter, (500 - counter.get_width() / 2, 350 - counter.get_height()))
        pygame.display.update()
        pygame.time.wait(1000)


def instructions(events, font, player):
    instructions_screen = pygame.Surface((1000, 650))
    instructions_screen.fill((89, 112, 112))
    title = font.render("SAVE YOUR MUSTACHE!", 1, (20, 0, 0))
    jump1 = font.render("Avoid the Barber's vicious attacks", 1, (20, 0, 0))
    jump2 = font.render("by jumping using the UP arrow key!", 1, (20, 0, 0))

    whip1 = font.render("Use your mustache to whip the barber using", 1, (20, 0, 0))
    whip2 = font.render("the SPACE key to get extra points and health!", 1, (20, 0, 0))

    back = font.render("BACK", 1, (20, 0, 0))
    back_button = pygame.Rect((480 - back.get_width() / 2, 390 - back.get_height(),
                                     back.get_width() + 40, back.get_height() + 40))
    # changing colour if mouse hovering over play again button
    if back_button.collidepoint(pygame.mouse.get_pos()):
        back = font.render("BACK", 1, (0, 128, 0))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.instructions = False
                return 0

    instructions_screen.blit(title, (500 - title.get_width() / 2, 200 - title.get_height()))
    instructions_screen.blit(jump1, (500 - jump1.get_width() / 2, 250 - jump1.get_height()))
    instructions_screen.blit(jump2, (500 - jump2.get_width() / 2, 280 - jump2.get_height()))
    instructions_screen.blit(whip1, (500 - whip1.get_width() / 2, 330 - whip1.get_height()))
    instructions_screen.blit(whip2, (500 - whip2.get_width() / 2, 360 - whip2.get_height()))
    instructions_screen.blit(back, (500 - back.get_width() / 2, 410 - back.get_height()))
    win.blit(instructions_screen, (0, 0))
    pygame.display.update()
    player.instructions = True


def homeScreen(events, start_font, player):
    title_font = pygame.font.Font('../fonts/ArcadeFont.ttf', 40)
    win.fill((89, 112, 112))
    title = title_font.render("BARBER RUN", 1, (113, 68, 47))
    how_to_play = start_font.render("How to Play", 1, (0, 0, 0))
    start = start_font.render("Start", 1, (0, 0, 0))
    how_to_play_button = pygame.Rect((480 - how_to_play.get_width() / 2, 330 - how_to_play.get_height(),
                                how_to_play.get_width() + 40, how_to_play.get_height() + 40))
    start_button = pygame.Rect((480 - start.get_width() / 2, 380 - start.get_height(),
                                start.get_width() + 40, start.get_height() + 40))

    # changing colour if mouse hovering over how to play button
    if how_to_play_button.collidepoint(pygame.mouse.get_pos()):
        how_to_play = start_font.render("How to Play", 1, (255, 255, 255))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.instructions = True
                return 0

    # changing colour if mouse hovering over start button
    if start_button.collidepoint(pygame.mouse.get_pos()):
        start = start_font.render("Start", 1, (125, 255, 71))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.start = True
                return 0

    razor = pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (118, 200))
    scissor = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (300, 171)), 300)
    blade = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/enemies/blade.png'), (79, 100)), 340)
    mustache = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/icon.png'), (70, 70)), 340)

    win.blit(title, (500 - title.get_width() / 2, 300 - title.get_height()))
    win.blit(how_to_play, (500 - how_to_play.get_width() / 2, 350 - how_to_play.get_height()))
    win.blit(start, (500 - start.get_width() / 2, 400 - start.get_height()))

    win.blit(mustache, (860 - title.get_width() / 2, 240 - title.get_height()))
    win.blit(razor, (100, 200))
    win.blit(scissor, (700, 20))
    win.blit(blade, (600, 450))
    pygame.display.update()
    player.start = False


def pauseScreen(events, font, player):
    pause_screen = pygame.Surface((1000, 650))
    pause_screen.set_alpha(5)
    pause_screen.fill((255, 255, 255))
    game_over = font.render("PAUSED", 1, (20, 0, 0))
    how_to_play = font.render("How to Play", 1, (20, 0, 0))
    resume = font.render("Resume", 1, (20, 0, 0))
    how_to_play_button = pygame.Rect((480 - how_to_play.get_width() / 2, 330 - how_to_play.get_height(),
                                 how_to_play.get_width() + 40, how_to_play.get_height() + 40))
    resume_button = pygame.Rect((480 - resume.get_width() / 2, 380 - resume.get_height(),
                                 resume.get_width() + 40, resume.get_height() + 40))

    # changing colour if mouse hovering over how to play button
    if how_to_play_button.collidepoint(pygame.mouse.get_pos()):
        how_to_play = font.render(f"How to Play", 1, (0, 128, 0))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.instructions = True
                return 0

    # changing colour if mouse hovering over resume button
    if resume_button.collidepoint(pygame.mouse.get_pos()):
        resume = font.render(f"Resume", 1, (0, 128, 0))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.pause = False
                return 0

    pause_screen.blit(game_over, (500 - game_over.get_width() / 2, 300 - game_over.get_height()))
    pause_screen.blit(how_to_play, (500 - how_to_play.get_width() / 2, 350 - how_to_play.get_height()))
    pause_screen.blit(resume, (500 - resume.get_width() / 2, 400 - resume.get_height()))
    win.blit(pause_screen, (0, 0))
    pygame.display.update()
    player.pause = True


def deadScreen(player, events, font):
    death_screen = pygame.Surface((1000, 650))
    death_screen.set_alpha(5)
    death_screen.fill((128, 0, 0))
    game_over = font.render("YOU LOST YOUR MUSTACHE :(", 1, (20, 0, 0))
    score = font.render(f"Score: {player.score // 10}", 1, (20, 0, 0))
    high_score = font.render(f"High Score: {player.high_score}", 1, (20, 0, 0))
    if player.high_score < player.score // 10:
        high_score = font.render("New High Score!!", 1, (20, 0, 0))
        with open('72105103104328399111114101.BHAENS', mode='wb') as high_score_file:
            high_score_file.write((player.score//10).to_bytes(length=1024, byteorder='big'))
    play_again = font.render(f"Play Again", 1, (20, 0, 0))
    play_again_button = pygame.Rect((480 - play_again.get_width() / 2, 355 - play_again.get_height(),
                                     play_again.get_width() + 40, play_again.get_height() + 40))
    # changing colour if mouse hovering over play again button
    if play_again_button.collidepoint(pygame.mouse.get_pos()):
        play_again = font.render(f"Play Again", 1, (255, 255, 255))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.dead = False
                return 0

    death_screen.blit(game_over, (500 - game_over.get_width() / 2, 300 - game_over.get_height()))
    death_screen.blit(score, (500 - score.get_width() / 2, 325 - score.get_height()))
    death_screen.blit(high_score, (500 - high_score.get_width() / 2, 350 - high_score.get_height()))
    death_screen.blit(play_again, (500 - play_again.get_width() / 2, 375 - play_again.get_height()))
    win.blit(death_screen, (0, 0))
    pygame.display.update()
    player.dead = True


def checkCollision(player, characters):
    for character in characters:
        if not isinstance(character, GrowthSerum):
            if player.invulnerability > 0 and player.attack_countdown == 40:
                continue

            if player.attack_hitbox.colliderect(character.hitbox):
                character.sound.play(maxtime=200)
                if player.attack_countdown < 40 and isinstance(character, Barber):
                    characters.append(GrowthSerum(character.x, character.y, 1, 80))
                    characters.remove(character)
                    Character.spawn = True
                    del character
                    player.score += 3000
                    continue
                if player.health > 1:
                    player.health = max(1, player.health - character.damage)
                else:
                    player.health = 0
                    pygame.mixer.music.load("../audio/dead.mp3")
                    pygame.mixer.music.play(-1)
                    player.dead = True
                    return 0
                player.setImage()
                player.invulnerability = 100
                player.hit_countdown = 20

        else:
            if player.hitbox.colliderect(character.hitbox):
                if player.health < 4:
                    character.sound.play()
                player.health = min(4, player.health - character.damage)
                player.setImage()
                player.hit_countdown = -20
                player.invulnerability = 100
                characters.remove(character)
                del character
    player.dead = False


def redrawGameWindow(player, background, characters, font, move_background=True):
    win.fill((151, 123, 89))
    background.draw(move_background)
    health = font.render(f"Health: {player.health}", 1, (45, 56, 56))
    score = font.render(f"Score: {player.score // 10}", 1, (45, 56, 56))
    high_score = font.render(f"High Score: {player.high_score}", 1, (45, 56, 56))
    win.blit(health, (18, 18))
    win.blit(score, (500 - (score.get_width() / 2), 18))
    win.blit(high_score, (1000 - high_score.get_width() - 18, 18))
    for character in characters:
        character.draw()
    player.draw()
    pygame.display.update()


def main():
    font = pygame.font.Font("../fonts/ArcadeFont.ttf", 20)
    pygame.mixer.music.load("../audio/music.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    background = Background()
    clock = pygame.time.Clock()
    running = True
    player = Player()
    enemy_types = [Razor, Scissors]
    serum_timer = random.randrange(3000, 4000)
    characters = []
    Character.spawn = True
    timer = 250
    # main loop
    while running:
        clock.tick(timer)
        # condition to quit program
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        if player.instructions:
            instructions(events,font, player)
        elif not player.start:
            homeScreen(events, font, player)
            if player.start:
                countdown(player, background, characters, font)
        elif player.dead:
            deadScreen(player, events, font)
            if not player.dead:
                main()
                break
        elif player.pause:
            pauseScreen(events, font, player)
            if not player.pause:
                countdown(player, background, characters, font)
        else:
            if Character.spawn:
                index = random.randint(0, len(enemy_types) - 1)
                y = 480
                if index == 1:
                    y = random.randrange(150, 350)
                characters.append(enemy_types[index](y))
                Character.spawn = False
                # to make sure first enemy is not a barber
                if len(enemy_types) == 2:
                    enemy_types.append(Barber)
                # to make sure barber doesnt come twice in a row
                if index == 2:
                    enemy_types.remove(Barber)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                player.pause = True

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
            if player.attack_cooldown > 0:
                player.attack_cooldown -= 1
            elif player.attack_countdown == 40 and keys[pygame.K_SPACE] and player.health > 1:
                player.sound.play()
                player.attack_countdown = 0

            for character in characters:
                character.move()
                if isinstance(character, Barber):
                    if character.throw_count == character.throw_limit:
                        character.throw_sound.play()
                        character.throw_sound.fadeout(1000)
                        characters.append(Blade(character.x, character.y))
                        character.throw_count = 0
                        character.throw_limit = random.randint(200, 300)
                    character.throw_count += 1
                if character.x < -character.image.get_width():
                    characters.remove(character)
                    if not isinstance(character, Blade) and not isinstance(character, GrowthSerum):
                        Character.spawn = True
                    del character

            if player.invulnerability > 0:
                player.invulnerability -= 1
            else:
                checkCollision(player, characters)

            serum_timer -= 1
            if serum_timer <= 0:
                serum_timer = random.randrange(1000, 3000)
                characters.append(GrowthSerum(1000, random.randrange(250, 500), 1, 80))

            player.score += 1
            timer += 0.000000001
            redrawGameWindow(player, background, characters, font)

if __name__ == '__main__':
    pygame.init()

    sc_width = 1000
    sc_height = 650

    # initializing game window
    win = pygame.display.set_mode((sc_width, sc_height))
    pygame.display.set_caption("Barber Run")
    pygame.display.set_icon(pygame.image.load('../images/icon.png'))


    # calling main loop
    main()

    pygame.quit()
