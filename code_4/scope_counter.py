
# -*- coding: utf-8 -*-

def counter(n):
    li = [n]
    def bar(x):
        li[0] += x           # 在bar裡，原地修改counter的li
        return li[0]
    return bar               # counter回傳「函式」
    
c0 = counter(0)              # 名稱c0與c100都指向函式物件
c100 = counter(100)

print(c0(1))         # 印出1
print(c100(10))      # 印出110

print(c0(1))         # 印出2
print(c0(3))         # 印出5
print(c100(20))      # 印出130

####
print()

def counter(n):
    def bar(x):
        nonlocal n
        n += x   
        return n
    return bar 
    
c0 = counter(0) 
c100 = counter(100)
print(c0(1))         # 印出1
print(c100(10))      # 印出110
print(c0(1))         # 印出2
print(c0(3))         # 印出5
print(c100(20))      # 印出130

