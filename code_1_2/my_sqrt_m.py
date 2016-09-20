

def my_sqrt(n, diff=0.00001):
    def is_ok(n, ans, diff):
        return abs(ans**2 - n) < diff
        
    def get_better(n, ans):
        print(((float(n) / ans) + ans) / 2)
        return ((float(n) / ans) + ans) / 2
        
    ans = 1
    while not is_ok(n, ans, diff):
        ans = get_better(n, ans)
    return ans

if __name__ == '__main__':
    import math
    print(my_sqrt(9), math.sqrt(9))
    print(my_sqrt(2), math.sqrt(2))
    print(my_sqrt(3), math.sqrt(3))



