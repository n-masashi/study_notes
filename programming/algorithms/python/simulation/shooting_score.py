# 射撃スコア計算
# 問題文は省略

# 概要：
# 得点対象となる的は N 個あり、それぞれ中心座標・命中得点・周囲得点が設定されている。
# M 回の射撃で命中したマスが与えられるので、命中または近接命中の得点を加算していき、合計得点を求める。

# --- 自作コード（2重ループ判定） ---
# ・aim, points, nearby をリストで個別管理
# ・各射撃に対してすべての的と比較して、命中 or 周囲8マスなら得点加算
# ・「近接判定」は max(abs(...)) == 1 によって8方向すべてをカバー
# ・テストケースに正答する構造であり、動作も明快
# ・ただし実行速度は O(N×M) とやや重め

# coding: utf-8
h, w = map(int, input().split())
n = int(input())
aim = []
points = []
nearby = []
target = []
ans = 0

for _ in range(n):
    y, x, p, z = map(int, input().split())
    aim.append((y, x))
    points.append(p)
    nearby.append(z)

m = int(input())
for _ in range(m):
    y, x = map(int, input().split())
    target.append((y, x))

for i in range(m):
    for j in range(n):
        if target[i] == aim[j]:
            ans += points[j]
        elif max(abs(target[i][0] - aim[j][0]), abs(target[i][1] - aim[j][1])) == 1:
            ans += nearby[j]

print(ans)

# --- 別解（辞書で高速化） ---
# ・的の中心をキー、命中得点・近接得点を値とする辞書 targets を用意
# ・各射撃について、まず中心に命中しているかを O(1) で判定
# ・命中していなければ周囲8方向をチェックし、どこかに近接していれば q 点加算
# ・重複のない辞書アクセスとbreakによる早期終了により、高速に処理できる（O(M×8)）

# coding: utf-8
h, w = map(int, input().split())
n = int(input())

targets = {}  # (y, x): (p, q)
for _ in range(n):
    y, x, p, q = map(int, input().split())
    targets[(y, x)] = (p, q)

m = int(input())
ans = 0
for _ in range(m):
    y, x = map(int, input().split())

    if (y, x) in targets:
        ans += targets[(y, x)][0]
    else:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                ny, nx = y + dy, x + dx
                if 1 <= ny <= h and 1 <= nx <= w and (ny, nx) in targets:
                    ans += targets[(ny, nx)][1]
                    break

print(ans)
