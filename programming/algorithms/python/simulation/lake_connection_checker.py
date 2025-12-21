# -----------------------------------------------
# ■ 実装概要
# ある2次元マップ上に存在する湖のつながりを保ったまま、
# どのマスに建物を建てられるかを調べる問題に対する解法。
# 条件：湖を1マス消しても、湖全体が分断されないこと。
#
# ■ 実装のポイント
# ・各マスを1つずつ除外し、その状態でDFSにより湖の連結性を判定。
# ・除外前と除外後の湖マス数を比較し、つながりが失われていないかを検証。
# ・各マスに対して上記を繰り返し、建設可能なマスをカウント。
#
# ■ 改善点
# ・再帰でのDFSのグローバル変数を排除して関数の再利用性を向上。
# ・湖の開始点探索を関数化し、可読性を向上。
# ・方向ベクトルを(dx, dy)で整理して簡潔に。
# -----------------------------------------------


# ======= オリジナル実装（自力解答） =======
h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]
visit_maps = [[False] * w for _ in range(h)]
lake_total = 0
lake_count = 0
ngpoint = 0

updown = [-1, 1, 0, 0]
leftright = [0, 0, -1, 1]

# 湖がつながってるかどうかの判定関数（再帰 DFS）
def lake_connection(y, x):
    global lake_count
    visit_maps[y][x] = True
    lake_count += 1
    
    for i in range(4):
        new_y = y + updown[i]
        new_x = x + leftright[i]
        if new_y < 0 or new_y >= h or new_x < 0 or new_x >= w:
            continue
        if not visit_maps[new_y][new_x] and maps[new_y][new_x] == "#":
            lake_connection(new_y, new_x)

for i in range(h):
    for j in range(w):
        if maps[i][j] == "#":
            maps[i][j] = "."
            lake_total = sum(row.count("#") for row in maps)
            
            start_y, start_x = -1, -1
            for k in range(h):
                for l in range(w):
                    if maps[k][l] == "#":
                        start_y, start_x = k, l
                        break
                if start_y != -1:
                    break   
                
            lake_connection(start_y, start_x)
            if lake_total != lake_count:
                ngpoint += 1
                
            maps[i][j] = "#"
            lake_total = 0
            lake_count = 0
            visit_maps = [[False] * w for _ in range(h)]

print(h*w - ngpoint)


# ======= 改善後の実装（リファクタリング） =======

def count_connected_lake(y, x, grid, visited):
    stack = [(y, x)]
    visited[y][x] = True
    count = 1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        cy, cx = stack.pop()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == "#":
                visited[ny][nx] = True
                stack.append((ny, nx))
                count += 1
    return count

def get_first_lake(grid):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                return i, j
    return -1, -1  # 念のため

h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]

ng_count = 0

for i in range(h):
    for j in range(w):
        if maps[i][j] == "#":
            maps[i][j] = "."
            total_lake = sum(row.count("#") for row in maps)
            sy, sx = get_first_lake(maps)
            visited = [[False] * w for _ in range(h)]
            connected = count_connected_lake(sy, sx, maps, visited)
            if total_lake != connected:
                ng_count += 1
            maps[i][j] = "#"

print(h * w - ng_count)
