# scikit-learn 基礎メモ（詳細）

> scikit-learnはPythonで機械学習モデルを学習・評価するためのライブラリ。分類、回帰、クラスタリングなどに対応。

---

## インポート
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
```

---

## データ準備
```python
# 特徴量Xと目的変数y
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,3,2,3,5])
```

---

## データ分割
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- `test_size` : テストデータの割合  
- `random_state` : 再現性確保

---

## モデル作成・学習
```python
model = LinearRegression()
model.fit(X_train, y_train)
```

---

## 予測
```python
y_pred = model.predict(X_test)
print("予測:", y_pred)
```

---

## 評価
```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R2:", r2)
```

---

## 応用ポイント
- 特徴量が複数の場合は `X` を2次元配列にする  
- モデルごとに `.fit()`, `.predict()` の流れは共通  
- 評価指標はタスクに応じて変更（分類なら accuracy, f1-score など）
