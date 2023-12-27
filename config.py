from typing import List, Dict
import pygame

background_color: List = (255, 255, 255)

width: int = 800
height: int = 600

time: int = 0

score: Dict = {
    "food_eaten": 0,
    "food_fallen": 0,
    "poison_eaten": 0,
    "poison_fallen": 0
}

element_size: int = 60
elements: List[Dict] = []
elements_speed_range: Dict = (50, 200)
elements_step_range: Dict = (1, 5)

elements_options: Dict = {
    "bomb": [
        pygame.transform.scale(pygame.image.load("resources/images/bomb-good.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/bomb-bad.png"), (element_size, element_size))
    ],
    "food": [
        pygame.transform.scale(pygame.image.load("resources/images/food-1.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-2.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-3.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-4.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-5.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-6.png"), (element_size, element_size)), 
        pygame.transform.scale(pygame.image.load("resources/images/food-7.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-8.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-9.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-10.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-11.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-12.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-13.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/food-14.png"), (element_size, element_size))
    ],
    "poison": [
        pygame.transform.scale(pygame.image.load("resources/images/poison-1.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-2.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-3.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-4.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-5.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-6.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-7.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-8.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-9.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-10.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-11.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-12.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-13.png"), (element_size, element_size)),
        pygame.transform.scale(pygame.image.load("resources/images/poison-14.png"), (element_size, element_size))
    ]
}