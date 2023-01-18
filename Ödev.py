import pygame

# Pygame Çalıştır Komutu
pygame.init()

# Pencere Boyutu Ayarlama
window_size = (800, 600)

# Pencere Oluşturma
screen = pygame.display.set_mode(window_size)

# Pencere Başlığı Oluşturma
pygame.display.set_caption("Drag and Drop Circles")

# Çark Yarıçaplarını Ayarlama
radius1 = 20
radius2 = 40
radius3 = 60
radius4 = 80
radius5 = 100

# Çark Başlangıç konumlarını Ayarlama
pos1 = (radius1, window_size[1] - radius1)
pos2 = (2 * radius1 + radius2, window_size[1] - radius2)
pos3 = (3 * radius1 + 2 * radius2 + radius3, window_size[1] - radius3)
pos4 = (4 * radius1 + 2 * radius2 + 2 * radius3 + radius4, window_size[1] - radius4)
pos5 = (5 * radius1 + 2 * radius2 + 2 * radius3 + 2 * radius4 + radius5, window_size[1] - radius5)

# Çark Renklerini Ayarlama
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 255, 0)
color5 = (0, 255, 255)

# Dairelerin sürükleme durumunu ayarlama
drag1 = False
drag2 = False
drag3 = False
drag4 = False
drag5 = False

#Oyun Döngüsü Çalıştırma
running = True
while running:
    # Olayları İşleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Farenin herhangi bir dairenin üzerinde olup olmadığını kontrol etme
            if (pos1[0] - pygame.mouse.get_pos()[0]) * 2 + (pos1[1] - pygame.mouse.get_pos()[1]) * 2 <= radius1 ** 2:
                drag1 = True
            elif (pos2[0] - pygame.mouse.get_pos()[0]) ** 2 + (
                    pos2[1] - pygame.mouse.get_pos()[1]) * 2 <= radius2 * 2:
                drag2 = True
            elif (pos3[0] - pygame.mouse.get_pos()[0]) ** 2 + (
                    pos3[1] - pygame.mouse.get_pos()[1]) * 2 <= radius3 * 2:
                drag3 = True
            elif (pos4[0] - pygame.mouse.get_pos()[0]) ** 2 + (
                    pos4[1] - pygame.mouse.get_pos()[1]) * 2 <= radius4 * 2:
                drag4 = True
            elif (pos5[0] - pygame.mouse.get_pos()[0]) ** 2 + (
                    pos5[1] - pygame.mouse.get_pos()[1]) * 2 <= radius5 * 2:
                drag5 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Sürükleme durumunu sıfırlama
            drag1 = False
            drag2 = False
            drag3 = False
            drag4 = False
            drag5 = False

        # Sürükleniyorlarsa dairelerin konumunu güncelleme
        if drag1:
            new_pos = pygame.mouse.get_pos()
            dist2 = (new_pos[0] - pos2[0]) * 2 + (new_pos[1] - pos2[1]) * 2
            dist3 = (new_pos[0] - pos3[0]) * 2 + (new_pos[1] - pos3[1]) * 2
            dist4 = (new_pos[0] - pos4[0]) * 2 + (new_pos[1] - pos4[1]) * 2
            dist5 = (new_pos[0] - pos5[0]) * 2 + (new_pos[1] - pos5[1]) * 2
            if dist2 > (radius1 + radius2) * 2 and dist3 > (radius1 + radius3) * 2 and dist4 > (
                    radius1 + radius4) * 2 and dist5 > (radius1 + radius5) * 2:
                pos1 = new_pos
        if drag2:
            new_pos = pygame.mouse.get_pos()
            dist1 = (new_pos[0] - pos1[0]) * 2 + (new_pos[1] - pos1[1]) * 2
            dist3 = (new_pos[0] - pos3[0]) * 2 + (new_pos[1] - pos3[1]) * 2
            dist4 = (new_pos[0] - pos4[0]) * 2 + (new_pos[1] - pos4[1]) * 2
            dist5 = (new_pos[0] - pos5[0]) * 2 + (new_pos[1] - pos5[1]) * 2
            if dist1 > (radius1 + radius2) * 2 and dist3 > (radius2 + radius3) * 2 and dist4 > (
                    radius2 + radius4) * 2 and dist5 > (radius2 + radius5) * 2:
                pos2 = new_pos
        if drag3:
            new_pos = pygame.mouse.get_pos()
            dist1 = (new_pos[0] - pos1[0]) * 2 + (new_pos[1] - pos1[1]) * 2
            dist2 = (new_pos[0] - pos2[0]) * 2 + (new_pos[1] - pos2[1]) * 2
            dist4 = (new_pos[0] - pos4[0]) * 2 + (new_pos[1] - pos4[1]) * 2
            dist5 = (new_pos[0] - pos5[0]) * 2 + (new_pos[1] - pos5[1]) * 2
            if dist1 > (radius1 + radius3) * 2 and dist2 > (radius2 + radius3) * 2 and dist4 > (
                    radius3 + radius4) * 2 and dist5 > (radius3 + radius5) * 2:
                pos3 = new_pos
        if drag4:
            new_pos = pygame.mouse.get_pos()
            dist1 = (new_pos[0] - pos1[0]) * 2 + (new_pos[1] - pos1[1]) * 2
            dist2 = (new_pos[0] - pos2[0]) * 2 + (new_pos[1] - pos2[1]) * 2
            dist3 = (new_pos[0] - pos3[0]) * 2 + (new_pos[1] - pos3[1]) * 2
            dist5 = (new_pos[0] - pos5[0]) * 2 + (new_pos[1] - pos5[1]) * 2
            if dist1 > (radius1 + radius4) * 2 and dist2 > (radius2 + radius4) * 2 and dist3 > (
                    radius3 + radius4) * 2 and dist5 > (radius4 + radius5) * 2:
                pos4 = new_pos
        if drag5:
            new_pos = pygame.mouse.get_pos()
            dist1 = (new_pos[0] - pos1[0]) * 2 + (new_pos[1] - pos1[1]) * 2
            dist2 = (new_pos[0] - pos2[0]) * 2 + (new_pos[1] - pos2[1]) * 2
            dist4 = (new_pos[0] - pos4[0]) * 2 + (new_pos[1] - pos4[1]) * 2
            dist3 = (new_pos[0] - pos3[0]) * 2 + (new_pos[1] - pos3[1]) * 2
            if dist1 > (radius1 + radius5) * 2 and dist2 > (radius2 + radius5) * 2 and dist4 > (
                    radius5 + radius4) * 2 and dist3 > (radius3 + radius5) * 2:
                pos5 = new_pos

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circles
    pygame.draw.circle(screen, color1, pos1, radius1)
    pygame.draw.circle(screen, color2, pos2, radius2)
    pygame.draw.circle(screen, color3, pos3, radius3)
    pygame.draw.circle(screen, color4, pos4, radius4)
    pygame.draw.circle(screen, color5, pos5, radius5)

    # Update the display
    pygame.display.flip()