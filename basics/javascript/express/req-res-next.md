# Expressの関数の引数：req, res, nextについて

---

## req（Request：リクエスト）

- ユーザー（ブラウザやアプリ）から送られてきた「情報」が入っている箱

### 主なプロパティ・使い方

- `req.url`  
  → ユーザーがアクセスしたページのURL（例：'/login'）

- `req.method`  
  → HTTPメソッド（'GET', 'POST'など）

- `req.headers`  
  → 送られてきたヘッダー情報（ブラウザ情報や認証情報など）

- `req.params`  
  → URLのパラメータ（例：`/user/:id` の:idの値）

- `req.query`  
  → URLの?以降のクエリパラメータ（例：`?search=abc` のsearch）

- `req.body`  
  → POSTやPUTで送られてきたデータ（JSONやフォームの内容）

- `req.cookies`  
  → クッキーの情報（cookie-parserを使った時）

---

## res（Response：レスポンス）

- サーバーからユーザーに「返す内容」を作る箱

### 主なメソッド・使い方

- `res.send(data)`  
  → 文字列やHTMLなどをそのまま送る

- `res.json(obj)`  
  → JSON形式のデータを返す（APIでよく使う）

- `res.render('view', data)`  
  → テンプレートを使ってHTMLを作り送る

- `res.redirect(url)`  
  → 別のURLにリダイレクト（ページ移動）

- `res.status(code)`  
  → ステータスコードを設定（例：404, 500）

- `res.set(headerName, value)`  
  → レスポンスヘッダーを設定

---

## next（次へ）

- ミドルウェアの「次の処理」に進むための関数

- 呼ばないと処理がそこで止まってしまう

- 例）複数の処理を順番に実行したいときに使う

---

## まとめイメージ

ユーザー → req（情報を受け取る）→ サーバー処理 → res（返事を作る）→ ユーザーへ返す

途中にミドルウェアがあれば

処理1 → next() → 処理2 → next() → 処理3 → res.send()

---

## 参考コード例

~~~js
app.get('/user/:id', (req, res, next) => {
  const userId = req.params.id;          // URLパラメータ取得
  console.log(req.method);               // 'GET'
  
  if(!userId) {
    return next(new Error('ユーザーIDがありません')); // エラーをnextに渡す
  }
  
  res.status(200).render('user', { id: userId }); // ユーザーページを返す
});
~~~
