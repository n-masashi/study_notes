def eratosthenes(n):
    """
    エラトステネスの篩（ふるい）

    - 2 から n までの整数の中から素数を効率的に見つけるアルゴリズム
    - 最初に全ての数を素数(True)と仮定し、
      素数でない数（合成数）を順番に False にしていく
    - 素数の倍数をすべて篩い落とすことで、最終的に素数だけが True に残る
    """

    # 0 から n までの数について素数判定の初期リストを作成（全て True に）
    isPrime = [True] * (n + 1)

    # 0 と 1 は素数ではないので False に設定
    isPrime[0], isPrime[1] = False, False

    # 2 から n までの数を順にチェック
    for i in range(2, n + 1):

        # もし i がすでに素数でないと判定されていたらスキップ
        if not isPrime[i]:
            continue

        # i が素数なら、その倍数（2i, 3i, 4i, ...）をすべて素数でないと判定する
        for j in range(i * 2, n + 1, i):
            isPrime[j] = False

    # 最終的に素数かどうかのリストを返す
    return isPrime


# --- 実行例 ---
if __name__ == "__main__":
    n = 813
    isPrime = eratosthenes(n)

    # 1 から n までの数を表示し、それぞれ素数かどうかを出力
    for i in range(1, n + 1):
        if isPrime[i]:
            print(f"{i} は素数")
        else:
            print(f"{i} は素数ではない")
