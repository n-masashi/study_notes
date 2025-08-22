# Pandas DataFrame メモ

## DataFrameの作成

```python
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})
print(df)
```

**出力例**:

```
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza
```

---

## index引数とcolumns引数による指定

```python
s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t},
                  index=["c", "a", "b", "d"], columns=["string", "num", "new"])
print(df)
```

**出力例**:

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

**出力例**:

```
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza
```

---

## リストを値とする辞書からの作成

```python
df = pd.DataFrame({"num": [3, 1], "string": ["paiza", "daiza"]}, index=["a", "b"])
print(df)
```

**出力例**:

```
   num string
a    3  paiza
b    1  daiza
```

---

## DataFrameの参照方法

DataFrame では **行・列・セル** を柔軟に参照できる。

```python
s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})
print(df)
```

**対象のDataFrame**:

```
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza
```

### 列の参照

```python
print(df["num"])   # 辞書風に列名を指定
print(df.num)      # 属性風にアクセス
```

**出力**:

```
a    3.0
b    1.0
c    NaN
Name: num, dtype: float64
```

### 行の参照

* `loc` : 行ラベルで指定
* `iloc`: 行番号で指定

```python
print(df.loc["b"])   # ラベルで 'b' 行を取得
print(df.iloc[0])    # 0番目の行を取得
```

**出力**:

```
num      1.0
string   NaN
Name: b, dtype: object

num        3.0
string    paiza
Name: a, dtype: object
```

### セルの参照

* `at` : 行ラベル×列ラベルで高速にアクセス
* `iat`: 行番号×列番号で高速にアクセス

```python
print(df.at["a", "string"])   # 行ラベルと列名で指定
print(df.iat[0, 1])           # 行番号と列番号で指定
```

**出力**:

```
paiza
paiza
```

### セルの更新

```python
df.at["a", "string"] = "new_value"
print(df)
```

**出力例**:

```
   num    string
a  3.0  new_value
b  1.0       NaN
c  NaN     daiza
```
