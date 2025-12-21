import random

def fermat_test(n, k=5):
    """
    フェルマーテスト（確率的素数判定）

    - n が素数なら、任意の a (1 < a < n-1) に対して
      a^(n-1) ≡ 1 (mod n) が成り立つ（フェルマの小定理）
    - k 回ランダムな a を選んでテストし、全て通れば「素数の可能性が高い」
    - 途中で成立しない場合は「合成数（素数ではない）」

    - 誤判定（フェルマ合成数）があるため
      完全判定ではないが高速で大きな数にも使いやすい
    """

    if n == 1:
        return False

    for _ in range(k):
        # 2 ～ n-2 の範囲でランダムに a を選ぶ
        a = random.randint(2, n - 2)

        # pow(a, n-1, n) は (a^(n-1)) mod n を高速計算
        if pow(a, n - 1, n) != 1:
            return False  # フェルマの条件を満たさなければ合成数

    return True  # すべての試行を通過したら素数の可能性が高い


# --- 実行例 ---
if __name__ == "__main__":
    n = 99465
    is_prime = fermat_test(n, k=10)  # 試行回数10回で判定
    if is_prime:
        print(f"{n} は素数の可能性が高い")
    else:
        print(f"{n} は素数ではない")
