import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

drawing = False
last_pos = None
pen_color = BLACK
pen_size = 5

screen.fill(WHITE)

def draw_line(screen, start, end, color, size):
    pygame.draw.line(screen, color, start, end, size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            draw_line(screen, last_pos, current_pos, pen_color, pen_size)
            last_pos = current_pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pen_color = RED
            elif event.key == pygame.K_g:
                pen_color = GREEN
            elif event.key == pygame.K_b:
                pen_color = BLUE
            elif event.key == pygame.K_k:
                pen_color = BLACK

    pygame.display.flip()
