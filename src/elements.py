from typing import List, Dict
from enum import Enum
import random
import pygame

Element_type = Enum('Element_type', ['FOOD', 'POISON'])


def element_create(x: int, y: int, width: int, height: int, type: Element_type, size: int) -> None:

    color: tuple = (0, 255, 0) if type == Element_type.FOOD else (255, 0, 0)

    return {
        "rect": pygame.Rect(random.randint(x, x+width-size), 0, size, size),
        "color": color
    }

def elements_draw(surface: pygame.Surface, elements: List[Dict]) -> None:
    for element in elements:
        pygame.draw.rect(surface, element['color'], element['rect'])
        print(element['rect'])
