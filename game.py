import pygame
import random
from items_class import Mask, Vaccine, Player, Enemy

#initialisation 
pygame.init()
screen  = pygame.display.set_mode((1000, 800))

#caption + icon
scoreboardIMG = pygame.image.load("111-400 x 400.png") #leaderboard
#background_image = pygame.image.load("12-1000 x 800.jpg")
background_image = pygame.image.load("panic_mode_.gif")

pygame.display.set_caption("COVID GAME")
background_image = pygame.image.load("panic_mode_.gif").convert()
textImg  = pygame.image.load("yay-30 x 30.PNG")

playerImg = pygame.image.load("coronavirus-70 x 70.png")
enemyImg = pygame.image.load("person-55 x 55.png") 

#adding some background music ~

pygame.mixer.music.load("helloo.wav")
pygame.mixer.music.play(-1)


enemyY = [600, 600, 600, 600, 600]
enemyX = []
enemyX_change = []
enemyY_change = []

#masklocation
xm = 630
ym = 560

#vaccine

v1 = 850
v2 = 460

isJump = False
jumpCount = 10

#game loop
running  = True

playerx = 250
playery = 380
score = 0
player = Player(250, 380)


def enemy(x, y): #draw
    screen.blit(enemyImg, (x, y)) #show at the end

def redrawGameWindow(): #change drawing 
    screen.blit(background_image, (0,0))
    screen.blit(scoreboardIMG, (-10, -80))
    
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerx > 2: # + boundary
        playerx -=2

    if keys[pygame.K_RIGHT] :
        playerx +=2

    if not isJump:
        if keys[pygame.K_UP] :
            playery -=2
        
        if keys[pygame.K_DOWN]:
            playery +=2

        if keys[pygame.K_SPACE]: #exit
            isJump = True 
    else:
        #player moves up, down
        if jumpCount >= -10:
            negative = 1
            #move slower on the way up and faster down
            if jumpCount < 0: #negative
                negative = -1

            playery -= (jumpCount **2 ) *0.5 * negative #move down a little
            jumpCount -=1 #slowly move down
    
        else: #jump ends
            isJump = False  #can jump up/down again
            jumpCount = 10 #reset 
    
    screen.fill((0,250, 60)) #fill screen before player shows up
    redrawGameWindow()
    #player = Player(250, 380)
    #player_show(player.x, player.y)
    player.player1(playerx, playery)

    vaccine2 = Vaccine()
    mask2 = Mask()
    mask2.mask_anim(xm, ym)
    mask2.add_mask()
    a = mask2.mask_collision(player)
    if a: # true
        mask2.y = player.y
        score +=1
        player.player_move(player.x, player.y)
        print(score)
        
    vaccine2.vaccine(v1, v2)
    vaccine2.end_game(player)
    
    
    for i in range(5):
        enemyX.append(random.randint(0, 830))
        #enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)
    
    #enemy movement 
    
    for i in range(5):
        enemy(enemyX[i], enemyY[i])
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 900:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
            
    enemyX += enemyX_change
    pygame.display.update() #shows player on screen
    

pygame.quit()
