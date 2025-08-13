# Djangoのルーティング（URLconf）

## 基本

- `urls.py` にURLとビューの対応を定義する
- `path()` 関数を使う

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
    ]
    ```

## ルーティングの分割

- アプリごとに `urls.py` を作成
- プロジェクトの `urls.py` で `include()` して読み込む

    ```python
    # project/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls')),
    ]
    ```

- `myapp/urls.py`  

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('hello/', views.hello, name='hello'),
    ]
    ```

## 名前付きURL

- `name` 引数を使ってURLに名前をつけられる
- テンプレートやコード内で `reverse()` や `{% url 'name' %}` で参照可能
