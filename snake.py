import pygame
from sys import exit
from random import randint
from pygame.math import Vector2

cellestørrelse = 40 
cellenumber = 20 

class slange:
    def __init__(self):
        self.body = [Vector2(4,10),Vector2(3,10),Vector2(2,10)] #alle de blokkene som slangen skal oppholde seg i starten
        self.direction = Vector2(1,0) # bevegelsen til hode
        self.new_blokk = False 

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bottomleft.png').convert_alpha()
        
    def tegne_slange(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        # for blokk in self.body:
        #     blokk_rect = pygame.Rect(int(blokk.x*cellestørrelse), int(blokk.y *cellestørrelse), cellestørrelse, cellestørrelse)
        #     pygame.draw.rect(vindu,"red",blokk_rect) 
        for index, blokk in enumerate(self.body): # self. body er en liste som inneholder slanges body som blokker og hver blokk er vektor2 - posisjon) enumerate gir oss mulighet til å gå gjennom både indeksene og blokkene i slangens body 
            x_pos = int(blokk.x * cellestørrelse) #gir oss den nøyaktige posisjonen i x-retning og i piksler
            y_pos = int(blokk.y * cellestørrelse) # gir oss den nøyeaktige posisjonene i y-retning og i piksler
            blokk_rect = pygame.Rect(x_pos,y_pos, cellestørrelse, cellestørrelse) #lager rektangel for blokk (blokker i slangens body ) posisjonen til den gjeldende blokk
        
            if index == 0:
                vindu.blit(self.head, blokk_rect)
            elif index == len(self.body) -1:
                vindu.blit(self.tail, blokk_rect)
            else: 
                previous_blokk = self.body[index + 1] - blokk  #self.body[index + 1] er den neste blokken i slangebodyen, ved å trekke blokk fra self.body[index + 1], finner vi avstanden fra den blokken til den neste blokken   
                next_blokk  = self.body[index - 1] -blokk  #self.body[index + 1] er den forrge blokken i slangebodyen, ved å trekke blokk fra self.body[index + -], finner vi avstanden fra den blokken til den neste blokken 
                if previous_blokk.x == next_blokk.x:   # hvis x kordinatene er like, ligger slangebodyen vertikalt 
                    vindu.blit(self.body_vertical,blokk_rect ) 
                elif previous_blokk.y == next_blokk.y: #hvis slangen ligger horisontalt 
                    vindu.blit(self.body_horizontal, blokk_rect) #blir tegnet på posisjonen til den gjeldene blokken i slangensbody
                else: 
                    if previous_blokk.x == -1 and  next_blokk.y == -1 or previous_blokk.y == -1 and next_blokk.x == -1:  #det er når slange går ned også til venstre
                        vindu.blit(self.body_tl,blokk_rect)
                    elif previous_blokk.x == -1 and  next_blokk.y == 1 or previous_blokk.y == 1 and next_blokk.x == -1: # dette er nå slange går  opp og til venstre
                        vindu.blit(self.body_bl,blokk_rect)
                    elif previous_blokk.x == 1 and  next_blokk.y == -1 or previous_blokk.y == -1 and next_blokk.x == 1: # dette er når slangen går ned også til høyre
                        vindu.blit(self.body_tr,blokk_rect)
                    elif previous_blokk.x == 1 and  next_blokk.y == 1 or previous_blokk.y == 1 and next_blokk.x == 1: # dette er når slangen går ned også til venstre
                        vindu.blit(self.body_br,blokk_rect)
                    
            # else: 
            #     pygame.draw.rect(vindu,(150,100,100),blokk_rect)

    
    def update_head_graphics(self):
        head_relation = self.body[1]- self.body[0] # for eks: 4/3 på hodet og 3/3 på den forrge blokk. hvis tr3kker posisjonen til hode fra blokken før hode dermed får vi en bevegeles retning 
        if head_relation == Vector2(1,0): # når hodet snur til venstre
            self.head = self.head_left
        if head_relation == Vector2(-1,0): #når hodet snur til høyre
            self.head = self.head_right
        if head_relation == Vector2(0,-1): #når hodet går ned
            self.head = self.head_down
        if head_relation == Vector2(0,1): #når hodet går opp
            self.head = self.head_up

    def update_tail_graphics(self):
        tail_relation = self.body[-2]- self.body[-1]   #for eks: halen 3/3 og 4/3 på den forrige blokk 
        if tail_relation == Vector2(1,0):#   når halen går mot venstre  4-3,3-3 = 1,0
            self.tail = self.tail_left
        if tail_relation == Vector2(-1,0): #
            self.tail = self.tail_right
        if tail_relation == Vector2(0,-1):
            self.tail = self.tail_down
        if tail_relation == Vector2(0,1):
            self.tail = self.tail_up

        #her er liksom at når slagen spiser et eple, beholder vi den siste verdien (halen), og adderer nye posisjonen til hode på starten av listen/vektoren), dermed blir slangen større 

    def flytte_slange(self): #the head moves to new blokk, blokken før hode går posisjonen hvor hode pleide å bli og det bare fortsetter
        if self.new_blokk == True: #når slangen har har akkurat spist et eple 
            body_copy = self.body[:] # kopierer hele listen 
            body_copy.insert(0,body_copy[0] + self.direction) # (vi også legger nye verdien på begynnelsen av body_copy(midlertidige body ) og det er == vi tar nåværende posisjonen til slanges hode og legger til retningen self.direction. Dermed får vi datamaskinen til å bestemme en ny posisjon for slagens. dermed illustrer disse rektangelene som slangen beveger seg
            self.body = body_copy[:] #etterpå oppdragerer vi den selve slangebodyp
            self.new_blokk = False # å tilføye nye blokk(at slangen blir lengere) blir slått av
            
        else: #den vanlige beveglesen til slangen
            body_copy = self.body[:-1] # kopierer hele listen med vektor utenom den siste til den nye listen. So den siste blokk bare forsvinner
            body_copy.insert(0,body_copy[0] + self.direction) #lager hodet på begynnelsen av listen og setter verdien til den første blokken i listen og plus retningen til slangen
            self.body = body_copy[:]


    def add_blokk(self):
        self.new_blokk = True

class FRUKT:
    def __init__(self):
        self.randomisere()
        
    def tegne_frukt(self):
        frukt_rect = pygame.Rect(int(self.pos.x * cellestørrelse),int(self.pos.y*cellestørrelse),cellestørrelse,cellestørrelse) # (20*40))800,800det den koden gjør å plassere fruktene kordinaten til 5 ganges med cellestørrelse og 4 gang cellestørrelse fra toppen  
        # frukt_rect = pygame.Rect(self.pos.x ,self.pos.y,cellestørrelse,cellestørrelse) #det den koden gjør å plassere fruktene 5 pixel fra hoyre og 4 pixels fra toppen
        # pygame.draw.rect(vindu,(126,166,114),frukt_rect)
        vindu.blit(eple,frukt_rect)
    def randomisere(self):
        self.x = randint(0,cellenumber-5)# fordi på grunn av random, kan posisjonen til eple bli dannet utenfor spillareat 
        self.y = randint(0,cellenumber-5) 
        self.pos = Vector2(self.x,self.y) #hvis vi ikke hadde from pygame.math import Vector2, jeg måtte skrive hvergang pyygame.math

class MAIN:
    def __init__(self):
        self.slange = slange()
        self.frukt = FRUKT()
    def update(self):
        self.slange.flytte_slange()
        self.skjekke_kollisjon()
        self.skjekke_feil()
        
    def tegne_ting(self):
        self.draw_grass()
        self.frukt.tegne_frukt()
        self.slange.tegne_slange()
        self.draw_score()
        
    def skjekke_kollisjon(self):
        if self.frukt.pos == self.slange.body[0]:
            self.frukt.randomisere()
            self.slange.add_blokk()
    def skjekke_feil(self):
        
        if not (0 <= self.slange.body[0].x < cellenumber) or not (0 <= self.slange.body[0].y < cellenumber):
            self.spillet_ferdig()


        for blokk in self.slange.body[1:]: #blokkene i slangebodyen 
            if blokk == self.slange.body[0]:
                self.spillet_ferdig()


    # def skjekke_feil(self):
    #     if (
    #         self.slange.body[0].x < 0
    #         or self.slange.body[0].x >= cellenumber
    #         or self.slange.body[0].y < 0
    #         or self.slange.body[0].y >= cellenumber
    #     ):
    #         self.spillet_ferdig()

    #     for blokk in self.slange.body[1:]:
    #         if blokk == self.slange.body[0]:
    #             self.spillet_ferdig()


    def spillet_ferdig(self):
        pygame.quit()
        exit()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cellenumber):
            if row % 2 == 0:
                for col in range(cellenumber):
                    if col %2 == 0:
                        grass_rect = pygame.Rect(col * cellestørrelse, row* cellestørrelse, cellestørrelse,cellestørrelse)
                        pygame.draw.rect(vindu,grass_color, grass_rect)
            else: 
                for col in range(cellenumber):
                    if col %2 != 0:
                        grass_rect = pygame.Rect(col * cellestørrelse, row* cellestørrelse, cellestørrelse,cellestørrelse)
                        pygame.draw.rect(vindu,grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.slange.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cellestørrelse * cellenumber - 160)
        score_y = int(cellestørrelse * cellenumber - 100)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        # apple_rect = eple.get_rect(midright = (score_rect.left,score_rect.centery))
        vindu.blit(score_surface, score_rect)

        # vindu.blit(eple,apple_rect)

    
