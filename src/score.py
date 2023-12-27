import pygame
from config import *

def score_display(surface: pygame.Surface, score: Dict):
    message: str = f"Food {score['food_eaten']}/{score['food_fallen']} - Poison {score['poison_eaten']}/{score['poison_fallen']}"
    font: pygame.font.Font = pygame.font.SysFont(None, 60)
    rendered: pygame.Surface = font.render(message, True, score_color)
    rect: pygame.rect.Rect = rendered.get_rect()
    rect.center = (width // 2, 30)
    surface.blit(rendered, rect)

def score_add_point(type: Element_type, status: Element_status, score: Dict):
    if status == Element_status.FALLEN:
        if type == Element_type.FOOD:
            score['food_fallen'] += 1
        elif type == Element_type.POISON:
            score['poison_fallen'] += 1
    elif status == Element_status.EATEN:
        pass        # TODO
    else:
        print(f"ERROR: Element_status unknown: {status}")