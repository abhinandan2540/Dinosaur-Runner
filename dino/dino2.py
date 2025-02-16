import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dragon Runner 🐉")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

dragon_img = pygame.image.load("drg.png")
cactus_img = pygame.image.load("cactus.png")

dragon_img = pygame.transform.scale(dragon_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (40, 50))


dino_x, dino_y = 50, HEIGHT - 80  # Ground level
dino_velocity_y = 0
gravity = 0.9
is_jumping = False

obstacle_x = WIDTH
obstacle_y = HEIGHT - 80
obstacle_speed = 10


score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_velocity_y = -12
                is_jumping = True

    dino_velocity_y += gravity
    dino_y += dino_velocity_y

    if dino_y >= HEIGHT - 80:
        dino_y = HEIGHT - 80
        is_jumping = False

    obstacle_x -= obstacle_speed
    if obstacle_x < -40:  # Reset position when off-screen
        obstacle_x = WIDTH + random.randint(100, 300)
        score += 1

    dino_rect = pygame.Rect(dino_x, dino_y, 50, 50)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 40, 50)

    if dino_rect.colliderect(obstacle_rect):
        print("Game Over! Final Score:", score)
        running = False  # End game

    screen.blit(dragon_img, (dino_x, dino_y))
    screen.blit(cactus_img, (obstacle_x, obstacle_y))

    pygame.draw.line(screen, BLACK, (0, HEIGHT - 30), (WIDTH, HEIGHT - 30), 3)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(30)

pygame.quit()
