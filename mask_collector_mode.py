import pygame
import random
from items_class import Mask, Vaccine, Player, Enemy

#initialisation 
pygame.init()
screen  = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

#caption + icons
pygame.display.set_caption("COVID GAME")
scoreboardIMG = pygame.image.load("111-400 x 400.png")
background_image1 = "panic_mode_.gif"
background_image2 = "bg-1000 x 800.PNG"
background_image_list = [background_image1, background_image2]

menuImg = pygame.image.load("menu-50 x 50.png")
pauseImg = pygame.image.load("pause-40 x 40.png")
textImg  = pygame.image.load("yay-80 x 80.PNG")

playerImg = pygame.image.load("virus-70 x 70.png")
enemyImg = pygame.image.load("person-55 x 55.png") #paper-40 x 40.PNG")
endImg = pygame.image.load("gameover.png")
#screen.blit(endImg, (200, 380))

def rotate(ls, index): #attempt create a scrolling background --> represent different locations
    return ls[index:] + ls[:index]

for x in background_image_list:
    background_image = pygame.image.load(x).convert()

#adding bgmmusic ~

pygame.mixer.music.load("helloo.wav")
pygame.mixer.music.play(-1)

isJump = False
jumpCount = 10

#game loop
running  = True

bgX = 0
bgX2 = background_image.get_width()

score = 0
player = Player(80, 400)
mask2 = Mask()

collide = False


def enemy(x, y): #draw
    screen.blit(enemyImg, (x, y)) #show at the end

def redrawGameWindow(): #change drawing 
    screen.blit(background_image, (bgX, 0))    
    screen.blit(background_image, (bgX2, 0))
    screen.blit(scoreboardIMG, (-10, -80))
    screen.blit(menuImg, (930,  20))
    screen.blit(pauseImg, (880, 20))


speed = 20 # for background-game mode (20 for med, 60 for hard)
counter = 0
counter2 = 0
person2 = Enemy()
person3 = Enemy()
person4 = Enemy()
person5 = Enemy()
person6 = Enemy()

while running:
    counter2 +=1
   
    if counter2 > 200:
        rotate(background_image_list, 1)
        x = background_image_list[0]
        background_image = pygame.image.load(x).convert()
        counter2 = 0
    
    clock.tick(speed)
    pygame.time.delay(40)
    
    bgX -=1.4
    bgX2 -=1.4

    if bgX < background_image.get_width() * -1:
        bgX = background_image.get_width()
    
    if bgX2 < background_image.get_width() * -1:
        bgX2 = background_image.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 2: # + boundary
        player.x -=2

    if keys[pygame.K_RIGHT] :
        player.x +=2

    if not isJump:
        if keys[pygame.K_UP] :
            player.y -=2
        
        if keys[pygame.K_DOWN]:
            player.y +=2

        if keys[pygame.K_SPACE]: #exit
            isJump = True 
    else:
        #player moves up, down
        if jumpCount >= -10:
            negative = 1
            #move slower on the way up and faster down
            if jumpCount < 0: #negative
                negative = -1

            player.y -= (jumpCount **2 ) *0.5 * negative #move down a little
            jumpCount -=1 #slowly move down
    
        else: #jump ends
            isJump = False  #can jump up/down again
            jumpCount = 10 #reset 

    screen.fill((0,250, 60)) #fill screen before player shows up
    redrawGameWindow()
    player.player1()
    mask2.show_mask()

    vaccine2 = Vaccine()
    if collide == False and mask2.mask_collision(player) == True: #distance = min
            #print("COLLECTED MASK!!!")
            collide = True 

    if collide == True:
        counter+=1
        player.x += 6
        if counter >= 10 and counter <=25:
            screen.blit(textImg, (player.x, player.y-50)) #display msg

        mask2.mask_anim(player)
       
    vaccine2.show_vaccine3()#print on screen
    
    person2.show_enemy(3)
    person3.show_enemy(3)
    person4.show_enemy(3)
    person5.show_enemy(3)
    person6.show_enemy(3)
    vaccine2.end_game(player)

    pygame.display.update() #shows player on screen

pygame.quit()

