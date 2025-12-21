# 整数 n を素因数分解し、「素因数: 指数」の辞書を返す関数
def factorize(n):
    # 結果を保存する辞書（キー: 素因数、値: 指数）
    primes = {}

    # 試し割り法（Trial Division）により、2 から sqrt(n) までの整数で割ってみる
    for i in range(2, int(n**0.5) + 1):
        if n % i != 0:
            continue  # 割り切れなければ次へ

        exp = 0  # 指数（その素因数が何回かけられるか）
        while n % i == 0:
            exp += 1
            n //= i  # 割った結果を n に戻す

        primes[i] = exp  # 辞書に追加

    # 最後に n が 1 でなければ、それ自体が素数
    if n != 1:
        primes[n] = 1

    return primes


# 整数 n の約数の個数を計算する関数
def calc_num_of_divisors(n):
    primes = factorize(n)

    # 約数の個数は (e1+1)*(e2+1)*...*(ek+1)
    # ※ 各素因数の指数 + 1 の積
    num_of_factors = 1
    for exp in primes.values():
        num_of_factors *= (exp + 1)

    return num_of_factors


# 入力を受け取り、結果を表示
n = int(input("整数を入力してください: "))

# 素因数分解の結果を表示
prime_table = factorize(n)
print(f"{n} の素因数分解結果:")
for prime, exp in prime_table.items():
    print(f"{prime}^{exp}")

# 約数の個数を表示
divisor_count = calc_num_of_divisors(n)
print(f"{n} の約数の個数は {divisor_count} 個です")
