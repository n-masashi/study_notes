import math

def is_prime_trial_division(n):
    """
    試し割り法（Trial Division）による素数判定
    
    - 入力された整数 n が素数かどうか判定する。
    - 2から √n までの整数で割り切れるかを調べる。
    - 割り切れれば素数ではない、割り切れなければ素数。
    - シンプルだが大きな数には遅い。

    Args:
        n (int): 判定したい整数

    Returns:
        bool: 素数なら True、そうでなければ False
    """
    if n == 1:
        return False  # 1は素数ではない

    # 2から√nまでの整数で割り切れるかチェック
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 割り切れるので素数ではない
    
    return True  # 割り切れる数がなければ素数


if __name__ == "__main__":
    # テスト例
    test_nums = [1, 2, 3, 4, 17, 20, 7919]

    for num in test_nums:
        result = is_prime_trial_division(num)
        print(f"{num} は{'素数' if result else '素数ではない'}")
