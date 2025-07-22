def selection_sort(arr):
    """
    選択ソート：
    配列の中から最小（最大）値を探し、それを先頭の要素と交換する操作を繰り返して昇順に整列するアルゴリズム。
    学習中にロジックとしてメモ。処理的に効率は良くない。ソートしたいならsort()等を使えばいい。
    """
    n = len(arr)  # 配列の長さを取得

    for i in range(n):
        min_index = i  # まずは i 番目の要素を最小値と仮定する

        # i 番目の要素以降の要素を順に調べる
        for j in range(i + 1, n):
            # より小さい値が見つかったら、そのインデックスを更新
            if arr[j] < arr[min_index]:
                min_index = j

        # ループが終わった時点で min_index が示すのは
        # i 番目以降で最小の値のインデックス

        # i 番目の値と最小値を交換する
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # ここまでで配列の最初から i 番目までは昇順に整列済み

    return arr  # 昇順に整列した配列を返す


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Before:", data)
    sorted_data = selection_sort(data)
    print("After:", sorted_data)
