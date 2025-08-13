# Django テンプレート基本メモ

## 1. 変数を埋め込む
    <p>{{ message }}</p>
- `{{ 変数名 }}` で Python から渡された変数の値を HTML に埋め込む
- 自動で HTML エスケープされる（`<` や `>` が文字列として表示される）

例：<br>
    context = {'message': 'Hello World!'}<br>
    return render(request, 'index.html', context)

→ HTML では `<p>Hello World!</p>` と表示される

---

## 2. 繰り返し処理（for ループ）
    {% for player in players %}
        <p>{{ player }}はモンスターと戦った</p>
    {% endfor %}
- `{% %}` の中に Django 独自のテンプレートタグを書く
- Python の `for` ループと同じイメージで使える
- ループ内の変数も `{{ player }}` のように埋め込む

### 補足：閉じタグの明示
- HTML はインデントだけだとどこまでループが続くか見にくいことがある
- 学習中は `<p>...</p>` の閉じタグを意識して書くと、構造が把握しやすい

例：
    context = {'players': ['Alice', 'Bob']}

表示結果：
    <p>Aliceはモンスターと戦った</p>
    <p>Bobはモンスターと戦った</p>

---

## 3. 条件分岐（if）
    {% if is_winner %}
        <p>勝利！</p>
    {% else %}
        <p>敗北…</p>
    {% endif %}
- Python の `if` と同じ使い方
- `elif` も使える：
    {% if score >= 100 %}
        <p>高得点！</p>
    {% elif score >= 50 %}
        <p>まずまず</p>
    {% else %}
        <p>頑張ろう</p>
    {% endif %}

---

## 4. コメント
    {# ここはコメント #}
- HTML に出力されない
- 説明やメモを書くのに便利

---

## 5. フィルタ
- 変数に対して加工を行う
    <p>{{ name|upper }}</p>  <!-- 大文字に変換 -->
    <p>{{ text|truncatechars:10 }}</p>  <!-- 文字数制限 -->

---

## 6. 覚えておくと便利なテンプレートポイント
1. `{% block %}` / `{% endblock %}`  
   - base.html を使ったテンプレート継承で必須  
2. `{% extends "base.html" %}`  
   - 共通レイアウトを利用する場合  
3. `{% include "header.html" %}`  
   - 部分テンプレートを読み込む  
4. `{% csrf_token %}`  
   - フォーム内で CSRF 保護を有効にする  
5. `{{ variable|default:"値" }}`  
   - 変数が None や空の場合にデフォルト値を設定  

---

## 7. まとめ
- `{{ }}` → 変数展開
- `{% %}` → タグ（制御構文、ループ、条件分岐など）
- `{# #}` → コメント
- フィルタで変数を加工できる
- HTML の閉じタグは学習時に明示すると構造理解が楽
- block / extends / include / csrf_token は実務でよく使う
