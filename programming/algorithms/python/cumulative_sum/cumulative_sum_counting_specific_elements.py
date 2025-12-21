# cumulative_sum_counting_specific_elements.py
# --------------------------------------------
# 配列の中から「特定の条件を満たす要素の個数」を区間ごとに高速に求める方法の例です。
#
# ここでは「偶数の個数」と「奇数の個数」を累積和を使って求めます。
#
# 累積和を使うことで、複数回区間の個数を知りたい場合でも
# 1回の前処理（累積和の計算）で高速に計算できます。

# 入力例
# n, x, y = 5 0 4
# a = [1, 2, 3, 4, 5]

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

# 偶数なら1、そうでなければ0のリストを作成
even = [1 if num % 2 == 0 else 0 for num in a]
# 奇数は偶数の反対（1 - 偶数の値）
odd = [1 - val for val in even]

# 偶数と奇数の累積和配列を作成（長さは n+1）
even_s = [0] * (n + 1)
odd_s = [0] * (n + 1)

for i in range(n):
    even_s[i + 1] = even_s[i] + even[i]
    odd_s[i + 1] = odd_s[i] + odd[i]

# 区間 [x, y] の偶数の個数は even_s[y+1] - even_s[x]
# 区間 [x, y] の奇数の個数は odd_s[y+1] - odd_s[x]

evens = even_s[y + 1] - even_s[x]
odds = odd_s[y + 1] - odd_s[x]

print(evens)
print(odds)
