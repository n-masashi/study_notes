## スタンプアート生成シミュレーション
複数のスタンプ（文字列アート）を、指定された行列に配置して並べるシミュレーション。
スタンプを2次元リストで管理し、行ごとに組み合わせて出力する処理の練習。

※問題文は含めない
# coding: utf-8

# スタンプ1つあたりの高さ h、幅 w、スタンプの種類数 n を受け取る
h, w, n = map(int, input().split())

# 各スタンプのデザインを、文字列で h 行 × n 種類ぶん受け取る
tmp = [input() for _ in range(h * n)]

# スタンプごとに h 行ずつ切り分けてリスト化する（各スタンプは 2次元リストになる）
stamps = [tmp[i:i + h] for i in range(0, len(tmp), h)]

# アート全体の行数 r と列数 c を受け取る（スタンプを r 行 × c 列に配置する）
r, c = map(int, input().split())

# 配置するスタンプの番号を r 行ぶん受け取る（1-indexed）
maps = [list(map(int, input().split())) for _ in range(r)]

# 出力処理：スタンプの配置通りに1行ずつ出力する
for i in range(r):           # アートの各行ごとに
    for hi in range(h):      # 各スタンプの縦方向の行に対して
        print_line = ""
        for j in range(c):   # アートの列（＝スタンプ）を順に並べて
            index = maps[i][j] - 1  # スタンプ番号を0-indexedに変換
            print_line += stamps[index][hi]  # スタンプのその行（hi行目）を結合
        print(print_line)    # 1行分の出力

