import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Drag and Drop Circles")

# Load the images
gear1_image = pygame.image.load("gear1.png")
gear2_image = pygame.image.load("gear2.png")
gear3_image = pygame.image.load("gear3.png")
gear4_image = pygame.image.load("gear4.png")
gear5_image = pygame.image.load("gear5.png")

# Set the radius of the circles
radius1 = 20
radius2 = 40
radius3 = 60
radius4 = 80
radius5 = 100

# Scale the images
gear1_image = pygame.transform.scale(gear1_image, (2 * radius1, 2 * radius1))
gear2_image = pygame.transform.scale(gear2_image, (2 * radius2, 2 * radius2))
gear3_image = pygame.transform.scale(gear3_image, (2 * radius3, 2 * radius3))
gear4_image = pygame.transform.scale(gear4_image, (2 * radius4, 2 * radius4))
gear5_image = pygame.transform.scale(gear5_image, (2 * radius5, 2 * radius5))

# Set the initial positions of the circles
pos1 = (radius1, window_size[1] - radius1)
pos2 = (2 * radius1 + radius2, window_size[1] - radius2)
pos3 = (3 * radius1 + 2 * radius2 + radius3, window_size[1] - radius3)
pos4 = (4 * radius1 + 2 * radius2 + 2 * radius3 + radius4, window_size[1] - radius4)
pos5 = (5 * radius1 + 2 * radius2 + 2 * radius3 + 2 * radius4 + radius5, window_size[1] - radius5)

# Set the initial positions of the images
gear1_rect = gear1_image.get_rect()
gear1_rect.center = pos1
gear2_rect = gear2_image.get_rect()
gear2_rect.center = pos2
gear3_rect = gear3_image.get_rect()
gear3_rect.center = pos3
gear4_rect = gear4_image.get_rect()
gear4_rect.center = pos4
gear5_rect = gear5_image.get_rect()
gear5_rect.center = pos5

# Set the colors of the circles
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 255, 0)
color5 = (0, 255, 255)

# Set the drag status of the circles
drag1 = False
drag2 = False
drag3 = False
drag4 = False
drag5 = False

# Create a blank surface for each gear
gear1_border = pygame.Surface((2 * radius1, 2 * radius1))
gear2_border = pygame.Surface((2 * radius2, 2 * radius2))
gear3_border = pygame.Surface((2 * radius3, 2 * radius3))
gear4_border = pygame.Surface((2 * radius4, 2 * radius4))
gear5_border = pygame.Surface((2 * radius5, 2 * radius5))

