"""
这是一个基于pygame引擎的游戏，名字叫软件的水果和屎
用wasd控制玩家移动，空格键控制玩家发射子弹，子弹可以消灭屎
非玩家角色（npc）自动往下掉，非玩家有屎和水果，吃水果得分，吃屎挂掉

作者：xx
时间：2026.3.20
"""

# pygame游戏非python自带，需安装。
# 安装方式：1.点击
# 2.cmd：pip install pygame
# 3.pycharm控制台输入pip install pygame

import pygame
import settings
from collision_handler import CollisionHandler
from game_manager import GameManager
from renderer import Renderer


class Game:
    def __init__(self):
        pygame.init()  # 初始化引擎
        self.clock = pygame.time.Clock()  # 时钟对象
        self.running = True  # 控制游戏主循环
        self.paused = False  # 游戏是否暂停的标志
        # 创建了一个游戏屏幕对象
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.GAME_NAME)

        self.game_manager = GameManager(self)  # 负责对象创建、销毁
        self.renderer = Renderer(self)  # 负责绘制
        self.collision_handler = CollisionHandler(self)  # 负责碰撞

    def run(self):
        pygame.mixer.music.play(-1)
        while self.running:
            self.clock.tick(settings.FPS)
            # 1. 处理输入
            self.handle_events()

            # 2. 更新逻辑 (如果没暂停)
            if not self.paused:
                self.game_manager.update()  # 更新所有对象位置
                self.collision_handler.check_all()  # 检查碰撞

            # 3. 绘制画面
            self.renderer.draw()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.game_manager.HP <= 0:  # 点击了关闭窗口的按钮或血量为零
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused  # 切换暂停状态