
# -*- coding: utf-8 -*-

tc = (0, 100, 30.2, 22.5, -15.8, 23.7)

def ctof(c): # 攝氏轉華氏
    return c * 9.0 / 5.0 + 32

itr_f = map(ctof, tc)

for f in itr_f:
    print(f)
    
#### 改用lambda
print('')
for f in map(lambda c: c*9.0/5.0+32, tc):
    print(f)

#### zip原攝氏溫度與華氏溫度
print('')
for c, f in zip(tc, map(ctof, tc)):
    print(c, f)

#### 運用產生器，自己寫map（功能較少）
def my_map(func, itb):
    for e in itb:
        yield func(e)

print('')
for f in my_map(ctof, tc):
    print(f)
    
    