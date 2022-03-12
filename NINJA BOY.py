import pygame , sys , random , time
from pygame.locals import*
from tkinter import *
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load("background and char/smsm_1.wav")
mixer.music.play(-1)
vec = pygame.math.Vector2
moveright=[pygame.image.load("background and char/Run__000.png")
,pygame.image.load("background and char/Run__001.png")
,pygame.image.load("background and char/Run__002.png")
,pygame.image.load("background and char/Run__003.png")
,pygame.image.load("background and char/Run__004.png")
,pygame.image.load("background and char/Run__005.png")
,pygame.image.load("background and char/Run__006.png")
,pygame.image.load("background and char/Run__007.png")
,pygame.image.load("background and char/Run__008.png")
,pygame.image.load("background and char/Run__009.png")]
moveleftt=[pygame.image.load("background and char/Run__100.png") 
,pygame.image.load("background and char/Run__101.png")
,pygame.image.load("background and char/Run__102.png")
,pygame.image.load("background and char/Run__103.png")
,pygame.image.load("background and char/Run__104.png")
,pygame.image.load("background and char/Run__105.png")
,pygame.image.load("background and char/Run__106.png")
,pygame.image.load("background and char/Run__107.png")
,pygame.image.load("background and char/Run__108.png")
,pygame.image.load("background and char/Run__109.png")]
throwright=[pygame.image.load("background and char/Throw__003.png")
,pygame.image.load("background and char/Throw__004.png")
,pygame.image.load("background and char/Throw__005.png")
,pygame.image.load("background and char/Throw__006.png")
,pygame.image.load("background and char/Throw__007.png")
,pygame.image.load("background and char/Throw__008.png")
,pygame.image.load("background and char/Throw__009.png")
,pygame.image.load("background and char/Throw__009.png")
,pygame.image.load("background and char/Throw__009.png")]
throwleft=[pygame.image.load("background and char/Throw__103.png")
,pygame.image.load("background and char/Throw__104.png")
,pygame.image.load("background and char/Throw__105.png")
,pygame.image.load("background and char/Throw__106.png")
,pygame.image.load("background and char/Throw__107.png")
,pygame.image.load("background and char/Throw__108.png")
,pygame.image.load("background and char/Throw__109.png")
,pygame.image.load("background and char/Throw__109.png")
,pygame.image.load("background and char/Throw__109.png")]
enemyr=[pygame.image.load("background and char/4_enemies_1_walk_000.png")
,pygame.image.load("background and char/4_enemies_1_walk_001.png")
,pygame.image.load("background and char/4_enemies_1_walk_002.png")
,pygame.image.load("background and char/4_enemies_1_walk_003.png")
,pygame.image.load("background and char/4_enemies_1_walk_004.png")
,pygame.image.load("background and char/4_enemies_1_walk_005.png")
,pygame.image.load("background and char/4_enemies_1_walk_006.png")
,pygame.image.load("background and char/4_enemies_1_walk_007.png")
,pygame.image.load("background and char/4_enemies_1_walk_008.png")
,pygame.image.load("background and char/4_enemies_1_walk_009.png")
,pygame.image.load("background and char/4_enemies_1_walk_010.png")
,pygame.image.load("background and char/4_enemies_1_walk_011.png")
,pygame.image.load("background and char/4_enemies_1_walk_012.png")
,pygame.image.load("background and char/4_enemies_1_walk_013.png")
,pygame.image.load("background and char/4_enemies_1_walk_014.png")
,pygame.image.load("background and char/4_enemies_1_walk_015.png")
,pygame.image.load("background and char/4_enemies_1_walk_016.png")
,pygame.image.load("background and char/4_enemies_1_walk_017.png")
,pygame.image.load("background and char/4_enemies_1_walk_018.png")
,pygame.image.load("background and char/4_enemies_1_walk_019.png")
,pygame.image.load("background and char/4_enemies_1_attack_000.png")
,pygame.image.load("background and char/4_enemies_1_attack_001.png")
,pygame.image.load("background and char/4_enemies_1_attack_002.png")
,pygame.image.load("background and char/4_enemies_1_attack_003.png")
,pygame.image.load("background and char/4_enemies_1_attack_004.png")
,pygame.image.load("background and char/4_enemies_1_attack_005.png")
,pygame.image.load("background and char/4_enemies_1_attack_006.png")
,pygame.image.load("background and char/4_enemies_1_attack_007.png")
,pygame.image.load("background and char/4_enemies_1_attack_008.png")
,pygame.image.load("background and char/4_enemies_1_attack_009.png")
,pygame.image.load("background and char/4_enemies_1_attack_010.png")
,pygame.image.load("background and char/4_enemies_1_attack_011.png")
,pygame.image.load("background and char/4_enemies_1_attack_012.png")
,pygame.image.load("background and char/4_enemies_1_attack_013.png")
,pygame.image.load("background and char/4_enemies_1_attack_014.png")
,pygame.image.load("background and char/4_enemies_1_attack_015.png")
,pygame.image.load("background and char/4_enemies_1_attack_016.png")
,pygame.image.load("background and char/4_enemies_1_attack_017.png")
,pygame.image.load("background and char/4_enemies_1_attack_018.png")
,pygame.image.load("background and char/4_enemies_1_attack_019.png")]
enemyl=[pygame.image.load("background and char/4_enemies_1_walk_100.png")
,pygame.image.load("background and char/4_enemies_1_walk_101.png")
,pygame.image.load("background and char/4_enemies_1_walk_102.png")
,pygame.image.load("background and char/4_enemies_1_walk_103.png")
,pygame.image.load("background and char/4_enemies_1_walk_104.png")
,pygame.image.load("background and char/4_enemies_1_walk_105.png")
,pygame.image.load("background and char/4_enemies_1_walk_106.png")
,pygame.image.load("background and char/4_enemies_1_walk_107.png")
,pygame.image.load("background and char/4_enemies_1_walk_108.png")
,pygame.image.load("background and char/4_enemies_1_walk_109.png")
,pygame.image.load("background and char/4_enemies_1_walk_110.png")
,pygame.image.load("background and char/4_enemies_1_walk_111.png")
,pygame.image.load("background and char/4_enemies_1_walk_112.png")
,pygame.image.load("background and char/4_enemies_1_walk_113.png")
,pygame.image.load("background and char/4_enemies_1_walk_114.png")
,pygame.image.load("background and char/4_enemies_1_walk_115.png")
,pygame.image.load("background and char/4_enemies_1_walk_116.png")
,pygame.image.load("background and char/4_enemies_1_walk_117.png")
,pygame.image.load("background and char/4_enemies_1_walk_118.png")
,pygame.image.load("background and char/4_enemies_1_walk_119.png")
,pygame.image.load("background and char/4_enemies_1_attack_100.png")
,pygame.image.load("background and char/4_enemies_1_attack_101.png")
,pygame.image.load("background and char/4_enemies_1_attack_102.png")
,pygame.image.load("background and char/4_enemies_1_attack_103.png")
,pygame.image.load("background and char/4_enemies_1_attack_104.png")
,pygame.image.load("background and char/4_enemies_1_attack_105.png")
,pygame.image.load("background and char/4_enemies_1_attack_106.png")
,pygame.image.load("background and char/4_enemies_1_attack_107.png")
,pygame.image.load("background and char/4_enemies_1_attack_108.png")
,pygame.image.load("background and char/4_enemies_1_attack_109.png")
,pygame.image.load("background and char/4_enemies_1_attack_110.png")
,pygame.image.load("background and char/4_enemies_1_attack_111.png")
,pygame.image.load("background and char/4_enemies_1_attack_112.png")
,pygame.image.load("background and char/4_enemies_1_attack_113.png")
,pygame.image.load("background and char/4_enemies_1_attack_114.png")
,pygame.image.load("background and char/4_enemies_1_attack_115.png")
,pygame.image.load("background and char/4_enemies_1_attack_116.png")
,pygame.image.load("background and char/4_enemies_1_attack_117.png")
,pygame.image.load("background and char/4_enemies_1_attack_118.png")
,pygame.image.load("background and char/4_enemies_1_attack_119.png")]
startb=pygame.image.load("background and char/Start.png")
exitb=pygame.image.load("background and char/EXIT.png")
knifep=pygame.image.load("background and char/Kunai.png")
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
score=0
screenwidth=1920
screenheight=1383
gameover=pygame.image.load("background and char/Gameover.png")
bgh=pygame.image.load("background and char/HOME.png")
bg=pygame.image.load("background and char/City1.png")
heroph=pygame.image.load("background and char/Idle__001.png")
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("NINJA BOY")
clock=pygame.time.Clock()

