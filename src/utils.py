def validate_input(user_input):
    """ユーザーからの入力を検証する関数"""
    if user_input in ['1', '2', '3', '4', '5', '6', '7', '8']:
        return True
    return False

def print_board(board):
    """ボードの状態を表示する関数"""
    for row in board:
        print(" ".join(row))
    print()

def get_coordinates():
    """ユーザーからの座標入力を取得する関数"""
    while True:
        user_input = input("石を置く位置を選んでください (1-8): ")
        if validate_input(user_input):
            return int(user_input) - 1
        else:
            print("無効な入力です。再度入力してください。")