def hangman(word):
    wrong = 0                                  # プレイヤーが何回間違えたかを記録する。
    stages = ["",
              "＿＿＿＿            ",
              "|                   ",
              "|                   ",
              "|       |           ",
              "|       O           ",
              "|      /|＼         ",
              "|      / ＼         ",
              "|                   "
              ]
    rletters = list(word)                       # 「word」の要素を一文字ずつリスト化。
    board = ["_"] * len(word)                  #  今回当てる言葉（word変数が持っている言葉）の文字数分のアンダーバーをboard変数に持たせる。
    win = False                                # プレイヤーがゲームに勝ったかどうかの状態を記録するwin。最初はFalseを入れる。
    print("ハングマンへようこそ！")           # 「ハングマンへようこそ！」を出力する。
# ゲームを進めるループ処理
    while wrong < len(stages) - 1:             # 間違えた回数がstagesの要素数と同じになるまで続ける処理。
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)                       # プレイヤーに何か文字を入力してもらうために、input関数を使う。入力してもらった文字はchar変数に格納する。
        if char in rletters:                   # 今回当てる言葉（word)の中にプレイヤーが入力した文字があれば、if以下の処理を行う。
            cind = rletters.index(char)         # 「rletters」にある「char」に格納された要素と同じ文字を取得する。
            board[cind] = char                  # 正解した文字をアンダースコアから文字に置き換える
            rletters[cind] = '$'                # 正解したrlettersに格納されている文字を$に置き換える
        else:
            wrong += 1                          # 間違えた回数を増やす
        print(" ".join(board))                 # ハングマンを出力
        e = wrong + 1                          # eはstage列の要素を出力するためのもの
        print("\n".join(stages[0:e]))          # ハングマンを出力。一部のみ出力したいので、酢羅臼する
        if "_" not in board:                  # 全て正解してアンダーズコアがなくなったら行う処理
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
# ゲームに負けた場合
    if not win:                                               # 勝たなかった場合に行う処理
        print("\n".join(stages[0:wrong+1]))                   # ハングマンをすべて出力する
        print("あなたの負け！正解は {}.".format(word))       # プレイヤーが負けたことを伝える。また、wordの単語を表示する。

# challenge1 ランダムでリストの中から単語を選ぶ
words_list = ["cat", "dog", "fox"]
import random
num = random.randint(0, 2)
hangman(words_list[num])