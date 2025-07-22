# 書き込み
with open("test.txt", "w") as f:
    f.write("Hello, file!")

# 読み込み
with open("test.txt", "r") as f:
    content = f.read()
    print(content)  # 出力: Hello, file!
