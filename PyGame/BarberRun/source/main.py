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
    
    def draw(self):
        win.blit(self.image, (self.x, self.y))
        win.blit(self.image, (self.x + self.image_width, self.y))
        win.blit(self.image, (self.x + self.image_width*2, self.y))
        if self.x+1 <= -self.image_width:
            self.x = 0
        else:
            self.x -= 1.5


class Character:
    spawn = True
    def __init__(self, y, image):
        # placeholder image
        self.image = image
        self.x = 1000
        self.y = y
        self.x_velocity = 3
        self.y_velocity = 0
        self.damage = 1
        self.hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())

    def move(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity
        self.hitbox = pygame.Rect(self.x + 20, self.y, self.image.get_width() - 30, self.image.get_height())


class GrowthSerum(Character):
    def __init__(self, x, y, regen_amount, height):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/growth_serum.png'), (int(round(0.5625*height)), height)))
        self.x = x
        self.damage = -regen_amount
        self.x_velocity = 1.5
        self.image_count = 0

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

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.image = self.sprites[1]
            self.image_count = 0


class Scissors(Character):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (245, 140)),
                             pygame.transform.scale(pygame.image.load('../images/enemies/scissors2.png'), (245, 140))]
        self.image_count = 0
        self.x_velocity = 5
        self.damage = 2

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = self.sprites[0]
        elif self.image_count == 80:
            self.image = self.sprites[1]
            self.image_count = 0

class Blade(Character):
    def __init__(self, x, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/blade.png'), (60, 76)))
        self.x = x
        self.x_velocity = 7
        self.damage = 2
        self.image_count = 0

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.image_count += 1
        if self.image_count == 40:
            self.image = pygame.transform.rotate(self.image, 90)
            self.image_count = 0


class Barber(Character):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)))
        self.sprites = [pygame.transform.scale(pygame.image.load('../images/enemies/barber1.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber2.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber3.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber4.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber5.png'), (88, 140)),
                        pygame.transform.scale(pygame.image.load('../images/enemies/barber6.png'), (88, 140))]
        self.image_count = 0
        self.x_velocity = 2
        self.throw_count = 250
        self.throw_limit = 250

    def draw(self):
        win.blit(self.sprites[self.image_count // 20], (self.x, self.y))
        # iterating through various barber sprites
        if self.image_count + 1 < len(self.sprites) * 20:
            self.image_count += 1
        else:
            self.image_count = 0


def countdown(player, background, characters, font):
    for i in range(3, 0, -1):
        redrawGameWindow(player, background, characters, font)
        counter = font.render(f"{i}", 1, (255, 255, 255))
        win.blit(counter, (500 - counter.get_width() / 2, 350 - counter.get_height()))
        pygame.display.update()
        pygame.time.wait(1000)


def homeScreen(events, start_font):
    title_font = pygame.font.Font('../fonts/ArcadeFont.ttf', 40)
    win.fill((89, 112, 112))
    title = title_font.render("BARBER RUN", 1, (113, 68, 47))
    start = start_font.render("Start", 1, (0, 0, 0))
    start_button = pygame.Rect((480 - start.get_width() / 2, 330 - start.get_height(),
                                start.get_width() + 40, start.get_height() + 40))
    # changing colour if mouse hovering over play again button
    if start_button.collidepoint(pygame.mouse.get_pos()):
        start = start_font.render(f"Start", 1, (125, 255, 71))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    razor = pygame.transform.scale(pygame.image.load('../images/enemies/razor1.png'), (118, 200))
    scissor = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/enemies/scissors1.png'), (300, 171)), 300)
    blade = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/enemies/blade.png'), (79, 100)), 340)
    mustache = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('../images/icon.png'), (70, 70)), 340)

    win.blit(title, (500 - title.get_width() / 2, 300 - title.get_height()))
    win.blit(start, (500 - start.get_width() / 2, 350 - start.get_height()))
    win.blit(mustache, (860 - title.get_width() / 2, 240 - title.get_height()))
    win.blit(razor, (100, 200))
    win.blit(scissor, (700, 20))
    win.blit(blade, (600, 450))
    pygame.display.update()
    return False


