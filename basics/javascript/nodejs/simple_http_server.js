"use strict";

// --- Node.jsで簡単なWebサーバを作る基本コード ---
// ここでは http モジュールを使って、ポート3000でHelloメッセージを返すサーバを作ってみる。

// ポート番号を3000に設定。サーバーがここでアクセスを待つ。
const port = 3000;

// Node.jsの標準HTTPモジュールを読み込む
// HTTPサーバーを作るための機能がたくさん入っている
const http = require("http");

// サーバーを作成。request(要求), response(応答)の2つを受け取って処理を行う関数を登録。
const server = http.createServer((request, response) => {

  // レスポンスの最初の部分（ヘッダー）を送信。
  // 200は応答、Content-Typeは返す内容がHTMLであることを示す。
  response.writeHead(200, {
    "Content-Type": "text/html"
  });

  // 返すHTMLメッセージを用意
  const responseMessage = "<h1>Hello Node.js!</h1>";

  // 実際にブラウザにメッセージを書き込む
  response.write(responseMessage);

  // レスポンスを終了してクライアントに返す
  response.end();

  // サーバーのコンソールに送ったメッセージを表示（動作確認用）
  console.log(`Sent a response : ${responseMessage}`);
});

// サーバーに、どのポート番号でアクセスを待つかを指示
server.listen(port);

// 起動完了メッセージをコンソールに出す
console.log(`The server has started and is listening on port number: ${port}`);

/*
HTTPモジュールで使った主な関数・メソッド

1. require('http')
   - HTTPモジュールを読み込むための関数

2. http.createServer(callback)
   - 新しいHTTPサーバーを作る関数
   - callbackはリクエストが来た時に呼ばれる関数で、requestとresponseを引数に取る

3. server.listen(port)
   - 作ったサーバーを指定したポート番号で起動させる関数

4. response.writeHead(statusCode, headers)
   - レスポンスのヘッダー（状態コードと情報）を送る関数

5. response.write(data)
   - レスポンスの本文（データ）を送る関数

6. response.end()
   - レスポンスの送信を終了する関数
*/
