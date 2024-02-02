import random
import pygame


class Player:
    def __init__(self):
        self.health = 8
        self.level = 4
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

    def draw(self):
        self.image = self.sprites[self.image_count // 15]

        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites)*15:
            self.image_count += 1
        else:
            self.image_count = 0

        if self.hit_countdown > 0:
            self.image = self.injured
            self.hit_countdown = max(0, self.hit_countdown - 1)
        if self.hit_countdown < 0:
            self.image = self.healed
            self.hit_countdown = min(0, self.hit_countdown + 1)
        win.blit(self.image, (self.x, self.y))
    def setImage(self, is_growth_serum=False):
        self.level = min((self.health+1)//2, 4)
        # loading the images for the player
        self.sprites = [pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man1.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man2.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man3.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man4.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man5.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man6.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man7.png'), (92, 120)),
                        pygame.transform.scale(pygame.image.load(f'../images/level_{self.level}/man8.png'), (92, 120))]
        self.attack_sprites.clear()
        # loading the images for when the player attacks
        for i in range(2, self.level+1):
            length = 176 if i == 2 else 318 if i == 3 else 459
            self.attack_sprites.append(
                pygame.transform.scale(pygame.image.load(f'../images/level_{i}/man_shooting.png'), (length, 120)))
        # loading image for when player is hit
        self.injured = pygame.transform.scale(
            pygame.image.load(f'../images/level_{self.level}/man_hit.png'), (92, 120))
        # loading image for when player is healed
        self.healed = pygame.transform.scale(
            pygame.image.load(f'../images/level_{self.level}/man_healed.png'), (92, 120))


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

    def move(self):
        self.x -= self.x_velocity
        self.y -= self.y_velocity


class GrowthSerum(Character):
    def __init__(self, y):
        super().__init__(y, pygame.transform.scale(pygame.image.load('../images/growth_serum.png'), (45, 80)))
        self.damage = -2
        self.x_velocity = 1.5
        self.image_count = 0

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

    def draw(self):
        win.blit(self.sprites[self.image_count // 20], (self.x, self.y))

        # iterating through various man sprites
        if self.image_count + 1 < len(self.sprites) * 20:
            self.image_count += 1
        else:
            self.image_count = 0


def death():
    print("ded :(")


def checkCollision(player, characters):
    for character in characters:
        if not isinstance(character, GrowthSerum):
            if player.invulnerability > 0:
                continue
            if character.x+20 < player.x+player.image.get_width() < character.x + character.image.get_width() and (
                    character.y < player.y < character.y + character.image.get_height() or character.y < player.y + 120 < character.y + character.image.get_height()):
                if player.health - character.damage > 0:
                    player.health = max(1, player.health - character.damage)
                    player.setImage()
                else:
                    death()
                player.invulnerability = 100
                player.hit_countdown = 20

        else:
            if (character.x + 20 < player.x < character.x + character.image.get_width() or character.x + 20 < player.x + player.image.get_width() < character.x + character.image.get_width()) and (
                    character.y < player.y < character.y + character.image.get_height() or character.y < player.y + 120 < character.y + character.image.get_height()):
                player.health = max(1, player.health - character.damage)
                player.setImage()
                player.hit_countdown = -20
                player.invulnerability = 100
                characters.remove(character)
                del character

def redrawGameWindow(player, background, characters, font):
    win.fill((151, 123, 89))
    background.draw()
    health = font.render(f"Health: {player.health}", 1, (45, 56, 56))
    win.blit(health, (18, 18))
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
    serum_timer = random.randrange(2000, 3000)
    characters = []
    # main loop
    while running:
        clock.tick(250)
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

        for character in characters:
            character.move()
            if isinstance(character, Barber):
                if character.throw_count == 250:
                    characters.append(Blade(character.x, character.y))
                    character.throw_count = 0
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
            characters.append(GrowthSerum(random.randrange(250, 500)))

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
