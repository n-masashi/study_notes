# Expressアプリの基本構造

## Expressとは？

- Node.jsで動くWebアプリを簡単に作れる仕組み（フレームワーク）
- ルーティングやミドルウェアの管理がしやすい

## 基本の流れ

1. express()でアプリを作る
2. app.use()でミドルウェアを登録（共通処理や静的ファイル配信など）
3. app.set()で設定（例：テンプレートエンジンの設定）
4. ルーティングを設定（URLごとの処理を決める）
5. サーバーを起動して、リクエストを待つ

## 例

~~~js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Express!');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
~~~

## app.jsの例

- ミドルウェア登録（例：ログ、JSON解析）
- ルーティング読み込み
- エラーハンドリング

---
