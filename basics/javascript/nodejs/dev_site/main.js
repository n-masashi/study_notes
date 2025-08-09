"use strict";

const port = 3000;
const http = require("http");
const fs = require("fs");

function readFile(file, contentType, response) {
    fs.readFile(`./${file}`, (errors, data) => {
        if (errors) {
            console.log("Error reading the file...");
            response.writeHead(500, { "Content-Type": "text/plain" });
            response.end("Internal Server Error");
            return;
        }
        // ファイル読み込み成功時にヘッダーとデータを送信
        response.writeHead(200, { "Content-Type": contentType });
        response.end(data);
    });
}

const app = http.createServer((request, response) => {
    if (request.url === "/" && request.method === "GET") {
        readFile("view/index.html", "text/html", response);
    } else if (request.url === "/public/image/nodejs.png" && request.method === "GET") {
        readFile("public/image/nodejs.png", "image/png", response);
    } else if (request.url === "/public/css/style.css" && request.method === "GET") {
        readFile("public/css/style.css", "text/css", response);
    } else {
    readFile("view/404.html", "text/html", response);
    }
});

app.listen(port);
console.log(`The server has started and is listening on port number: ${port}`);
