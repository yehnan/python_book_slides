
# -*- coding: utf-8 -*-

class Frange():
    def __init__(self, start, end=None, inc=None):
        self.start = float(start)  # 避免某些情況出現int
        self.end = end
        self.inc = inc
        
        if self.end is None:      # 傳入一個參數的情況
            self.end = self.start
            self.start = 0.0
            
        if self.inc is None:
            self.inc = 1.0 
            
    def __iter__(self): # 既是Iterable、也是Iterator
        return self
        
    def __next__(self):
        x = self.start
        self.start += self.inc
        
        if abs(x) < abs(self.end):  # 處理正、負的情況
            return x
        else:
            raise StopIteration

####

for x in Frange(3):
    print(x)
print()
print(list(Frange(2.55, 3.7, 0.1)))
print()
print(list(Frange(0, 1, 0.1)))

