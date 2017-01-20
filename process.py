import pygame
import sys
import classes
from random import randint


def process(player_car, fps, total_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_car.vel_x = 10
    elif keys[pygame.K_LEFT]:
        player_car.vel_x = -10
    else:
        player_car.vel_x = 0

    spawn(fps, total_frames)
    collision_detection()


def spawn(fps, total_frames):
    time_to_spawn = fps * 1.25
    list_of_x_position = {1: 15, 2: 165, 3: 330, 4: 480}
    list_of_cars = {1: "./images/enemy_car_01.png", 2: "./images/enemy_car_02.png", 3: "./images/enemy_car_03.png"}

    if total_frames % time_to_spawn == 0:
        position_selected = randint(1, 4)
        car_selected = randint(1, 3)
        classes.EnemyCar(list_of_x_position[position_selected], 0, list_of_cars[car_selected])

    if total_frames % (fps * 5) == 0:
        classes.EnemyCar.vel_y += 1


def collision_detection():
    for my_car in classes.MyCar.List:
        if pygame.sprite.spritecollide(my_car, classes.EnemyCar.List, False):
            classes.MyCar.game_lost = True
