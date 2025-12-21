def insertion_sort(a, n, h):
    """
    間隔 h の挿入ソート（Shell Sort 用）

    - h 個ずつ離れた要素に対して挿入ソートを行う
    - 広く離れた要素を先に並べておくことで、後の整列が速くなる
    - 移動（右にずらした）回数をカウントして出力する
    """

    num_of_move = 0

    for i in range(h, n):
        x = a[i]
        j = i - h

        while j >= 0 and a[j] > x:
            a[j + h] = a[j]
            j -= h
            num_of_move += 1

        a[j + h] = x

    print(f"h = {h} のときの移動回数: {num_of_move}")


def shell_sort(a, n, h, k):
    """
    Shell Sort（シェルソート）

    - h[] という複数の間隔を使って挿入ソートを繰り返す
    - 通常の挿入ソートより高速化される
    - 最適な間隔の選び方は未解決問題（研究中）
    """

    for i in range(k):
        insertion_sort(a, n, h[i])


# --- 実行部分 ---
if __name__ == "__main__":
    # 入力例
    # 数列の要素数
    n = 8
    # ソート対象の配列
    a = [5, 1, 4, 7, 2, 6, 3, 8]
    # 間隔の数
    k = 3
    # 使用する間隔列
    h = [5, 3, 1]  # 一般的なShell sortの例（大きい順）

    print("元の配列:", a)
    shell_sort(a, n, h, k)
    print("整列後の配列:", a)
