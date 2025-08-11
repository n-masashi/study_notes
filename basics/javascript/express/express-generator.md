# Expressテンプレート生成ツール（express-generator）について

---

## express-generatorとは？

- Express公式のテンプレート生成ツール  
- CLIでプロジェクトの雛形を簡単に作成できる  
- ルーティングやビュー、設定ファイルなどの基本構造があらかじめ用意される

---

## インストール方法

    npm install express-generator -g

- `-g` はグローバルインストールの意味  
- どこでも `express` コマンドが使えるようになる

---

## プロジェクトの作成

    express myapp

- `myapp` は作成するプロジェクト名  
- カレントディレクトリに `myapp` フォルダができる

---

## オプション例

- `--view pug`  
  → ビューエンジンをPugに指定（デフォルトはJade）  
- `--view ejs`  
  → EJSを使う場合  
- `--css stylus`  
  → CSSプリプロセッサを指定（stylus, less, sassなど）  
- `--git`  
  → `.gitignore` ファイルも作成する

例：

    express myapp --view ejs --git

---

## 使い方の流れ

1. express-generatorで雛形作成

        express myapp

2. 作成フォルダに移動

        cd myapp

3. 依存モジュールをインストール

        npm install

4. サーバー起動

        npm start

5. ブラウザで `http://localhost:3000` にアクセスして動作確認

---

## まとめ

- express-generatorでテンプレをさっと作って、開発を効率化できる  
- 生成された構成をベースに、自分の機能を追加していく

---

## 参考

- [express-generator公式リポジトリ](https://github.com/expressjs/generator)
