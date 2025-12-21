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

## メインファイル（app.js）でのルーティング登録の一般的な書き方

- ルーティングは基本的に一箇所（例えば `routes/index.js`）にまとめるのが一般的
- `app.js` に追加するルーティングは以下のように1行だけで済むことが多い

~~~js
app.use('/', require('./routes'));
~~~

- これにより、`routes/index.js` が親ルーターとして機能し
- さらに細かいページ別の処理は `routes/index.js` 内で分割・管理できる

---

## 例：routes/index.js 内での分割例

~~~js
const express = require('express');
const router = express.Router();

router.use('/login', require('./login'));
router.use('/logout', require('./logout'));

router.get('/', (req, res) => {
    res.render('home');
});

module.exports = router;
~~~

---

このようにすると、  
`app.js` ではシンプルに親ルーターを登録するだけで済み、  
ルーティングの管理・拡張がしやすくなる。
