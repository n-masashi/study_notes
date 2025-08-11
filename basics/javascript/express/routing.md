# ルーティングの基本と分割方法

## ルーティングとは？

- URLごとに違う処理をすること

## 書き方例

~~~js
app.get('/login', (req, res) => {
  res.render('login');
});
~~~

## ルーティングの分割

- 複数ページがあるときはファイルを分けると見やすい
- 例：routes/login.js、routes/logout.js

~~~js
// app.js
app.use('/login', require('./routes/login'));
~~~

## index.jsの役割

- ルート（親）ルーティングとして使う
- 何も指定しないと自動的にindex.jsを読み込む

---
