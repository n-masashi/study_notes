# 数値型（int: 整数, float: 小数）
num = 10          # int
price = 3.5       # float

# 文字列型（str）
name = "Taro"

# 真偽値型（bool）
is_valid = True

# リスト型（list）
fruits = ["apple", "banana", "orange"]

# タプル型（tuple）※変更不可のリスト
point = (10, 20)

# 辞書型（dict）
person = {"name": "Taro", "age": 20}

# セット型（set）※重複なし
unique_numbers = {1, 2, 2, 3}  # => {1, 2, 3}

# 型の確認
print(type(name))       # <class 'str'>
print(type(fruits))     # <class 'list'>

# 型変換（キャスト）
age_str = "30"
age = int(age_str)      # 文字列 → 数値

height = 170
height_str = str(height)  # 数値 → 文字列
