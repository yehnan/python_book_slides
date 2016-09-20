
# -*- coding: utf-8 -*-
def queen(n):
    answers = []

    # 已有部分擺法ans，判斷是否可在下一列的第col欄擺上皇后
    def is_safe(ans, col):
        for i, c in enumerate(ans):
            if len(ans)-i == abs(c-col):
                return False
        return True
        
    # def is_safe(ans, col):
        # return all([not len(ans)-i == abs(c-col)
                     # for i, c in enumerate(ans)])

    # 遞迴
    def sub(ans):
        if len(ans) == n: # 已擺入n個皇后
            answers.append(ans)
        else:
            for col in range(n): # 逐一判斷要把皇后擺在次列的第0~(n-1)欄
                if col not in ans and is_safe(ans, col):
                    sub(ans + (col,)) # 若可以，加入答案，繼續下次遞迴
    
    sub(())  # 一開始ans是()空tuple，什麼都還沒擺
    return answers

####
def is_safe(ans, col):
    for i, c in enumerate(ans):
        if len(ans)-i == abs(c-col):
            return False
    return True

def queen_gf(n, ans=()):
        
    if len(ans) == n: 
        yield ans
    else:
        for col in range(n): 
            if col not in ans and is_safe(ans, col):
                yield from queen_gf(n, (ans + (col,))) 
    
####
if __name__ == '__main__':
    n = 8
    answers = queen(n)
    for ans in answers:
        print(ans)
    print(len(answers))
    print('-' * 20)
    answers2 = tuple(queen_gf(n))
    if set(answers) == set(answers2):
        print('yes')
    else:
        print('no')
    print(len(answers2))
    
