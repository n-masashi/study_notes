// const と let の違い
const PI = 3.14;
// PI = 3; // エラー: constは再代入不可

let count = 10;
count = 20; // OK

// var の問題点（巻き上げ）バグの元何で知っておくだけ。今は使われないらしい
function test() {
  console.log(x); // undefined（巻き上げ）
  var x = 5;
}
test();

// ブロックスコープ
{
  let x = 1;
  const y = 2;
  // var z = 3; // varは関数スコープ
}
// console.log(x); // エラー: xはブロックスコープ内のみ有効

// 論理演算子
console.log(true && false); // false
console.log(true || false); // true
console.log(!true);         // false

// 比較演算子
console.log(1 == "1");  // true（型変換あり）
console.log(1 === "1"); // false（型も値もチェック）

// 三項演算子
let age = 20;
let canVote = (age >= 18) ? "yes" : "no";
console.log(canVote); // yes

// 整数除算
console.log(Math.floor(5 / 3));  // 1
console.log(Math.trunc(-5 / 3)); // -1
