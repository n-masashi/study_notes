# Djangoのログイン・認証メモ（チャット上で崩れない版）

## 1. ログイン判定

- ビューで判定する場合
```python
    from django.shortcuts import render, redirect

    def index(request):
        if request.user.is_authenticated:
            context = {'message': f'ようこそ {request.user.username} さん！'}
        else:
            context = {'message': 'ようこそゲストさん！'}
        return render(request, 'index.html', context)
```

- テンプレートで判定する場合
```python
    {% if user.is_authenticated %}
        <p>こんにちは、{{ user.username }}さん</p>
    {% else %}
        <p>ログインしていません</p>
    {% endif %}
```
## 2. ログイン必須ビュー

- @login_required デコレータで保護
```python
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import render

    @login_required
    def profile(request):
        return render(request, 'profile.html')
```
- デフォルトのリダイレクト先は /accounts/login/
- settings.py で変更可能
```python
    # settings.py
    LOGIN_URL = '/login/'
```

## 3. ログイン処理

- Django標準の authenticate() と login() を使用
```
    from django.contrib.auth import authenticate, login
    from django.shortcuts import render, redirect

    def user_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': '認証失敗'})
        return render(request, 'login.html')
```

## 4. ログアウト処理
```python
    from django.contrib.auth import logout
    from django.shortcuts import redirect

    def user_logout(request):
        logout(request)
        return redirect('index')
```

## 5. request.user の主な属性・メソッド

- username, email, first_name, last_name
- is_staff, is_superuser, is_active
- is_authenticated
- get_full_name(), check_password(raw_password)

- カスタムUserモデルを作れば属性は自由に変更可能
- request.user には DB上のそのユーザー情報が丸ごと入る

## 6. まとめポイント

- ログイン判定: request.user.is_authenticated
- ビュー・テンプレート両方で判定可能
- ログイン必須ビュー: @login_required デコレータ
- ログイン処理: authenticate() + log
