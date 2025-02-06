import pygame

pygame.init()

# ゲーム画面の作成
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("オセロ")

# マスの設定
square_num = 8
square_size = screen_width // square_num

# フレームレートの設定
FPS = 60
clock = pygame.time.Clock()

# 色の設定
White = (255, 255, 255)
Black = (0, 0, 0)
Green = (0, 130, 0)

# 盤面(黒 : 1, 白 : -1)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# プレイヤー
player = 1
vec_table = [
    (-1, -1), # 左上
    (0, -1),  # 上
    (1, -1),  # 右上
    (-1, 0),  # 左
    (1, 0),   # 右
    (-1, 1),  # 左下
    (0, 1),   # 下
    (1, 1)    # 右下
]

# グリッド線の描画
def draw_grid():
    for i in range(square_num):
        # 横線
        pygame.draw.line(screen, Black, (0, i * square_size), (screen_width, i * square_size), 3)
        # 縦線
        pygame.draw.line(screen, Black, (i * square_size, 0), (i * square_size, screen_height), 3)

# 盤面の描画
def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, Black, (col_index * square_size + square_size // 2, row_index * square_size + square_size // 2), square_size // 2 - 5)
            elif col == -1:
                pygame.draw.circle(screen, White, (col_index * square_size + square_size // 2, row_index * square_size + square_size // 2), square_size // 2 - 5)

# 石を置ける場所の判定
def is_valid_move(board, row, col, player):
    if board[row][col] != 0:
        return False
    opponent = -player
    for dr, dc in vec_table:
        r, c = row + dr, col + dc
        if 0 <= r < square_num and 0 <= c < square_num and board[r][c] == opponent:
            while 0 <= r < square_num and 0 <= c < square_num:
                r += dr
                c += dc
                if not (0 <= r < square_num and 0 <= c < square_num):
                    break
                if board[r][c] == player:
                    return True
                if board[r][c] == 0:
                    break
    return False

# 石をひっくり返す
def flip_discs(board, row, col, player):
    opponent = -player
    board[row][col] = player
    for dr, dc in vec_table:
        r, c = row + dr, col + dc
        discs_to_flip = []
        while 0 <= r < square_num and 0 <= c < square_num and board[r][c] == opponent:
            discs_to_flip.append((r, c))
            r += dr
            c += dc
        if 0 <= r < square_num and 0 <= c < square_num and board[r][c] == player:
            for rr, cc in discs_to_flip:
                board[rr][cc] = player

# メインループ
run = True
while run:
    # 背景の塗りつぶし
    screen.fill(Green)

    # グリッド線の描画
    draw_grid()

    # 盤面の描画
    draw_board()

    # イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # クリックアンドドロップ
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = mx // square_size
            y = my // square_size
            if is_valid_move(board, y, x, player):
                flip_discs(board, y, x, player)
                player *= -1

    # 画面の更新
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
