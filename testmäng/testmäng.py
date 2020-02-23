import pygame, sys
import time
from timeit import default_timer as timer
pygame.init()
class MenuTaust():
    def __init__(self):
        white = 255, 255, 255
        self.menu = pygame.Surface(size)
        self.rect = pygame.Rect(0,0, 400, 400)
        self.menu.fill(white)
class Buttons:
    def __init__(self,):
        self.up = pygame.K_UP
        self.down =pygame.K_DOWN
        self.left =pygame.K_LEFT
        self.right =pygame.K_RIGHT
        self.x = 110
        self.y = 315


    def yles(self, step = 5):
        pass
class Clock():
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0
class Nurk():
    def _init_(self):
        self.nurk = 0
        self.s = 0
    def imageUp(self, car):
        if self.nurk == 90:
            car.image = pygame.transform.rotate(car.image, 270)
        if self.nurk == 180:
            car.image = pygame.transform.rotate(car.image, 180)
        if self.nurk == 270:
            car.image = pygame.transform.rotate(car.image, 90)
        self.nurk = 0
        self.s = 1
    def imageLeft(self, car):
        if self.nurk == 0:
            car.image = pygame.transform.rotate(car.image, 90)
        if self.nurk == 180:
            car.image = pygame.transform.rotate(car.image, 270)
        if self.nurk == 270:
            car.image = pygame.transform.rotate(car.image, 180)
        self.s = 3
        self.nurk = 90
    def imageRight(self, car):
        if self.nurk == 0:
            car.image = pygame.transform.rotate(car.image, 270)
        if self.nurk == 90:
            car.image = pygame.transform.rotate(car.image, 180)
        if self.nurk == 180:
            car.image = pygame.transform.rotate(car.image, 90)
        self.s = 4
        self.nurk = 270
    def imageDown(self, car):
        if self.nurk == 0:
            car.image = pygame.transform.rotate(car.image, 180)
        if self.nurk == 90:
            car.image = pygame.transform.rotate(car.image, 90)
        if self.nurk == 270:
            car.image = pygame.transform.rotate(car.image, 270)
        self.s = 2
        self.nurk = 180

def Text(text = "a"):
    font = pygame.font.SysFont("Arial Bold", 20)
    tekst =font.render(text, 1, (0, 0, 0))
    return tekst
def StartMenu(screen, menuTaust, start, group):
    hiir = pygame.sprite.Sprite()
    hiir.rect = pygame.Rect((0, 0), (1, 1))
    number = 10
    while number != 0:
        b = pygame.mouse.get_pos #pooleli
        #hiir.rect = pygame.Rect(b, (1, 1))
        a = (55,185) #vana oli 190, 190
        b = (55, 200)
        tekst = Text("Mäng algab " + str(number) + " sekundi pärast...")
        tekst2 = Text("Mängu eesmärk on sõita 3 ringi võimalikult kiiresti.")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(menuTaust.menu, menuTaust.rect)
        screen.blit(tekst2, a)
        screen.blit(tekst, b)
        pygame.display.flip()
        time.sleep(1)
        number -= 1
    
"""if pygame.mouse.get_pressed() == (1, 0, 0):
                #if event.type == pygame.MOUSEMOTION:

                x, y = pygame.mouse.get_pos()
                mouse_pos = (x, y)
                hiir.rect = pygame.Rect((x, y), (1, 1))
                test = pygame.sprite.spritecollide(hiir, group, False, collided=pygame.sprite.collide_rect_ratio(1.0))
                if test:
                    break

                print(mouse_pos)"""

def EndMenu(screen, menuTaust, aeg):
    number = 5
    while number != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        a = (105,185)
        b = (105, 200)
        tekst = Text("Te sõitsite 3 ringi ajaga " + str(aeg) + " sekundiga")
        tekst2 = Text("Te saate uuesti proovida " + str(number) + " sekundi pärast")
        
        screen.blit(menuTaust.menu, menuTaust.rect)
        screen.blit(tekst, a)
        screen.blit(tekst2, b)
        pygame.display.flip()
        time.sleep(1)
        number -= 1
    
#Menu tekstid
start = Text("Start")
start_sprite = pygame.sprite.Sprite()
ssize = (20, 20)
start_sprite.image = start
start_group = pygame.sprite.Group()
start_group.add(start_sprite)
#vajalikud muutujad
nupp = Buttons()
nurk = Nurk()
nurk.nurk = 0
nurk.s = 0
#Screen
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
#rada
rada1 = pygame.image.load("radai.jpg").convert()
rajapunane = pygame.image.load("rajapunane.jpg").convert()
colorkey = rada1.get_at((0, 0))
rajapunane.set_colorkey(colorkey, )
x = 36
y = 33.7

