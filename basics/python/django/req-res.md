# DjangoのRequest・Responseについて

## requestオブジェクト

- ビュー関数の第1引数に自動で渡される
- ユーザーからのリクエスト情報を保持

### 主な属性
- `request.method`  
  → HTTPメソッド（'GET', 'POST'など）

- `request.GET`  
  → クエリパラメータ（例：`?search=abc`）

- `request.POST`  
  → POST送信されたフォームデータ

- `request.FILES`  
  → アップロードされたファイル

- `request.path`  
  → アクセスされたパス（例：`/login/`）

- `request.headers`  
  → ヘッダー情報

## responseオブジェクト

- ビュー関数の戻り値として返す
- `HttpResponse` や `render()` で生成

### 主な使い方
- 文字列を返す  
    ```python
    return HttpResponse("Hello World")
    ```

- テンプレートを使って返す  
    ```python
    return render(request, 'myapp/index.html', {'name': 'Taro'})
    ```

- JSONを返す  
    ```python
    from django.http import JsonResponse
    return JsonResponse({'result': 'ok'})
    ```

- リダイレクトする  
    ```python
    from django.shortcuts import redirect
    return redirect('/login/')
    ```
