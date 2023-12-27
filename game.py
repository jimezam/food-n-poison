from typing import List, Dict
import pygame
from config import *
from src.events import handle_events
from src.elements import *
from src.score import *

####################################################

# fonts = pygame.font.get_fonts()
# for f in fonts:
#    print(f)

def main():
    pygame.init()
    surface: pygame.Surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Food and Poison game!')

    # print(type(surface).__name__)

    ####################################################

    elements.append(element_create(0, 0, width, height, Element_type.FOOD, element_size, elements_options))
    elements.append(element_create(0, 0, width, height, Element_type.FOOD, element_size, elements_options))
    elements.append(element_create(0, 0, width, height, Element_type.POISON, element_size, elements_options))
    elements.append(element_create(0, 0, width, height, Element_type.POISON, element_size, elements_options))
    elements.append(element_create(0, 0, width, height, Element_type.POISON, element_size, elements_options))

    while True:
        time = pygame.time.get_ticks() 
        surface.fill(background_color)
        handle_events()
        elements_move(elements, time)
        elements_draw(surface, elements)
        elements_detect_fallen(elements)
        score_display(surface, score)
        pygame.display.update()

####################################################

if __name__ == '__main__':
    main()
