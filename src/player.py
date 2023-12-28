import pygame
from typing import List, Dict
from config import *
from src.score import score_add_point
from src.elements import *

def player_draw(surface: pygame.Surface, player: pygame.Surface) -> None:
    scaled_player: pygame.Surface = pygame.transform.scale(player, player_rect.size)
    player_rect.center = pygame.mouse.get_pos()
    surface.blit(scaled_player, player_rect)

def player_check_collisions(elements: List[Dict], player: pygame.Surface, score: Dict) -> None:
    for element in elements:
        if player_rect.colliderect(element['rect']):
            elements_eat(elements, element, score)