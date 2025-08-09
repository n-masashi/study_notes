"use strict";

/*
  HTTPレスポンスでよく使うメソッドをまとめる。

  response.writeHead(statusCode, headers)
    - レスポンスの最初の情報（ステータスコードやヘッダー）を送る。
    - 例：200は成功、404は見つからない、500はサーバーエラーなど。

  response.write(data)
    - レスポンス本文を送る。複数回呼ぶことも可能。

  response.end()
    - レスポンスの送信を終了する。最後に必ず呼ぶ必要がある。
    - 引数にデータを渡すと、write() と end() を同時に行うこともできる。
*/

// 例として、レスポンスメソッドを使うサーバー
const http = require("http");

const server = http.createServer((req, res) => {
  // ステータス200でHTMLを返す
  res.writeHead(200, { "Content-Type": "text/html" });

  // 本文の一部を送る
  res.write("<p>Hello, </p>");

  // 本文の続きと終了を同時に送る
  res.end("<strong>world!</strong>");
});

server.listen(3000);
console.log("Server running on port 3000");

/*
まとめ：

- writeHead でステータスとヘッダーを送る。
- write は本文の一部を送る（複数回可能）。
- end で送信終了。引数を渡せば本文の追加も可能。

これらを正しく使うことでブラウザに適切なレスポンスを返せます。
*/
