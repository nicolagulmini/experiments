import pygame
import random

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self, width=WIDTH // CELL_SIZE, height=HEIGHT // CELL_SIZE):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.direction = (0, 1)  # start moving right
        self.food = self.generate_food()
        self.game_over = False

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def change_direction(self, new_direction):
        # don't allow a 180 degrees flip
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def move(self):
        if self.game_over:
            return

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        # Check collision with walls
        if not (0 <= new_head[0] < self.width and 0 <= new_head[1] < self.height):
            self.game_over = True
            return

        # Check collision with itself
        if new_head in self.snake:
            self.game_over = True
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Check if food is eaten
        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()  

    def get_state(self):
        return {
            'snake': self.snake,
            'food': self.food,
            'game_over': self.game_over
        }

def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, WHITE, rect, 1)

def draw_snake(surface, snake):
    for segment in snake:
        rect = pygame.Rect(segment[1] * CELL_SIZE, segment[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, GREEN, rect)

def draw_food(surface, food):
    rect = pygame.Rect(food[1] * CELL_SIZE, food[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, RED, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    game = SnakeGame()

    # keys map
    key_to_direction = {
        pygame.K_UP: (-1, 0),
        pygame.K_DOWN: (1, 0),
        pygame.K_LEFT: (0, -1),
        pygame.K_RIGHT: (0, 1)
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in key_to_direction:
                    game.change_direction(key_to_direction[event.key])

        game.move()

        # draw
        screen.fill(BLACK)
        draw_grid(screen)
        draw_snake(screen, game.snake)
        draw_food(screen, game.food)
        pygame.display.flip()

        clock.tick(10)  # velocity of the game

        if game.game_over:
            print("Game Over!")
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
