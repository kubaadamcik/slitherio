import pygame
import sys
from random import randrange

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 800

WHITE = (255, 255, 255)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# random variables
last_tick = 0
interval = 5000
score = 0

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

    def eat(self, fruit):
        return self.head.colliderect(fruit.fruit)

    

class Fruit:
    def __init__(self, position) -> None:
        self.position = position
        self.fruit = pygame.rect.Rect((*self.position, 20, 20))
    
    def draw(self):
        pygame.draw.rect(window, RED, self.fruit)

    def spawn(self, new_pos):
        self.fruit = pygame.rect.Rect((*new_pos, 20, 20))


def ShowText(text):
    text = font.render(str(text), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    window.blit(text, textRect) 

    pygame.display.flip 

fruit = Fruit((randrange(10, 990), randrange(10, 790)))


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



    fruit.draw()

    player1.draw()

    player1.move(keys)

    if player1.eat(fruit):
        player1.length += 1

        fruit.spawn((randrange(10, 990, 10), randrange(10, 790, 10)))
    
    ShowText(player1.length)

    pygame.display.update()

    clock.tick(60)

