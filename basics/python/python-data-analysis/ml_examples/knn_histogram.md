# 画像分類（明度ヒストグラム＋KNN）メモ

## 1. 使用ライブラリ
```python
import cv2                   # 画像処理用
import numpy as np           # 数値計算用
from matplotlib import pyplot as plt  # グラフ描画用
import pandas as pd          # 表形式データ操作用
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

- OpenCV (cv2) : 画像を読み込む・加工する
- NumPy : 配列操作や数値計算
- Matplotlib : グラフ描画
- Pandas : CSVなど表形式データの操作
- scikit-learn : 機械学習ライブラリ（ここでは KNN を使用）

---

## 2. CSV（ラベルデータ）の読み込み
```python
targets_data = pd.read_csv('y_classified.csv')
```

- y_classified.csv の 'Kirishima' 列を読み込み
- 分類の正解ラベルとして使用

---

## 3. 画像データの読み込みと明度ヒストグラム化
```python
images_data = np.empty((0,256), int)

for i in range(100):
    png = ('images/%03d.png' % (i))
    img = cv2.imread(png, cv2.IMREAD_GRAYSCALE)
    hist = np.histogram(img.ravel(), 256, [0,256])
    images_data = np.append(images_data, np.array([hist[0]]), axis=0)

print(images_data.shape)
```

- `images_data = np.empty((0,256), int)`  
  → 行0、列256の空配列を作成（0～255の明度ヒストグラム用）
- `.ravel()`  
  → 2次元画像を1次元ベクトルに変換
- `np.histogram(img.ravel(), 256, [0,256])`  
  → 画像の明度ヒストグラムを計算（256ビン）
- `np.append(..., axis=0)`  
  → 1枚ずつヒストグラムを `images_data` に追加
- `images_data` の形： `(100, 256)`  
  → 100枚の画像 × 256次元（明度ヒストグラム）

---

## 4. 学習データとテストデータに分割
```python
X_train, X_test, y_train, y_test = train_test_split(
    images_data, targets_data['Kirishima'], random_state=0
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
```

- データをランダムに分割
- `X_train`, `y_train` : 学習用
- `X_test`, `y_test` : 評価用
- `random_state=0` で結果を再現可能
- デフォルト：学習75%、テスト25%

---

## 5. KNN モデルの作成と学習
```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
```

- 1近傍法（k=1）の KNN モデルを使用
- `.fit()` で学習

---

## 6. 予測と評価
```python
# 1枚だけ予測
print(knn.predict(np.array([X_test[0]])))
print(y_test) # 正解ラベルと比較

# 複数枚まとめて予測
print(knn.predict(np.array([X_test[0], X_test[1], X_test[2], X_test[3]])))
print(y_test)

# 全体の予測
y_pred = knn.predict(X_test)
print(y_pred)

# 正答率（accuracy）
print(np.mean(y_pred == y_test))  # 0.84
```

- np.mean(y_pred == y_test) で正答率を計算
- 今回は **84%** 正解

---

## 7. ポイントまとめ
1. 画像を **明度ヒストグラム（256次元）** に変換して特徴量化
2. 学習用・評価用に分割して KNN で分類
3. np.append で行を追加する形式なので、画像枚数を後で変えても対応可能
4. KNN は距離が近いサンプルでラベルを決める
5. 正答率でモデル性能を確認

---

## 8. 改善・次のステップ
- ビン数を変えて精度を確認（例：128ビンや512ビン）
- ヒストグラム以外の特徴量を追加（平均明度、コントラストなど）
- k の値を変えて KNN 精度を比較
- 他の分類器（SVM, ロジスティック回帰, ニューラルネット）も試す

---
