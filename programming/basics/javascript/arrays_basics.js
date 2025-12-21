// 配列の生成
let arr = new Array(3);      // [ <3 empty items> ]
let arr2 = Array.of(1, 2, 3); // [1, 2, 3]
let arrCopy = [...arr2];      // 浅いコピー

// ループ
for (let i = 0; i < arr2.length; i++) {
  console.log(arr2[i]);
}

for (const val of arr2) {
  console.log(val);
}

arr2.forEach((val) => console.log(val));

// push / pop
arr2.push(4);
console.log(arr2);  // [1, 2, 3, 4]

let last = arr2.pop();
console.log(last);  // 4
console.log(arr2);  // [1, 2, 3]

// unshift / shift
arr2.unshift(0);
console.log(arr2);  // [0, 1, 2, 3]

let first = arr2.shift();
console.log(first); // 0
console.log(arr2);  // [1, 2, 3]

// splice / slice
arr2.splice(1, 1);   // インデックス1から1つ削除
console.log(arr2);   // [1, 3]

let sliced = arr2.slice(0, 1);
console.log(sliced); // [1]

// indexOf / includes
console.log(arr2.indexOf(3));    // 1
console.log(arr2.includes(5));   // false

// sort の注意点
let nums = [10, 2, 30];
nums.sort();
console.log(nums); // [10, 2, 30] ・・・ 文字列比較なので注意
// 数値比較のための書き方
nums.sort((a,b) => a - b);
console.log(nums); // [2, 10, 30]

// 多次元配列
let matrix = [
  [1, 2],
  [3, 4]
];
console.log(matrix[0][1]); // 2
