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
    
    def draw(self):
        pygame.draw.rect(window, (0, 255, 0), (*self.position, 10, 10))


player1 = Snake(1, (WIDTH//2, HEIGHT//2), (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    window.fill((0, 0, 0))

    player1.draw()

    clock.tick(60)

