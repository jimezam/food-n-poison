import pygame
from config import *

def player_draw(surface: pygame.Surface, player: pygame.Surface):
    scaled_player: pygame.Surface = pygame.transform.scale(player, (player_size, player_size))
    rect: pygame.Rect = scaled_player.get_rect()
    rect.center = pygame.mouse.get_pos()
    surface.blit(scaled_player, rect)

