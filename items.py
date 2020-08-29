import pygame, random

screen  = pygame.display.set_mode((1000, 800))
maskImg = pygame.image.load("mask-65 x 65.png")
vaccine1 = pygame.image.load("vaccine-40 x 40.JPG")
playerImg = pygame.image.load("coronavirus-70 x 70.png")

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10
        # self.left = False
        # self.right = False
        # self.walkcount = 0
   
    def player1(self, x, y): #draw start
        screen.blit(playerImg, (x, y))

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
        self.x = 930
        self.y = 800

    def mask_anim(self, x, y): #draw 
        screen.blit(maskImg, (x, y))

    def add_mask(self, playerx, playery): #onto virus
    #if player hits mask
        player = Player(playerx, playery)
        if (player.x, player.y) == (929, 758):
            screen.blit(maskImg, (self.x, self.y)) 

class Vaccine:
    def __init__(self):
        self.v_x = 920
        self.v_y = 500
    
    def vaccine(self, x, y): #draw
        screen.blit(vaccine1, (x, y)) #show at the end

    def end_game(self, player):
        if (player.x, player.y) == (self.v_x, self.v_y):
            print("GAME OVER")
            font = pygame.font.Font('freesansbold.ttf', 32)
            green = (0, 255, 0) 
            blue = (0, 0, 128) 
            text = font.render('GeeksForGeeks', True, green, blue) 
  