# Set the clipping area of each surface to a circular shape
gear1_border.set_clip(pygame.draw.circle(gear1_border, (0, 0, 0), (radius1, radius1), radius1))
gear2_border.set_clip(pygame.draw.circle(gear2_border, (0, 0, 0), (radius2, radius2), radius2))
gear3_border.set_clip(pygame.draw.circle(gear3_border, (0, 0, 0), (radius3, radius3), radius3))
gear4_border.set_clip(pygame.draw.circle(gear4_border, (0, 0, 0), (radius4, radius4), radius4))
gear5_border.set_clip(pygame.draw.circle(gear5_border, (0, 0, 0), (radius5, radius5), radius5))

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Set the collision status of the gears
            collision1 = False
            collision2 = False
            collision3 = False
            collision4 = False
            collision5 = False
            # Check if the mouse is over any of the images
            if gear1_rect.collidepoint(event.pos):
                drag1 = True
            elif gear2_rect.collidepoint(event.pos):
                drag2 = True
            elif gear3_rect.collidepoint(event.pos):
                drag3 = True
            elif gear4_rect.collidepoint(event.pos):
                drag4 = True
            elif gear5_rect.collidepoint(event.pos):
                drag5 = True
            # Check if the borders of the gears are colliding
            if gear1_border.get_rect(center=gear1_rect.center).colliderect(
                    gear2_border.get_rect(center=gear2_rect.center)):
                collision1 = True
                collision2 = True
            if gear1_border.get_rect(center=gear1_rect.center).colliderect(
                    gear3_border.get_rect(center=gear3_rect.center)):
                collision1 = True
                collision3 = True
            if gear1_border.get_rect(center=gear1_rect.center).colliderect(
                    gear4_border.get_rect(center=gear4_rect.center)):
                collision1 = True
                collision4 = True
            if gear1_border.get_rect(center=gear1_rect.center).colliderect(
                    gear5_border.get_rect(center=gear5_rect.center)):
                collision1 = True
                collision5 = True
            if gear2_border.get_rect(center=gear2_rect.center).colliderect(
                    gear3_border.get_rect(center=gear3_rect.center)):
                collision2 = True
                collision3 = True
            if gear2_border.get_rect(center=gear2_rect.center).colliderect(
                    gear4_border.get_rect(center=gear4_rect.center)):
                collision2 = True
                collision4 = True
            if gear2_border.get_rect(center=gear2_rect.center).colliderect(
                    gear5_border.get_rect(center=gear5_rect.center)):
                collision2 = True
                collision5 = True
            if gear3_border.get_rect(center=gear3_rect.center).colliderect(
                    gear4_border.get_rect(center=gear4_rect.center)):
                collision3 = True
                collision4 = True
            if gear3_border.get_rect(center=gear3_rect.center).colliderect(
                    gear5_border.get_rect(center=gear5_rect.center)):
                collision3 = True
                collision5 = True
            if gear4_border.get_rect(center=gear4_rect.center).colliderect(
                    gear5_border.get_rect(center=gear5_rect.center)):
                collision4 = True
                collision5 = True
            # Update the positions of the gears if they are not colliding
            if not collision1:
                gear1_rect.center = event.pos
            if not collision2:
                gear2_rect.center = event.pos
            if not collision3:
                gear3_rect.center = event.pos
            if not collision4:
                gear4_rect.center = event.pos
            if not collision5:
                gear5_rect.center = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            # Reset the drag status
            drag1 = False
            drag2 = False
            drag3 = False
            drag4 = False
            drag5 = False



        elif event.type == pygame.MOUSEMOTION:
             # Update the positions of the images
             if drag1:
                 gear1_rect.center = event.pos
             elif drag2:
                 gear2_rect.center = event.pos
             elif drag3:
                 gear3_rect.center = event.pos
             elif drag4:
                 gear4_rect.center = event.pos
             elif drag5:
                 gear5_rect.center = event.pos
        # Update the position of the circles if they are being dragged
        if drag1:
             new_pos = pygame.mouse.get_pos()
             dist2 = (new_pos[0] - pos2[0]) ** 2 + (new_pos[1] - pos2[1]) ** 2
             dist3 = (new_pos[0] - pos3[0]) ** 2 + (new_pos[1] - pos3[1]) ** 2
             dist4 = (new_pos[0] - pos4[0]) ** 2 + (new_pos[1] - pos4[1]) ** 2
             dist5 = (new_pos[0] - pos5[0]) ** 2 + (new_pos[1] - pos5[1]) ** 2
             if dist2 > (radius1 + radius2) ** 2 and dist3 > (radius1 + radius3) ** 2 and dist4 > (
                     radius1 + radius4) ** 2 and dist5 > (radius1 + radius5) ** 2:
                 gear1_rect.center = new_pos
        if drag2:
             new_pos = pygame.mouse.get_pos()
             dist1 = (new_pos[0] - pos1[0]) ** 2 + (new_pos[1] - pos1[1]) ** 2
             dist3 = (new_pos[0] - pos3[0]) ** 2 + (new_pos[1] - pos3[1]) ** 2
             dist4 = (new_pos[0] - pos4[0]) ** 2 + (new_pos[1] - pos4[1]) ** 2
             dist5 = (new_pos[0] - pos5[0]) ** 2 + (new_pos[1] - pos5[1]) ** 2
             if dist1 > (radius1 + radius2) ** 2 and dist3 > (radius2 + radius3) ** 2 and dist4 > (
                     radius2 + radius4) ** 2 and dist5 > (radius2 + radius5) ** 2:
                 gear2_rect.center = new_pos
        if drag3:
             new_pos = pygame.mouse.get_pos()
             dist1 = (new_pos[0] - pos1[0]) ** 2 + (new_pos[1] - pos1[1]) ** 2
             dist2 = (new_pos[0] - pos2[0]) ** 2 + (new_pos[1] - pos2[1]) ** 2
             dist4 = (new_pos[0] - pos4[0]) ** 2 + (new_pos[1] - pos4[1]) ** 2
             dist5 = (new_pos[0] - pos5[0]) ** 2 + (new_pos[1] - pos5[1]) ** 2
             if dist1 > (radius1 + radius3) ** 2 and dist2 > (radius2 + radius3) ** 2 and dist4 > (
                     radius3 + radius4) ** 2 and dist5 > (radius3 + radius5) ** 2:
                 gear3_rect.center = new_pos
        if drag4:
             new_pos = pygame.mouse.get_pos()
             dist1 = (new_pos[0] - pos1[0]) ** 2 + (new_pos[1] - pos1[1]) ** 2
             dist2 = (new_pos[0] - pos2[0]) ** 2 + (new_pos[1] - pos2[1]) ** 2
             dist3 = (new_pos[0] - pos3[0]) ** 2 + (new_pos[1] - pos3[1]) ** 2
             dist5 = (new_pos[0] - pos5[0]) ** 2 + (new_pos[1] - pos5[1]) ** 2
             if dist1 > (radius1 + radius4) ** 2 and dist2 > (radius2 + radius4) ** 2 and dist3 > (
                     radius3 + radius4) ** 2 and dist5 > (radius4 + radius5) ** 2:
                 gear4_rect.center = new_pos
        if drag5:
             new_pos = pygame.mouse.get_pos()
             dist1 = (new_pos[0] - pos1[0]) ** 2 + (new_pos[1] - pos1[1]) ** 2
             dist2 = (new_pos[0] - pos2[0]) ** 2 + (new_pos[1] - pos2[1]) ** 2
             dist4 = (new_pos[0] - pos4[0]) ** 2 + (new_pos[1] - pos4[1]) ** 2
             dist3 = (new_pos[0] - pos3[0]) ** 2 + (new_pos[1] - pos3[1]) ** 2
             if dist1 > (radius1 + radius5) ** 2 and dist2 > (radius2 + radius5) ** 2 and dist4 > (
                     radius5 + radius4) ** 2 and dist3 > (radius3 + radius5) ** 2:
                 gear5_rect.center = new_pos

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the images on the screen
    screen.blit(gear1_image, gear1_rect)
    screen.blit(gear2_image, gear2_rect)
    screen.blit(gear3_image, gear3_rect)
    screen.blit(gear4_image, gear4_rect)
    screen.blit(gear5_image, gear5_rect)

    # Update the display
    pygame.display.flip()

    