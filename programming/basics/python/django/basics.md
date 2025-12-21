# Djangoアプリの基本構造

## Djangoとは？

- Pythonで動くフルスタックWebアプリケーションフレームワーク
- URLルーティング、ビュー、テンプレート、データベース（ORM）まで一通り揃っている
- 管理画面や認証機能も標準搭載

## 基本の流れ

1. プロジェクトを作成  
    ```bash
    django-admin startproject myproject
    ```

2. アプリを作成  
    ```bash
    python manage.py startapp myapp
    ```

3. `settings.py` にアプリを登録（`INSTALLED_APPS` に追加）

4. URLルーティングを設定  
    - プロジェクトの `urls.py` にアプリの `urls.py` を紐づける

5. ビューを作成（`views.py`）

6. テンプレートを作成（`templates/` フォルダ内）

7. サーバーを起動してリクエストを待つ  
    ```bash
    python manage.py runserver
    ```

## 最小の例（Hello World）

    # views.py
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello Django!")

    # urls.py（プロジェクトまたはアプリ側）
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

## プロジェクト構成例

    myproject/
        manage.py
        myproject/
            settings.py
            urls.py
            wsgi.py
            asgi.py
        myapp/
            views.py
            models.py
            urls.py
            templates/
                myapp/
                    index.html
            static/
