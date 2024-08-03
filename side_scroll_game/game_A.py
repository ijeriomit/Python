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
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Create your screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

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

        self.rect.x = SCREEN_WIDTH // 2 - player_width // 2
        self.rect.y = SCREEN_HEIGHT - player_height - 20

        self.velocity = [0, 0]
        self.lives = 3

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # Check that you are within the boundaries of the screen
        if self.rect.x >= SCREEN_WIDTH - player_width:
            self.rect.x = SCREEN_WIDTH - player_width
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y > SCREEN_HEIGHT - player_height:
            self.rect.y = SCREEN_HEIGHT - player_height
        if self.rect.y < 0:
            self.rect.y = 0

    def moveRight(self, pixels):
        self.velocity[0] = pixels

    def moveLeft(self, pixels):
        self.velocity[0] = -pixels

    def moveUp(self, pixels):
        self.velocity[1] = -pixels

    def moveDown(self, pixels):
        self.velocity[1] = pixels
    
    def stop(self):
        self.velocity[0] = 0
        self.velocity[1] = 0


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

        self.reset_position()
        self.velocity = [randint(2, 4), randint(-3, 3)]

    def reset_position(self):
        self.rect.x = randint(0, SCREEN_WIDTH - enemy_width)
        self.rect.y = 0

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.x >= SCREEN_WIDTH - enemy_width:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y > SCREEN_HEIGHT:
            self.reset_position()


# The player
player = Player()

# The enemy
enemy = Enemy()

# All the sprites in the game
all_sprites_list = pygame.sprite.Group()

# Add the player to the list of objects
all_sprites_list.add(player)
all_sprites_list.add(enemy)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player score
score = 0

# Initialise font
font = pygame.font.Font('freesansbold.ttf', 32)

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    # Moving the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        player.moveRight(5)
    if keys[pygame.K_UP]:
        player.moveUp(5)
    if keys[pygame.K_DOWN]:
        player.moveDown(5)
    if keys[pygame.K_SPACE]:
        player.stop()

    # --- Game logic should go here
    all_sprites_list.update()
    
    # Check if the player and the enemy collide
    if pygame.sprite.collide_mask(player, enemy):
        player.lives -= 1
        enemy.reset_position()        
    
    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    # Draw the player onto the screen
    all_sprites_list.draw(screen)

    # Draw Lives
    text = font.render(str(player.lives), 1, WHITE)
    screen.blit(text, (20, 10))
    
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()