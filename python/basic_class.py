class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

p = Person("Taro")
p.greet()  # 出力: Hello, Taro!
