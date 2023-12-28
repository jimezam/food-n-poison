from typing import List, Dict
import pygame
from config import *
from src.events import handle_events
from src.elements import *
from src.score import *
from src.player import *

####################################################

def main():
    pygame.init()
    surface: pygame.Surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Food and Poison game!')

    # print(type(surface).__name__)

    ####################################################

    while True:
        time = pygame.time.get_ticks() 
        surface.fill(background_color)
        surface.blit(background, (0, 0))
        handle_events()
        elements_move(elements, time)
        elements_draw(surface, elements)
        elements_detect_fallen(elements)
        elements_keep_amount(elements)
        player_draw(surface, player)
        player_check_collisions(elements, player, score)
        score_display(surface, score)
        pygame.display.update()

####################################################

if __name__ == '__main__':
    main()