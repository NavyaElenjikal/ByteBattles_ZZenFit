
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ZzenFit - FITNESS GAME")

# Load assets
player_image = pygame.image.load("player.png")
item_image = pygame.image.load("item.png")
player_image = pygame.transform.scale(player_image, (50, 50))
item_image = pygame.transform.scale(item_image, (30, 30))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
player_pos = [WIDTH // 2, HEIGHT - 60]
falling_items = []
score = 0
lives = 3
item_speed = 5

# Add falling items
def add_falling_item():
    x_pos = random.randint(0, WIDTH - 30)
    y_pos = 0
    falling_items.append({"x": x_pos, "y": y_pos})

# Draw player
def draw_player():
    screen.blit(player_image, (player_pos[0], player_pos[1]))

# Draw items
def draw_items():
    for item in falling_items:
        screen.blit(item_image, (item["x"], item["y"]))

# Check collision
def check_collision():
    global lives, score
    for item in falling_items[:]:
        if player_pos[0] < item["x"] < player_pos[0] + 50 and player_pos[1] < item["y"] < player_pos[1] + 50:
            score += 10
            falling_items.remove(item)
        elif item["y"] > HEIGHT:
            lives -= 1
            falling_items.remove(item)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Display score and lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 100, 10))

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
        player_pos[0] += 10

    # Add and move falling items
    if random.randint(1, 20) == 1:
        add_falling_item()
    for item in falling_items:
        item["y"] += item_speed

    # Check collisions
    check_collision()

    # Draw elements
    draw_player()
    draw_items()

    # End game if lives are 0
    if lives <= 0:
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
