# Django フォームの流れ（GET / POST）

Django フォームは大きく 2 つの使い方がある。

- **POST** … データ送信（新規登録・コメント投稿・更新など）
- **GET** … 検索やフィルター（クエリパラメータを扱う場合）



---

## ✅ POST の流れ（例: コメント投稿）

### forms.py
~~~python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="名前", max_length=50)
    text = forms.CharField(label="コメント", widget=forms.Textarea)
~~~

### views.py
~~~python
from django.shortcuts import render
from .forms import CommentForm

def comment_view(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            # ここでDB保存などの処理
            return render(request, "thanks.html", {"name": name})
    else:
        form = CommentForm()

    return render(request, "comment.html", {"form": form})
~~~

### HTML
※{% csrf_token %} を書くと、Django がランダムな値を <input type="hidden"> に埋め込んでくれる
~~~django
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">送信</button>
</form>
~~~

---

## ✅ GET の流れ（例: 検索フォーム）

### forms.py
~~~python
from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)
~~~

### views.py
~~~python
from django.shortcuts import render
from .forms import SearchForm
from .models import Article

def index(request):
    searchForm = SearchForm(request.GET)  # GETパラメータをバインド
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Hello Django',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)
~~~

### HTML
~~~django
{% extends './base.html' %}
{% block content %}
  <h1>paiza bbs</h1>
  <p>{{ message }}</p>

  {% if searchForm %}
    <form action='{% url "bbs:index" %}' method="get">
      <div class="form-group">
        {{ searchForm }}
        <input type="submit" class="btn btn-outline-primary" value="OK" />
        <a href="{% url 'bbs:index' %}" class="btn btn-outline-secondary">クリア</a>
      </div>
    </form>
  {% endif %}

  <ul>
    {% for article in articles %}
      <li>{{ article.content }}</li>
    {% endfor %}
  </ul>
{% endblock %}
~~~

---

## 💡 まとめ
- **POST** … 新しいデータを送信・保存（csrf_token が必須）  
- **GET** … 既存データを検索・絞り込み（URL のクエリパラメータを利用）  
- 両方とも **forms.py で定義したフォームクラスを views.py で使い、テンプレートに渡す** 流れは同じ
