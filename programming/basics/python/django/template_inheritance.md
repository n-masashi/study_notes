# Django テンプレート継承

Django ではテンプレートを継承することで、共通部分をまとめて管理できます。



## 基本構文

~~~django
{% extends './base.html' %}
~~~

- `base.html` を親テンプレートとして継承する  
- `./` は同じテンプレートディレクトリを指す



## ブロックの定義と利用

~~~django
{% block content %}
  <h1>Hello Django!</h1>
{% endblock %}
~~~

- `{% block %}` ～ `{% endblock %}` で囲んだ部分を、子テンプレート側で上書きできる  
- `content` はブロックの名前。`base.html` 側に同じ名前のブロックが必要  
