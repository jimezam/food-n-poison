import pygame

def handle_events():
    handle_key(pygame.key.get_pressed())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def handle_key(key: pygame.key.ScancodeWrapper):
    if key[pygame.K_q]:
        pygame.quit()
        exit()
