import pygame
import sys
from random import randrange

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000, 800

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PLAYER_SIZE = (45, 45)
FRUIT_SIZE = (30, 30)
TAIL_SIZE = (45, 45)
PLAYER_SPEED = 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# temp variables

class Snake:
    def __init__(self, length, player_position, player_speed, tail_size, player_size) -> None:
        self.length = length
        self.tail_size = tail_size
        self.player_position = player_position
        self.player_size = player_size
        self.player_speed = player_speed
        self.head = pygame.rect.Rect((*self.player_position, *self.player_size))
        self.tails = []
        self.right = False
        self.up = False
        self.new_direction = [1, 0]
        self.old_direction = [1, 0]
        self.turning_pos = self.player_position

        
    
    def draw(self) -> None:
        # draw head
        pygame.draw.rect(window, WHITE, self.head)

        #draw tail
        for ocas in self.tails:
            pygame.draw.rect(window, RED, ocas)
        
        self.tails.clear()

    def move(self, keys) -> None:

        if keys[pygame.K_UP]:
            self.new_direction[1] = -1
            self.new_direction[0] = 0
            self.turning_pos = self.player_position
        if keys[pygame.K_DOWN]:
            self.new_direction[1] = 1
            self.new_direction[0] = 0
            self.turning_pos = self.player_position
        if keys[pygame.K_LEFT]:
            self.new_direction[0] = -1
            self.new_direction[1] = 0
            self.turning_pos = self.player_position
        if keys[pygame.K_RIGHT]:
            self.new_direction[0] = 1
            self.new_direction[1] = 0
            self.turning_pos = self.player_position
        

        self.player_position = (self.player_position[0] + self.new_direction[0] * self.player_speed, self.player_position[1] + self.new_direction[1] * self.player_speed)
        self.player_position = (max(0, min(self.player_position[0], WIDTH - self.player_size[0])), max(0, min(self.player_position[1], HEIGHT - self.player_size[1])))

        self.head = pygame.rect.Rect((*self.player_position, *self.player_size))

        # TODO: Ocas pronásleduje hada postupně
        for i in range(self.length):
            x = self.player_position[0] - self.tail_size[0] * self.old_direction[0] * (i + 1)
            y =  self.player_position[1] - self.tail_size[1] * self.old_direction[1] * (i + 1)

            if x == self.turning_pos[0] and y == self.turning_pos[1]:
                self.old_direction = self.new_direction
                x = self.player_position[0] - self.tail_size[0] * self.new_direction[0] * (i + 1)
                y =  self.player_position[1] - self.tail_size[1] * self.new_direction[1] * (i + 1)
                self.tails.append(pygame.rect.Rect(x, y, *self.tail_size))
            else:
                self.new_direction = self.old_direction
                self.tails.append(pygame.rect.Rect(x, y, *self.tail_size))



    def check_eat(self, fruit):
        return self.head.colliderect(fruit.fruit)
    
    # TODO: Dodělat
    def check_death(self):
        if self.player_position[0] + PLAYER_SIZE[0] >= WIDTH or self.player_position[0] <= 0:
            return True
        if self.player_position[1] + PLAYER_SIZE[1] >= HEIGHT or self.player_position[1] <= 0:
            return True

    

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

def MainMenu():
    pass

fruit = Fruit((randrange(10, 990), randrange(10, 790)), FRUIT_SIZE)

player1 = Snake(1, (10, 10), PLAYER_SPEED, TAIL_SIZE, PLAYER_SIZE)
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


    if not player1.check_death():
        fruit.draw()

        player1.draw()

        player1.move(keys)

        if player1.check_eat(fruit):
            player1.length += 1

            fruit.spawn((randrange(10, 990, 10), randrange(10, 790, 10)))

        
        ShowText(player1.length)
    else:
        ShowText("You died")

    pygame.display.update()

    clock.tick(60)

