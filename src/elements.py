from typing import List, Dict
from enum import Enum
import random
import pygame

Element_type = Enum('Element_type', ['FOOD', 'POISON'])


def element_create(x: int, y: int, width: int, height: int, type: Element_type, size: int, elements_options: Dict) -> None:

    color: tuple = (0, 255, 0) if type == Element_type.FOOD else (255, 0, 0)
    options: List[pygame.Surface] = elements_options['food'] if type == Element_type.FOOD else elements_options['poison']

    return {
        "rect": pygame.Rect(random.randint(x, x+width-size), 0, size, size),
        "color": color,
        "image": options[random.randint(0, len(options)-1)]
    }

def elements_draw(surface: pygame.Surface, elements: List[Dict]) -> None:
    for element in elements:
        surface.blit(element['image'], element['rect'])
        # pygame.draw.rect(surface, element['color'], element['rect'])