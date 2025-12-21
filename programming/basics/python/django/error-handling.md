# Djangoのエラーハンドリング

## ビュー内での例外

- Pythonの例外をそのまま発生させることができる
- Djangoが自動的に404や500ページを表示

    ```python
    from django.shortcuts import get_object_or_404

    def article_detail(request, pk):
        article = get_object_or_404(Article, pk=pk)
        return render(request, 'article/detail.html', {'article': article})
    ```

## 独自エラーページ

- プロジェクト直下に `templates/404.html` や `500.html` を置くと自動で使用される
- 開発環境では詳細エラー、運用環境では独自ページが表示される
