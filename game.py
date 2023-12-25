from typing import List, Dict
import pygame
from src.handle_events import handle_events
from src.elements import *

####################################################

width: int = 800
height: int = 600
elements: List[Dict] = []

####################################################


def main():
    pygame.init()
    surface: pygame.Surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Food and Poison game!')

    # print(type(surface).__name__)

    ####################################################

    elements.append(element_create(0, 0, width, height, Element_type.FOOD, 70))
    elements.append(element_create(0, 0, width, height, Element_type.FOOD, 70))
    elements.append(element_create(0, 0, width, height, Element_type.POISON, 70))

    while True:
        handle_events()
        elements_draw(surface, elements)
        pygame.display.update()

####################################################

if __name__ == '__main__':
    main()
