import pygame

# Initializing pygame and images
pygame.init()
playerImg = pygame.image.load('Block.png')

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
        self.x = height/2-7
        self.y = 800/4
        self.width = 16
        self.height = 15
        self.image = playerImg

    
# Obstacle Class



# Main Game Loop
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
            if event.key == pygame.K_ESCAPE:
                gameOver = True
    
    