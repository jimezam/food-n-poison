from typing import List, Dict
import pygame
from config import *
from src.events import handle_events, handle_key
from src.elements import *

####################################################

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
        handle_events()
        handle_key(pygame.key.get_pressed())
        elements_draw(surface, elements)
        pygame.display.update()

####################################################

if __name__ == '__main__':
    main()
