

#### powerset, all subsets of a set ####
def powerset(li):
    ps = []
    for n in range(0, 2**len(li)):
        sub = []
        x = n
        for i in range(len(li)):
            if x & 0x1:
                sub.append(li[i])
            x >>= 1
        ps.append(sub)
    return ps

if __name__ == '__main__':
    ps = powerset([1, 2, 3])
    for x in ps:
        print(x)
    print('Size is ' + str(len(ps)))
