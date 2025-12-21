# エラーハンドリングの流れ

## 404エラー

- ページが見つからなかったときの処理

~~~js
app.use((req, res, next) => {
  const err = new Error('Not Found');
  err.status = 404;
  next(err);
});
~~~

## エラーハンドラー

- エラーが起きたときの最終処理

~~~js
app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.render('error', { message: err.message });
});
~~~

---
