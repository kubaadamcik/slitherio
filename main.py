import pygame
import sys
from random import randrange

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 800

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PLAYER_SIZE = (40, 40)
FRUIT_SIZE = (30, 30)

window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# temp variables
score = 0


class Snake:
    def __init__(self, length, position, player_speed, tail_size, player_size) -> None:
        self.length = length
        self.tail_size = tail_size
        self.position = position
        self.player_size = player_size
        self.player_speed = player_speed
        self.head = pygame.rect.Rect((*self.position, *self.player_size))
        self.tails = []
        
    
    def draw(self) -> None:
        # draw head
        pygame.draw.rect(window, WHITE, self.head)

        #draw tail
        for ocas in self.tails:
            pygame.draw.rect(window, WHITE, ocas)
        
        self.tails.clear()

    def move(self, keys) -> None:
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
        self.position = (max(0, min(self.position[0], WIDTH - self.player_size[0])), max(0, min(self.position[1], HEIGHT - self.player_size[1])))

        self.head = pygame.rect.Rect((*self.position, *self.player_size))

        for i in range(self.length):
            self.tails.append(pygame.rect.Rect(self.position[0] - 50 * (i+1), self.position[1], *self.tail_size))

    def eat(self, fruit):
        return self.head.colliderect(fruit.fruit)        

    

class Fruit:
    def __init__(self, position, fruit_size) -> None:
        self.position = position
        self.fruit_size = fruit_size
        self.fruit = pygame.rect.Rect((*self.position, *self.fruit_size))
    
    def draw(self):
        pygame.draw.rect(window, RED, self.fruit)

    def spawn(self, new_pos):
        self.fruit = pygame.rect.Rect((*new_pos, *self.fruit_size))


def ShowText(text):
    text = font.render(str(text), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    window.blit(text, textRect) 

    pygame.display.flip 

fruit = Fruit((randrange(10, 990), randrange(10, 790)), FRUIT_SIZE)


player1 = Snake(1, (10, 10), 2, (45, 45), PLAYER_SIZE)
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

