import pygame

pygame.init()

#ゲーム画面の作成
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("オセロ")

#マスの設定
square_num = 8
square_size = screen_width//square_num

#フレームレートの設定
FPS = 60
clock = pygame.time.Clock()

#色の設定
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

#メインループ========================================
run = True
while run:

#イベントの取得
    for event in pygame.event.get():
        if event.type==pygame.Quit():
            run = False

#===================================================

pygame.quit()
