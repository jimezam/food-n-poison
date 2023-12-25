import pygame
from src.handle_events import handle_events

####################################################

width = 800
height = 600

####################################################

def main():
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Food and Poison game!')

    ####################################################

    while True:
            handle_events()

####################################################
        
if __name__ == '__main__':
      main()