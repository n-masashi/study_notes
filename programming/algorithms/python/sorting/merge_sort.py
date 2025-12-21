INF = 1000000001  # とても大きな値（番兵として使う）
count = 0         # 比較や移動の回数を数えるグローバル変数

def print_array(a):
    """ 配列の中身をスペース区切りで表示する """
    print(*a)

def merge(a, left, mid, right):
    """
    マージ処理（merge関数）

    - a[left:right] の範囲を左右2つの部分配列に分割し、それぞれソート済みと仮定してマージする
    - 番兵（とても大きな数）を最後に入れて比較の範囲外を防ぐ
    - 左右の先頭から比較し、小さい方を元の配列に書き戻していく
    - 右側の値を選んだ回数をグローバル変数 count にカウントする
    """
    global count

    l = a[left:mid]   # 左半分のコピー
    r = a[mid:right]  # 右半分のコピー

    l.append(INF)  # 左配列の最後に番兵を追加
    r.append(INF)  # 右配列の最後に番兵を追加

    lindex, rindex = 0, 0  # 左右配列の先頭位置

    for i in range(left, right):
        if l[lindex] < r[rindex]:
            a[i] = l[lindex]
            lindex += 1
        else:
            a[i] = r[rindex]
            rindex += 1
            count += 1  # 右配列から選んだ回数をカウント

def merge_sort(a, left, right):
    """
    マージソート（再帰関数）

    - 配列を半分に分けてそれぞれを再帰的にソート
    - サイズが1以下になったら終了（分割終了条件）
    - 分割した左右を merge 関数でマージする
    """
    if left >= right - 1:
        return

    mid = (left + right) // 2  # 分割の中間点

    merge_sort(a, left, mid)   # 左半分をソート
    merge_sort(a, mid, right)  # 右半分をソート

    merge(a, left, mid, right) # 左右をマージ

# --- 実行部分 ---
if __name__ == "__main__":
    n = int(input())                  # 配列の要素数を入力
    a = [int(x) for x in input().split()]  # 配列を入力

    merge_sort(a, 0, n)  # マージソート開始（配列全体）

    print_array(a)       # ソート結果を表示
    print(f"右配列から選んだ回数: {count}")  # カウント結果を表示
