# 音声データの波形表示メモ（librosa）
---

## 1. 使うライブラリ
```python
import librosa
import librosa.display
import matplotlib.pyplot as plt
```
### 解説
- `librosa`：音声データを読み込んだり解析するライブラリ  
- `librosa.display`：音声をグラフとして描画するためのツール  
- `matplotlib.pyplot`：グラフを描く標準ライブラリ

---

## 2. 音声を読み込む
```python
a, sr = librosa.load('voiceset/kirishima_b01.wav')
```
### 解説
- `librosa.load()` → 音声ファイルを読み込む
- 戻り値：
  - `a` → 音声の **波形データ**（振幅の数値の列）
  - `sr` → **サンプリングレート**（1秒間に何回測ったか）
- 例：`sr = 22050` → 1秒間に 22050 フレームある

---

## 3. 波形を描く
```python
librosa.display.waveplot(a, sr)
plt.show()
```
### 解説
- `librosa.display.waveplot(a, sr)` → 音の強さ（振幅）を時間軸に沿って線で描く  
- `plt.show()` → グラフを画面に表示  
- 波の高さ → 音の強さ  
- 波の横軸 → 時間

---

## 4. 波形データの中身
```python
print(a)
print(len(a))
```
### 解説
- `a` → 音の強さを並べた数値の列（リストのような配列）  
- `len(a)` → 音声のフレーム数（サンプルの数）

---

## 5. サンプリングレートの確認
```python
print(sr)
```
### 解説
- 1秒間に何回音を測ったか  
- 音質が高いほど値は大きくなる  
- 波形配列の長さは `sr * 秒数` にほぼ一致する

---

## 6. 音声ファイルごとの波形描画
### 高音
```python
a, sr = librosa.load('sample/hi.wav')
librosa.display.waveplot(a, sr)
plt.show()
```
### 低音
```python
a, sr = librosa.load('sample/lo.wav')
librosa.display.waveplot(a, sr)
plt.show()
```
### 解説
- 同じ `waveplot` で、音声ファイルごとに波形を確認できる
- 高音は振幅の波が細かく、低音はゆったり波打つ特徴がある

---

## 7. 一部だけ描く（先頭100サンプル）
### 高音
```python
a, sr = librosa.load('sample/hi.wav')
librosa.display.waveplot(a[0:100], sr)
plt.show()
```
### 低音
```python
a, sr = librosa.load('sample/lo.wav')
librosa.display.waveplot(a[0:100], sr)
plt.show()
```
### 解説
- `a[0:100]` → 配列の最初の100フレームだけ使う
- 波の細かい部分（瞬間の変化）を確認できる
- 高音は短い時間で振動が多い → 波が細かくなる  
- 低音は振動が少ない → 波がゆったりになる

---

## 8. まとめ
- **音声データ = 数字の列（振幅）**  
- **サンプリングレート = 1秒間に何回音を測ったか**  
- `librosa.load()` で読み込み  
- `librosa.display.waveplot()` で波形を描画  
- 高音は細かく振動、低音はゆったり振動  
- `a[0:100]` のように部分を抜き出して波形を見ることもできる

---

💡 ポイント
- 音声データは「見えない波」を数値で表したもの
- 波形を見ると、高音・低音の違いが直感的に分かる
- `librosa` は音声の読み込みと可視化に便利なライブラリ
