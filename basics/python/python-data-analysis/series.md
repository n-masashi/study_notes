# pandas Series 学習メモ（print結果付き）

## 基本

```python
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s)
```
```
a    3
b    1
c    2
dtype: int64
```

## スライス

```python
print(s[1:2])
```
```
b    1
dtype: int64
```

## ラベルを別だしで指定

```python
ind = ["a", "c"]
print(s[ind])
```
```
a    3
c    2
dtype: int64
```

## 更新・追加・削除

```python
s["a"] = 813     # 更新
s["d"] = 100     # 追加
del s["a"]       # 削除
print(s)
```
```
b      1
c      2
d    100
dtype: int64
```

```python
s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s.pop("a"))  # 値を取得して削除
print(s)
```
```
3
b    1
c    2
dtype: int64
```

```python
print(s.drop("b"))  # 新しいSeriesを返す
```
```
c    2
dtype: int64
```

## Series の演算

```python
s = pd.Series({"a": 3, "b": 1, "c": 2})
t = pd.Series({"b": 11, "c": 22, "a": 33})
print(s + t)
```
```
a    36
b    12
c    24
dtype: int64
```

### 欠損値が生じる演算

```python
t = pd.Series({"b": 11, "d": 22, "a": 33})
print(s + t)
```
```
a    36.0
b    12.0
c     NaN
d     NaN
dtype: float64
```

### スカラー演算

```python
print(s * 10)
```
```
a    30
b    10
c    20
dtype: int64
```

## Series の属性

### index 属性

```python
print(s.index)
s.index = ["x", "y", "z"]
print(s)
```
```
Index(['a', 'b', 'c'], dtype='object')
x     3
y     1
z     2
dtype: int64
```

### name 属性

```python
s = pd.Series([3, 1, 2], name="nums")
print(s.name)
```
```
nums
```

### dtype 属性

```python
s = pd.Series([3, 1, 2], dtype="float64")
print(s.dtype)
```
```
float64
```

```python
s.rename("values", inplace=True)
s.index.name = "chars"
print(s)
```
```
chars
0    3.0
1    1.0
2    2.0
Name: values, dtype: float64
```

## フィルタリング

```python
s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s > 1)
print(s[s > 1])
```
```
a     True
b    False
c     True
dtype: bool

a    3
c    2
dtype: int64
```

### ビット演算

```python
p = pd.Series([True, True, False])
q = pd.Series([True, False, False])

print(p & q)
print(p | q)
print(~p)
```
```
0     True
1    False
2    False
dtype: bool

0     True
1     True
2    False
dtype: bool

0    False
1    False
2     True
dtype: bool
```

## ソート

```python
print(s.sort_index())
print(s.sort_index(ascending=False))
```
```
a    3
b    1
c    2
dtype: int64

c    2
b    1
a    3
dtype: int64
```

```python
print(s.sort_values())
print(s.sort_values(ascending=False))
```
```
b    1
c    2
a    3
dtype: int64

a    3
c    2
b    1
dtype: int64
```
