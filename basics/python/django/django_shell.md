# Django Shellの基礎

## Django Shellとは？

- Djangoの環境付きPython対話モード
- `settings.py` や ORM が利用可能な状態で起動するので、モデルを使ったDB操作をすぐに試せる
- デバッグ・データ確認・簡易スクリプトに便利

---

## 起動方法

    python manage.py shell

---

## よく使うパターン

### 1. モデルをインポートして操作

    >>> from myapp.models import Book
    >>> Book.objects.all()
    <QuerySet []>

    >>> book = Book(title="Django入門", author="山田太郎", price=2000)
    >>> book.save()

    >>> Book.objects.all()
    <QuerySet [<Book: Book object (1)>]>

### 2. Django拡張パッケージの利用（便利機能）

Django Extensions をインストールすると、より便利な `shell_plus` が使える。  
自動でモデルが import される。

    pip install django-extensions

`settings.py` の `INSTALLED_APPS` に追加:

    INSTALLED_APPS = [
        ...
        "django_extensions",
    ]

起動:

    python manage.py shell_plus

---

## よくある使い方まとめ

- **データ確認**  
    Book.objects.all()  
    Book.objects.filter(author="山田太郎")  

- **データ追加**  
    Book.objects.create(title="新しい本", author="佐藤花子", price=1500)

- **更新**  
    book = Book.objects.get(id=1)  
    book.price = 2500  
    book.save()  

- **削除**  
    book = Book.objects.get(id=1)  
    book.delete()  

---

## ポイント

- **`python manage.py shell`** は Djangoプロジェクトの設定を読み込んで起動するPythonコンソール
- **ORMの実験・データベース操作** を安全に試せる
- **Django Extensions の `shell_plus`** を使うとさらに効率的
