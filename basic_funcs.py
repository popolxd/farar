import pygame
from constants import *
import math

def get_image(tilesprite, x, y, image_width, image_height):
    rect = pygame.Rect(x * image_width, y * image_height, image_width, image_height)
    image = pygame.Surface(rect.size, pygame.SRCALPHA)
    image.blit(tilesprite, (0,0), rect)
    return pygame.transform.scale(image, (width * 0.1, width * 0.1))

def is_valid_move(new_pos, old_pos, current_board):
    if current_board[new_pos[1]][new_pos[0]] != 0:
        return False
    
    if (abs(new_pos[0] - old_pos[0]) == 1 and new_pos[1] == old_pos[1]) or (abs(new_pos[1] - old_pos[1]) == 1 and new_pos[0] == old_pos[0]):
        return True
    
    return False

def draw_light(precision, reach, surface, lowest_lighting, x, y):
    for j in range(1, precision + 1):
        current_light = (precision - j) / precision * 255
        current_radius = (precision - j) * reach

        if current_light < lowest_lighting:
            pygame.draw.circle(surface, (0, 0, 0, current_light), (x, y), current_radius)

    return surface