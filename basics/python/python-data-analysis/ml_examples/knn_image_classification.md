# 画像分類（KNN）入門メモ

## 1. 使用ライブラリ
```python
import cv2                   # 画像処理用
import numpy as np           # 数値計算用
from matplotlib import pyplot as plt  # グラフ描画用
import pandas as pd          # 表形式データ操作用
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

- OpenCV (cv2) : 画像を読み込んだり加工する
- NumPy : 配列操作やベクトル化に使う
- Matplotlib : グラフ表示に使う
- Pandas : CSVなど表形式データの読み込み
- scikit-learn : 機械学習ライブラリ（ここでは KNN を使用）

---

## 2. CSV（ラベルデータ）の読み込み
```python
targets_data = pd.read_csv('y_classified.csv')
print(targets_data['Kirishima'])
```

- y_classified.csv の 'Kirishima' 列を読み込み
- これが今回の分類の「正解ラベル」になります

---

## 3. 画像データの読み込み
```python
images = []
for i in range(100):
    file = 'images/%03d.png' % i       # 000.png 〜 099.png
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    images.append(img)
```

- 100枚の画像を読み込む
- グレースケールで読み込み → 1チャンネルにする
- `images` は画像のリスト

---

## 4. 画像を機械学習用に整形
```python
images_data = np.empty((100, len(images[0].ravel())), int)
for i in range(100):
    images_data[i] = images[i].ravel()
print(images_data.shape)
```
- np.empty(shape, dtype) は 空の配列を作る<br>shape=(100, len(images[0].ravel()))<br>　100 → サンプル数（画像の枚数）<br>　len(images[0].ravel()) → 1枚の画像を1次元にしたときの要素数（ピクセルの数）<br>※np.zeros でもOKだが、empty は初期化されていないだけなので少し高速
- `.ravel()` で 2次元画像を1次元ベクトルに変換
- `images_data` は (100, ピクセル数) の形
- この形にすると scikit-learn に入力可能

---

## 5. 学習データとテストデータに分割
```python
X_train, X_test, y_train, y_test = train_test_split(
    images_data, targets_data['Kirishima'], random_state=0
)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
```

- `train_test_split` でデータをランダムに分割
- `X_train`, `y_train` : 学習用
- `X_test`, `y_test` : 評価用
- `random_state=0` で結果を再現可能
- train_test_split のデフォルト引数は：test_size=None, train_size=None　
- デフォルト動作： テストデータ 25%、学習データ 75% に自動で分割
- だから 100枚の画像 → 75枚が学習用、25枚がテスト用
- 明示的に比率を変えたい場合は train_test_split(..., test_size=0.2) のように指定できる ※例：80:20 → 80枚学習、20枚テスト

---

## 6. KNN モデルの作成と学習
```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
```

- 1近傍法（k=1）のKNNモデルを使用
- `.fit()` で学習

---

## 7. 予測と評価
```python
# 1枚だけ予測
print(knn.predict(np.array([X_test[0]])))
print(y_test.iloc[0])  # 正解

# 複数枚まとめて予測
print(knn.predict(np.array([X_test[0], X_test[1], X_test[2], X_test[3]])))
print(y_test.head(4))  # 正解ラベル

# 全体の予測
y_pred = knn.predict(X_test)
print(y_pred)

# 正答率（accuracy）
print(np.mean(y_pred == y_test))
```
- np.mean() は「平均」を計算(y_predとy_testの値を要素ごとに比較する感じ)
- `np.mean(y_pred == y_test)` で正答率を計算
- 例：0.60 → 60% 正解

---

## 8. ポイントまとめ
1. 画像はまず **1次元ベクトル** に変換する
2. ラベルと画像データを分けて、学習と評価に分割
3. KNN は距離が近いサンプルでラベルを決める
4. 正答率でモデル性能を評価
5. データが少ないと精度が低くなることもある
6. ランダム分割なので再現性を確保したい場合は `random_state` を指定

---

## 9. 精度向上のための工夫
- データ数を増やす
- 前処理（正規化、標準化）を行う
- k の数を変えて精度を確認
- 他の分類器（SVM, ロジスティック回帰など）も試す

