# 教習車の周回数計算
# 問題文は省略
# 概要：車番1からNまで順に公道に出ていく中で、最後の車（N番）が出口前を通過した回数を求める

# --- 自作コード ---
# ・flagを使って順番に車を出していく
# ・cars（固定された順番）を毎回1周しながら、
#   最後の車（N番）が通過した回数をカウントする
# ・問題の「出口前を通り過ぎた回数＝周回数」を正しく表現できている
# ・全テストケースに合格（正答・実行速度OK）

n = int(input())
cars = [int(input()) for _ in range(n)]
last_car_count = 0
flag = 1

while flag < n:
    for car in cars:
        if car == flag:
            flag += 1
        elif car == n:
            last_car_count += 1
        else:
            continue

print(last_car_count)


# --- 別解（この解き方を意図して問題が出題されてた？） ---
# ・「最長増加部分列」の考え方を応用
# ・車番1〜Nを順に数える代わりに、N番の車の出走タイミングがどれだけ遅れたかを直接調べる
# ・carsの中で「車番の昇順が崩れる瞬間＝新しい周回の始まり」と考え、
#   その区切りの数がそのままN番の車の周回数になる

n = int(input())
cars = [int(input()) for _ in range(n)]
rounds = 0
max_seen = 0
for car in cars:
    if car < max_seen:
        rounds += 1
    max_seen = max(max_seen, car)
print(rounds)

# この解法の特徴：
# ・車の並び順に昇順の塊が何回切れたかを数える
# ・N番の車が最後なので、これが出口前を通過する周回数と一致する
# ・自作コードより高速（O(N)で済む）
