const fs = require("fs");

// 複数行を読み込み
const input = fs.readFileSync("/dev/stdin", "utf-8").trim().split("\n");

// 入力例：数値に変換
const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);

console.log(N, arr);

// 競プロテンプレ（よく使う形）
const lines = input;
const n = +lines[0];
for(let i=1; i<=n; i++) {
  const nums = lines[i].split(" ").map(Number);
  console.log(nums);
}

// 非同期入力 (補足)
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.on("line", (line) => {
  console.log(`入力：${line}`);
});
