# Django とデータベース（DB）学習メモ

## 1. Django から MySQL に接続
settings.py に接続情報を設定

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'データベース名',   # phpMyAdminで作ったDB名
            'USER': 'ユーザー名',
            'PASSWORD': 'パスワード',
            'HOST': 'localhost',       # 同じPCの場合
            'PORT': '3306',            # MySQL標準ポート
        }
    }

---

## 2. モデル作成（設計図）
    # blog/models.py
    from django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=100)
        body = models.TextField()

        def __str__(self):
            return self.title

- モデル = テーブル設計図
- __str__ は管理画面表示用

---

## 3. マイグレーションで DB に反映
### ① マイグレーションファイル作成
    python manage.py makemigrations
### ② テーブル作成
    python manage.py migrate

- これで MySQL にテーブルが作られる
- GUI から確認可能

---

## 4. 既存テーブルを使う場合
    class ExistingTable(models.Model):
        name = models.CharField(max_length=50)

        class Meta:
            db_table = '既存テーブル名'
            managed = False  # Djangoはテーブル作成・削除を管理しない

- 事前にあるテーブルを使う場合は managed = False
- CREATE / DROP 権限がなくてもデータ操作可能

---

## 5. 権限と安全性
- MySQL では権限を細かく設定可能

    GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'user1'@'localhost';
    REVOKE CREATE, DROP ON mydb.* FROM 'user1'@'localhost';

- Django は CREATE TABLE 権限がなくても既存テーブルを操作可能
- ORM を使う限り SQL インジェクションは基本的に安全
- 生 SQL を文字列連結で書く場合は注意

---

## 6. ビューで DB を操作
    # blog/views.py
    from django.shortcuts import render
    from .models import Post

    def post_list(request):
        posts = Post.objects.all()
        return render(request, "blog/list.html", {"posts": posts})

- ORM を通して CRUD 操作可能
- 生 SQL を書く場合はパラメータ化必須

---

## 7. テンプレートで表示
    <!-- blog/templates/blog/list.html -->
    <h1>投稿一覧</h1>
    <ul>
    {% for post in posts %}
        <li>{{ post.title }} - {{ post.body }}</li>
    {% endfor %}
    </ul>

---

## 8. 現場での DB 運用イメージ

| パターン | 多いケース | 権限 |
|----------|------------|------|
| 新規プロジェクト | Django がテーブル作成 | CREATE/DROP あり |
| 既存 DB 利用 | 既存テーブルを参照のみ | CREATE/DROP なし、CRUD 権限あり |

- GUI は「確認・テスト用」
- Django は「Web アプリとして操作・表示・連携用」

---

💡 ポイントまとめ
- Django は DB を直接作るわけではなく、マイグレーションでテーブル作成
- 既存 DB 利用も可能（managed=False）
- 権限や ORM の安全性を理解して使い分ける
