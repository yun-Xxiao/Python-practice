import sprites
import pygame
import settings

class GameManager:
    def __init__(self, game):
        self.game = game
        # 1. 加载资源 (图片、音乐)
        self.load_assets()

        # 2. 初始化游戏数据
        self.init_game_data()

    def _add_shit(self):
        shit = sprites.Shit(self.shit_image)
        self.shit_group.add(shit)
        self.all_sprites_group.add(self.shit_group)

    def _add_fruit(self):
        fruit = sprites.Fruit(self.fruit_image)
        self.fruit_group.add(fruit)
        self.all_sprites_group.add(self.fruit_group)

    def update(self):
        self.all_sprites_group.update()  # 更新群组，会自动调用所有精灵的update函数

        if self.player.can_shoot:
            bullet = sprites.Bullet(self.bullet_image)  # 按下空格产生对象
            bullet.rect.center = self.player.rect.center  # 子弹从玩家中心发射
            self.bullet_group.add(bullet)
            self.all_sprites_group.add(self.bullet_group)  # 将子弹群添加到大群

    def load_assets(self):
        #  加载图片
        self.bg_image = pygame.image.load(settings.BG_IMAGE_PATH).convert_alpha()  # 背景图
        self.player_image = pygame.image.load(settings.PLAYER_IMAGE_PATH).convert_alpha()  # 玩家图
        self.shit_image = pygame.image.load(settings.SHIT_IMAGE_PATH).convert_alpha()  # 屎图
        self.fruit_image = pygame.image.load(settings.FRUIT_IMAGE_PATH).convert_alpha()  # 水果
        self.bullet_image = pygame.image.load(settings.BULLET_IMAGE_PATH).convert_alpha()  # 子弹
        # 加载音乐
        pygame.mixer_music.load(settings.BG_MUSIC_PATH)

    def init_game_data(self):
        self.HP = 5
        self.eat_fruit = 0
        # 创建一个玩家对象
        self.player = sprites.Player(self.player_image)
        # 创建一个精灵群组，用于存放所以精灵。然后将群组中的精灵显示到游戏屏幕上
        self.all_sprites_group = pygame.sprite.Group()
        # 创建一个屎群组
        self.shit_group = pygame.sprite.Group()
        # 创建一个水果群组
        self.fruit_group = pygame.sprite.Group()
        # 创建一个子弹群组
        self.bullet_group = pygame.sprite.Group()
        # 将玩家添加到大群
        self.all_sprites_group.add(self.player)
        self._create_initial_objects()
        self.all_sprites_group.add(self.shit_group)
        self.all_sprites_group.add(self.fruit_group)

    def _create_initial_objects(self):
        # 创建10坨屎
        for i in range(settings.INITIAL_SHITS):
            shit = sprites.Shit(self.shit_image)
            self.shit_group.add(shit)
        # 创建5个水果
        for i in range(settings.INITIAL_FRUITS):
            fruit = sprites.Fruit(self.fruit_image)
            self.fruit_group.add(fruit)