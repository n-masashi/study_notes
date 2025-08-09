"use strict";

/*
  http.createServer() は Node.js の HTTP サーバーを作るための関数です。

  使い方：
  - 引数に「リクエストが来た時に実行する関数」を渡します。
  - その関数は request（リクエスト情報）と response（レスポンス操作用）の2つを受け取ります。
  - createServer はサーバーオブジェクトを返します。
*/

// HTTPモジュールの読み込み
const http = require("http");

// サーバーを作成する
const server = http.createServer((request, response) => {
  // ここでリクエストを処理し、レスポンスを返す

  // レスポンスのヘッダーを書き込み（成功、HTML形式）
  response.writeHead(200, { "Content-Type": "text/html" });

  // レスポンスボディ（本文）を書き込み
  response.write("<h1>Hello from createServer!</h1>");

  // レスポンス終了
  response.end();
});

// ポート番号3000でサーバーを起動
server.listen(3000);

// 起動完了メッセージ
console.log("Server is listening on port 3000");

/*
ポイントまとめ：

1. http.createServer(callback)
   - HTTPサーバーを作る。
   - callback関数は、アクセスがあったときに呼ばれる。
   - 引数は request（アクセス情報）, response（返事用）。

2. response.writeHead(statusCode, headers)
   - レスポンスのステータスコードとヘッダーを設定。

3. response.write(data)
   - レスポンスの本文を送る。

4. response.end()
   - レスポンスを終了してクライアントに送信。

5. server.listen(port)
   - 作成したサーバーを指定したポート番号で起動する。
*/