class Player():
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = 25
        self.left = False
        self.right = False
        self.attacking = False
        self.moves = 0
        self.speed = 15 
        self.isJumping = False
        self.start_x = x
        self.start_y = y
        self.visible=True
        self.standing = True
        self.health = 40
        self.direction=0
        self.hitbox = (self.x+30 , self.y+140 , self.width+150 , self.height+300 )
    def move(self):
      keys = pygame.key.get_pressed()
      if (keys[pygame.K_LEFT] |keys[pygame.K_a]) and self.x - self.step >= 0+200:   
        self.x -= self.step
        self.left = True
        self.right = False
        self.standing = False
      elif (keys[pygame.K_RIGHT]|keys[pygame.K_d]) and self.x + self.width + self.step+450 <= screenwidth: 
        self.x +=self.step
        self.right = True
        self.left = False
        self.standing = False  
      elif keys[pygame.K_SPACE] : 
            self.attack()    
      else:         
        self.standing = True
        self.moves = 0
    def attack(self):   
      if keys[pygame.K_SPACE]:
        while len(knifes)==0:
            if self.right:
                self.direction=1
                s=100
            else: 
                self.direction=-1
                s=200              
            kn=knife(self.x+80,self.y+270,self.direction,s)  
            knifes.append(kn)   
    def hit(self):
        self.speed = 15 
        self.isJumping = False
        self.x = self.start_x
        self.y = self.start_y
        self.moves = 0     
        i = -1
        while i < 0:
            i += 1
            pygame.time.delay(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()  
    def jump(self):
        if not self.isJumping:
            if keys[pygame.K_UP]|keys[pygame.K_w]:
                self.isJumping = True
        else:
            if self.speed >= -15 :
                neg = 1
                if self.speed < 0:
                    neg = -1
                self.y -= (self.speed ** 2) * 0.25 * neg
                self.speed -= 1
            else:
                self.speed = 15
                self.isJumping = False  
    def draw(self, screen):
        if self.visible:
            if not self.standing:
                if self.left:
                    screen.blit(moveleftt[self.moves // 2], (self.x, self.y))
                    self.moves += 1
                    if self.moves == 18:
                        self.moves = 0
                elif self.right:
                    screen.blit(moveright[self.moves // 2], (self.x, self.y))
                    self.moves += 1
                    if self.moves == 18:
                        self.moves = 0                                            
            else:
                if self.left:
                    screen.blit(pygame.image.load("background and char/Idle__101.png"), (self.x, self.y))
                else:
                    screen.blit(pygame.image.load("background and char/Idle__001.png"), (self.x, self.y))
            self.hitbox = (self.x+30 , self.y+140 , self.width+150 , self.height+300 )
            #pygame.draw.rect(screen, RED, self.hitbox, 2)        
        pygame.draw.rect(screen, RED, (500, 285, 400, 40))
        pygame.draw.rect(screen, GREEN, (500, 285 , self.health*10, 40))    
        text=font.render("HEALTH:",True,BLACK)
        screen.blit(text,(200,267))
class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = x
        self.step = 9
        self.moves = 0
        self.hitbox = (self.x+115 , self.y+50 , self.width+100 , self.height+240 )
        self.health = 10
        self.visible = True
    def draw(self, screen):
        if self.visible:
            self.move()
            if self.step < 0:
                screen.blit(enemyl[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 38 * 2:
                    self.moves = 0
            else:
                screen.blit(enemyr[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 38 * 2:
                    self.moves = 0
            self.hitbox = (self.x+100 , self.y+30 , self.width+150 , self.height+250 )
            #pygame.draw.rect(screen, RED, self.hitbox, 2) 
            pygame.draw.rect(screen, RED, (self.hitbox[0], self.hitbox[1] - 15, 140, 20))
            pygame.draw.rect(screen, GREEN, (self.hitbox[0], self.hitbox[1] - 15, self.health * 15, 20))    
    def move(self):
        if self.step > 0:
            if self.x + self.step > self.end:
                self.step *=-1
            else:
                self.x += self.step
        else:
            if self.x - self.step < self.start:
                self.step *= -1
            else:
                self.x += self.step
    def stepc(self):
        self.step+=1            
    def kill(self): 
            self.health -= 1
            if self.health == 0:
                self.visible=False    
                self.hitbox=(0,0,0,0)   
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action

class knife(): 
    def __init__ (self,x,y,direction,step): 
        self.x=x
        self.y=y
        self.direction=direction
        self.step=step*direction
        self.moves=0
    def drawknife(self,screen): 
        screen.blit(pygame.image.load("background and char/Kunai.png"), (self.x, self.y))
man = Player(1200, 660, 10, 10)
en = Enemy(100,820,10,10,1400)
start_button = Button(screenwidth // 2 - 265, screenheight // 2-200, startb)
exit_button = Button(screenwidth // 2 - 265, screenheight // 2-100, exitb)
font=pygame.font.SysFont("Courier New",70,True)

screen.fill((0,0,0))
screen.blit(bgh,(0,0))
start_button.draw() 
exit_button.draw()
pygame.display.update()
def redrawGame():
     global moves
     screen.fill((0,0,0))
     screen.blit(bg,(xb,yb))
     text=font.render("SCORE:"+str(score),True,BLACK)
     screen.blit(text,(200,350))
     for en in enemies:
        en.draw(screen)
     man.draw(screen)
     man.jump()
     man.attack() 
     man.move()
     for k in knifes: 
        k.drawknife(screen)
     pygame.display.update()

knifes=[]
xb=0
yb=-200
enemies=[]
#Main 
run=True
main_menu=True
gameoverr=True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(30)
    x_mid = (man.hitbox[0] + man.hitbox[0] + man.hitbox[2]) // 2
    y_mid = (man.hitbox[1] + man.hitbox[1] + man.hitbox[3]) // 2
    if en.hitbox[0] < x_mid < en.hitbox[0] + en.hitbox[2]:
        if en.hitbox[1] < y_mid < en.hitbox[1] + en.hitbox[3]:
            man.health-= 1
            man.hit()       
            if man.health == 0:
                man.visible=False    
                man.hitbox=(0,0,0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()       
    for k in knifes :
        if k.x >en.hitbox[0] and k.x<en.hitbox[0]+en.hitbox[2]: 
            if k.y >en.hitbox[1] and k.y<en.hitbox[1]+en.hitbox[3]:
                knifes.remove(k)
                en.kill()
                if en.visible==False:
                  score+=5
        if k.x<screenwidth and k.x>0: 
            k.x+=k.step+50
        else: 
            knifes.remove(k)
    if len(enemies) == 0:
        en = Enemy(100,820,10,10,1400)
        en2= Enemy(400,820,10,10,1400)
        enemies.append(en)
        enemies.append(en2)         
    for en in enemies:
        en.move()
        if en.health == 0: 
            enemies.remove(en)                        
    if main_menu == True:
	    if exit_button.draw():
		    run = False  
	    if start_button.draw():
		    main_menu = False 
    elif  man.health==0 and man.visible==False:
        score=0
        gameoverr==True
        screen.fill((0,0,0))
        screen.blit(gameover,(0,0))
        pygame.display.update() 
        if keys [pygame.K_ESCAPE]:
            main_menu=True
            gameoverr=False
            screen.fill((0,0,0))
            screen.blit(bgh,(0,0))
            start_button.draw()
            exit_button.draw()
            man.visible=True
            man.health=40
            pygame.display.update()           
    elif keys [pygame.K_ESCAPE]:
            screen.fill((0,0,0))
            screen.blit(bgh,(0,0))
            start_button.draw()
            exit_button.draw()
            man.visible=True
            man.health=40
            pygame.display.update()
            main_menu=True              
    else: 
        redrawGame()          