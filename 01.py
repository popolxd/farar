import pygame
from constants import *
from classes import *

pygame.display.set_icon(icon)
pygame.display.set_caption('Poklad z minulosti!')
pygame.mouse.set_visible(False)

run = True

def draw_window(click, mouse):
    win.fill((0, 0, 0))

    room_manager.draw(click, mouse)

    pygame.display.update()

def move(click, mouse):
    room_manager.interact(click, mouse)

while run:
    clock.tick(fps)
    click = False
    keys_pressed = False

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

            if room_manager.return_current_interaction() == 13 and pygame.Rect.collidepoint(pygame.Rect(width * 0.59, height * 0.54, width * 0.255, height * 0.2), mouse):
                run = False

        if event.type == pygame.KEYDOWN:
            run = False

    draw_window(click, mouse)
    move(click, mouse)

pygame.quit()