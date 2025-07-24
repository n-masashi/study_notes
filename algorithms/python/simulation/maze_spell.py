# 問題：迷路のような地点を指示に従って移動し、通過した文字をつなげて呪文を完成させる
# 分類：シミュレーション・状態遷移（探索は不要）

# 入力例：
# 4 4 1
# h 2 4
# o 3 1
# g 4 2
# e 1 2
# 1
# 1
# 1
# 2

# 出力：
# hogeo

# ───────────────────────────────────────────────────────────────

# 入力：waycnt → 地点の数, movcnt → 移動回数, start → 開始地点番号
waycnt, movcnt, start = map(int, input().split())

# 地点情報（Mapオブジェクト）を格納するリスト
maps = []

# 出力用の文字列リスト（各地点のアルファベットを記録）
results = []

# クラス：各地点を表す（地点にある文字と2方向の道情報）
class Map:　#今回Mapにしたけど標準ライブラリと名前がバッティングするからやめたほうがいいらしい
    def __init__(self, char, way1, way2):
        self.char = char      # この地点にあるアルファベット
        self.waya = way1      # 道1（移動指示が1のとき進む先）
        self.wayb = way2      # 道2（移動指示が2のとき進む先）

# 各地点の入力情報を読み込んで Map オブジェクトを作成
for _ in range(waycnt):
    inputvalue = input().split()
    char = inputvalue[0]
    waya = int(inputvalue[1])
    wayb = int(inputvalue[2])
    maps.append(Map(char, waya, wayb))

# index：現在位置（入力は1-indexedなので -1 する）
index = start - 1

# 最初の地点の文字を記録
results.append(maps[index].char)

# 移動指示に従って移動し、通過地点の文字を記録していく
for _ in range(movcnt):
    input_num = int(input())  # 移動指示（1 または 2）
    if input_num == 1:
        index = maps[index].waya - 1
    else:
        index = maps[index].wayb - 1
    results.append(maps[index].char)

# 最後に呪文（結果文字列）を出力
print("".join(results))

# ───────────────────────────────────────────────────────────────

# - 状態を保持するためにクラスを活用
# - グラフのように見えるが探索ではなくシーケンシャルな状態遷移
# - 入力インデックスの -1 に注意（1-indexed → 0-indexed 変換）
