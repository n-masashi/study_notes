"""
basic_class.py

Pythonにおけるクラスの基礎まとめ

- インスタンス変数とメソッド
- コンストラクタ (__init__)
- クラス変数とクラスメソッド
- 継承とメソッドオーバーライド
"""

# --- 基本のクラス定義とインスタンス化 ---

class Person:
    # クラス変数（全インスタンス共通）
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name  # インスタンス変数

    def greet(self):
        print(f"Hello, I'm {self.name}!")

    # クラスメソッド（クラスから呼び出せる）
    @classmethod
    def what_species(cls):
        print(f"We are {cls.species}.")

    # スタティックメソッド（状態に関係しない便利メソッド）
    @staticmethod
    def say_hello():
        print("Hello from static method!")


# --- 継承とオーバーライド ---

# Personを継承してStudentクラスを作る
class Student(Person):
    def __init__(self, name, school):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(name)
        self.school = school

    # greetをオーバーライド（上書き）
    def greet(self):
        print(f"Hi, I'm {self.name} from {self.school}.")


# --- 動作確認 ---

# Personインスタンスの使用
p = Person("Taro")
p.greet()              # → Hello, I'm Taro!
p.what_species()       # → We are Homo sapiens.
Person.say_hello()     # → Hello from static method!

print("---")

# Studentインスタンスの使用（継承確認）
s = Student("Jiro", "UTokyo")
s.greet()              # → Hi, I'm Jiro from UTokyo.
s.what_species()       # → We are Homo sapiens.（クラスメソッドは継承される）