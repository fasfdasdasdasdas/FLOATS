import pygame

#player = virus?
#maybe create another py file for people walking class(moving randomly) and import here

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initializing pygame and images
pygame.init()
playerImg = pygame.image.load('Block.png') #must be in same directory
all_sprites = pygame.sprite.Group()

# Define Screen size
width = 800
height = 1200

# Game Loop Variable
gameOver = False

# Initialize game screen
gameScreen = pygame.display.set_mode((width,height))

# Game Class

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.x = height/2-7
        self.y = 800/4
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    
    def update(self):
        return

    
# Obstacle Class


# Sprites to load
player = Player()
player.add(all_sprites)

isJumping = False
jump_count = 10

# Main Game Loop
while not gameOver:
    # Loop Speed
    clock.tick(30)

    # Update game positions
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True
            if event.type == pygame.QUIT:
                gameOver = True
    
    keys = pygame.key.get_pressed() #moving player
    if keys[pygame.K_LEFT]: #+ add boundaries later
        player.playerX -= 3
        
    if keys[pygame.K_RIGHT]:
        player.playerX +=2
    
    if not isJumping:
        
        if keys[pygame.K_UP]:
            player.playerY -=2

        if keys[pygame.K_DOWN]:
            player.playerY +=2
        
        if event.key == pygame.K_SPACE: #jumping - make it move kinda like a parabola? 
            print("Space")
            isJumping = True 
     
    else:
        if jump_count >= -10: #pass lim
            negative = 1
            if jump_count < 0:
                negative = -1
            
            player.playerY -= (jump_count * jump_count) * 0.5 * negative #moves up a little
            jump_count -= 2 #slowly move down
        else:
            isJumping = False
            jump_count = 10 #reset again

    
    gameScreen.blit(background_image, [0, 0])

    all_sprites.update()

    # Draw 
    screen.fill(WHITE)
    player.x += player.playerX_change
    
    all_sprites.draw(screen)

    # Flip 
    pygame.display.flip()

pygame.quit()
    
    
