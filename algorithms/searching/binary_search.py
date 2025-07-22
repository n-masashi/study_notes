def binary_search(arr, target):
    """
    二分探索
    ソート済み配列arrからtargetを探し、見つかったらインデックスを返す。見つからなければ-1を返す。
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
          
        # 真ん中の値がtargetより小さければ、左半分はすべて小さいので除外
        elif arr[mid] < target:
            left = mid + 1
          
        # 逆に真ん中の値がtargetより大きければ、右半分は除外
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    data = [1, 2, 3, 4, 7]
    target = 7

    index = binary_search(data, target)
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found in the list")


    # 文字列の比較は辞書順で行われるので、文字列でも二分探索可能
    # 例:
    # print("apple" < "banana")  # True
    # print("cat" > "car")       # True
    # print("dog" == "dog")      # True
  
    data = ["apple", "banana", "cherry", "dragonfruits"]
    target = "cherry"

    index = binary_search(data, target)
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found in the list")
