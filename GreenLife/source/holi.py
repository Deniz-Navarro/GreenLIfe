import pygame,sys 
from random import randint
from pygame.locals import *

class Character(pygame.sprite.Sprite):
    def __init__(self,lifes):
        pygame.sprite.Sprite.__init__(self)
        self.ipersonaje = pygame.image.load("../assets/Personajes/Principal/mov.png").convert_alpha()
        self.rect= self.ipersonaje.get_rect() 
        self.rect.top = 720/2
        self.rect.left = 1280/2
        self.speed = 150 
        self.lifes = lifes
        self.points = 0
        segundos = "0"

    def draw(self,surface): #Draw Character
        surface.blit(self.ipersonaje,self.rect)
    
    def move(self,event): #Player move
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: 
                    self.rect.top -= self.speed

        if event.type == pygame.KEYUP: 
                if event.key == pygame.K_UP:
                    self.rect.top += self.speed

    def drawl(self,surface,fuente): #Draw Lifes
        lifess = str(self.lifes)
        clifes=fuente.render("Lifes: "+lifess,0,(0,0,0))
        surface.blit(clifes,(100,650))
    
    def drawp(self,surface,fuente): #Draw Points
        pointss = str(self.points)
        cpoints=fuente.render("Points: "+pointss,0,(0,0,0))
        surface.blit(cpoints,(1280/2,650))
    
    def win(self,surface,fuente): #Draw Win
        lectura=fuente.render("You Win",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2))
    
    def lose(self,surface,fuente): #Draw Lose 
        lectura=fuente.render("You Lose",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2))

class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.iciclista = pygame.image.load("../assets/Personajes/NPC/ciclista.png").convert_alpha()
        self.rect= self.iciclista.get_rect() 
        self.rect.top = 720/2
        self.rect.left = 1450
        self.speed = speed
        

    def draw(self,surface): #Enemy Draw
        surface.blit(self.iciclista,self.rect)
    
    def collision(self,player): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top) 
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):  
            (player.rect.left,player.rect.top)=(xr,yr) 
            self.rect.left= 1450
            self.rect.top = 720/2
            player.lifes-=1
        if self.rect.left <= -20:
            self.rect.left= 1450
            self.rect.top = 720/2

class Object(pygame.sprite.Sprite):
    def __init__(self,speed,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.iobject = imagen
        self.rect= self.iobject.get_rect() 
        self.rect.top = randint(200,400)
        self.rect.left = randint(1280,1500)
        self.speed = speed
        

    def draw(self,surface): #Enemy Draw
        surface.blit(self.iobject,self.rect)
    
    def collision(self,player,points): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top) 
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):  
            (player.rect.left,player.rect.top)=(xr,yr) 
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)
            player.points+=points
        if self.rect.left <= -20:
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)

def Game():
    pygame.init() #Initialize pygame modules
    ventana=pygame.display.set_mode([1280,720])
    pygame.display.set_caption("GREEN LIFE")
    #Variables
    salir = False
    termino = False
    reloj1=pygame.time.Clock()
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",100,True,False)
    texto1=fuente1.render("Goal: get 150 points in 25 seconds",0,(0,0,0))
    rojo=(200,20,50)
    verde=(50,205,50)
    seconds = 0
    #Images
    ifondo = pygame.image.load("../assets/Fondos/esc1.png").convert_alpha()
    ipapel = pygame.image.load("../assets/Items/papel.png").convert_alpha()
    iperiodico = pygame.image.load("../assets/Items/periodico.png").convert_alpha()
    #Calling Classes
    player = Character(5)
    ciclista = Enemy(25)
    objeto = Object(20,ipapel)
    objeto2 = Object(20,iperiodico)


    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            player.move(event)
           
        #Chronometer
        if termino == False:
            seconds = pygame.time.get_ticks()/1000
            segundos= str(seconds)
        #End Game
        if termino == False:
            ciclista.collision(player)
            objeto.collision(player,5)
            objeto2.collision(player,10)
        reloj1.tick(15) #Frame Counter
        #Draw on the surface
        ventana.blit(ifondo,(0,0))
        player.draw(ventana)
        player.drawl(ventana,fuente1)
        player.drawp(ventana,fuente1)
        ventana.blit(texto1,(50,20))
        chronometer=fuente1.render(segundos,0,(0,0,0))
        ventana.blit(chronometer,(1200,650)) #Draw Chronometer
        ciclista.draw(ventana) 
        objeto.draw(ventana)
        objeto2.draw(ventana)
        #Lose Condition
        if player.lifes == 0 or seconds == 30:
            termino = True
            ventana.fill(rojo)
            player.lose(ventana,fuente2)  
        #Win Condition
        if player.points >= 100 and seconds < 30:
            termino = True
            ventana.fill(verde)
            player.win(ventana,fuente2)  
        pygame.display.update()  

Game()