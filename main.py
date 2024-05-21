import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)

window = pygame.display.set_mode((1000, 800))

class Snake:
    def __init__(self, length, position, player_speed) -> None:
        self.length = length
        self.position = position
        self.player_speed = player_speed
        self.head = pygame.rect.Rect((*self.position, 50, 50))
    
    def draw(self):
        pygame.draw.rect(window, WHITE, self.head)

    def move(self, keys):
        x = 0
        y = 0
        
        if keys[pygame.K_UP]:
            y -= 1 * self.player_speed
        if keys[pygame.K_DOWN]:
            y += 1 * self.player_speed
        if keys[pygame.K_LEFT]:
            x -= 1 * self.player_speed
        if keys[pygame.K_RIGHT]:
            x += 1 * self.player_speed
        
        self.position = (self.position[0] + x, self.position[1] + y)
        self.head = pygame.rect.Rect((*self.position, 50, 50))

class Fruit:
    def __init__(self, position) -> None:
        self.position = position
        self.fruit = pygame.rect.Rect((*self.position, 20, 20))


player1 = Snake(1, (10, 10), 2)
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

    player1.move(keys)

    pygame.display.update()

    clock.tick(60)

