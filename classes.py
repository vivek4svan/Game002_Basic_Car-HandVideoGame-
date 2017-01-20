import pygame


class BaseClass(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()
    score = 0

    def __init__(self, x, y, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.all_sprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self, class_name):
        class_name.List.remove(self)
        BaseClass.all_sprites.remove(self)
        del self
        BaseClass.score += 1
        print "A Car passed (Total : %d)" % BaseClass.score


class MyCar(BaseClass):
    List = pygame.sprite.Group()
    game_lost = False

    def __init__(self,  x, y, image_string):
        BaseClass.__init__(self,  x, y, image_string)
        MyCar.List.add(self)
        self.vel_x = 0

    def motion(self, screen_width, screen_height):
        next_loc_x = self.rect.x + self.vel_x

        if next_loc_x < 0:
            self.vel_x = 0
        elif next_loc_x + self.rect.width > screen_width:
            self.vel_x = 0

        self.rect.x += self.vel_x


class EnemyCar(BaseClass):
    List = pygame.sprite.Group()
    vel_y = 5

    def __init__(self, x, y, image_string):
        BaseClass.__init__(self, x, y, image_string)
        EnemyCar.List.add(self)
        # Below 2 lines of health for Fire Implementation
        self.health = 100
        self.reduce_health = self.health / 2.0

    def motion(self, screen_width, screen_height):
        self.rect.y += EnemyCar.vel_y

    @staticmethod
    def update_all(screen_width, screen_height):
        for enemy_cars in EnemyCar.List:
            enemy_cars.motion(screen_width, screen_height)
            if enemy_cars.rect.y > screen_height:
                enemy_cars.destroy(EnemyCar)
