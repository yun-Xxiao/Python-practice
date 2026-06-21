import pygame
import random
import settings


#################玩家角色
class Player(pygame.sprite.Sprite):  # class Player extends Sprite
    def __init__(self, image_surface):
        pygame.sprite.Sprite.__init__(self)  # 初始化
        # self.image = pygame.Surface([50, 50])  # 宽高
        # self.image.fill([200, 0, 50])  # 颜色
        self.image = pygame.transform.scale(image_surface, (50, 50))
        self.image.set_colorkey((0, 0, 0))  # 把黑色背景设为透明
        self.rect = self.image.get_rect()  # 玩家的形状为矩形
        self.rect.centerx = float.__round__(settings.SCREEN_WIDTH / 2)  # x坐标
        self.rect.bottom = settings.SCREEN_HEIGHT  # y坐标
        self.last_shot_time = 0  # 上一次发射子弹的时刻
        self.shoot_delay = 200  # 冷却时间（毫秒）
        self.speed = settings.PLAYER_SPEED  # 玩家速度
        self.can_shoot = False

    def update(self, *args, **kwargs):
        key_pressed = pygame.key.get_pressed()  # 获取按下去的键盘是哪个键。键盘press事件监听
        current_time = pygame.time.get_ticks()
        if key_pressed[pygame.K_w]:
            if self.rect.top > 1:
                self.rect.y -= self.speed
        if key_pressed[pygame.K_a]:
            if self.rect.left > 1:
                self.rect.x -= self.speed
        if key_pressed[pygame.K_s]:
            if self.rect.bottom < settings.SCREEN_HEIGHT:
                self.rect.y += self.speed
        if key_pressed[pygame.K_d]:
            if self.rect.right < settings.SCREEN_WIDTH:
                self.rect.x += self.speed
        self.can_shoot = False
        if key_pressed[pygame.K_SPACE]:
            if current_time - self.last_shot_time > self.shoot_delay:
                self.last_shot_time = current_time
                self.can_shoot = True


##################子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image_surface, (50, 50))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.speed = settings.BULLET_SPEED
        pygame.mixer.Sound(settings.SHOOT_MUSIC_PATH).play()

    def update(self, *args, **kwargs):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


#################掉落物
class DroppingItem(pygame.sprite.Sprite):
    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.transform.scale(image_path, (50, 50))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.SCREEN_WIDTH - 50)
        self.rect.y = random.randint(-2000, 0)
        self.speed = speed  # 速度

    def update(self, *args, **kwargs):
        self.rect.y += self.speed
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.rect.x = random.randint(0, settings.SCREEN_WIDTH - 50)
            self.rect.y = random.randint(-2000, 0)


#################屎
class Shit(DroppingItem):
    def __init__(self, image_surface):
        super().__init__(image_surface, settings.SHIT_SPEED)


##################水果
class Fruit(DroppingItem):
    def __init__(self, image_surface):
        super().__init__(image_surface, settings.FRUIT_SPEED)
