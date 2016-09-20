
# -*- coding: utf-8 -*-
# Steve Howell
# http://wiki.python.org/moin/SimplePrograms

def queen(n):
    answers = [()]    # ()是空tuple，代表還沒擺上任一皇后
    
    # 已有擺法ans，想在下列的第col欄擺皇后，判斷會不會被攻擊
    def under_attack(col, ans):
        return (col in ans or
                any([len(ans)-i == abs(c-col)
                    for i,c in enumerate(ans)]))
            
    for row in range(n): # n列
        answers = [ans + (col,)
                    for ans in answers
                    for col in range(n) # n欄
                    if not under_attack(col, ans)]
    return answers



