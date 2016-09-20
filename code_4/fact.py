

def fact_i(n):
    result = 1
    for i in range(1, n+1):    
        result *= i
    return result
####
def fact_r(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)
####
def fact_r2(n, answer=1):
    if n == 1 or n == 0:
        return answer
    else:
        return fact_r2(n-1, n*answer)
####

if __name__ == '__main__':
    for n in range(10):
        fi = fact_i(n)
        fr = fact_r(n)
        fr2 = fact_r2(n)
        if fi != fr:
            print('error: %d, %d, %d' % (n, fi, fr))
        if fi != fr2:
            print('error: %d, %d, %d' % (n, fi, fr2))            
            
            