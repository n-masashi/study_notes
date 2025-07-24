# 問題：各勇者にステータスがあり、様々なイベントに応じて能力が変化する。全イベント処理後のステータスを出力する。
# 分類：シミュレーション・状態管理（イベント処理）

# 入力例：
# 1 3
# 23 128 533 552 44 69 420
# 1 muscle_training 565 241
# 1 study 132
# 1 levelup 379 585 4 145 276 8

# 出力例：
# 24 1072 1359 556 189 477 428

# ───────────────────────────────────────────────────────────────

# 勇者の人数とイベントの回数を受け取る（高速入力にしたいなら sys.stdin.readline を推奨らしい）
pcnt, ecnt = map(int, input().split())
player_list = []  # 勇者たちのリストを保持

# 各勇者のステータスを保持するクラス
class Player:
    def __init__(self, lvl, H, A, D, S, I, L):
        self.lvl = lvl  # レベル
        self.H = H      # 体力
        self.A = A      # 攻撃力
        self.D = D      # 防御力
        self.S = S      # 素早さ
        self.I = I      # 賢さ
        self.L = L      # 運

    # イベントに応じたステータス更新メソッド
    def levelup(self, H, A, D, S, I, L):
        self.lvl += 1
        self.H += H
        self.A += A
        self.D += D
        self.S += S
        self.I += I
        self.L += L

    def muscle_training(self, H, A): 
        self.H += H
        self.A += A

    def running(self, D, S):
        self.D += D
        self.S += S        

    def study(self, I):
        self.I += I

    def pray(self, L): 
        self.L += L

# 勇者の初期ステータスを読み取り、リストに格納
for _ in range(pcnt):
    lvl, H, A, D, S, I, L = map(int, input().split())
    player_list.append(Player(lvl, H, A, D, S, I, L))
    # 改善余地：名前付きtupleやdataclassを使うと簡潔になる

# イベントを読み取って対象の勇者に反映
for _ in range(ecnt):
    event_str = input().split()
    index = int(event_str[0]) - 1  # 1-indexed → 0-indexed に変換
    event = event_str[1]

    if event == "levelup":
        H, A, D, S, I, L = map(int, event_str[2:])
        player_list[index].levelup(H, A, D, S, I, L)

    elif event == "muscle_training":
        H, A = map(int, event_str[2:])
        player_list[index].muscle_training(H, A)

    elif event == "running":
        D, S = map(int, event_str[2:])
        player_list[index].running(D, S)

    elif event == "study":
        I = int(event_str[2])
        player_list[index].study(I)

    elif event == "pray":
        L = int(event_str[2])
        player_list[index].pray(L)

# 最終的な各勇者のステータスを出力
for p in player_list:
    print(p.lvl, p.H, p.A, p.D, p.S, p.I, p.L)
    # 改善余地：出力フォーマットをf-stringなどにして見やすくしても良い

# ───────────────────────────────────────────────────────────────
# - 各勇者の状態（ステータス）を Player クラスで表現
# - 各イベントは定義済みのメソッドで処理
# - 勇者番号は1-indexedなので、処理時に0-indexedに変換（-1）
# - 入力量が多いため、sys.stdin.readline() の利用で高速化可能
# ───────────────────────────────────────────────────────────────
