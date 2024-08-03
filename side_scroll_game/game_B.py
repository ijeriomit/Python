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
player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * player_scale), int(player_image.get_height() * player_scale)))

# Rescale the enemy image
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_scale = 0.1
enemy_image = pygame.transform.scale(enemy_image, (int(enemy_image.get_width() * enemy_scale), int(enemy_image.get_height() * enemy_scale)))

# Load the platform image
platform_image = pygame.image.load("platform.png").convert_alpha()
platform_scale = 0.2
platform_image = pygame.transform.scale(platform_image, (int(platform_image.get_width() * platform_scale), int(platform_image.get_height() * platform_scale)))

# Load the coin image
coin_image = pygame.image.load("coin.png").convert_alpha()  
coin_scale = 0.1
coin_image = pygame.transform.scale(coin_image, (int(coin_image.get_width() * coin_scale), int(coin_image.get_height() * coin_scale)))

# Color variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the platform, its width and height.
        # Set the background color and set it to be transparent
        self.image = platform_image
        self.image.set_colorkey(BLACK)

        self.width = width
        self.height = height

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y


# Player class
class Player(pygame.sprite.Sprite):
    # This class represents a player. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the image for the player.
        # Set the background color and set it to be transparent
        self.image = player_image
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.rect.x = 300
        self.rect.y = SCREEN_HEIGHT - self.rect.height

        self.velocity = [0, 0]
        self.lives = 3
        self.jumping = False

    def update(self):
        self.velocity[0] = 0  # Reset the player's horizontal movement

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.velocity[0] += 5
        if keys[pygame.K_SPACE]:
            self.jump()

        # Apply gravity
        self.velocity[1] += 0.5
        # Move the player
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Check if we hit the bottom of the screen
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity[1] = 0

    def jump(self):
        # Only allow jumping if the player is on the ground
        if not self.jumping:
            self.velocity[1] -= 13
            self.jumping = True

    def collision(self):
        self.lives -= 1
        print(f"Lives: {self.lives}")


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Pass in the image for the enemy.
        # Set the background color and set it to be transparent
        self.image = enemy_image
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.rect.x = SCREEN_WIDTH
        self.rect.y = randint(80, SCREEN_HEIGHT - 100)

        self.speed = randint(4, 8)

    def update(self):
        self.rect.x -= self.speed
        # If the enemy is off the screen, reset its position
        if self.rect.right <= 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = randint(80, SCREEN_HEIGHT - 100)
            self.speed = randint(4, 8)


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = coin_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = randint(SCREEN_WIDTH / 2, SCREEN_WIDTH - 30)
        self.rect.y = randint(-100, -40)

        self.speed = 3

    def update(self):
        self.rect.y += 1