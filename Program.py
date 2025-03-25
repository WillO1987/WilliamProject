import pygame
import math
import random
import time






# Initialize the game engine
pygame.init()

# Define some colors
ORANGE = (255,100,10)
FERN = ( 79 , 121, 66)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
BROWN =  (120, 42 , 42)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
moveSide = 0
moveUp = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project: ")

score = 0

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
game_over = False

def replaceObject(object1,object2):
    pass



class SEEDButton(pygame.sprite.Sprite):
    def __init__(self,xcoord,ycoord, text, colour, Single_click):
        # super.__init__()
        self.clicked = False
        
        self.text = text
        
        self.image = pygame.Surface([100,40 ])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord
        self.rect.x = 585
        self.rect.y = 85
        self.single_click = Single_click # prevents when the mouse collides with button from it getting pressed multiple times.


    def draw(self, screen):
        # Draw the button
        screen.blit(self.image, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                if not self.clicked:
                    seed = Seed("Wheat", 15, 15)
                    seed.rect.x = random.randrange(screen_width)
                    seed.rect.y = random.randrange(screen_height)
                    # seed.rect.topleft = (500, 25)
                    block_list.add(seed)
                    all_sprites.add(seed)
                    self.clicked = True
        else:
            self.clicked = False



# create a Block object for testing :
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor
        super().__init__()
        
        #self.image.fill(color)
        self.image =  pygame.image.load('tree.png').convert_alpha()
        
       
        self.rect = self.image.get_rect()

#endclass

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, health, damagelvl):
        pygame.sprite.Sprite.__init__(self)
        self.name = name 
        self.health = health
        self.damagelvl = damagelvl
        # self.rect.x = 300
        # self.rect.y = 100
        
        self.original_image = pygame.image.load('scary zombiesmaller.png').convert_alpha()
        self.image = self.original_image
        # self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        # self.rect.x = 400
        # self.rect.y = 200
    def update(self) :
        self.move_towards_farmtile()
        self.move_towards_player()
    def move_towards_farmtile(self):
        closestTile = None
        minDist = float('inf')
        for farmtile in farmtile_group:
            if farmtile.image.get_at((0, 0)) == YELLOW or farmtile.image.get_at((0, 0)) == WHITE:
                distance = self.calculateDist(farmtile.rect.x, farmtile.rect.y)
                if distance < minDist:
                    closestTile = farmtile
                    minDist = distance
           
        if closestTile:
            dx = closestTile.rect.x - self.rect.x
            dy = closestTile.rect.y - self.rect.y


            if dx != 0 or dy != 0:
                angle = math.degrees(math.atan2(-dy, dx))  # Negate dy because pygame's y-axis is inverted
                self.image = pygame.transform.rotate(self.original_image, angle)
                self.rect = self.image.get_rect(center=self.rect.center)  # Maintain position after rotation

            if self.rect.x < closestTile.rect.x:
                self.rect.x += 1
            if self.rect.x > closestTile.rect.x:
                self.rect.x -= 1 
            if self.rect.y < closestTile.rect.y:
                self.rect.y += 1 
            if self.rect.y > closestTile.rect.y:
                self.rect.y -= 1 
            
            
            if self.rect.x == closestTile.rect.x and self.rect.y == closestTile.rect.y:
                game_over = True
                Endscreen()
        



    def move_towards_player(self):
        if any(farmtile.image.get_at((0, 0)) in [YELLOW, WHITE] for farmtile in farmtile_group):
            return # Prioritize farm tiles, do not move towards player if any valid farm tile exists

        closest_player = None
        minDist = float('inf')
    
        for player in player_sprite:
            distance = self.calculateDist(player.rect.x, player.rect.y)
            if distance < minDist:
                closest_player = player
                minDist = distance

        if closest_player:
            dx = closest_player.rect.x - self.rect.x
            dy = closest_player.rect.y - self.rect.y

            if dx != 0 or dy != 0:
                angle = math.degrees(math.atan2(-dy, dx))
                self.image = pygame.transform.rotate(self.original_image, angle)
                self.rect = self.image.get_rect(center=self.rect.center)

            if self.rect.x < closest_player.rect.x:
                self.rect.x += 1
            if self.rect.x > closest_player.rect.x:
                self.rect.x -= 1
            if self.rect.y < closest_player.rect.y:
                self.rect.y += 1
            if self.rect.y > closest_player.rect.y:
                self.rect.y -= 1

            if self.rect.x == closest_player.rect.x and self.rect.y == closest_player.rect.y:
                    
                    game_over = True
                    Endscreen()
    
    def calculateDist(self, x, y):
        return math.sqrt((self.rect.x - x) ** 2 + (self.rect.y - y) ** 2)
            


    def attack():
        pass

