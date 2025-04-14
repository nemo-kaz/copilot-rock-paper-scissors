# じゃんけんゲームを書いてください
import random

# ロジックを全てハンドルするmain関数を定義

def main():
    # プレイヤーの手を入力
    player_hand = input("じゃんけんをしましょう！(グー、チョキ、パー)：")
    # プレイヤーの手を表示
    print("あなたの手は" + player_hand + "です。")
    # コンピューターの手をランダムに選択
    computer_hand = random.choice(["グー", "チョキ", "パー"])
    # コンピューターの手を表示
    print("コンピューターの手は" + computer_hand + "です。")
    # プレイヤーの手とコンピューターの手を比較して結果を表示
    if player_hand == computer_hand:
        print("あいこです。")
    elif player_hand == "グー":
        if computer_hand == "チョキ":
            print("あなたの勝ちです。")
        else:
            print("あなたの負けです。")
    elif player_hand == "チョキ":
        if computer_hand == "パー":
            print("あなたの勝ちです。")
        else:
            print("あなたの負けです。")
    elif player_hand == "パー":
        if computer_hand == "グー":
            print("あなたの勝ちです。")
        else:
            print("あなたの負けです。")
    else:
        print("グー、チョキ、パーのいずれかを入力してください。")

# main関数を呼び出す
if __name__ == "__main__":
    main()
