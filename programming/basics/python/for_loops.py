# -------- List形式 --------
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
 
 # 出力: apple banana orange
    
# -------- 数字 --------
for i in range(5):
    print(i)  
    
 # 出力: 0 1 2 3 4 
    
# -------- 開始/終了、ステップ指定 --------    
for i in range(1, 10, 2):
    print(i) 
    
 # 出力: 1 3 5 7 9（1から始まり、2ずつ増加）
 
 # -------- 辞書ループ -------- 
person = {'name': 'Taro', 'age': 25}
for key, value in person.items():
    print(f"{key} → {value}")
    
 # 出力: name → Taro  age → 25  
