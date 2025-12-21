# subset_sum_variants.py
# --------------------------------------------
# 「部分和問題（Subset Sum Problem）」の基本とその派生パターンのまとめ
# 1. おもりを選んで目標の重さ x が作れるか？（True / False）
# 2. おもりを選んで目標の重さ x を何通りの方法で作れるか？（通り数）
# 3. おもりを選んで目標の重さ x を作るとき、おもりの最小個数は？
#
# 【条件】
# - おもりは1個ずつしか使えない（重複選択不可）
# - 重さはすべて正の整数
#
# 【使うDP配列】
# - 作れるかどうか：      dp[重さ] = True/False
# - 通り数：              dp[重さ] = 作り方の数
# - 最小個数：            dp[重さ] = 使ったおもりの個数（最小）

MOD = 10**9 + 7  # 通り数問題で使う場合のみ（答えが大きくなるため）

# --- 1. 作れるかどうか（True/False） ---
n, x = map(int, input().split())
weights = [int(input()) for _ in range(n)]

dp = [False] * (x + 1)
dp[0] = True

for w in weights:
    for j in range(x, w - 1, -1):
        if dp[j - w]:
            dp[j] = True

print("Yes" if dp[x] else "No")


# --- 2. 作り方は何通りあるか？ ---
dp = [0] * (x + 1)
dp[0] = 1

for w in weights:
    for j in range(x, w - 1, -1):
        dp[j] = (dp[j] + dp[j - w]) % MOD

print(dp[x])  # xを作る方法の通り数


# --- 3. 最小で何個で作れるか？ ---
INF = float('inf')
dp = [INF] * (x + 1)
dp[0] = 0

for w in weights:
    for j in range(x, w - 1, -1):
        if dp[j - w] != INF:
            dp[j] = min(dp[j], dp[j - w] + 1)

print(dp[x] if dp[x] != INF else "作れない")


# --- 4. おもりを無限個使える場合（無制限部分和問題） ---
# ・おもりは無限に使ってOK
# ・重さの合計が x になるかどうか判定
# ・DP配列は dp[j] = 重さ j が作れるかどうか（True/False）
# ・ループは「前から」（小さい重さから大きい重さへ）進めることが重要
#   （同じおもりを何度も使うため、更新済みの状態をすぐ活用できる）

dp = [False] * (x + 1)
dp[0] = True

for w in weights:
    for j in range(w, x + 1):
        if dp[j - w]:
            dp[j] = True

print("Yes" if dp[x] else "No")
