from typing import List, Dict
import random
import pygame
from config import *
from src.score import score_add_point

def element_create(x: int, 
                   width: int, height: int,
                   type: Element_type, size: int,
                   elements_options: Dict) -> None:

    color: tuple = (0, 255, 0) if type == Element_type.FOOD else (255, 0, 0)
    options: List[pygame.Surface] = elements_options['food'] if type == Element_type.FOOD else elements_options['poison']

    return {
        "type": type,
        "rect": pygame.Rect(random.randint(x, x+width-size), 0, size, size),
        "color": color,
        "image": options[random.randint(0, len(options)-1)],
        "speed": random.randint(elements_speed_range[0], elements_speed_range[1]),
        "next_move": 0,
        "step_size": random.randint(elements_step_range[0], elements_step_range[1])
    }


def elements_draw(surface: pygame.Surface, elements: List[Dict]) -> None:
    for element in elements:
        surface.blit(element['image'], element['rect'])
        # pygame.draw.rect(surface, element['color'], element['rect'])


def elements_move(elements: List[Dict], time: int) -> None:
    for element in elements:
        if time >= element['next_move']:
            element['rect'] = element['rect'].move(0, element['step_size'])
            element['next_move'] = time + element['speed']

def elements_detect_fallen(elements: List[Dict]) -> None:
    for element in elements:
        if element['rect'].y > height:      # Has fallen
            elements_fall(elements, element, score)

def elements_keep_amount(elements: List[Dict]) -> None:
    if len(elements) <= elements_max_count:
        probability: int = random.randint(0, 100)
        if probability >= elements_probability_add:
            type: Element_type =  Element_type.FOOD if random.randint(0, 100) <= 60 else Element_type.POISON
            elements.append(element_create(0, width, height, type, element_size, elements_options))

def elements_eat(elements: List[Dict], element: Dict, score: Dict) -> None:
    elements.remove(element)
    score_add_point(element['type'], Element_status.EATEN, score)
    # sound
    # TODO

def elements_fall(elements: List[Dict], element: Dict, score: Dict) -> None:
    elements.remove(element)
    score_add_point(element['type'], Element_status.FALLEN, score)
    # sound
    # TODO
    pass