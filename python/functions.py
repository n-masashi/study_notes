
# 関数の定義と呼び出し
def greet(name):
    print(f"Hello, {name}!")

greet("Taro")  # 出力: Hello, Taro!


# 戻り値（return）
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 出力: 8


# デフォルト引数
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

say_hello()          # 出力: Hello, Guest!
say_hello("Hanako")  # 出力: Hello, Hanako!


# 引数の種類（位置・キーワード）
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Taro", 20)               # 位置引数
introduce(age=30, name="Hanako")    # キーワード引数


# 可変長引数
def show_args(*args):
    for arg in args:
        print(arg)

show_args("apple", "banana", "orange")
# 出力: apple banana orange（1行ずつ）

def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_kwargs(name="Taro", age=25)
# 出力:
# name: Taro
# age: 25

# 関数はオブジェクト
def double(n):
    return n * 2

f = double
print(f(4))  # 出力: 8
