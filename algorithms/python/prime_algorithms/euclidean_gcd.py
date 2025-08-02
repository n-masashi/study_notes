# gcd_multi.py

def calc_gcd(a, b):
    """
    2つの整数 a, b の最大公約数をユークリッドの互除法で計算する関数。

    - b が 0 になったら a が最大公約数なのでそれを返す。
    - そうでなければ、b と a を b で割った余りの最大公約数を再帰で計算する。
    - a, b の大小関係は気にしなくて良い（ユークリッドの互除法の性質）。
    """
    if b == 0:
        return a
    return calc_gcd(b, a % b)


def calc_multi_gcd(a):
    """
    整数のリスト a の最大公約数を計算する関数。

    - リストの最初の値を gcd として初期化。
    - 2つずつ gcd を計算しながらリストの要素を順に処理。
    - リストの順序（昇順・降順）に依存しない（最大公約数の結合法則・交換法則による）。
    """
    n = len(a)
    gcd = a[0]
    for i in range(1, n):
        gcd = calc_gcd(gcd, a[i])
    return gcd


# --- 実行例 ---
if __name__ == "__main__":
    a = [12, 30, 42]
    gcd = calc_multi_gcd(a)
    print(*a, "の最大公約数は", gcd)
