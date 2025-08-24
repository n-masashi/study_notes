# 音声データを使った分類（予測）の入門メモ

## 1. 使うライブラリ
```python
import numpy as np                # 数値データや配列を扱う
import librosa                     # 音声データを読み込んだり解析する
import librosa.display             # 音声データをグラフで可視化する
import os                          # ファイルやディレクトリを操作する
import matplotlib.pyplot as plt    # グラフを描く
from sklearn.model_selection import train_test_split  # 学習用・テスト用に分ける
from sklearn import svm            # SVMモデルで分類
from scipy import fftpack           # フーリエ変換の計算
```

### 解説
- `librosa` は音声データを読み込んだり、波形や周波数を扱う便利ツール  
- `matplotlib` は波形や結果を可視化するのに使う  
- `svm` は分類モデルとして利用  

---

## 2. 音声データの読み込みと波形表示
```python
dir_name = 'voiceset'
for file_name in sorted(os.listdir(path=dir_name)):
    print("read: {}".format(file_name))
    a, sr = librosa.load(os.path.join(dir_name, file_name))
    print(a.shape)
    librosa.display.waveplot(a, sr)
    plt.show()
```

### 解説
- `librosa.load()` → 音声ファイルを読み込み、波形データ `a` とサンプリングレート `sr` を取得  
- `waveplot()` → 音の強さ（振幅）を時間軸に沿って描画  
- `plt.show()` → グラフを表示  

---

## 3. スピーカーのラベル設定
```python
speakers = {'kirishima' : 0, 'suzutsuki' : 1, 'belevskaya' : 2}
```

### 解説
- 音声ファイルの話者を数字で管理  
- SVMに渡すために文字列より数字の方が扱いやすい  

---

## 4. 特徴量の作成（波形直接利用）
```python
def get_feat(file_name):
    a, sr = librosa.load(file_name)
    return a[0:5000]   # 最初の5000フレームだけ使う
```

### 解説
- 音声をそのまま使って特徴量とする  
- フレーム数が多いので、最初の5000だけ取り出して簡略化  
- この方法は完全一致を狙うので精度は低め

---

## 5. データセット作成
```python
def get_data(dir_name):
    data_X = []
    data_y = []
    for file_name in sorted(os.listdir(path=dir_name)):
        print("read: {}".format(file_name))
        speaker = file_name[0:file_name.index('_')]
        data_X.append(get_feat(os.path.join(dir_name, file_name)))
        data_y.append((speakers[speaker], file_name))
    return (np.array(data_X), np.array(data_y))

data_X, data_y = get_data('voiceset')
```

### 解説
- `data_X` → 特徴量（波形やフーリエ変換後の数値列）  
- `data_y` → 教師ラベル（誰の声か）  
- SVMで学習するために数字ラベルと紐付ける

---

## 6. 教師データとテストデータに分ける
```python
train_X, test_X, train_y, test_y = train_test_split(data_X, data_y, random_state=11813)
```

### 解説
- データの一部を学習用（train）、一部を評価用（test）に分ける  
- `random_state` を固定すると再現性あり

---

## 7. SVMで学習
```python
clf = svm.SVC(gamma =0.0001, C=1)
clf.fit(train_X, train_y.T[0])
```

### 解説
- `SVC` → サポートベクターマシンによる分類モデル  
- `gamma` / `C` → 境界線の柔らかさや制約の強さを調整  
- `fit()` → 学習用データで境界線を決める

---

## 8. 予測して正解率を確認
```python
ok_count = 0
for X, y in zip(test_X, test_y):
    actual = clf.predict(np.array([X]))[0]
    expected = y[0]
    file_name = y[1]
    ok_count += 1 if actual == expected else 0
    result = 'o' if actual == expected else 'x'
    print("{} file: {}, actual: {}, expected: {}".format(result, file_name, actual, expected))

print("{}/{}".format(ok_count, len(test_X)))
```

### 解説
- `clf.predict()` → 学習済みモデルに新しいデータを渡して分類  
- `actual` → 予測結果  
- `expected` → 本当のラベル  
- 正解なら `'o'`、不正解なら `'x'` を表示  
- 最後に正解数/テスト数を表示

---

## 9. フーリエ変換を使った特徴量
```python
from scipy import fftpack

def get_feat(file_name):
    a, sr = librosa.load(file_name)
    fft_wave = fftpack.rfft(a, n=sr)
    fft_freq = fftpack.rfftfreq(n=sr, d=1/sr)
    y = librosa.amplitude_to_db(fft_wave, ref=np.max)
    return y
```

### 解説
- 音声は時間とともに振幅が変わる波のようなデータ
- **フーリエ変換** を使うと、波を「どんな高さの音がどれくらい含まれているか」に分解できる  
  - 例：高い音・低い音の成分を数字にするイメージ
- `fftpack.rfft(a, n=sr)`  
  - 音の波形を周波数の波に変換  
  - どの周波数（高さの音）がどれくらい強いかがわかる  
- `fftpack.rfftfreq(n=sr, d=1/sr)`  
  - 変換後の各数字がどの周波数に対応するかを計算  
- `librosa.amplitude_to_db(fft_wave, ref=np.max)`  
  - 音の強さ（振幅）を **デシベル表示** に変換  
  - グラフにしたとき見やすくなる  
- この方法で作った特徴量は、**波形をそのまま使うより高音・低音の情報が明確**  
- そのため、SVMで分類すると精度が上がりやすい

---

💡 ポイント
- 波形だけで判断するのは「波の形が完全に一致するか」を見ている状態  
- フーリエ変換を使うと「どんな音の高さが含まれているか」に注目できるので、同じ人の声をより正確に判定できる

---

## 10. まとめ
- 音声データの分類にはまず **特徴量作り** が重要  
- **波形直接** は簡単だが精度低め  
- **フーリエ変換** は周波数情報を使えるので精度向上  
- `librosa` は音声データの読み込み・可視化に便利  
- `svm` は少量データでも簡単に分類できる  
- 正解率を見て、特徴量やパラメータを調整するのが基本
