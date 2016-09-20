
# -*- coding: utf-8 -*-

scores = (30, 45, 60, 80, 20)

def failed(score):
    return score < 60
    
# 挑出被當掉的 
sf = filter(failed, scores)

for s in sf:
    print(s)

#### 調整分數，開根號除以十

def adjust(score):
    from math import sqrt
    
    return sqrt(score) * 10
    
print('')
for s in filter(failed, map(adjust, scores)):
    print(s)

#### 保留原分數與調整後的分數
print('')

for so, sn in filter(lambda item: item[1] < 60, zip(scores, map(adjust, scores))):
    print(so, sn)

