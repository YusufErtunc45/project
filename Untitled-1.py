import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 300
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
player_x, player_y = 50, HEIGHT - PLAYER_HEIGHT - 30

CACTUS_WIDTH, CACTUS_HEIGHT = 30, 50
cactus_x, cactus_y = WIDTH, HEIGHT - CACTUS_HEIGHT - 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), pygame.SRCALPHA)
pygame.draw.rect(player_image, WHITE, (0, 0, PLAYER_WIDTH, PLAYER_HEIGHT))

cactus_image = pygame.Surface((CACTUS_WIDTH, CACTUS_HEIGHT), pygame.SRCALPHA)
pygame.draw.rect(cactus_image, WHITE, (0, 0, CACTUS_WIDTH, CACTUS_HEIGHT))

clock = pygame.time.Clock()

player_velocity_y = 0
gravity = 1
jump_height = -15
is_jumping = False

cactus_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_jumping:
            player_velocity_y = jump_height
            is_jumping = True

    player_y += player_velocity_y
    player_velocity_y += gravity

    if player_y > HEIGHT - PLAYER_HEIGHT - 30:
        player_y = HEIGHT - PLAYER_HEIGHT - 30
        player_velocity_y = 0
        is_jumping = False

    cactus_x -= cactus_speed

    if (
        player_x < cactus_x + CACTUS_WIDTH
        and player_x + PLAYER_WIDTH > cactus_x
        and player_y < cactus_y + CACTUS_HEIGHT
        and player_y + PLAYER_HEIGHT > cactus_y
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if cactus_x < -CACTUS_WIDTH:
        cactus_x = WIDTH
        cactus_y = HEIGHT - CACTUS_HEIGHT - 30

    screen.fill(BLACK)

    screen.blit(player_image, (player_x, player_y))
    screen.blit(cactus_image, (cactus_x, cactus_y))

    pygame.display.flip()

    clock.tick(30)
