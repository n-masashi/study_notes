# Django テンプレートでの URL 指定

Django では `href` に直接パスを書く代わりに、URL 名を使って遷移先を指定できます。



## 基本構文

~~~django
<a href="{% url 'bbs:index' %}">掲示板トップへ</a>
~~~

- `bbs` : アプリ名  
- `index` : `urls.py` で定義した `name="index"` の部分  
- URL が変わっても `name` を変えなければリンクは有効のまま  
