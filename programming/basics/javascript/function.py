/**
 * JavaScriptの関数まとめメモ
 * - 基本の関数定義
 * - 無名関数
 * - アロー関数
 * - 関数の引数と戻り値
 * - this の挙動の違い（簡単に）
 */

/**
 * 1. 通常の関数定義
 */
function greet(name) {
  return "こんにちは、" + name + "さん！";
}
console.log(greet("タロウ"));  // こんにちは、タロウさん！

/**
 * 2. 無名関数（関数リテラル）
 *    変数に代入して使う
 */
const greet2 = function(name) {
  return "やあ、" + name + "さん！";
};
console.log(greet2("ハナコ"));  // やあ、ハナコさん！

/**
 * 3. アロー関数（ES6以降）
 *    短く書けて、thisの扱いが違う
 */
const greet3 = (name) => {
  return "ハロー、" + name + "さん！";
};
console.log(greet3("ジロー"));  // ハロー、ジローさん！

/**
 * 引数が1つなら () は省略可能
 */
const greet4 = name => "こんにちは〜、" + name + "さん！";
console.log(greet4("ケン"));  // こんにちは〜、ケンさん！

/**
 * 複数行の処理や複雑な処理は波括弧と return が必要
 */
const greet5 = name => {
  const msg = "ようこそ、" + name + "さん！";
  return msg;
};
console.log(greet5("ミカ"));  // ようこそ、ミカさん！

/**
 * 4. this の挙動の違い（ざっくり）
 * - 通常関数は呼び出し元で this が変わる
 * - アロー関数は定義された場所の this を使う
 */
const obj = {
  name: "オブジェクト",
  normalFunc: function() {
    console.log("normalFunc this.name =", this.name);
  },
  arrowFunc: () => {
    console.log("arrowFunc this.name =", this.name);
  }
};
obj.normalFunc(); // オブジェクト
obj.arrowFunc();  // undefined（またはグローバルのthis.name）

/**
 * 5. 無名関数を使ったsetTimeoutの例
 */
setTimeout(function() {
  console.log("1秒後に無名関数が実行されました");
}, 1000);

/**
 * 6. アロー関数を使ったsetTimeoutの例
 */
setTimeout(() => {
  console.log("1秒後にアロー関数が実行されました");
}, 1000);
