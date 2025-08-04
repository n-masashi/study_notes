let score = 75;

if (score >= 90) {
    console.log("Excellent");
} else if (score >= 60) {
    console.log("Pass");
} else {
    console.log("Fail");
}

// === を使うと型もチェック（== だと型を無視）
console.log("5" == 5);   // true
console.log("5" === 5);  // false

// Tips: 複数比較は && や || を使って a === b && b === c のように書く
