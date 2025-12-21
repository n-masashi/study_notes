# Djangoのルーティング（URLconf）

## 基本

- `urls.py` にURLとビューの対応を定義する
- `path()` 関数を使う
- 型変換コンバータを使ってURLパラメータを取得可能（int, str, slug, uuid, path など）

    from django.urls import path
    from . import views

    urlpatterns = [<br>
        path('', views.index, name='index'),<br>
        path('about/', views.about, name='about'),<br>
        path('articles/<int:id>/', views.detail, name='detail'),  # URLパラメータをビューに渡す例<br>
        path('show/<str:content>/', views.show, name='show'),    # 文字列パラメータ<br>
        path('files/<path:file_path>/', views.file_view, name='file_path'),  # / を含むパス<br>
    ]<br>

## ルーティングの分割

- アプリごとに `urls.py` を作成
- プロジェクトの `urls.py` で `include()` して読み込む
- ルートURLやアプリごとのURLを整理できる

    # project/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [<br>
        path('admin/', admin.site.urls),<br>
        path('bbs/', include('bbs.urls')),<br>
        path('', include('myapp.urls')),<br>
    ]<br>

- `myapp/urls.py`  

    from django.urls import path
    from . import views

    urlpatterns = [<br>
        path('', views.index, name='index'),<br>
        path('hello/', views.hello, name='hello'),<br>
        path('<int:id>/delete/', views.delete, name='delete'),<br>
    ]<br>

## 名前付きURL

- `name` 引数を使ってURLに名前をつけられる
- テンプレートやビュー内で URL を参照できる
    - テンプレート: `{% url 'detail' id=3 %}`
    - ビュー: `redirect('index')`
- URL変更に強く、ハードコーディングを避けられる

## 汎用ビュー（Generic View）でのリダイレクト

- `RedirectView` を使うと簡単にリダイレクト処理ができる
- クラスベースビューなので `as_view()` で呼び出す

    from django.views.generic import RedirectView
    from django.urls import path

    urlpatterns = [<br>
        path('', RedirectView.as_view(url='/bbs/')),  # ルートURLにアクセスしたら /bbs/ に転送<br>
    ]<br>

- 使いどころ: トップページからアプリに誘導したいときなど

## ビューでの URL パラメータ利用と DB 取得

- URLで渡されたパラメータを受け取り、DBから該当オブジェクトを取得する
- `get_object_or_404` を使うと、存在しない場合は自動で 404 を返す

    from django.shortcuts import get_object_or_404, render
    from .models import Article

    def detail(request, id):
        article = get_object_or_404(Article, pk=id)
        context = {
            'message': 'Show Article ' + str(id),
            'article': article,
        }
        return render(request, 'bbs/detail.html', context)

## まとめ

- URLとビューを対応させる基本: `path('url/', views.func, name='name')`
- URLパラメータは型を指定してビューに渡せる
- アプリごとに `urls.py` を分割し、`include()` でまとめる
- 名前付きURLでテンプレートやリダイレクトから安全にURLを参照
- `RedirectView` などの汎用ビューでよくある処理を簡単に実装可能
- `get_object_or_404` で安全にDBからオブジェクト取得、存在しない場合は404を返す
