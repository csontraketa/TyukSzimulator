import pygame, time, random, sys, os
from pygame import mixer

pygame.init()
pygame.font.init()

ablak = pygame.display.set_mode((1000, 600)) # A B L A K
ablak.fill((0,0,0))
ablak.blit(pygame.image.load("loadscreen.png"),(0,0))  
pygame.display.update()
time.sleep(5)


isProgramRunning = True

mixer.init()
mixer.music.load("menuTrack.mp3")
mixer.music.set_volume(1)
mixer.music.play(loops=-1)
   
while isProgramRunning:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ablakIsRunning = True
                isProgramRunning = False
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        
    ablak.fill ((0,0,0))
    ablak.blit(pygame.image.load("menu.png"),(0,0))  
    pygame.display.update()
    
pygame.quit()

### E L Ő K É S Z Í T É S 
pygame.init()
ablak = pygame.display.set_mode((1000, 600)) # A B L A K
pygame.display.set_caption("gombóc game")
isGameOver = 0


### A U D I O

mixer.init()
mixer.music.load("track.mp3")
mixer.music.set_volume(1)
mixer.music.play(loops=-1)


### I N T R O

ablak.blit(pygame.image.load("intro.png"),(0,0))
#szoveg = pygame.font.SysFont(None, 64)
#szovegSet = szoveg.render("gombóc game", True, (255,255,255))
#ablak.blit(szovegSet, (500, 300))
pygame.display.update()
time.sleep(2)
#ablak.fill((255,255,255))
#pygame.display.update()
#time.sleep(1)


### P L A Y E R S
repuloX =      20
repuloY =     300
repuloWidth =  45
repuloHeight = 15
repuloVel =    20

akadaly1X =     980 # lesz több akadály is, csak
akadaly1Y =     300 # akok azzal 1 vonalban...
akadaly1Width =  40 # talán ferdén is :)
akadaly1Height = 40
akadaly1Vel =    60
akadaly1Irany =  -1

akadaly2X = 1020
akadaly2Y = akadaly1Y -50

akadaly3X = 1060
akadaly3Y = akadaly2Y +50 

akadaly4X = 1100
akadaly4Y = akadaly2Y +100

akadaly5X = 1140
akadaly5Y = akadaly2Y -100

### F Ő P R O G R A M

while ablakIsRunning:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            ablakIsRunning = False
   

    # I N P U T
    gomb = pygame.key.get_pressed()
    
    if gomb[pygame.K_w]:
        repuloY -= repuloVel

    if gomb[pygame.K_s]:
        repuloY += repuloVel

    if gomb[pygame.K_q]:
            pygame.quit()
            sys.exit()

    
    ### T Á R G Y A K   M O Z G Á S A 
    akadalyGyorsit = random.randint(0,30)
    akadaly1X += (akadaly1Vel +akadalyGyorsit) * akadaly1Irany
    akadaly2X += (akadaly1Vel +akadalyGyorsit) * akadaly1Irany
    akadaly3X += (akadaly1Vel +akadalyGyorsit) * akadaly1Irany
    akadaly4X += (akadaly1Vel +akadalyGyorsit) * akadaly1Irany
    akadaly5X += (akadaly1Vel +akadalyGyorsit) * akadaly1Irany
    
    if akadaly1X <= 0:
        akadaly1X = 980
        akadaly1Y = repuloY 
    
    if akadaly2X <= 0:
        akadaly2X = 1020
        akadaly2Y = repuloY
  
    if akadaly3X <= 0:
        akadaly3X = 1060
        akadaly3Y = repuloY
   
    if akadaly4X <= 0:
        akadaly4X = 1100
        akadaly4Y = repuloY
     
    if akadaly5X <= 0:
        akadaly5X = 1140
        akadaly5Y = repuloY

    if repuloY >= 580:
        repuloY -= repuloVel
    if repuloY <= 0:
        repuloY += repuloVel

    
    # K A R A K T E R E K  É S  R A J Z O L Á S
    def rajzolasdi():
        #ablak.fill((0,0,0))
        ablak.blit(pygame.image.load("hatter.png"),(0,0))   
        pygame.draw.rect(ablak, (255, 255, 255), (repuloX, repuloY, repuloWidth, repuloHeight)) # igazából nem fehér...
        pygame.draw.rect(ablak, (255, 0, 0), (akadaly1X, akadaly1Y, akadaly1Width, akadaly1Height))#ez se
        pygame.draw.rect(ablak, (0, 255, 0), (akadaly2X, akadaly2Y, akadaly1Width, akadaly1Height))#ez se
        pygame.draw.rect(ablak, (0, 0, 255), (akadaly3X, akadaly3Y, akadaly1Width, akadaly1Height))#ez se
        pygame.draw.rect(ablak, (255, 0, 255), (akadaly4X, akadaly4Y, akadaly1Width, akadaly1Height))#ez se
        pygame.draw.rect(ablak, (0, 255, 255), (akadaly4X, akadaly4Y, akadaly1Width, akadaly1Height))#ez se
        ablak.blit(pygame.image.load("repulo.png"),(repuloX,repuloY))
        ablak.blit(pygame.image.load("golyo.png"),(akadaly1X,akadaly1Y))
        ablak.blit(pygame.image.load("golyo.png"),(akadaly2X,akadaly2Y))
        ablak.blit(pygame.image.load("golyo.png"),(akadaly3X,akadaly3Y))
        ablak.blit(pygame.image.load("golyo.png"),(akadaly4X,akadaly4Y))
        ablak.blit(pygame.image.load("golyo.png"),(akadaly5X,akadaly5Y))
    rajzolasdi()

    # G A M E  O V E R
    def gameOver():
        if gomb[pygame.K_q]:
            pygame.quit()
            sys.exit()
        else:
            ablak.blit(pygame.image.load("outro.png"),(0,0))
            pygame.display.update()
            time.sleep(1)
            rajzolasdi()
            #pygame.quit()
            #sys.exit()
    
    if repuloX in range(akadaly1X-40, akadaly1X+40) and repuloY in range(akadaly1Y-40, akadaly1Y+40):
        print("Game Over! Kampec!")
        gameOver()

   
    if repuloX in range(akadaly2X-40, akadaly2X+40) and repuloY in range(akadaly2Y-40, akadaly2Y+40):
        print("Game Over! Jó vót.")
        gameOver()

    if repuloX in range(akadaly3X-40, akadaly3X+40) and repuloY in range(akadaly3Y-40, akadaly3Y+40):
        print("Game Over! Majd máskor...")
        gameOver()
  
    if repuloX in range(akadaly4X-40, akadaly4X+40) and repuloY in range(akadaly4Y-40, akadaly4Y+40):
        print("Game Over!")
        gameOver()
    
    if repuloX in range(akadaly5X-40, akadaly5X+40) and repuloY in range(akadaly5Y-40, akadaly5Y+40):
        print("Game Over! Véged!")
        gameOver()

   
    # S A F E T Y  |V
    print ("Pliz dont close meee! I am running!")
    print ("...0...")
    print ("..-|-..")
    print ("../ \..")
    

    pygame.display.update()     
    
pygame.quit()
