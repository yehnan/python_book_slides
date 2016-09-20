

def my_sqrt(n):
    diff = 0.00001

    def is_good_enough(ans):
        return abs(ans**2 - n) < diff

    def get_better_ans(ans):
        return ((float(n) / ans) + ans) / 2

    ans = 1
    while not is_good_enough(ans):
        ans = get_better_ans(ans)
    return ans

if __name__ == '__main__':
    import math
    print(my_sqrt(9), math.sqrt(9))
    print(my_sqrt(2), math.sqrt(2))
    print(my_sqrt(3), math.sqrt(3))



