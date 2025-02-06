import pygame

pygame.init()

#関数

#グリッド線の描画
def draw_grid():
    for i in range(square_num):
        #横線
        pygame.draw.line(screen, Black, (0, i*square_size), (screen_width, i*square_size), 3)

        #縦線
        pygame.draw.line(screen, Black, (i*square_size, 0), (i*square_size, screen_height), 3)

#盤面の描画
def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, Black, (col_index * square_size + 50, row_index * square_size + 50), 30)
            elif col == -1:
                pygame.draw.circle(screen, White, (col_index * square_size + 50, row_index * square_size + 50), 30)
                 
            
        



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
Green = (0, 130, 0 )
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

#盤面(黒 : 1, 白　: -1,)
board = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 1, -1, 0, 0, 0, ],
        [0, 0, 0, -1, 1, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ]]

#メインループ========================================
run = True
while run:

#背景の塗りつぶし
    screen.fill(Green)

#グリッド線の描画
    draw_grid()

#盤面の描画
    draw_board()




#イベントの取得 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#画面の更新
    pygame.display.update()
    clock.tick(FPS)

#=============================================================
pygame.quit()
