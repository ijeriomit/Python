# Import the pygame library and initialise the game engine
import pygame
from random import randint
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
 
# Set the height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Create your screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
 
# Load the player image
player_image = pygame.image.load("player.png").convert_alpha()

# Rescale the player image to the desired size
player_scale = 0.1
player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * player_scale), int(player_image.get_height() * player_scale)))
 
# Get the dimensions of your player's image
player_width, player_height = player_image.get_size()

# Load the enemy image
enemy_image = pygame.image.load("enemy.png").convert_alpha()  
# Rescale the enemy image to the desired size
enemy_scale = 0.1
enemy_image = pygame.transform.scale(enemy_image, (int(enemy_image.get_width() * enemy_scale), int(enemy_image.get_height() * enemy_scale)))
 
# Get the dimensions of your enemy's image
enemy_width, enemy_height = enemy_image.get_size()

# Clock to control frame rate
clock = pygame.time.Clock()

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
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
        self.rect.y = 200

        self.velocity = [0, 0]
        self.lives = 3
    def update(self):
        self.velocity[0] = 0  # Reset the player's horizontal movement

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.velocity[0] += 5
        if keys[pygame.K_a]:
            self.velocity[0] -= 5
        if keys[pygame.K_d]:
            self.velocity[0] += 5     
       
        # Add gravity
        self.velocity[1] += 0.5
        # Apply the velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Prevent the player from going out of the display
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def collision(self):
        self.lives -= 1
        print(f"Lives: {self.lives}")

 
# Enemy Class
class Enemy(pygame.sprite.Sprite):
    # This class represents a enemy. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the image for the enemy.
        # Set the background color and set it to be transparent
        self.image = enemy_image
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.rect.x = randint(SCREEN_WIDTH - 100, SCREEN_WIDTH)
        self.rect.y = randint(-100, -40)

        self.speed = randint(4, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = randint(SCREEN_WIDTH - 100, SCREEN_WIDTH)
            self.rect.y = randint(-100, -40)
            self.speed = randint(4, 8)

 
# Create the player
player = Player()
all_sprites_list.add(player)

# Create all the enemies
enemy = Enemy()
all_sprites_list.add(enemy)

# Hearts for life
heart = pygame.image.load("heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (20, 20)) 

 
# Game loop
carryOn = True

# The loop will carry on until the user exits the game (e.g. clicks the close button).
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    # Moving the enemy
    all_sprites_list.update()
    
    # Check if the player collides with the enemy
    if pygame.sprite.collide_mask(player, enemy):
        player.collision()
        if player.lives == 0:
            print("Game Over")
            break
    
    # --- Game logic should go here
    all_sprites_list.update()
    
    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    # Draw the background
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # Displaying the number of lives
    for i in range(player.lives):
        screen.blit(heart, (350 + i * 20, 10))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()