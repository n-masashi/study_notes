def linear_search(arr, target):
    """
    線形探索
    配列arrからtargetを探し、見つかったらインデックスを返す。見つからなければ-1を返す。
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

if __name__ == "__main__":
    data = [4, 2, 7, 1, 3]
    target = 7

    index = linear_search(data, target)
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found in the list")
