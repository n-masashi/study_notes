# ------------------------------
# フィボナッチ数列を求める2つの方法
# 1. 再帰だけで書く方法（遅い）
# 2. 再帰 + メモ化で書く方法（速い）
# ------------------------------

import time  # 時間比較用

def fib_recursive(n):
    """
    フィボナッチ数列を再帰だけで求める方法（非効率）

    n: 何番目のフィボナッチ数か（0から始まる）

    注意：同じ計算を何度も繰り返すので、nが大きいととても遅くなる
    """
    if n == 0:
        return 0  # 最初の値は 0
    elif n == 1:
        return 1  # 2番目の値は 1
    else:
        # それ以降は、前の2つの値を足したもの
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# メモを保存するための辞書（キー: n、値: フィボナッチ数）
memo = {}

def fib_memoized(n):
    """
    フィボナッチ数列を再帰＋メモ化で求める方法（効率的）

    メモ化（memoization）とは、一度計算した結果を覚えておくことで、
    同じ計算を何度もしないようにするテクニック
    """
    if n in memo:
        return memo[n]  # メモにあれば、それを使う（再計算しない）

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        # 再帰呼び出ししながらも、結果は1回しか計算されない
        result = fib_memoized(n - 1) + fib_memoized(n - 2)

    # 計算した結果をメモに保存
    memo[n] = result
    return result


# ------------------------------
# 動作確認用：0〜9番目のフィボナッチ数を2つの方法で表示
# ------------------------------
if __name__ == "__main__":
    print("n : recursive      | memoized       ")
    print("-------------------------------------")

    for i in range(10):
        start = time.time()  # 時間スタート
        r = fib_recursive(i)
        end = time.time()    # 時間終了
        recursive_time = end - start  # 秒数

        start = time.time()
        m = fib_memoized(i)
        end = time.time()
        memoized_time = end - start

        print(f"{i} : {r:<15} | {m:<13} | rec_time: {recursive_time:.6f}s | memo_time: {memoized_time:.6f}s")
