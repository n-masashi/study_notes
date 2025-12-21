# coding: utf-8
# ============================================
# 格闘ゲームシミュレーション
# --------------------------------------------
# N人のプレイヤーが、それぞれHPと3つの技（発生フレーム・攻撃力）を持つ。
# 技には強化技（F=0, A=0）もあり、使うと他の全ての技が強化される。
#
# K回の対戦があり、それぞれ攻撃者と反撃者の技が与えられる。
#
# 対戦ルール：
# ・どちらかが退場済み（HP≤0）の場合、何も起こらない
# ・強化技 vs 攻撃技：強化側は強化し、攻撃をそのまま受ける
# ・強化技 vs 強化技：両者強化のみ
# ・攻撃技 vs 攻撃技：
#     - フレームが小さい方が勝ち、相手にダメージ
#     - 同フレームならお互いノーダメージ
#
# 最終的にHP>0で残っているプレイヤー数を出力する
# ============================================

# プレイヤー数と攻撃回数を取得
player_cnt, atk_cnt = map(int, input().split())
players = []

# プレイヤー1人分の状態と行動をまとめたクラス
class Player:
    def __init__(self, hp, a_frame, a_atk, b_frame, b_atk, c_frame, c_atk):
        # 各プレイヤーの体力と3つの技の性能（発生フレーム・攻撃力）
        self.hp = hp
        self.a_frame = a_frame
        self.b_frame = b_frame
        self.c_frame = c_frame
        self.a_atk = a_atk
        self.b_atk = b_atk
        self.c_atk = c_atk
    
    # 技番号に応じて対応する発生フレームと攻撃力を返す
    def frames(self, skill_num):
        if skill_num == 1:
            return self.a_frame, self.a_atk
        elif skill_num == 2:
            return self.b_frame, self.b_atk
        elif skill_num == 3:
            return self.c_frame, self.c_atk  
            
    # 強化技：他の技のフレームを-3（最小1）、攻撃力を+5
    def kyoka(self):
        if self.a_frame != 0: 
            self.a_frame = max(self.a_frame - 3, 1)
            self.a_atk += 5
        if self.b_frame != 0:
            self.b_frame = max(self.b_frame - 3, 1)
            self.b_atk += 5
        if self.c_frame != 0:
            self.c_frame = max(self.c_frame - 3, 1)
            self.c_atk += 5    

    # ダメージ処理
    def damage(self, dmg):
        self.hp -= dmg
        

# プレイヤー情報を読み込み、Playerインスタンスとしてリストに格納
for _ in range(player_cnt):
    hp, a_frame, a_atk, b_frame, b_atk, c_frame, c_atk = map(int, input().split())
    players.append(Player(hp, a_frame, a_atk, b_frame, b_atk, c_frame, c_atk))

# 各攻撃のシミュレーション
for _ in range(atk_cnt):
    player_a, skill_a, player_b, skill_b = map(int, input().split())

    # インデックス調整
    a = players[player_a - 1]
    b = players[player_b - 1]

    # 退場しているプレイヤーは無視
    if a.hp <= 0 or b.hp <= 0:
        continue    

    # 技情報を取得
    a_frame, a_atk = a.frames(skill_a)
    b_frame, b_atk = b.frames(skill_b)

    # 攻撃・強化の処理分岐
    if a_frame == 0 and b_frame != 0:
        a.kyoka()
        a.damage(b_atk)
    elif b_frame == 0 and a_frame != 0:
        b.kyoka()
        b.damage(a_atk)
    elif a_frame == 0 and b_frame == 0:
        a.kyoka()
        b.kyoka()
    elif a_frame > b_frame:
        a.damage(b_atk)
    elif a_frame < b_frame:
        b.damage(a_atk)
    # 同時なら何も起こらない

# 生き残っているプレイヤーの数をカウント
count = 0
for player in players:
    if player.hp > 0:
        count += 1

# 結果出力
print(count)

# ============================================
# ▼ 模範解答との違いと改善ポイント
# --------------------------------------------

# ① 技の管理方法
# ・自分のコード：各技を個別の変数（a_frame, b_frame...）で管理
# ・模範解答：f[], a[] というリストで管理 → ループでの操作が簡潔になる

# ② 生存判定
# ・自分：毎回 player.hp > 0 をチェック
# ・模範：alive フラグを持たせ、退場した時点で False → 以降はチェック高速＆明快

# ③ 技番号処理
# ・自分：frames() メソッドで if によって技情報を切り替え
# ・模範：リストアクセス (f[i], a[i]) で O(1) に技情報取得 → 無駄な分岐がない

# ④ 強化処理
# ・自分：各技ごとに if 文で強化
# ・模範：ループでまとめて処理 → 短く、保守性も高い

# ⑤ 共通点
# ・どちらも仕様通りに正しく動作し、処理速度も問題ない

# ⑥ 改善ポイントまとめ（任意で行う）
# ・技データをリストにすることでループ処理・拡張性を向上
# ・プレイヤーに alive フラグを導入すれば、生死チェックの重複を避けられる
# ・メソッド内の if 分岐をリスト活用で減らすと、よりスッキリした設計になる

