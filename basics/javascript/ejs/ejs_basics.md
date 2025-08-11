# EJSの基本まとめ

---

## EJSとは？

- Embedded JavaScriptの略
- JavaScriptのコードをテンプレート内に埋め込めるビューエンジン
- Expressでよく使われるテンプレートエンジンのひとつ
- HTMLにJavaScriptの変数や制御構文を書いて動的なページを作成できる

---

## 基本的なテンプレート構造

- `.ejs` ファイルにHTMLとEJSタグを混在して書く
- EJSのタグ種類：
  - `<%= %>` ：値の埋め込み（エスケープあり）
  - `<%- %>` ：値の埋め込み（エスケープなし、HTMLをそのまま出す）
  - `<% %>`  ：JavaScriptの処理（出力はしない）

---

## 変数の埋め込み

~~~ejs
<p>こんにちは、<%= userName %> さん！</p>
~~~

- `userName` はExpressから渡される変数
- `<%= %>` で囲むとHTMLエスケープされた値が出力される

---

## 条件分岐の書き方

~~~ejs
<% if (isLoggedIn) { %>
  <p>ログインしています</p>
<% } else { %>
  <p>ゲストユーザーです</p>
<% } %>
~~~

---

## 繰り返し（ループ）の書き方

~~~ejs
<ul>
<% items.forEach(function(item) { %>
    <li><%= item %></li>
<% }); %>
</ul>
~~~

---

## 部分テンプレート（include）の使い方

- ヘッダーやフッターなど共通部分を分けて管理できる

~~~ejs
<%- include('partials/header') %>

<p>メインコンテンツ</p>

<%- include('partials/footer') %>
~~~

- `partials/header.ejs` などのファイル名を指定

---

## Expressとの連携方法

- Expressのコントローラで `res.render()` を使い、変数を渡す

~~~js
app.get('/profile', (req, res) => {
    res.render('profile', { 
        userName: '山田太郎',
        items: ['りんご', 'みかん', 'バナナ']
    });
});
~~~

---

## レイアウトテンプレートの作り方（基本例）

- EJS単体では標準レイアウト機能はないため、`include` を使って対応することが多い

`views/layout.ejs`（共通の枠組み）

~~~ejs
<!DOCTYPE html>
<html>
<head>
  <title><%= title %></title>
</head>
<body>
  <%- include('partials/header') %>

  <main>
    <%- body %>
  </main>

  <%- include('partials/footer') %>
</body>
</html>
~~~

Express側でレンダリング時に、`body` に個別ページの内容を埋め込む形で実装するか、  
`express-ejs-layouts` などのライブラリを利用すると便利

---

# まとめ

- EJSはHTMLにJavaScriptを埋め込むテンプレートエンジン
- 変数埋め込み、条件分岐、ループ、部分テンプレートなどが使える
- Expressと組み合わせて動的なWebページを作成するのに便利
