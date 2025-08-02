def insertion_sort(arr):
    """
    挿入ソート：
    配列の要素を左から順に見て、前の部分配列に対して適切な位置に挿入していくことで整列させるアルゴリズム。
    バブルソートよりも交換回数が少なく、部分的に整列されている配列に対しては比較的効率が良い。
    あくまで学習目的で実装。実用では組み込みのsort()を使うのがよい。
    """
    n = len(arr)

    for i in range(1, n):
        # 現在注目している要素
        current = arr[i]

        # その左側の要素たち（整列済み）を見ていく
        j = i - 1

        # current より大きい値を右へずらしていく
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        # 最後に、ずらした隙間に current を挿入
        arr[j + 1] = current

    return arr


if __name__ == "__main__":
    data = [5, 3, 8, 6, 2]
    print("Before:", data)
    sorted_data = insertion_sort(data)
    print("After:", sorted_data)
