import pygame

# 碰撞检测
class CollisionHandler:
    def __init__(self, game):
        self.game = game
        self.manager = game.game_manager

    def check_all(self):
        if self.game.paused:
            return

        # 检查玩家和屎的碰撞
        hit_shit = pygame.sprite.spritecollide(self.manager.player, self.manager.shit_group, True)  # True:碰到屎，屎对象被干掉，消失
        if hit_shit:
            self.manager.HP -= 1
            for _ in hit_shit: self.manager._add_shit()

        # 检查玩家和水果的碰撞
        hit_fruit = pygame.sprite.spritecollide(self.manager.player, self.manager.fruit_group, True)  # True:碰到水果，水果对象被干掉，消失

        if hit_fruit:
            self.manager.eat_fruit += 1
            for _ in hit_fruit: self.manager._add_fruit()

        if self.manager.eat_fruit == 5:
            self.manager.HP += 1
            self.manager.eat_fruit = 0

        # 检查子弹与屎的碰撞
        hits = pygame.sprite.groupcollide(self.manager.bullet_group, self.manager.shit_group, True, True)
        if hits:
            # 遍历字典的值（即被击中的屎的列表）
            for enemy_list in hits.values():
                for _ in enemy_list:
                    self.manager._add_shit()  # 打掉几坨屎，就补充几坨

