# Djangoのミドルウェア

## ミドルウェアとは？

- リクエストとレスポンスの間に入る処理
- 認証、ログ記録、セキュリティ対策など

## 作成例

    # myapp/middleware.py
    class SimpleMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            print(f"Request path: {request.path}")
            response = self.get_response(request)
            print(f"Response status: {response.status_code}")
            return response

## settings.pyへの登録

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'myapp.middleware.SimpleMiddleware',  # ← 追加
    ]
