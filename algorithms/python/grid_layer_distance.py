"""
2次元座標上での「中心からの距離（レイヤー）」を使った処理の学習用メモ

問題例：
- N x N グリッド（正方形）
- 各マスに石が積まれていて、中心からの距離に応じて積むべき石の数が決まっている
- 実際の石の数から、積みすぎた分（余分な石の数）を計算する
"""

def calculate_excess_stones(grid):
    N = len(grid)
    center = N // 2  # 中心座標（0-indexed）

    total_excess = 0

    for i in range(N):
        for j in range(N):
            # 中心からの距離を「層」として計算
            layer = max(abs(i - center), abs(j - center))

            # 層に応じた本来の石の数（中心: 最大、外側: 1）
            expected = (N + 1) // 2 - layer

            # 運び出すべき石の数（期待値より多い分だけ）
            total_excess += grid[i][j] - expected

    return total_excess
  

# --- 動作確認用サンプル ---

if __name__ == "__main__":
    # サンプル入力（5x5 グリッド）
    grid = [
        [3, 3, 3, 2, 6],
        [1, 9, 4, 5, 3],
        [1, 8, 4, 6, 5],
        [4, 9, 2, 6, 8],
        [7, 5, 8, 1, 6]
    ]

    result = calculate_excess_stones(grid)
    print("余分な石の合計:", result)  # 期待される出力: 84
