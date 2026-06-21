import pygame
import settings

class Renderer:
    def __init__(self, game):
        self.game = game
        self.manager = game.game_manager
        # 创建文字对象
        self.font = pygame.font.SysFont(settings.FONT_NAME, settings.FONT_SIZE)

    def draw(self):
        # 绘制背景图片，图片左上角与(0,0)对齐
        self.game.screen.blit(
            pygame.transform.scale(self.manager.bg_image, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT]),
            (0, 0))

        # 2. 绘制所有精灵 (飞机、屎、水果、子弹)
        self.manager.all_sprites_group.draw(self.game.screen)

        # 绘制文字
        hp_message = self.font.render(f"HP: {self.manager.HP}", True, (255, 255, 255))
        self.game.screen.blit(hp_message, (30, 30))

        eat_fruit_message = self.font.render(f"eat fruit: {self.manager.eat_fruit}", True, (255, 255, 255))
        self.game.screen.blit(eat_fruit_message, (settings.SCREEN_WIDTH - 150, 30))

        if self.game.paused:
            self._draw_pause_screen()

        # 5. 更新屏幕
        pygame.display.update()

    def _draw_pause_screen(self):
        """在屏幕中央显示暂停提示"""
        # 创建一个半透明的遮罩层（可选，让暂停效果更明显）
        overlay = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        overlay.set_alpha(128)  # 半透明
        overlay.fill((0, 0, 0))  # 黑色
        self.game.screen.blit(overlay, (0, 0))

        # 显示"PAUSED"文字
        font = pygame.font.SysFont(settings.FONT_NAME, 64)
        text = font.render("PAUSED", True, (255, 255, 255))
        text_rect = text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
        self.game.screen.blit(text, text_rect)

        # 提示按 P 继续
        small_font = pygame.font.SysFont(settings.FONT_NAME, 24)
        tip = small_font.render("Press P to continue the game", True, (200, 200, 200))
        tip_rect = tip.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 + 50))
        self.game.screen.blit(tip, tip_rect)

