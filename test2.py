
# じゃんけんゲームを書いてください
import random
import unittest

# 勝敗の判定ロジックをハンドルするjudge関数を定義

def judge(player_hand, computer_hand):
    # プレイヤーの手とコンピューターの手を比較して結果を表示
    if player_hand == computer_hand:
        return "あいこです。"
    elif player_hand == "グー":
        if computer_hand == "チョキ":
            return "あなたの勝ちです。"
        else:
            return "あなたの負けです。"
    elif player_hand == "チョキ":
        if computer_hand == "パー":
            return "あなたの勝ちです。"
        else:
            return "あなたの負けです。"
    elif player_hand == "パー":
        if computer_hand == "グー":
            return "あなたの勝ちです。"
        else:
            return "あなたの負けです。"
    else:
        return "グー、チョキ、パーのいずれかを入力してください。"

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
    # judge関数を呼び出して結果を表示
    print(judge(player_hand, computer_hand))

    # 9通りのテストケースを書いてみる
    class TestRockPaperScissors(unittest.TestCase):
        # Copilot が提案をします
        # じゃんけんの勝敗を判定する関数をテストするクラス
        def test_judge(self):
            self.assertEqual(judge("グー", "グー"), "あいこです。")
            self.assertEqual(judge("グー", "チョキ"), "あなたの勝ちです。")
            self.assertEqual(judge("グー", "パー"), "あなたの負けです。")
            self.assertEqual(judge("チョキ", "グー"), "あなたの負けです。")
            self.assertEqual(judge("チョキ", "チョキ"), "あいこです。")
            self.assertEqual(judge("チョキ", "パー"), "あなたの勝ちです。")     
            