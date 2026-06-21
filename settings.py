import os

FPS = 60  # 游戏界面刷新的帧率
SCREEN_WIDTH = 500  # 游戏屏幕宽
SCREEN_HEIGHT = 700  # 高
GAME_NAME = "MyFirstGame" #游戏名

# 字体设置
FONT_NAME = "Arial"
FONT_SIZE = 22

# 游戏对象设置
PLAYER_SPEED = 8
SHIT_SPEED = 5
FRUIT_SPEED = 5
BULLET_SPEED = 8

# 初始数量
INITIAL_SHITS = 10
INITIAL_FRUITS = 5

# 图片路径
BG_IMAGE_PATH = os.path.join("assets/pngs", "background2.png")
PLAYER_IMAGE_PATH = os.path.join("assets/pngs", "aircraft-100.png")
SHIT_IMAGE_PATH = os.path.join("assets/pngs", "shit.png")
FRUIT_IMAGE_PATH = os.path.join("assets/pngs", "vitamin.png")
BULLET_IMAGE_PATH = os.path.join("assets/pngs", "子弹.png")

# 音乐路径
BG_MUSIC_PATH = os.path.join("assets/music", "background.mp3")
SHOOT_MUSIC_PATH = os.path.join("assets/music", "shoot.mp3")