#spriteid ja nende groupid
green = (1, 255, 1)
white = (255, 255, 255)
sprite = pygame.sprite.Sprite()
sprite.rect = pygame.Rect((37,33), (1, 323) )
sprite2 = pygame.sprite.Sprite()
sprite2.rect = pygame.Rect((37,33), (323, 1))
sprite3 = pygame.sprite.Sprite()
sprite3.rect = pygame.Rect((350, 33),(1, 323))
sprite4 = pygame.sprite.Sprite()
sprite4.rect = pygame.Rect((37, 356), (323, 1))
joone_group = pygame.sprite.Group()
joone_group.add(sprite)
joone_group.add(sprite2)
joone_group.add(sprite3)
joone_group.add(sprite4)
finish = pygame.sprite.Sprite()
finish.image = pygame.image.load("finish.jpg").convert()
finish.rect = finish.image.get_rect()
finish.rect.x = 130
finish.rect.y = 301.5
finish_group = pygame.sprite.Group()
finish_group.add(finish)
ruut = pygame.sprite.Sprite()
ruut.rect = pygame.Rect((77, 73),(225, 225))
ruut_group = pygame.sprite.Group()
ruut_group.add(ruut)
#auto
car = pygame.sprite.Sprite()
car.image = pygame.image.load("car3.jpg").convert()
car.rect = car.image.get_rect()
colorkey = car.image.get_at((0,0))
car.image.set_colorkey(colorkey)
car.rect.x = 110
car.rect.y = 315
#taust
taust = pygame.Surface(size)
taustrect = pygame.Rect(0, 0, 400, 400)
taust.fill((240, 240, 23))
menuTaust = MenuTaust()

#rectid
rada1rect = rada1.get_rect()
rajapunanerect = rajapunane.get_rect()
#koordinaadid
step = 5 #Auto kiirus
#värvid
green = 1, 255, 1
screen.fill([1, 255, 1])
#fps
clock = pygame.time.Clock()
#nupud töötavad koguaeg
wait = 100
intervall = 50
pygame.key.set_repeat(wait, intervall)
#tekstid
ring = 0
ringtekst = "ring: " + str(ring) #prindib mängu ringi arvu viisil ring: 0
#time
aeg = 0
#music
background_music = pygame.mixer.music.load("Milco Ross - Electric Yellow.mp3")
background_music = pygame.mixer.music.play(loops = -1, start = 0.0)
#
number = 0
k = 0
while 1 != number:
    if k == 0:
        k = 1
        StartMenu(screen, menuTaust, start_sprite.image, start_group)
        start_time = time.time()
    end_time = time.time()
    aeg = end_time - start_time
    aeg = round(aeg, 1)
    test = pygame.sprite.spritecollide(car, joone_group, False, collided=pygame.sprite.collide_rect_ratio(1.0))
    test2 = pygame.sprite.spritecollide(car, finish_group, False, collided=pygame.sprite.collide_rect_ratio(1.0))
    test3 = pygame.sprite.spritecollide(car, ruut_group, False, collided=pygame.sprite.collide_rect_ratio(1.0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if  test:
            car.rect.x = 110
            car.rect.y = 315
        if test2:
            if olek != 1:
                ring +=1
                ringtekst = "ring: " + str(ring)
                #start_time = time.time() siit edasi saab teha ringiaja lugejat
            olek = 1
        if not test2:
            olek = 0
        if test3:
            step = 3
        if ring == 3:
            EndMenu(screen, menuTaust, aeg)
            ring = 1
            car.rect.x = 110
            car.rect.y = 315
            start_time = time.time()
        if event.type == pygame.KEYDOWN:
                if event.key == nupp.up:
                    if nurk.s != 1:
                        nurk.imageUp(car)
                    if step != 20:
                        step += 0.5

                    car.rect.y -= step
                if event.key == nupp.down:
                    if nurk.s != 2:
                        nurk.imageDown(car)
                    if step != 20:
                        step += 0.5
                    car.rect.y += step
                if event.key == nupp.left:
                    if nurk.s != 3:
                        nurk.imageLeft(car)
                    if step != 20:
                        step += 0.5

                    car.rect.x -= step
                if event.key == nupp.right:
                    if nurk.s != 4:
                        nurk.imageRight(car)
                    if step != 20:
                        step += 0.5
                    car.rect.x += step

        if event.type == pygame.KEYUP:
            if event.key == nupp.up:
                """while step != 5:
                    step -= 1
                    car.rect.y -= step"""
                step = 5
            if event.key == nupp.down:
                """while step != 5:
                    step -= 1
                    car.rect.y += step"""
                step = 5
            if event.key == nupp.left:
                """while step != 5:
                    step -= 1
                    car.rect.x -= step"""
                step = 5
            if event.key == nupp.right:
                """while step != 5:
                    step -= 1
                    car.rect.x += step"""
                step = 5
    a = Text(ringtekst)
    b = Text(str(aeg))
    screen.blit(taust ,taustrect)
    screen.blit(a, (2, 5))
    screen.blit(b, (2,27))
    #screen.blit(rajapunane, rajapunanerect)
    screen.blit(rada1, (x,y))
    #screen.blit(rajapunane, rajapunanerect)
    screen.blit(finish.image, (finish.rect.x, finish.rect.y))
    screen.blit(car.image, (car.rect.x, car.rect.y ))

    pygame.display.flip()
    pygame.time.delay(1)
    #print(x, y)
    clock.tick(40)
