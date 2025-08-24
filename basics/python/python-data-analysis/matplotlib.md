# Matplotlib 基礎メモ（詳細）

> MatplotlibはPythonでグラフを描く基本ライブラリ。折れ線、棒グラフ、ヒストグラム、散布図などに対応。

---

## インポート
```python
import matplotlib.pyplot as plt
```
慣習的に `plt` で使用。

---

## 折れ線グラフ
```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, label='線1', color='blue', marker='o')
plt.title('折れ線グラフ例')
plt.xlabel('X軸')
plt.ylabel('Y軸')
plt.legend()    # 凡例表示
plt.grid(True)  # グリッド表示
plt.show()
```

---

## 棒グラフ
```python
categories = ['A','B','C']
values = [5,7,3]

plt.bar(categories, values, color='green')
plt.title('棒グラフ例')
plt.show()
```

---

## ヒストグラム
```python
import numpy as np
data = np.random.randn(1000)  # 正規分布乱数

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('ヒストグラム例')
plt.show()
```

---

## 散布図
```python
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='x')
plt.title('散布図例')
plt.show()
```

---

## 複数グラフを重ねる
```python
plt.plot(x, y, label='線1')
plt.scatter(x, y, color='red', label='点')
plt.legend()
plt.show()
```
