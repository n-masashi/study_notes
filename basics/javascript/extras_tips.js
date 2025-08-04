// 数値の最大・最小
let max = -Infinity;
let min = Infinity;

// 三項演算子
let result = (score >= 60) ? "Pass" : "Fail";

// 配列から最大・最小を取得
let nums = [3, 7, 2, 9];
console.log(Math.max(...nums));
console.log(Math.min(...nums));
