import pygame, random, math

screen  = pygame.display.set_mode((1000, 800))
maskImg = pygame.image.load("mask-65 x 65.png")
vaccine1 = pygame.image.load("vaccine-40 x 40.JPG")
playerImg = pygame.image.load("virus-70 x 70.png")
enemyImg = pygame.image.load("person.png")# paper-40 x 40.PNG")
textImg  = pygame.image.load("yay-80 x 80.PNG")
endImg = pygame.image.load("gameover.png")

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10
   
    def player1(self): 
        screen.blit(playerImg, (self.x, self.y)) #draw start
    
    def player_move(self, x, y): #speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# and self.x > 4: # + boundary
            self.x -=4

        if keys[pygame.K_RIGHT] :
            self.x +=4
        
        if not self.isJump:
            if keys[pygame.K_UP] :
                self.y -=4
            if keys[pygame.K_DOWN]:
                self.y +=4
            if keys[pygame.K_SPACE]: #exit
                self.isJump = True 
        else:
            #player moves up, down
            if self.jumpCount >= -10:
                negative = 1
                #move slower on the way up and faster down
                if self.jumpCount < 0: #negative
                    negative = -1

                self.y -= (self.jumpCount **2 ) *0.5 * negative #move down a little
                self.jumpCount -=1 #slowly move down
        
            else: #jump ends
                self.isJump = False  #can jump up/down again
                self.jumpCount = 10 #reset 

    #check for out of bounds:
    def print_player(self, x, y):
        print(self.x, self.y)
    def check_boundary(self, x, y):
        if self.x <=0:
            self.x = 0
        elif self.x >= 960: #< 800
            self.x = 960
    
class Mask:

    def __init__(self):
        self.x = 280
        self.y = 400
        self.isJump = False
        self.jumpCount = 10
    
    def show_mask(self):
        screen.blit(maskImg, (self.x, self.y)) #set mask location

    def mask_anim(self, player): #draw         
       
        self.x = player.x 
        self.y = player.y
        self.show_mask()

    def mask_collision(self, player):
        #if distance is small, show they collide and different things happen
        distance = math.sqrt((math.pow(self.x - player.x, 2)) + (math.pow(self.y - player.y, 2)))
        
        if distance < 10:
            # screen.blit(textImg, (self.x, self.y-50)) #display msg
            # screen.blit(textImg, (self.x, self.y-80)) #display msg
            # screen.blit(textImg, (self.x, self.y-100)) #display msg

            return True
        else:
            return False 

class Vaccine:
    def __init__(self):
        self.v_x = 920
        self.v_y = 400
    
    def show_vaccine3(self): #draw
        screen.blit(vaccine1, (self.v_x, self.v_y)) #show at the end

    def end_game(self, player):
        distance = math.sqrt((math.pow(self.v_x - player.x, 2)) + (math.pow(self.v_y - player.y, 2)))        
        
        if distance <= 12:
     
            #pygame.time.delay(1000)
            screen.blit(endImg, (50, 0))
            pygame.time.delay(1500)

            #exit()

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 850)
        self.y = 540 #480
        
    def show_enemy(self, step):
        if self.x<=800 and self.x >= 0:
            self.x +=step
        else:
            self.x = 0

        screen.blit(enemyImg, (self.x, self.y)) #show at the end

    def enemy(self): #draw
        screen.blit(enemyImg, (self.x, self.y)) #show at the end

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# and self.x > 4: # + boundary
            self.x -=1.4

        if keys[pygame.K_RIGHT] :
            self.x +=1.4

#hand san 
