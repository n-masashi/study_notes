-- ======================================
-- 01. データベースの選択と前提
-- ======================================

-- 使用するデータベースを指定
USE bookstore;

-- ※前提：このデータベースには books, authors, orders などのテーブルがあると仮定

-- ======================================
-- 02. データの取得（SELECT 基本）
-- ======================================

-- 全カラムを取得
SELECT * FROM books;

-- 必要なカラムだけを取得
SELECT title, price FROM books;

-- ======================================
-- 03. 絞り込みとNULLの扱い（WHERE / NULL）
-- ======================================

-- NULLかどうかを確認
SELECT title FROM books WHERE price IS NULL;

-- NULLでないデータを取得
SELECT title FROM books WHERE price IS NOT NULL;

-- COALESCEでNULLをデフォルト値に変換
SELECT title, COALESCE(price, 0) AS price_with_default FROM books;

-- ======================================
-- 04. 並び替え・件数制限（ORDER BY / LIMIT）
-- ======================================

-- 価格が安い順に並び替え
SELECT title, price FROM books ORDER BY price ASC;

-- 発売日が新しい順に並び替え
SELECT title, published_date FROM books ORDER BY published_date DESC;

-- 最初の5件を取得
SELECT * FROM books LIMIT 5;

-- 6件目から10件目までを取得
SELECT * FROM books LIMIT 5 OFFSET 5;

-- ======================================
-- 05. Tips（コメント / 書式 / スタイル）
-- ======================================

-- コメントの書き方：
-- 一行コメント： -- を使う
-- 複数行コメント： /* ... */ を使う

/*
複数行コメントの例：
このクエリでは在庫がある本を価格順に表示しています。
*/

SELECT title, price
FROM books
WHERE stock > 0
ORDER BY price ASC;

-- コーディングスタイル：
-- ・SQLのキーワードは大文字に
-- ・テーブル名・カラム名は小文字が一般的（ただし自由）

-- ======================================
-- 06. BETWEEN 
-- ======================================

-- length が 85 以上 95 以下
SELECT *
FROM film
WHERE
   length BETWEEN 85 AND 95;
