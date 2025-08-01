# 問題の詳細は省略
# ---------------------------------------------------
# 初期実装（試行錯誤あり・後で改善した）
# ---------------------------------------------------

# coding: utf-8
n, h, w, p, q = map(int, input().split())
served = [(tuple(map(int, input().split()))) for _ in range(n)]
seats = [[(i, j) for j in range(w)] for i in range(h)]
aval_seats = []
indexs = []
best_seat = (p, q)

for i in range(h):
    for j in range(w):
        if seats[i][j] not in served:
            aval_seats.append(seats[i][j])

for seat in aval_seats:
    dist = abs(seat[0] - best_seat[0]) + abs(seat[1] - best_seat[1])
    indexs.append(dist)

best_dist = min(indexs)
for i in range(len(aval_seats)):
    if indexs[i] == best_dist:
        print(aval_seats[i][0], aval_seats[i][1])

# 振り返りメモ:
# - `seats` の作り方や `aval_seats` の抽出が冗長。
# - 距離を別リスト `indexs` に保存してしまい、扱いにくかった。
# - 結果的に処理が分散していて見づらくなった。

# ---------------------------------------------------
# 改善版（簡潔・可読性重視・処理を統合）
# ---------------------------------------------------

# n: 予約済みの席数、h: 座席の縦の数、w: 座席の横の数、p, q: 最も見やすい席の座標
n, h, w, p, q = map(int, input().split())

# 予約済みの座席を集合（set）で格納 → 探索を高速化（O(1)で存在確認できる）
reserved = {tuple(map(int, input().split())) for _ in range(n)}

# 最も見やすい席（ベスト席）の座標を変数に格納
best_seat = (p, q)

# 空席の中での最小マンハッタン距離（初期値は無限大にしておく）
min_dist = float('inf')

# 最小距離となる空席のリスト（複数ある可能性がある）
best_candidates = []

# 映画館のすべての座席を1つずつチェック
for i in range(h):         # 縦方向のループ
    for j in range(w):     # 横方向のループ
        if (i, j) in reserved:
            continue  # すでに予約されている席はスキップ

        # マンハッタン距離を計算
        dist = abs(i - best_seat[0]) + abs(j - best_seat[1])

        # より近い距離が見つかったら、最小距離を更新し、候補リストをリセット
        if dist < min_dist:
            min_dist = dist
            best_candidates = [(i, j)]
        # 同じ距離の席も候補として追加
        elif dist == min_dist:
            best_candidates.append((i, j))

# 最も見やすい空席（マンハッタン距離が最小の空席）を出力
for seat in best_candidates:
    print(seat[0], seat[1])


# ---------------------------------------------------
# 学んだこと・改善点まとめ
# ---------------------------------------------------
# ・予約席の除外は set を使うことで検索高速化（O(1））
# ・距離計算と最小値保持を1ループに統合 → ロジックが明快に
# ・変数名を抽象的なものから意味のある名前に変更（例：indexs → best_candidates）
# ・最終的に、見通しよく、再利用しやすいコード構造に整理できた。
# ---------------------------------------------------
