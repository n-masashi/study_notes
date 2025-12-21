text = "  Hello, World!  "

# 大文字に変換
print(text.upper())  # "  HELLO, WORLD!  "

# 先頭・末尾の空白削除
print(text.strip())  # "Hello, World!"

# 分割
words = text.split(",")
print(words)  # ['  Hello', ' World!  ']

# 結合
print("-".join(words))  # "  Hello- World!  "

# 部分文字列の検索
print(text.find("World"))  # 8 （見つからなければ -1）

# 文字列の長さ
print(len(text))  # 15

# フォーマットの別パターン
name = "Taro"
age = 20
print("My name is {}, and I'm {} years old.".format(name, age))
print(f"My name is {name}, and I'm {age} years old.")

# 文字列のエスケープ
print("She said, \"Hello!\"")

# 文字列の繰り返し
print("Hi! " * 3)  # "Hi! Hi! Hi! "
