import sys
import pygame
from random import randint

# Initialize
pygame.init()

# Set screen size/dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Create your screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Load the player image
player_image = pygame.image.load("player.png").convert_alpha()
player_scale = 0.1
player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * player_scale), 
int(player_image.get_height() * player_scale)))

# Rescale the enemy image
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_scale = 0.1
enemy_image = pygame.transform.scale(enemy_image, (int(enemy_image.get_width() * enemy_scale), 
int(enemy_image.get_height() *enemy_scale)))

# Load the coin image
coin_image = pygame.image.load("coin.png").convert_alpha()  
coin_scale = 0.2
coin_image = pygame.transform.scale(coin_image, (int(coin_image.get_width() * coin_scale), 
int(coin_image.get_height() * coin_scale)))

# Load the platform image
platform_image = pygame.image.load("platform.png").convert_alpha()
platform_scale = 0.5
platform_image = 
pygame.transform.scale(platform_image,(int(platform_image.get_width() * platform_scale), 
int(platform_image.get_height() * platform_scale)))

# Color keys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# FPS
FPS = 60

# Player attributes
player_width, player_height = player_image.get_size()
player_speed = 3  
player_jump_speed = 10

# Create the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - player_height - 30
        self.velocity = [0, 0]
        self.lives = 3
        self.jumping = False

    def jump(self):
        self.velocity[1] = -player_jump_speed
        self.jumping = True

    def update(self):
        self.velocity[0] = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            self.velocity[0] += player_speed
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jump()
        
        self.rect.x += self.velocity[0]
        # Check for collision with the walls
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Apply gravity
        self.velocity[1] += 0.5
        self.rect.y += self.velocity[1]
        # Check for collision with the ground
        if self.rect.bottom >= SCREEN_HEIGHT - 30:
            self.velocity[1] = 0
            self.rect.bottom = SCREEN_HEIGHT - 30
            self.jumping = False

    def collision(self):
        self.lives -= 1
        print(f"Lives: {self.lives}")


# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 100
        self.rect.y = randint(-100, SCREEN_HEIGHT - 100)
        self.speed = randint(4, 8)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.x = SCREEN_WIDTH - 100
            self.rect.y = randint(-100, SCREEN_HEIGHT - 100)
            self.speed = randint(4, 8)


# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = randint(50, SCREEN_WIDTH - 100)
        self.rect.y = randint(-100, SCREEN_HEIGHT - 100)

    def update(self):
        self.rect.x -= platform_speed


# Platform Class
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = platform_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = randint(50, SCREEN_WIDTH - 100)
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 40

    def update(self):
        self.rect.x -= platform_speed


# All sprites group
all_sprites_list = pygame.sprite.Group()

# Player sprite
player = Player()
all_sprites_list.add(player)

# Enemy sprites
enemy = Enemy()
all_sprites_list.add(enemy)

# Coin sprites
coin = Coin()
all_sprites_list.add(coin)