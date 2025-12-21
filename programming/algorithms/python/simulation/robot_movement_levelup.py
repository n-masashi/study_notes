# coding: utf-8
# ============================================
# ロボット移動＆レベルアップシミュレーション
# --------------------------------------------
# 無限座標系の工場にN台のロボットが存在。
# 各ロボットはレベル(1～4)に応じて移動距離が異なる。
# 工具箱10カ所が設置されており、移動後に工具箱の位置に止まるとレベルアップ（最大4）。
#
# 入力：
# ・H, W：初期座標の上限（ただし、実際は無限座標系で移動制限なし）
# ・N：ロボット数
# ・K：移動回数
# ・工具箱の座標（x, y）10行
# ・ロボットの初期座標(x, y)とレベル
# ・移動指示：ロボット番号と移動方向(N, S, E, W)
#
# 出力：
# ・K回の移動後の各ロボットの最終座標とレベルを出力
#
# --------------------------------------------
# ▼ 実装ポイントと引っ掛かった点
# --------------------------------------------
# 1. 移動範囲の制限なし
#    - 問題文でH, Wは初期位置の上限のみで、移動時に範囲制限はない（ここを移動範囲制限と勘違いして時間がかかった）
#    - そのため移動時の座標クリップ（最大値・最小値制限）は不要
# ============================================

import sys
max_y, max_x, robotcnt, jobcnt = map(int,sys.stdin.readline().strip().split())
robots = []
levelup_zone = []
level_moves = {1: 1, 2: 2, 3: 5, 4: 10}

class Robot:
    def __init__(self, max_y, max_x, y, x, level):
        self.level = level
        self.move = level_moves.get(level)      
        self.max_y = max_y
        self.max_x = max_x      
        self.y = y
        self.x = x

    def levelup(self):
        if self.level < 4:
            self.level += 1
            self.move = level_moves.get(self.level)

    def move_job(self, direction):
        if direction == "N":
            self.y -= self.move

        elif direction == "S":
            self.y += self.move
        
        elif direction == "E":
            self.x += self.move
          
        elif direction == "W":
            self.x -= self.move

# 工具箱座標は入力通り(x, y)の順で保存
for _ in range(10):
    x, y = map(int,sys.stdin.readline().strip().split())
    levelup_zone.append((x, y))

# ロボットは入力(x, y, level)だが
# Robotクラスは(y, x, level)で保持。座標の取り違えに注意
for _ in range(robotcnt):
    x, y, level = map(int,sys.stdin.readline().strip().split())
    robots.append(Robot(max_y, max_x, y, x, level))

# 移動実行とレベルアップ判定
for _ in range(jobcnt):
    num, direction = sys.stdin.readline().strip().split()
    index = int(num) - 1
    start_x, start_y = robots[index].x, robots[index].y 
    robots[index].move_job(direction)
    
    # 移動があった場合のみレベルアップ判定
    if start_x != robots[index].x or start_y != robots[index].y:
        for zone in levelup_zone:
            # 座標比較は(x, y)の順で行う
            if zone[0] == robots[index].x and zone[1] == robots[index].y:
                robots[index].levelup()
                break
        
# 結果出力
for robot in robots:
    print(robot.x, robot.y, robot.level)

 ============================================
# ▼ 模範解答との違いと改善ポイント
# --------------------------------------------

# ① 移動処理の座標管理方法
# ・自分のコード：y, xの順でRobotに座標を保持。移動も方向別にif文で処理。
# ・模範解答：移動方向を辞書（dirs）でベクトル化し、移動を一行で計算。コードが簡潔で拡張しやすい。

# ② レベルアップ判定の座標比較方法
# ・自分：forループでレベルアップゾーンの(x,y)とロボット座標を逐一比較。
# ・模範解答：工具箱座標をリストにし、移動後の座標がその中にあるか点在チェック。
#   （setを使うなど高速化も可能）

# ③ 移動範囲の制限
# ・自分：max_y, max_xを保持しているが、移動時に座標制限を実装していない（問題文どおり）。
# ・模範解答：移動範囲の制限がないことを前提に実装。

# ④ レベルアップの最大値制御
# ・どちらもレベル4を超えないよう制御済み。

# ⑤ クラス設計の差異
# ・模範解答は、座標取得用のget_pointメソッドや出力用printメソッドを持ち、役割が分かりやすい。
# ・自分のコードはシンプルに移動・レベルアップのみ実装。

# ⑥ 改善ポイントまとめ（任意）
# ・移動方向を辞書化してシンプルに
# ・工具箱座標をsetにして高速検索
# ・Robotクラスに座標取得・表示メソッドを追加すると可読性UP
# ・max_y, max_xの変数は不要なら削除し、混乱防止
# ・座標の(x,y)と(y,x)の取り扱いは特に注意し、コメントで明示すると良い

# ============================================
