import pygame

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Defining Variables
width = 800
height = 1200
gravity = 5

# Initializing pygame 
vec = pygame.math.Vector2
pygame.init()
gameScreen = pygame.display.set_mode((width,height))

# Loading Sprites
playerImg = pygame.image.load('Block.png').convert()
obstacleImg = pygame.Surface((50,800))
obstacleImg.fill(GREEN)

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Game Loop Variable
gameOver = False

# Game Class

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playerImg
        self.image = pygame.transform.scale(self.image, (50,45))
        self.rect = self.image.get_rect()
        self.rect.center = (200,600)
        self.image.set_colorkey(BLACK)
        self.vel = -10
        self.isJump = False
        self.jumpCount = 6
    
    def update(self):
        keys = pygame.key.get_pressed()

        # Jump Mechanic
        if not self.isJump:
            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.rect.move_ip(0,self.vel)
        else:
            if self.jumpCount > 0:
                self.jumpCount -= 1
                self.rect.move_ip(0,self.vel) 
            else:
                self.isJump = False 
                self.jumpCount = 6

        # Still need to build in Acceleration of gravity on the player.
        self.rect.move_ip(0,gravity)
            
# Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacleImg
        self.rect = self.image.get_rect()
        self.rect.center = (500,0)



# Sprites to load
player = Player()
player.add(all_sprites)
obs = Obstacle()
obs.add(all_sprites)

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

    all_sprites.update()

    # Draw 
    gameScreen.fill(WHITE)
    all_sprites.draw(gameScreen)

    # Flip 
    pygame.display.flip()

pygame.quit()
    
    