pygame.init()
# HOYDE = 600
# BREDDE = 600


vindu = pygame.display.set_mode((cellenumber* cellestørrelse,cellenumber* cellestørrelse))
pygame.display.set_caption("slange")
# test_font = pygame.font.Font('Arial', 50)
# font_surface = test_font.render(f"Score ; {score}",True, "black")
clock = pygame.time.Clock()
FPS = 60 # makes sure that the game runs at consistent fast at every pc
game_font = pygame.font.Font(None,25)

eple = pygame.image.load('Graphics/apple.png').convert_alpha()

main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit() #video system not initialized ends any types of code that runs (closes the game without error) 
        if event.type == SCREEN_UPDATE:
            main_game.slange.flytte_slange()
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.slange.direction.y != 1:  # Only change to up if not already moving down
                    main_game.slange.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.slange.direction.y != -1:  # Only change to down if not already moving up
                    main_game.slange.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.slange.direction.x != -1:  # Only change to right if not already moving left
                    main_game.slange.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.slange.direction.x != 1:  # Only change to left if not already moving right
                    main_game.slange.direction = Vector2(-1, 0)

            
    vindu.fill((175,215,70))
    main_game.tegne_ting()
    main_game.skjekke_kollisjon()
    main_game.skjekke_feil()
    pygame.display.update()  

    clock.tick(FPS)