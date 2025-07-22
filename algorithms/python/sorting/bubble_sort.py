def bubble_sort(arr):
    """
    バブルソート：
    隣り合う要素を比較して大小が逆なら交換し、これを繰り返して配列を昇順に整列するアルゴリズム。
    学習中に得たロジックとしてメモ。ソートしたいならsort()等を使えばいい。処理的にバブルソートは非効率。
    """
    n = len(arr)  # 配列の長さを取得

    # 配列の要素数だけ繰り返す
    for i in range(n):
        # i回目の繰り返しでは、末尾のi個はすでに整列済みなので無視できる
        # そのため、比較は n - i - 1 までにする
        for j in range(0, n - i - 1):
            # 隣り合う要素を比較
            if arr[j] > arr[j + 1]:
                # 左側の要素が大きければ、2つの要素を交換する（入れ替える）
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # これにより、大きい値が右に「泡のように」移動していく

    # 全ての比較と交換が終わった後、arrは昇順に整列されている
    return arr

if __name__ == "__main__":
    data = [5, 3, 8, 6, 2]
    print("Before:", data)
    sorted_data = bubble_sort(data)
    print("After:", sorted_data)
