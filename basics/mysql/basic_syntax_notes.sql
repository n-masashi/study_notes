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

-- ======================================
-- 07. 内部結合（INNER JOIN）
-- ======================================

-- 映画ごとの言語名を取得（film と language テーブルを結合）
SELECT
    film.title,
    language.name AS language_name
FROM
    film
INNER JOIN
    language
ON
    film.language_id = language.language_id;

-- 別の例：books と authors を結合して、本のタイトルと著者名を取得
SELECT
    books.title,
    authors.name AS author_name
FROM
    books
INNER JOIN
    authors
ON
    books.author_id = authors.author_id;

-- 補足：
-- ・INNER JOIN は、両方のテーブルに共通するデータがある場合のみ結果に表示
-- ・ON で結合条件を指定
-- ・JOINの書き方は複数あるが、INNER JOIN が最も基本形

-- ======================================
-- 08. 外部結合（OUTER JOIN）
-- ======================================

-- LEFT OUTER JOIN（左外部結合）の例：
-- すべての本と、あれば著者名を取得（著者が不明でも本は出力される）
SELECT
    books.title,
    authors.name AS author_name
FROM
    books
LEFT OUTER JOIN
    authors
ON
    books.author_id = authors.author_id;

-- RIGHT OUTER JOIN（右外部結合）の例：
-- すべてのカテゴリと、そこに属する映画（film）があれば表示
SELECT
    category.name,
    film.title
FROM
    film
RIGHT OUTER JOIN
    category
ON
    film.category_id = category.category_id;

-- 補足：
-- ・LEFT OUTER JOIN：左テーブルを優先し、結合できない右側は NULL で埋める
-- ・RIGHT OUTER JOIN：右テーブルを優先し、結合できない左側は NULL で埋める
-- ・OUTER は省略可能（LEFT JOIN / RIGHT JOIN と書くのが一般的）
-- ・LEFT JOIN は非常によく使われる。RIGHT JOIN は LEFT JOIN に書き換え可能なので、使用頻度は少ない

-- ======================================
-- 09. グループ化（GROUP BY）
-- ======================================

-- 集計関数と組み合わせて、特定の列でグループ化する

-- 例：言語ごとの映画本数を取得（film テーブル）
SELECT
    language_id,
    COUNT(*) AS film_count
FROM
    film
GROUP BY
    language_id;

-- 例：著者ごとの本の平均価格（books テーブル）
SELECT
    author_id,
    AVG(price) AS avg_price
FROM
    books
GROUP BY
    author_id;

-- 例：各カテゴリに属する映画数を取得（JOIN + GROUP BY）
SELECT
    category.name,
    COUNT(film.film_id) AS film_count
FROM
    film
INNER JOIN
    category
ON
    film.category_id = category.category_id
GROUP BY
    category.name;

-- 補足：
-- ・GROUP BY は集計関数（COUNT, SUM, AVG, MAX, MINなど）と併用される
-- ・GROUP BY の列に含まれていない非集計列は SELECT で使えない（ONLY_FULL_GROUP_BY が有効な場合）
-- ・HAVING 句を使えば、GROUP BY 後の条件絞り込みが可能（WHERE ではなく）
