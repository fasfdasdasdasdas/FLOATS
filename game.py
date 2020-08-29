import pygame, random

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Defining Variables
width = 1944
height = 1094

# Initializing pygame 
vec = pygame.math.Vector2
pygame.init()
gameScreen = pygame.display.set_mode((width,height))
background = pygame.image.load('classroom.png')
pygame.display.set_caption('FLOATS! Covid Run')

# Loading Sprites
playerImg = pygame.image.load('coronavirus.png').convert()
obstacleImg = pygame.Surface((80,500))
obstacleImg.fill(RED)

clock = pygame.time.Clock()

# Game Loop Variable
gameOver = False

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playerImg
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (200,600)
        self.image.set_colorkey(BLACK)
        self.vel = -20
        self.isJump = False
        self.jumpCount = 5
        self.gravity = 10
    
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
        self.rect.move_ip(0,self.gravity)

 
# Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, y, length):
        super().__init__()
        self.image = obstacleImg
        self.y = y
        self.image = pygame.transform.scale(self.image, (80,length))
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = y
        self.gameSpeed = -20

    def update(self):
        # Movement of obstacle
        self.rect.move_ip(self.gameSpeed, 0)
        if self.rect.right < 0:
            self.kill()

# Game Class
## This class is used to generate all the sprites required
class Game():
    def __init__(self):
        self.score = 0
        self.gameOver = False
        self.player_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        self.obsSpawnRate = 40
        self.obsSpawnTimer = 40
    
    def makeObstacle(self):
        gap = 150
        number = random.randint(0 + 200, height - 200)
        topCoord = number - gap
        botCoord = number + gap
        top = Obstacle(0, topCoord)
        top.add(self.obstacle_sprite)
        bottom = Obstacle(botCoord, height-botCoord)
        bottom.add(self.obstacle_sprite)

    def newGame(self):
        self.player = Player()
        self.player.add(self.player_sprite)
        self.makeObstacle()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self.gameOver = True	
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.obstacle_sprite.update()
        self.player_sprite.update()
        # Collision Detection
        collide = pygame.sprite.spritecollide(self.player, self.obstacle_sprite, False)
        if collide:
            self.gameOver = True
        # Spawning extra Obstacles
        self.obsSpawnTimer -= 1
        if self.obsSpawnTimer <= 0:
            self.makeObstacle()
            self.obsSpawnTimer = self.obsSpawnRate

    def draw(self):
        gameScreen.fill(WHITE)
        gameScreen.blit(background,(0,0))
        self.obstacle_sprite.draw(gameScreen)
        self.player_sprite.draw(gameScreen)

        # Flip 
        pygame.display.flip()

    def main(self):
        while not self.gameOver:
            self.event()
            self.update()
            self.draw()


# Main Game Loop
game = Game()
game.newGame()
game.main()