# pandas DataFrame 学習メモ（print結果付き）

## Series からの作成

```python
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})
print(df)
```
```
   num  string
a  3.0  paiza
b  1.0     NaN
c  NaN  daiza
```

---

## index 引数・columns 引数による指定

```python
s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame(
    {"num": s, "string": t},
    index=["c", "a", "b", "d"],
    columns=["string", "num", "new"]
)
print(df)
```
```
  string  num  new
c  daiza  NaN  NaN
a  paiza  3.0  NaN
b    NaN  1.0  NaN
d    NaN  NaN  NaN
```

---

## 辞書を値とする辞書からの作成

```python
s = {"a": 3, "b": 1}
t = {"a": "paiza", "c": "daiza"}
df = pd.DataFrame({"num": s, "string": t})
print(df)
```
```
   num  string
a    3  paiza
b    1     NaN
c  NaN  daiza
```

---

## リストを値とする辞書からの作成

```python
df = pd.DataFrame(
    {"num": [3, 1], "string": ["paiza", "daiza"]},
    index=["a", "b"]
)
print(df)
```
```
   num  string
a    3  paiza
b    1  daiza
```