#endclass


class WateringCan(pygame.sprite.Sprite):
    def __init__(self, b_width , b_length):
        super().__init__()
        self.image = pygame.Surface((b_width, b_length))
        
        self.image = pygame.image.load('can.png').convert_alpha()
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
    def update(self) :
        pass
#endclass
        
class FarmTile(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # self.image = pygame.image.load('mud.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.contains_crop = False
        self.isreadytoharvest = False
        self.watered = False
        
    #endconstructor
    def update(self):
        if self.color == YELLOW:
            self.contains_crop = True

            
        
    def growcrop(self):
        if self.contains_crop and self.watered and not self.isreadytoharvest:
            self.isreadytoharvest = True
            self.image.fill(WHITE) 
    def harvestcrop(self):
        if self.isreadytoharvest:
            self.contains_crop = False
            self.watered = False
            self.isreadytoharvest = False
            self.image.fill(BROWN)
            return True
        return False


#endclass

class Seed(pygame.sprite.Sprite):
    def __init__(self, type, Swidth, Sheight):
        super().__init__()
        self.type = type
        self.image = pygame.Surface([Swidth,Sheight])
        
        
        
        self.image.fill(YELLOW)
        self.image = pygame.image.load('seed1.png').convert_alpha()
        self.rect = self.image.get_rect()
#endclass
    def grow(self):
        self.growtime = self.growtime + 1
        if(self.growtime == 5):

            return Wheat("Wheat", 5 )


class Wheat(pygame.sprite.Sprite):
    def __init__(self, type, growtime):
        self.type = type
        
        self.growtime = growtime
    
    #endclass
    def update(self):
        return 0 

class Bullet(pygame.sprite.Sprite):
     def __init__(self,x , y , angle ):
         super().__init__()
         self.image = pygame.Surface([10,4])
         self.image.fill(WHITE)
         self.rect = self.image.get_rect()
         self.rect.center = (x,y)
         self.angle = angle 
         self.speed = 10
     def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill()

class Gun(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.bullets = pygame.sprite.Group()
    
    def fire(self, x , y, target_x, target_y):
        global bullet
        angle = math.atan2(target_y - y, target_x - x)
        bullet = Bullet(x, y , angle)
        self.bullets.add(bullet)
        all_sprites.add(bullet)


#adding a Player class that can interact with the Block objects 
class Player(pygame.sprite.Sprite):
    carry_Item_List = []

    def __init__(self, image, initial_x, initial_y):
        super().__init__()
        self.x_val2 = x_val
        # self.width = s_width
        # self.height = s_length
        self.image = image
        # self.image.fill(GREEN), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.diff_x = 0
        self.diff_y = 0
        self.Gun = Gun()
        self.health = 5

        
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
        

        self.Gun.bullets.update()
        
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
    def fire_gun(self, target_x, target_y): 
        self.Gun.fire(self.rect.centerx, self.rect.centery, target_x, target_y)

    def harvest(self):
        global score
        global farmtile
        collided_tiles = pygame.sprite.spritecollide(self, farmtile_group, False)
        for farmtile in collided_tiles:
                if farmtile.watered ==  True and farmtile.isreadytoharvest:
                    farmtile.harvestcrop()
                    score += 20


def seed_collision(seed, farmtile_group):
    global score
    # Check if the seed collides with any farm tile
    collided_tiles = pygame.sprite.spritecollide(seed, farmtile_group, False)
    if collided_tiles:  
        for farmtile in collided_tiles:
            # Replace the farm tile with a "planted" state
            planted_tile = FarmTile(YELLOW, tile_size, tile_size)
            planted_tile.rect.x = farmtile.rect.x
            planted_tile.rect.y = farmtile.rect.y
            
            # Add the planted tile to the game
            all_sprites.add(planted_tile)
            farmtile_group.add(planted_tile)
            score = score + 10
            
            # Remove the old tile
            all_sprites.remove(farmtile)
            farmtile_group.remove(farmtile)
            if len(player.carry_Item_List) > 0:
                    block = player.carry_Item_List[(len(player.carry_Item_List) -1)]  # Gets the last block from inventory
                    block_list.add(block)  # Adds it back to the block_list
                    all_sprites.add(block)  # Adds it back to all_sprites
                    player.carry_Item_List.remove(block)  # Removes it from player's inventory

        
        # Remove the seed from the game
        seed.kill()


start_time = 180
elapsed_time = 0


def timer(elapsed_time):
    remaining_time = max(start_time - elapsed_time, 0)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    time_text = f"Time: {minutes:02}:{seconds:02}"
    font = pygame.font.Font(None, 36)
    timer_surface = font.render(time_text, True, BLACK)
    screen.blit(timer_surface, (562, 50))
#endfunction

def Endscreen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Game Over", True, WHITE)
    score_surface = font.render(f"Final Score: {score}", True, WHITE)
    # Center the text
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    score_rect = score_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

    screen.blit(text_surface, text_rect)
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
    pygame.time.wait(3000)


def StartScreen():
    
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text_surface = font.render("Press Space to begin!!!", True, BLUE)
        # Center the text
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
         
        instr_font = pygame.font.Font(None, 28)
        instructions = [
            "How to play:",
            " - Move with W A S D.",
            " - Press Space to pick up items.",
            " - Press Backspace to drop or use items.",
            " - Press H to harvest crops.",
            " - Click in the direction of enemies to shoot!",
            "ENJOY!"
        ]
        
        # Draw each line separately
        y_offset = screen_height // 2 - 50  # Starting position for text
        for line in instructions:
            instruction_surface = instr_font.render(line, True, BLUE)
            instr_rect = instruction_surface.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(instruction_surface, instr_rect)
            y_offset += 30  # Move down for the next line


        screen.blit(text_surface, text_rect)
       
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  #exit function to start main game loop
    #endwhile
    

    
                    



all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

farmtile_group = pygame.sprite.Group()

grid_rows = 5
grid_columns = 5
tile_size = 40  # Size of each Farmtile
grid_spacing = 15  # Spacing between Farmtiles
    
# Spawn Farmtiles in a grid pattern
for row in range(grid_rows):
    for col in range(grid_columns):
        # Calculate position for each Farmtile
        x = col * (tile_size + grid_spacing) + 140
        y = row * (tile_size + grid_spacing) + 100
        
        # Create Farmtile sprite
        #farmtile_picture = pygame.image.load('mud.png').convert_alpha()
        farmtile = FarmTile(BROWN, tile_size, tile_size)
        farmtile.rect.x = x
        farmtile.rect.y = y
        # Add Farmtile sprite to sprite group
        farmtile_group.add(farmtile)

# Adding Farmtile sprites to all_sprites 
all_sprites.add(farmtile_group)




zombie1 = Enemy("Zombie", 100, 1)
enemy_list.add(zombie1)
all_sprites.add(enemy_list)

playerimage = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()
player = Player(playerimage, x_val , y_val )
player_sprite.add(player)
all_sprites.add(player)

Wateringcann = WateringCan(20,15)
block_list.add(Wateringcann)
all_sprites.add(Wateringcann)
Wateringcann.rect.x = random.randrange(screen_width)
Wateringcann.rect.y = random.randrange(screen_height)
wheat = "Wheat"

Sbutton1 = SEEDButton(550, 100, "Seed", YELLOW, True)

enemy1 = Enemy(5, 1, 4)
enemy_list.add(enemy1)
all_sprites.add(enemy_list)

# # This represents a block
# block = Block(BLACK, 15, 15)

# block.rect.x = 400
# block.rect.y = 300

# block_list.add(block)
# all_sprites.add(block)
# wall_list.add(block)
    
def water_collision(watering_can, farmtile_group):
    collided_tiles = pygame.sprite.spritecollide(watering_can, farmtile_group, False)
    for farmtile in collided_tiles:
        farmtile.watered = True

    


waveIntervals = 15000

lastwave = pygame.time.get_ticks()

def wavesspawning():
    screenedges = ['top', 'bottom' , 'left' , 'right']
    for _ in range(5):  # Number of enemies per wave
        edge = random.choice(screenedges)
        if edge == 'top':
            x, y = random.randint(0, screen_width), 0
        elif edge == 'bottom':
            x, y = random.randint(0, screen_width), screen_height
        elif edge == 'left':
            x, y = 0, random.randint(0, screen_height)
        elif edge == 'right':
            x, y = screen_width, random.randint(0, screen_height)

        enemy = Enemy("Zombie", 100, 1)
        enemy.rect.x = x
        enemy.rect.y = y
        enemy_list.add(enemy)
        all_sprites.add(enemy)

StartScreen()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    current_ticks = pygame.time.get_ticks()
    elapsed_time = (current_ticks- start_time)// 1000
    
            
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_x, target_y = pygame.mouse.get_pos()
            player.fire_gun(target_x, target_y)
        elif event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_SPACE:
                player.carry_Item_List = player.carry_Item_List
                if len(player.carry_Item_List) >=1:
                    pass
                else:

                    item_hit_list = pygame.sprite.spritecollide(player, block_list, False) # true
                


            #    if len(player.carry_Item_List) < 1:
                    player.carry_Item_List = item_hit_list
        
            if event.key == pygame.K_BACKSPACE:
                if len(player.carry_Item_List) > 0:
                    block = player.carry_Item_List[(len(player.carry_Item_List) -1)]  # Gets the last block from inventory
                    block_list.add(block)  # Adds it back to the block_list
                    all_sprites.add(block)  # Adds it back to all_sprites
                    player.carry_Item_List.remove(block)  # Removes it from player's inventory
                    if isinstance(block, WateringCan):
                        water_collision(block, farmtile_group)

            if event.key == pygame.K_h:  # Harvest crops
                player.harvest()
                    # score += 20
            
        
        
    
        if current_ticks - lastwave >= waveIntervals:
            wavesspawning()
            lastwave = current_ticks
                

        if elapsed_time >= start_time:
            game_over = True
            Endscreen(score)
            break
        

    # --- Game logic should go here
    player_diff_x = player.diff_x
    player_diff_y = player.diff_y
    all_sprites.update()
    Sbutton1.handle_click()
   
    
    #kills enemeys.
    hits = pygame.sprite.groupcollide(enemy_list, player.Gun.bullets, True, True)
    
    
   
    #seed_collision(seed, farmtile_group)

    for seed in block_list:
        if isinstance(seed, Seed):  # Check if the object is a Seed
            seed_collision(seed, farmtile_group)
    
    for farmtile in farmtile_group:
        if farmtile.watered and farmtile.contains_crop:
            farmtile.growcrop()

        
    
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   
    Backgroundimage = pygame.image.load('grass background.png').convert_alpha()
    screen.blit(Backgroundimage,(0,0))
    
    
    
    #draw stuff here:
    all_sprites.draw(screen)
    player_sprite.draw(screen)
    block_list.draw(screen)
    enemy_list.draw(screen)
    Sbutton1.draw(screen)
    font = pygame.font.Font(None, 36)  


    score_text = font.render(f"Score: {score}", True, WHITE)  

    #place in the corner
    text_rect = score_text.get_rect()
    text_rect.topright = (screen_width - 10, 10)  
    
    screen.blit(score_text, text_rect)


    timer(elapsed_time)
    


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()