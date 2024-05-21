import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((800, 600))

class Snake:
    def __init__(self, length, position, direction) -> None:
        self.length = length
        self.position = position
        self.direction = direction

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

