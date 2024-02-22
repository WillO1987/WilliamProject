import pygame
import math
import random
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
size = (700, 500)
moveSide = 0
moveUp = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project: ")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_val = 100
y_val = 200
x_offset = 0
y_offset = 0
pi= 3.141592652
counter = 0

# create a Block object for testing :
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


#endclass
#adding a Player class that can interact with the Block objects 
class Player(pygame.sprite.Sprite):
    carry_Item_List = []

    def __init__(self, s_width, s_length, initial_x, initial_y):
        super().__init__()
        self.x_val2 = x_val
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.diff_x = 0
        self.diff_y = 0

        
    def update(self):
         # Calculate diff_x and diff_y based on key input
        keys = pygame.key.get_pressed()
        self.diff_x = 0
        self.diff_y = 0
        if keys[pygame.K_LEFT]:
            self.diff_x -= 2
        if keys[pygame.K_RIGHT]:
            self.diff_x += 2
        if keys[pygame.K_UP]:
            self.diff_y -= 2
        if keys[pygame.K_DOWN]:
            self.diff_y += 2

        # Update the positions of the player and carried items
        self.rect.x += self.diff_x
        self.rect.y += self.diff_y

        for item in self.carry_Item_List:
            item.rect.x += self.diff_x
            item.rect.y += self.diff_y
        
        # Check for collisions with walls
        wall_collisions = pygame.sprite.spritecollide(self, wall_list, False)
        for wall in wall_collisions:
            if moveSide > 0:
                self.rect.right = wall.rect.left
            elif moveSide < 0:
                self.rect.left = wall.rect.right
            if moveUp > 0:
                self.rect.bottom = wall.rect.top
            elif moveUp < 0:
                self.rect.top = wall.rect.bottom

 
all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
item_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

player = Player(10, 10 , x_val , y_val )
player_sprite.add(player)
all_sprites.add(player)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   
        
    screen.fill(WHITE)
    
    
    
    #draw stuff here:

    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()