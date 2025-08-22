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

## DataFrameの参照方法（復習＋追加）

DataFrameには **行・列・セル** それぞれを参照する方法があります。

```python
print(df["num"])     # 列参照
print(df.num)        # 列参照（属性アクセス）
print(df.loc["b"])   # 行参照（index名指定）
print(df.iloc[0])    # 行参照（番号指定）
print(df.at["a", "string"])  # セル参照（index名＋列名）
print(df.iat[0, 1])  # セル参照（番号指定）
```

---

## スライスと部分選択

`[]`・`loc`・`iloc` を使うと部分的に抜き出せる。

```python
s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
u = pd.Series({"b": True})
df = pd.DataFrame({"num": s, "string": t, "bool": u})

print(df["b":"c"])              # 行index名で範囲
print(df[1:3])                  # 行番号で範囲
print(df.loc[:"b", "string":])  # locで範囲（行名＋列名範囲）
print(df.iloc[[0, 2], [0, 2]])  # ilocで特定の位置
```

### 出力例（df\["b":"c"]）

```
   num string  bool
b    1   NaN  True
c  NaN daiza   NaN
```

---

## 列の更新・追加

Seriesや定数を代入して列を更新できる。

```python
df["num"] = pd.Series({"a": 300, "b": 100})  # 既存列の更新
df["bool"] = pd.Series({"b": True})          # 新しい列の追加
df["bool"] = False                           # 全部Falseで追加
```

---

## 行の追加

行は `append`（非推奨）や `loc` を使って追加できる。

```python
print(df.append(pd.Series({"num": 813, "string": "pizza"}, name="d")))
df.loc["d"] = pd.Series({"num": 813, "string": "pizza"})
```

### 出力例（append使用時）

```
   num string
a    3  paiza
b    1    NaN
c  NaN  daiza
d  813  pizza
```

---

## セルの更新

`iat` や `at` でセルを直接更新できる。

```python
df.iat[0, 1] = "pizza"  # 0行目・1列目を書き換え
```

---

## 列の削除

* `del`：対象の列を削除
* `pop`：削除した列を返す
* `drop`：削除した結果を返す（元のdfは残る）

```python
del df["string"]

print(df.pop("string"))  # 削除した列を返す
print(df)                 # 残ったDataFrame

print(df.drop("string", axis=1))  # 新しいdfを返す（元はそのまま）
```

---

## 行の削除

`drop` に index を渡すと行削除。

```python
print(df.drop("a"))
```

---

## まとめ

* **参照**：列は `df["col"]`、行は `loc`/`iloc`、セルは `at`/`iat`
* **更新**：列は代入、セルは `at`/`iat`
* **追加**：行は `loc`、列は代入
* **削除**：`del`/`pop`/`drop` の違いを押さえる

