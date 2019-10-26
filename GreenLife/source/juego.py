import pygame,sys 
import random
from pygame.locals import *

def main():
    pygame.init() #Inicializar todos los modulos de pygame
    ventana=pygame.display.set_mode([1280,720]) #Fijar pantalla y hacerla superficie
    pygame.display.set_caption("GREEN LIFE")
    salir=False
    reloj1=pygame.time.Clock() #Crea variale tipo tiempo
    salto_sound = pygame.mixer.Sound("mario-bros-jump.mp3")
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",20,False,True)
    texto1=fuente1.render("Goal: get 100 points in 30 seconds",0,(0,0,0))
    blanco=(255,255,255)
    rojo=(200,20,50)
    azul=(70,70,190)
    #Images
    ifondo = pygame.image.load("../assets/Fondos/esc1.png").convert_alpha()
    ipersonaje = pygame.image.load("../assets/Personajes/Principal/mov.png").convert_alpha()#Carga una imagen y devuelve una superficie
    iciclista = pygame.image.load("../assets/Personajes/NPC/ciclista.png").convert_alpha()
    ipapel = pygame.image.load("../assets/Items/papel.png").convert_alpha()
    #Sprites
    #1
    spersonaje = pygame.sprite.Sprite() #Instruccion que devuelve un sprite
    spersonaje.image=ipersonaje #Carga una imagen en el sprite
    spersonaje.rect= ipersonaje.get_rect() #Devuelve rectangulo con dimensiones de la imgaen
    spersonaje.rect.top = 720/2
    spersonaje.rect.left = 1280/2
    #2
    sciclista = pygame.sprite.Sprite()
    sciclista.image=iciclista
    sciclista.rect= iciclista.get_rect()
    sciclista.rect.top = 720/2
    sciclista.rect.left = 1280
    #3
    spapel = pygame.sprite.Sprite()
    spapel.image=ipapel
    spapel.rect= ipapel.get_rect()
    #Other variales
    termino = False
    segundosint = 0
    puntos = 0
    lifes = 5
    aux = True
    listarec=[]

    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
           
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #Evaluar si se presiono flecha hacia arriba
                    spersonaje.rect.move_ip(0,-150)
                    salto_sound.play()

            if event.type == pygame.KEYUP: #Evalua si se suelta una tecla
                if event.key == pygame.K_UP:
                    spersonaje.rect.move_ip(0,150)
   
   	#Random Oject Generator 
        aux+=1
        if aux%40==0:
            for x in range (2):
                w = 32
                h = 32
                x = random.randrange(1280,1500)
                y = random.randrange(200,400)
                listarec.append(pygame.Rect(x,y,w,h))
	#Collisions witch the npc
        (xr,yr)=(spersonaje.rect.left,spersonaje.rect.top) 
        if termino==False:
            sciclista.rect.move_ip(-20,0)
            if sciclista.rect.colliderect(spersonaje.rect):  
                (spersonaje.rect.left,spersonaje.rect.top)=(xr,yr) 
                sciclista.rect.left= 1280
                sciclista.rect.top = 720/2
                lifes-=1
            if sciclista.rect.left == 0:
                sciclista.rect.left= 1280
                sciclista.rect.top = 720/2
	    #Collisions with random objects
            if termino==False:
                for recs in listarec: 
                    recs.move_ip(-15,0)
                    if recs.colliderect(spersonaje.rect):
			recs.x=0
                        recs.width = 0
                        recs.height = 0
                        puntos += 5

            if lifes == 0:
                termino=True
		print 'Perdiste'
            if puntos == 100:
                termino=True
		print 'Ganaste'

        reloj1.tick(15) #Frame Counter

	#Draw Screens
        ventana.fill(blanco) 
        ventana.blit(ifondo,(0,0))
        ventana.blit(texto1,(50,20))
        ventana.blit(spersonaje.image,spersonaje.rect)
        ventana.blit(sciclista.image,sciclista.rect)
        for recs in listarec:
             pygame.draw.rect(ventana,(90,228,10),recs)
        
        #Chronometer
        if segundosint == 30:
            termino=True
        if termino == False:
            segundosint = pygame.time.get_ticks()/1000
            segundos= str(segundosint)
        lifess= str(lifes)
        puntoss= str(puntos)
        contador=fuente1.render(segundos,0,(0,0,0))
        clifes=fuente1.render("Lifes: "+lifess,0,(0,0,0))
        cpuntos=fuente1.render("Points: "+puntoss,0,(0,0,0))
        ventana.blit(contador,(1200,650))
        ventana.blit(clifes,(100,650))
        ventana.blit(cpuntos,(1280/2,650))

        pygame.display.update()


    pygame.quit()


main()
