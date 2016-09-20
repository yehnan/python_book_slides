
# -*- coding: utf-8 -*-
# Raymond Hettingers
# http://code.activestate.com/recipes/576647/
from itertools import permutations

def queen(n):
    answers = []
    cols = range(n)
    
    # 產生出所有可能的擺法
    for ans in permutations(cols): # 逐一迭代，判斷擺法是否安全
        if (n == 
            len(set([ans[i]+i for i in cols])) == 
            len(set([ans[i]-i for i in cols]))):
            answers.append(ans)
            
    return answers

