import pygame
import math
import sys

# Initialize Pygame
pygame.init()
00

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Spur Gears")

# Set the default font and font size
font = pygame.font.Font(None, 24)

# Set the center of the window
center1 = (window_size[0] / 2, window_size[1] / 2)
center2 = (window_size[0]/ 4 , window_size[1]/ 4 )

# Set the radius of the gears
radius1 = 100
radius2 = 50

# Set the default number of teeth on the gears
num_teeth1 = 10
num_teeth2 = 20

# Set the rotation speed of the gears (in degrees per frame)
rotation_speed = 1

# Set the default gear ratio
gear_ratio = num_teeth1 / num_teeth2

# Set the default angle of rotation for the gears
angle1 = 0
angle2 = 0

# Set the default color of the gears
color = (0, 0, 0)

# Set the default running state of the game
running = True

# Main game loop
while running:
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Update the angle of rotation for the gears
    angle1 += rotation_speed
    angle2 += rotation_speed * gear_ratio

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the first gear
    for i in range(num_teeth1):
        tooth_angle = 2 * math.pi * i / num_teeth1 + math.radians(angle1)
        x = center1[0] + radius1 * math.cos(tooth_angle)
        y = center1[1] + radius1 * math.sin(tooth_angle)
        point_list = [(center1[0], center1[1]), (x, y)]
        pygame.draw.lines(screen, color, True, point_list, 3)

    # Draw the second gear
    for i in range(num_teeth2):
        tooth_angle = 2 * math.pi * i / num_teeth2 + math.radians(angle2)
        x = center2[0] + radius2 * math.cos(tooth_angle)
        y = center2[1] + radius2 * math.sin(tooth_angle)
        point_list = [(center2[0], center2[1]), (x, y)]
        pygame.draw.lines(screen, color, True, point_list, 3)

        # Check for keypresses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            num_teeth1 += 1
            gear_ratio = num_teeth1 / num_teeth2
        if keys[pygame.K_DOWN]:
            num_teeth1 -= 1
            gear_ratio = num_teeth1 / num_teeth2


        # Display the gear ratio
        text = font.render("Gear Ratio: {:.2f}".format(gear_ratio), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        # Update the display
        pygame.display.flip()

    # Quit Pygame

    