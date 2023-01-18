import pygame
import button

# Initialize Pygame
pygame.init()

# Set the window size
w = 800
h = 600
window_size = (w, h)

clock = pygame.time.Clock()  #fps değeri

# Gearwheel for scale
s1 = 200
s2 = 160   #scale değerleri
s3 = 120
s4 = 80

angle1=0.0
angle2=0.0  #çarkların dönme açısı
angle3=0.0
angle4=0.0

speed1=0.0      #çarkların hızlarını aldığımız değişkenler
speed2=0.0
speed3=0.0
speed4=0.0
pi=3  # formül için kullanılan

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Spinning GearWheels")

# Set the radius of the circles
radius1 = 100
radius2 = 80
radius3 = 60   #yarıçaplar
radius4 = 40
radius5 = 20


button2_img = pygame.image.load('button2.png').convert_alpha()
button3_img = pygame.image.load('button3.png').convert_alpha()  #buton resimleri yükleme
button4_img = pygame.image.load('button4.png').convert_alpha()
backbutton_img = pygame.image.load('backbutton.png').convert_alpha()

button2 = button.Button(w//2 - 200, 100, button2_img, 0.5)
button3 = button.Button(w//2 - 200, 250, button3_img, 0.5)    #butonların konumlarını ve ölçeklendirilmesini ayarlama
button4 = button.Button(w//2 - 200, 400, button4_img, 0.5)
backbutton = button.Button(w//2 - 200, 475, backbutton_img, 0.5)

main_backgroundimage = pygame.image.load("main_background.png").convert()
wheels_backgroundimage = pygame.image.load("wheel_background.png").convert()

# Run the game loop
mainMenu = True
gearWheels2 = False
gearWheels3 = False    #menüler arası geçiş için yazılan kontrol
gearWheels4 = False
backMenu = False

pygame.font.init()         #text girişi yapılması için yazılan metod
my_font = pygame.font.SysFont('Aerial', 30)  #font-family ve font-size
maimmenu_font = pygame.font.SysFont('Aerial', 40)

while mainMenu:
    screen.blit(main_backgroundimage, [0, 0])
    if button2.draw(screen):
        mainMenu = False        #2 li çark istendiğinde anamenü false olup 2li çark menüsü true oluyor
        gearWheels2 = True      #ve diğer while döngüsü aktif olmuş oluyor

    if button3.draw(screen):
        mainMenu = False
        gearWheels3 = True

    if button4.draw(screen):
        mainMenu = False
        gearWheels4 = True
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mainMenu = False

    mainmenu_text = my_font.render('-II- ÇARK DÖNDÜR', True, (0, 0, 0))
    mainmenu_text2 = my_font.render('-III- ÇARK DÖNDÜR', True, (0, 0, 0))
    mainmenu_text3 = my_font.render('-IV- ÇARK DÖNDÜR', True, (0, 0, 0))
    screen.blit(mainmenu_text, (310, 135))
    screen.blit(mainmenu_text2, (310, 285))
    screen.blit(mainmenu_text3, (310, 435))

    pygame.display.update()
    # Clear the screen
    screen.fill((255, 255, 255))


while gearWheels2:
    screen.blit(wheels_backgroundimage, [0, 0])
    pygame.display.set_caption("Double Gearwheel Spin")

    if backbutton.draw(screen):
        gearWheels3 = True
        gearWheels2 = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gearWheels2 = False



    clock.tick(60)

    gearwheel1 = pygame.image.load("gear1.png")
    rect1 = gearwheel1.get_rect()         #stabil şekilde dönmesi için rect metodu
    gearwheel1 = pygame.transform.scale(gearwheel1, (s1, s1)) #döndürme metodu
    speed1 = 1.0
    angle1 += speed1    #açısal dönme
    rect1.center = w // 2, h // 2
    rotated_gearwheel1 = pygame.transform.rotate(gearwheel1, angle1)
    rect1 = rotated_gearwheel1.get_rect()
    pos_r1 = (((s1 + 300 - rect1.width) / 2), ((s1 + 300 - rect1.height) / 2))

    screen.blit(rotated_gearwheel1, pos_r1)

    gearwheel2 = pygame.image.load("gear2.png")
    rect2 = gearwheel2.get_rect()
    gearwheel2 = pygame.transform.scale(gearwheel2, (s2, s2))
    speed2 = (radius1* 2 * pi)/(radius2* 2 * pi)
    angle2 -= speed2
    rect2.center = w // 2, h // 2
    rotated_gearwheel2 = pygame.transform.rotate(gearwheel2, angle2)
    rect2 = rotated_gearwheel2.get_rect()
    pos_r2 = (((s2 + 535 - rect2.width) / 2), ((s2 + 535 - rect2.height) / 2))
    screen.blit(rotated_gearwheel2, pos_r2)


    wheels1_text1 = my_font.render('1', True, (0, 0, 0))
    wheels2_text1 = my_font.render('2', True, (0, 0, 0))
    backbuttontext1 = my_font.render('-III- ÇARK DÖNDÜR', True, (0, 0, 0))
    wheels1_textinf1 = my_font.render('1. Çarkın Dönme Hızı:'+str(speed1*10), True, (0, 0, 0))
    wheels2_textinf1 = my_font.render('2. Çarkın Dönme Hızı:'+str(speed2*10), True, (0, 0, 0))
    screen.blit(wheels1_text1, (165, 135))         #ekranda text i gösterme
    screen.blit(wheels2_text1, (375, 245))            
    screen.blit(wheels1_textinf1, (450, 135))
    screen.blit(wheels2_textinf1, (450, 185))    #textinformation
    screen.blit(backbuttontext1, (310, 510))
    pygame.display.update()

while gearWheels3:
    pygame.display.set_caption("Triple Gearwheel Spin")
    screen.blit(wheels_backgroundimage, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gearWheels3 = False

    if backbutton.draw(screen):
        gearWheels4 = True
        gearWheels3 = False

    clock.tick(60)
    #gear1 dönme
    gearwheel1 = pygame.image.load("gear1.png")
    rect1 = gearwheel1.get_rect()
    gearwheel1 = pygame.transform.scale(gearwheel1, (s1, s1))
    speed1 = 1.0
    angle1 += speed1
    rect1.center = w // 2, h // 2
    rotated_gearwheel1 = pygame.transform.rotate(gearwheel1, angle1)
    rect1 = rotated_gearwheel1.get_rect()
    pos_r1 = (((s1 + 300 - rect1.width) / 2), ((s1 + 300 - rect1.height) / 2))
    screen.blit(rotated_gearwheel1, pos_r1)
    # gear2 dönme
    gearwheel2 = pygame.image.load("gear2.png")
    rect2 = gearwheel2.get_rect()
    gearwheel2 = pygame.transform.scale(gearwheel2, (s2, s2))
    speed2 = (radius1 * 2 * pi) / (radius2 * 2 * pi)
    angle2 -= speed2
    rect2.center = w // 2, h // 2
    rotated_gearwheel2 = pygame.transform.rotate(gearwheel2, angle2)
    rect2 = rotated_gearwheel2.get_rect()
    pos_r2 = (((s2 + 535 - rect2.width) / 2), ((s2 + 535 - rect2.height) / 2))
    screen.blit(rotated_gearwheel2, pos_r2)
    # gear3 dönme
    gearwheel3 = pygame.image.load("gear3.png")
    rect3 = gearwheel3.get_rect()
    gearwheel3 = pygame.transform.scale(gearwheel3, (s3, s3))
    speed3 = (radius2 * 2 * pi)/(radius3 * 2 * pi)
    angle3 -= speed3
    rect3.center = w // 2, h // 2
    rotated_gearwheel3 = pygame.transform.rotate(gearwheel3, angle3)
    rect3 = rotated_gearwheel3.get_rect()
    pos_r3 = (((s3 + 205 - rect3.width) / 2), ((s3 + 205 - rect3.height) / 2))
    screen.blit(rotated_gearwheel3, pos_r3)

    wheels1_text2 = my_font.render('1', True, (0, 0, 0))
    wheels2_text2 = my_font.render('2', True, (0, 0, 0))
    wheels3_text2 = my_font.render('3', True, (0, 0, 0))
    backbuttontext2 = my_font.render('-IV- ÇARK DÖNDÜR', True, (0, 0, 0))
    wheels1_textinf2 = my_font.render('1. Çarkın Dönme Hızı:' + str(speed1*10), True, (0, 0, 0))
    wheels2_textinf2 = my_font.render('2. Çarkın Dönme Hızı:' + str(speed2*10), True, (0, 0, 0))
    wheels3_textinf2 = my_font.render('3. Çarkın Dönme Hızı:' + str(round(speed3 * 10, 1)), True, (0, 0, 0))
    screen.blit(wheels1_text2, (260, 135))
    screen.blit(wheels2_text2, (375, 245))
    screen.blit(wheels3_text2, (150, 90))
    screen.blit(wheels1_textinf2, (450, 135))
    screen.blit(wheels2_textinf2, (450, 185))
    screen.blit(wheels3_textinf2, (450, 235))
    screen.blit(backbuttontext2, (310, 510))

    pygame.display.update()

while gearWheels4:
    pygame.display.set_caption("Four Gearwheel Spin")
    screen.blit(wheels_backgroundimage, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gearWheels4 = False

    if backbutton.draw(screen):
        gearWheels2 = True
        gearWheels4 = False

    clock.tick(60)
    # gear1 dönme
    gearwheel1 = pygame.image.load("gear1.png")
    rect1 = gearwheel1.get_rect()
    gearwheel1 = pygame.transform.scale(gearwheel1, (s1, s1))
    speed1 = 1.0
    angle1 += speed1
    rect1.center = w // 2, h // 2
    rotated_gearwheel1 = pygame.transform.rotate(gearwheel1, angle1)
    rect1 = rotated_gearwheel1.get_rect()
    pos_r1 = (((s1 + 300 - rect1.width) / 2), ((s1 + 300 - rect1.height) / 2))
    screen.blit(rotated_gearwheel1, pos_r1)
    # gear2 dönme
    gearwheel2 = pygame.image.load("gear2.png")
    rect2 = gearwheel2.get_rect()
    gearwheel2 = pygame.transform.scale(gearwheel2, (s2, s2))
    speed2 = (radius1 * 2 * pi) / (radius2 * 2 * pi)
    angle2 -= speed2
    rect2.center = w // 2, h // 2
    rotated_gearwheel2 = pygame.transform.rotate(gearwheel2, angle2)
    rect2 = rotated_gearwheel2.get_rect()
    pos_r2 = (((s2 + 535 - rect2.width) / 2), ((s2 + 535 - rect2.height) / 2))
    screen.blit(rotated_gearwheel2, pos_r2)
    # gear3 dönme
    gearwheel3 = pygame.image.load("gear3.png")
    rect3 = gearwheel3.get_rect()
    gearwheel3 = pygame.transform.scale(gearwheel3, (s3, s3))
    speed3 = (radius2 * 2 * pi) / (radius3 * 2 * pi)
    angle3 -= speed3
    rect3.center = w // 2, h // 2
    rotated_gearwheel3 = pygame.transform.rotate(gearwheel3, angle3)
    rect3 = rotated_gearwheel3.get_rect()
    pos_r3 = (((s3 + 205 - rect3.width) / 2), ((s3 + 205 - rect3.height) / 2))
    screen.blit(rotated_gearwheel3, pos_r3)
    # gear4 dönme
    gearwheel4 = pygame.image.load("gear4.png")
    rect4 = gearwheel4.get_rect()
    gearwheel4 = pygame.transform.scale(gearwheel4, (s4, s4))
    speed4 = (radius3 * 2 * pi) / (radius4 * 2 * pi)
    angle4 += speed4
    rect4.center = w // 2, h // 2
    rotated_gearwheel4 = pygame.transform.rotate(gearwheel4, angle4)
    rect4 = rotated_gearwheel4.get_rect()
    pos_r4 = (((s4 + 725 - rect4.width) / 2), ((s4 + 460 - rect4.height) / 2))
    screen.blit(rotated_gearwheel4, pos_r4)

    wheels1_text3 = my_font.render('1', True, (0, 0, 0))
    wheels2_text3 = my_font.render('2', True, (0, 0, 0))
    wheels3_text3 = my_font.render('3', True, (0, 0, 0))
    wheels4_text3 = my_font.render('4', True, (0, 0, 0))
    backbuttontext3 = my_font.render('SİMÜLASYONDAN ÇIK', True, (0, 0, 0))
    wheels1_textinf3 = my_font.render('1. Çarkın Dönme Hızı:' + str(speed1 * 10), True, (0, 0, 0))
    wheels2_textinf3 = my_font.render('2. Çarkın Dönme Hızı:' + str(speed2 * 10), True, (0, 0, 0))
    wheels3_textinf3 = my_font.render('3. Çarkın Dönme Hızı:' + str(round(speed3 * 10, 1)), True, (0, 0, 0))
    wheels4_textinf3 = my_font.render('4. Çarkın Dönme Hızı:' + str(round(speed4 * 10, 1)), True, (0, 0, 0))
    screen.blit(wheels1_text3, (260, 135))
    screen.blit(wheels2_text3, (345, 425))
    screen.blit(wheels3_text3, (150, 90))
    screen.blit(wheels4_text3, (400, 210))
    screen.blit(wheels1_textinf3, (450, 100))
    screen.blit(wheels2_textinf3, (450, 150))
    screen.blit(wheels3_textinf3, (450, 200))
    screen.blit(wheels4_textinf3, (450, 250))
    screen.blit(backbuttontext3, (310, 510))

    pygame.display.update()