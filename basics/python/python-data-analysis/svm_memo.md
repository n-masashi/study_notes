# SVM（サポートベクターマシン）と描画の詳しいメモ

## 1. SVMってそもそも何？
- **SVM = Support Vector Machine**
- データを分類するためのモデル
- 2種類のデータ（赤・青など）を分ける境界線を数学的に決める
- 特徴：
  1. 境界線を「両側のデータからできるだけ離れるように」決める（マージン最大化）
  2. 2次元なら線、3次元以上なら面
  3. 線形で分けられない場合でも、カーブ状に変換して分けられる

---

## 2. 学習した流れ
1. 2次元座標に点を置く
2. 青チーム・赤チームに手で分ける
3. SVMで境界線を学習
4. 新しい点の赤・青を予想
5. 境界線を描く

---

## 3. 使ったライブラリ
- `numpy`：数字や座標を扱う箱
- `matplotlib.pyplot`：点や線を描く
- `random`：ランダムな数字を作る
- `sklearn.svm`：SVMモデルを便利に使えるライブラリ

---

## 4. データ作成
```python
N = 15
train_X = np.array([[random.randint(0, 100), random.randint(0, 100)] for i in range(N)])
```
- 15個の点を作る
- x,y座標は0～100のランダム
- `train_X` に座標を格納

---

## 5. 点を描く（詳しく）
```python
for i in range(len(train_X)):
    plt.plot(train_X[i][0], train_X[i][1], 'o', color='blue')
    plt.annotate(i, (train_X[i][0], train_X[i][1]), size=20)
```
### 解説
- `for i in range(len(train_X)):` → 点を1つずつ順番に処理  
- `plt.plot(x, y, 'o', color='blue')`  
  - 点を丸で描く  
  - `'o'` = 丸マーク  
  - `color='blue'` = 青色  
- `plt.annotate(text, (x, y), size=20)`  
  - 点のそばに文字を描く  
  - `text = i` → 点番号  
  - `(x, y)` → 文字の位置  
  - `size=20` → 文字サイズ

---

## 6. 手で分類
```python
train_y = np.array([0 for i in range(N)])
train_y[1] = train_y[2] = train_y[3] = train_y[4] = train_y[5] = train_y[6] = train_y[11] = 1
```
- `0` = 青チーム, `1` = 赤チーム

---

## 7. 分類したデータを描く（詳しく）
```python
colors = ['blue', 'red']
for i in range(len(train_X)):
    plt.plot(train_X[i][0], train_X[i][1], 'o', color=colors[train_y[i]])
    plt.annotate(i, (train_X[i][0], train_X[i][1]), size=20)
```
- `colors[train_y[i]]` → 0なら青、1なら赤

---

## 8. テストデータで予想
```python
test_X = np.array([[30, 60]])
plt.plot(test_X[0][0], test_X[0][1], 'x', color='black')
plt.annotate('test', (test_X[0][0], test_X[0][1]), size=20)
```
- `plt.plot(..., 'x')` → ×印で描画  
- `color='black'` → 黒  
- `plt.annotate` で「test」と表示

---

## 9. SVMで学習
```python
clf = svm.SVC(gamma=0.0001, C=1)
clf.fit(train_X, train_y)
```
- `gamma`, `C` → 境界の柔らかさを調整するパラメータ
- `fit` → 学習

---

## 10. SVMで分類
```python
test_y = clf.predict(test_X)
```

### 解説
- `clf.predict()` は **学習済みのSVMモデルに新しい点を渡して、どちらのチームかを予想する関数** です
- `test_X` の各点に対して：
  1. 事前に学習した境界線を見て
  2. 点が境界のどちら側にあるかを計算
  3. 青（0）か赤（1）かを返す
- 返り値 `test_y` は **点ごとの予想ラベルの配列** になります
  - 例：`test_y = [0, 1, 0]` → 1つ目の点は青、2つ目は赤、3つ目は青

### イメージ
```
境界線
    赤
    -----
    青
```
- この線を基準に「上か下か」を自動で判断するのが `predict` です

### まとめ
- `fit()` で学習したモデルに `predict()` で新しいデータを渡す
- すると **「赤か青か」を自動判定** してくれる
- 人間が「赤にする」「青にする」と決めなくてもよい

---

## 11. 複数テストデータで描画（詳しく）
```python
test_X = np.array([[30, 60], [90, 90], [50, 50], [60, 40]])
test_y = clf.predict(test_X)
for i in range(len(test_X)):
    plt.plot(test_X[i][0], test_X[i][1], 'x', color=colors[test_y[i]])
    plt.annotate('test', (test_X[i][0], test_X[i][1]), size=20)
```
- 点ごとに色を決める（青/赤）
- ×印で描画
- 「test」とラベルを表示

---

## 12. 決定境界を描く（詳しく）
```python
x = np.linspace(0, 100, 30)
y = np.linspace(0, 100, 30)
yy, xx = np.meshgrid(y, x)
xy = np.vstack([xx.ravel(), yy.ravel()]).T
P = clf.decision_function(xy).reshape(xx.shape)
plt.contour(xx, yy, P, colors='k', levels=[0], alpha=0.5, linestyles=['-'])
```
- `np.linspace(0,100,30)` → 0～100を30分割  
- `np.meshgrid(y, x)` → グリッド作成  
- `clf.decision_function(xy)` → 各点がどちら側かの数値を計算  
- `plt.contour(...)` → 等高線のように境界線を描く

---

## 13. まとめ
- SVM = データを分類するモデル（境界線を決める計算）
- sklearnのSVM = 便利なライブラリとして使える
- matplotlibで描画すると、分類の結果や境界線がわかりやすくなる
- `.plot` = 点、`.annotate` = 点のラベル、`.contour` = 境界線
