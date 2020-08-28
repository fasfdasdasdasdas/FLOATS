import pygame

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define Screen size
width = 800
height = 1200

# Initializing pygame and images
vec = pygame.math.Vector2

pygame.init()
gameScreen = pygame.display.set_mode((width,height))
playerImg = pygame.image.load('Block.png').convert()
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
        self.rect = self.image.get_rect()
        self.rect.center = (200,600)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("I dont know how to make it jump")

# Obstacle Class


# Sprites to load
player = Player()
player.add(all_sprites)

# Main Game Loop
while not gameOver:
    # Loop Speed
    clock.tick(30)

    # Update game positions
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True	

    all_sprites.update()

    # Draw 
    gameScreen.fill(WHITE)
    all_sprites.draw(gameScreen)

    # Flip 
    pygame.display.flip()

pygame.quit()
    
    