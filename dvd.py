import pygame
import random

pygame.init()

x = 200
y = 200
window_width = 1600
window_height = 900
width = 300
height = 150
velocity_x = 4
velocity_y = 4


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("DVD")

icon = pygame.image.load('cassette.png')
pygame.display.set_icon(icon)

logo = pygame.image.load('dvd-logo.png').convert_alpha()
logo = pygame.transform.scale(logo, (width, height))

color = (0, 0, 255)
run = True
while run:
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if x + width > window_width or x < 0:
        velocity_x = -velocity_x
        color = random_color
    if y + height > window_height or y < 0:
        velocity_y = -velocity_y
        color = random_color
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    x += velocity_x
    y += velocity_y


    window.fill((0, 0, 0))
    pygame.draw.rect(window, color, (x, y, width, height))
    window.blit(logo, (x, y))
    pygame.display.update()


pygame.quit()