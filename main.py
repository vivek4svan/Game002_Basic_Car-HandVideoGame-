import os
from classes import *
from process import *

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 1000
FPS = 64
total_frames = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1100, 30)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

background = pygame.image.load("./images/background_01.png")
player_car = MyCar(165, SCREEN_HEIGHT - 210, "./images/my_car_01.png")

while not MyCar.game_lost:
    process(player_car, FPS, total_frames)

    player_car.motion(SCREEN_WIDTH, SCREEN_HEIGHT)
    EnemyCar.update_all(SCREEN_WIDTH, SCREEN_HEIGHT)
    total_frames += 1

    screen.blit(background, (0, 0))  # Instead of bg color # screen.fill((0, 0, 0))
    BaseClass.all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

print "\n\n\n\n\n\n\n NO OF CARS PASSED : %d\n\n\n\n\n\n\n" % MyCar.score
background = pygame.image.load("./images/lost_01.png")
while MyCar.game_lost:
    screen.blit(background, (0, 0))  # Instead of bg color # screen.fill((0, 0, 0))
    BaseClass.all_sprites.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