def pauseScreen(events, font):
    death_screen = pygame.Surface((1000, 650))
    death_screen.set_alpha(5)
    death_screen.fill((255, 255, 255))
    game_over = font.render("PAUSED", 1, (20, 0, 0))
    play_again = font.render("Resume", 1, (20, 0, 0))
    play_again_button = pygame.Rect((480 - play_again.get_width() / 2, 330 - play_again.get_height(),
                                     play_again.get_width() + 40, play_again.get_height() + 40))
    # changing colour if mouse hovering over play again button
    if play_again_button.collidepoint(pygame.mouse.get_pos()):
        play_again = font.render(f"Resume", 1, (0, 128, 0))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return False

    death_screen.blit(game_over, (500 - game_over.get_width() / 2, 300 - game_over.get_height()))
    death_screen.blit(play_again, (500 - play_again.get_width() / 2, 350 - play_again.get_height()))
    win.blit(death_screen, (0, 0))
    pygame.display.update()
    return True


def deadScreen(player, events, font):
    death_screen = pygame.Surface((1000, 650))
    death_screen.set_alpha(5)
    death_screen.fill((128, 0, 0))
    game_over = font.render("YOU LOST YOUR MUSTACHE :(", 1, (20, 0, 0))
    score = font.render(f"Score: {player.score // 10}", 1, (20, 0, 0))
    play_again = font.render(f"Play Again", 1, (20, 0, 0))
    play_again_button = pygame.Rect((480 - play_again.get_width() / 2, 330 - play_again.get_height(),
                                     play_again.get_width() + 40, play_again.get_height() + 40))
    # changing colour if mouse hovering over play again button
    if play_again_button.collidepoint(pygame.mouse.get_pos()):
        play_again = font.render(f"Play Again", 1, (255, 255, 255))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return False

    death_screen.blit(game_over, (500 - game_over.get_width() / 2, 300 - game_over.get_height()))
    death_screen.blit(score, (500 - score.get_width() / 2, 325 - score.get_height()))
    death_screen.blit(play_again, (500 - play_again.get_width() / 2, 350 - play_again.get_height()))
    win.blit(death_screen, (0, 0))
    pygame.display.update()
    return True


def checkCollision(player, characters):
    for character in characters:
        if not isinstance(character, GrowthSerum):
            if player.invulnerability > 0:
                continue

            if player.attack_hitbox.colliderect(character.hitbox):
                if player.attack_countdown < 40 and isinstance(character, Barber):
                    characters.append(GrowthSerum(character.x, character.y, 2, 120))
                    characters.remove(character)
                    Character.spawn = True
                    del character
                    player.score += 3000
                    continue
                if player.health > 1:
                    player.health = max(1, player.health - character.damage)
                else:
                    player.health = 1
                    return True
                player.setImage()
                player.invulnerability = 100
                player.hit_countdown = 20

        else:
            if player.hitbox.colliderect(character.hitbox):
                player.health = min(4, player.health - character.damage)
                player.setImage()
                player.hit_countdown = -20
                player.invulnerability = 100
                characters.remove(character)
                del character
    return False


def redrawGameWindow(player, background, characters, font):
    win.fill((151, 123, 89))
    background.draw()
    health = font.render(f"Health: {player.health}", 1, (45, 56, 56))
    attack_status = "Unavailable" if player.health == 1 else "Ready" if not player.attack_cooldown else "Reloading"
    cooldown = font.render(f"Attack {attack_status}", 1, (45, 56, 56))
    score = font.render(f"Score: {player.score//10}", 1, (45, 56, 56))
    win.blit(health, (18, 18))
    win.blit(cooldown, (500-(cooldown.get_width()/2), 18))
    win.blit(score, (1000-score.get_width()-18, 18))
    for character in characters:
        character.draw()
    player.draw()
    pygame.display.update()


def main():
    font = pygame.font.Font("../fonts/ArcadeFont.ttf", 20)
    background = Background()
    clock = pygame.time.Clock()
    running = True
    player = Player()
    enemy_types = [Razor, Scissors]
    serum_timer = random.randrange(3000, 4000)
    timer = 250
    characters = []
    dead = False
    pause = False
    start = False
    Character.spawn = True
    # main loop
    while running:
        clock.tick(timer)
        # condition to quit program
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        if not start:
            start = homeScreen(events, font)
            if start:
                countdown(player, background, characters, font)
        elif dead:
            dead = deadScreen(player, events, font)
            if not dead:
                main()
                break
        elif pause:
            pause = pauseScreen(events, font)
            if not pause:
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
                pause = True

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
            elif player.attack_countdown == 40 and keys[pygame.K_SPACE]:
                player.attack_countdown = 0

            for character in characters:
                character.move()
                if isinstance(character, Barber):
                    if character.throw_count == character.throw_limit:
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
                dead = checkCollision(player, characters)

            serum_timer -= 1
            if serum_timer <= 0:
                serum_timer = random.randrange(1000, 3000)
                characters.append(GrowthSerum(1000, random.randrange(250, 500), 1, 80))

            timer += 0.000000001
            player.score += 1
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
