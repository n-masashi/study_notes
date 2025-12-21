# Pandas 基礎メモ（詳細）

> Pandasは表形式のデータ（DataFrame）を効率的に扱えるライブラリ。行列の操作、統計、ファイル入出力が簡単。

---

## インポート
```python
import pandas as pd
```
慣習的に `pd` という別名で使う。

---

## データフレーム作成
```python
data = {'name': ['Alice','Bob','Carol'], 'age':[25,30,22], 'score':[90,80,85]}
df = pd.DataFrame(data)
df
```
```
  name  age  score
0 Alice 25   90
1 Bob   30   80
2 Carol 22   85
```

---

## 基本操作
```python
df.head()       # 先頭5行
df.tail(2)      # 末尾2行
df.info()       # 列ごとの情報
df.describe()   # 数値列の統計情報
df['age']       # 特定の列を取得
df[['name','score']]  # 複数列
```

---

## 行・列のアクセス
```python
df.iloc[0]          # 0行目
df.iloc[0,1]        # 0行目のage列
df.loc[0,'score']   # 行ラベル0, score列
df.loc[df['age']>23]  # 条件で行選択
```

---

## 列の追加・変更
```python
df['passed'] = df['score']>=80
df['age_plus_1'] = df['age'] + 1
```

---

## 行の追加・削除
```python
df.loc[3] = ['David',28,88,True,29]  # 新しい行追加
df.drop(3, axis=0, inplace=True)      # 行削除
```

---

## ソート
```python
df.sort_values('score', ascending=False)   # score列で降順
df.sort_values(['age','score'])           # 複数列でソート
```

---

## ファイル入出力
```python
df.to_csv('data.csv', index=False)    # CSV出力
df2 = pd.read_csv('data.csv')        # CSV読み込み
```

---

## 集計
```python
df['score'].mean()     # 平均
df['score'].sum()      # 合計
df.groupby('passed')['score'].mean()  # 条件別平均
```
