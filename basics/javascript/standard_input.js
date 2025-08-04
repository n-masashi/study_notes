// Node.jsでの標準入力（1行）
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf-8").trim();
console.log("入力値:", input);

// 複数行の処理
const lines = input.split("\n");
for (let i = 0; i < lines.length; i++) {
    console.log("Line", i + 1, ":", lines[i]);
}

// Tips: input.split(" ") で空白区切り、map(Number)で数値変換できる！


// テンプレ（よく使う形）
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
