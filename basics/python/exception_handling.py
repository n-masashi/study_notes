# 例外クラスの確認（組み込み例外）
# ----------------------------
# - ValueError: 無効な値
# - TypeError: 型の不一致
# - ZeroDivisionError: 0で除算
# - IndexError: インデックス範囲外
# - KeyError: 存在しないキーを使用
# などがある


# 基本構文
try:
    num = int(input("数字を入力してください: "))
    print(f"2倍すると {num * 2}")
except ValueError:
    print("数字を入力してね")


# 複数の例外を処理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません")
except ValueError:
    print("値のエラーです")


# else句とfinally句（必要に応じて）
try:
    print("正常な処理")
except:
    print("エラー発生")
else:
    print("例外が発生しなければ実行される")
finally:
    print("必ず最後に実行される")
