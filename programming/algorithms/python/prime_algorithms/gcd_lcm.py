
# --- 素因数分解関数 ---
def factorize(n):
    """
    整数 n を素因数分解し、
    素因数をキー、指数（何回割れるか）を値とする辞書を返す。

    例: 12 -> {2: 2, 3: 1}
    """
    primes = {}
    # 2 から n まで試し割り（小さい数から割っていく）
    for i in range(2, n + 1):
        if n % i != 0:
            continue  # 割り切れなければスキップ

        exp = 0  # 指数カウント用
        while n % i == 0:
            exp += 1
            n //= i  # 割った結果を n に代入

        primes[i] = exp  # 素因数と指数を記録

    # ループ終了後に n が 1 でなければ、n 自身が素数
    if n != 1:
        primes[n] = 1

    return primes


# --- 最大公約数を計算する関数 ---
def calc_gcd(a, b):
    """
    2つの整数 a, b の最大公約数(GCD)を
    素因数分解の結果を利用して計算する。

    共通の素因数の指数の小さい方を掛け合わせて求める。
    """
    table_a = factorize(a)
    table_b = factorize(b)
    table_gcd = {}

    for prime in table_a:
        if prime in table_b:
            # 共通素因数の指数の小さい方を使う
            exp = min(table_a[prime], table_b[prime])
            table_gcd[prime] = exp

    gcd = 1
    for prime, exp in table_gcd.items():
        for _ in range(exp):
            gcd *= prime

    return gcd


# --- 最小公倍数を計算する関数 ---
def calc_lcm(a, b):
    """
    2つの整数 a, b の最小公倍数(LCM)を
    素因数分解の結果を利用して計算する。

    素因数の指数は大きい方を使い掛け合わせる。
    """
    table_a = factorize(a)
    table_b = factorize(b)
    table_lcm = {key: val for key, val in table_a.items()}

    for prime in table_b:
        exp = table_b[prime]
        if prime in table_lcm:
            exp = max(exp, table_lcm[prime])

        table_lcm[prime] = exp

    lcm = 1
    for prime, exp in table_lcm.items():
        for _ in range(exp):
            lcm *= prime

    return lcm


# --- 動作確認用の実行部分 ---
if __name__ == "__main__":
    a = 30
    b = 12

    gcd = calc_gcd(a, b)
    print(f"{a} と {b} の最大公約数は {gcd}")

    lcm = calc_lcm(a, b)
    print(f"{a} と {b} の最小公倍数は {lcm}")
