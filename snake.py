# Step 1: Import the necessary libraries
import pygame
import sys
import time
import random

# Step 2: Initialize Pygame
pygame.init()

# Step 3: Set up some constants
width = 800
height = 600
block_size = 20
fps = 10

# Step 4: Create the game window
win = pygame.display.set_mode((width, height))

# Step 5: Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Step 6: Set up the font
font = pygame.font.Font(None, 36)

# Step 7: Set up the clock
clock = pygame.time.Clock()

# Step 8: Set up the snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)

# Step 9: Set up the direction
direction = 'RIGHT'

# Game loop
while True:
    # Step 10: Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction!= 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction!= 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction!= 'LEFT':
                direction = 'RIGHT'

    # Step 11: Move the snake
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - block_size)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + block_size)
    elif direction == 'LEFT':
        new_head = (head[0] - block_size, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + block_size, head[1])
    snake.append(new_head)

    # Step 12: Check for food collision
    if snake[-1] == food:
        food = (random.randint(0, width - block_size) // block_size * block_size,
                random.randint(0, height - block_size) // block_size * block_size)
    else:
        snake.pop(0)

    # Step 13: Check for wall collision
    if (snake[-1][0] < 0 or snake[-1][0] >= width or
            snake[-1][1] < 0 or snake[-1][1] >= height):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Step 14: Check for self collision
    if snake[-1] in snake[:-1]:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Step 15: Draw everything
    win.fill(black)
    for pos in snake:
        pygame.draw.rect(win, green, (pos[0], pos[1], block_size, block_size))
    pygame.draw.rect(win, red, (food[0], food[1], block_size, block_size))
    text = font.render(f"Score: {len(snake)}", True, white)
    win.blit(text, (10, 10))
    pygame.display.update()

    # Step 16: Cap the frame rate
    clock.tick(fps)