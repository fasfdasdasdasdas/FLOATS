import pygame

# Initializing pygame and images
pygame.init()
images = 

# Define Screen size
width = 800
height = 1200

# Game Loop Variable
gameOver = False

# Initialize game screen
gameScreen = pygame.display.set_mode((width,height))

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = 
        x = 
        y = 


# Obstacle Class

# Game Class


# Main Game Loop
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
            if event.key == pygame.K_ESCAPE:
                gameOver = True
    
    