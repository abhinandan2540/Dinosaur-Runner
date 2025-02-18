import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner 🦖")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Dinosaur settings
dino_width, dino_height = 50, 50
dino_x, dino_y = 50, HEIGHT - dino_height - 30  # Ground level
dino_velocity_y = 0
gravity = 0.8
is_jumping = False

# Obstacle settings
obstacle_width = 30
obstacle_height = 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 30
obstacle_speed = 15

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_velocity_y = -12  # Jumping force
                is_jumping = True

    # Apply gravity
    dino_velocity_y += gravity
    dino_y += dino_velocity_y

    # Check if dino is on the ground
    if dino_y >= HEIGHT - dino_height - 30:
        dino_y = HEIGHT - dino_height - 30
        is_jumping = False

    # Move obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH + random.randint(100, 300)  # Respawn obstacle
        score += 1  # Increase score

    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    obstacle_rect = pygame.Rect(
        obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if dino_rect.colliderect(obstacle_rect):
        print("Game Over! Final Score:", score)
        running = False  # End the game on collision

    # Draw elements
    pygame.draw.rect(screen, GREEN, (dino_x, dino_y,
                     dino_width, dino_height))  # Dino
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y,
                     obstacle_width, obstacle_height))  # Obstacle

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, HEIGHT - 30), (WIDTH, HEIGHT - 30), 3)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Control FPS
    clock.tick(30)

pygame.quit()
