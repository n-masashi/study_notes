def quick_sort(a, left, right, depth=0):
    """
    クイックソート（Quick Sort）

    - 「pivot（基準値）」を決めて配列を分割し、再帰的に整列するアルゴリズム。
    - pivotより小さい値は左側、大きい値は右側に集める。
    - 配列の部分ごとにこの操作を繰り返し、効率的に整列する。
    - 再帰の深さに応じてインデント表示し、処理の流れがわかりやすくなる。
    - 交換回数をカウントし、動作の目安を記録する。

    引数:
        a     : ソート対象のリスト
        left  : 部分配列の開始インデックス（含む）
        right : 部分配列の終了インデックス（含まない）
        depth : 再帰の深さ（表示用）

    動作概要:
        1. 配列の範囲が1以下なら終了（整列済み）。
        2. 右端の値をpivotに選ぶ。
        3. 左から順にpivotより小さい値を左端から詰める。
        4. pivotを正しい位置に移動する。
        5. pivotより左側・右側の部分配列に対して再帰的に同様の処理を行う。
    """

    global count

    indent = "  " * depth  # 処理の深さに応じた空白を作る（見やすさ向上）

    if left >= right - 1:
        print(f"{indent}部分配列[{left}:{right}]は1つ以下なので終了")
        return

    pivot = a[right - 1]  # 右端の値をpivotに設定
    print(f"{indent}pivot = {pivot} を選択（範囲: {left}〜{right-1}）")
    cur_index = left  # pivotより小さい値を詰める位置の開始点

    for i in range(left, right - 1):
        if a[i] < pivot:
            a[i], a[cur_index] = a[cur_index], a[i]  # pivotより小さい値を左側へ移動
            cur_index += 1
            count += 1  # 交換回数をカウント
        print(f"{indent}  比較 i={i}, 配列: ", end="")
        print(*a)

    # pivotを正しい位置(cur_index)に移動
    a[right - 1], a[cur_index] = a[cur_index], pivot
    print(f"{indent}pivot {pivot} を位置 {cur_index} に移動 => ", end="")
    print(*a)

    # pivotより左側の部分配列に対して再帰処理
    quick_sort(a, left, cur_index, depth + 1)
    # pivotより右側の部分配列に対して再帰処理
    quick_sort(a, cur_index + 1, right, depth + 1)


if __name__ == "__main__":
    n = 6
    a = [4, 2, 6, 1, 3, 5]

    print("元の配列:")
    print(*a)
    print("クイックソート開始\n")

    quick_sort(a, 0, n)

    print("\n整列後の配列:")
    print(*a)
    print(f"交換回数: {count}")
