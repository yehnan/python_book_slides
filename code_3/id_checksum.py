
# -*- coding: utf-8 -*-
from __future__ import print_function
import random

#### use list to store
# 'A' index is 0, 'B' index is 1, etc.. 'Z' is 25
loc_li = [10, 11, 12, 13, 14,
              15, 16, 17, 34, 18,
              19, 20, 21, 22, 35,
              23, 24, 25, 26, 27,
              28, 29, 32, 30, 31,
              33]
# location is 'A' or 'B' or ... 'Z'
def location_to_number(location):
    return loc_li[ord(location) - ord('A')]

#### use dict to store
loc_d = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14,
       'F':15, 'G':16, 'H':17, 'I':34, 'J':18,
       'K':19, 'L':20, 'M':21, 'N':22, 'O':35,
       'P':23, 'Q':24, 'R':25, 'S':26, 'T':27,
       'U':28, 'V':29, 'W':32, 'X':30, 'Y':31,
       'Z':33}

# input an id as str, use the first 9 characters
# to calculate the checksum
def checksum(id):
    total = 0
    
    x = loc_d[id[0]]
    # x = location_to_number(id[0])

    total += (x % 10) * 9 + (x // 10)
    
    for i in range(1, 8+1):
        total += int(id[i]) * (9-i)
        
    cksum = total % 10
    if cksum != 0:
        cksum = 10 - cksum

    return cksum
    
# 檢查id是否正確，回傳True或False
def check(id):
    return checksum(id) == int(id[9])

# location: 'A'~'Z'
# gender: 1 male, 2 female
def random_id(location, gender):
    id = location + str(gender)
    for _ in range(2, 8+1):
        n = random.randint(0, 9)
        id += str(n)
        
    id += str(checksum(id))
    
    return id


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('Usage: ' + __file__ + ' [-c id] or [-g [male/female]]')
    elif len(sys.argv) >= 2:
        if sys.argv[1] == '-c':
            if len(sys.argv) == 3:
                print('Verification: ', end='')
                if check(sys.argv[2]):
                    print('PASS')
                else:
                    print('FAIL')
                    cksum = checksum(sys.argv[2])
                    print('Correct: ' + sys.argv[2][:9] + str(cksum))
            else:
                print('Usage: ' + __file__ + ' -c id')
        elif sys.argv[1] == '-g':
            loc = chr(ord('A') + random.randint(0, 25))
            gender = random.randint(1, 2)
            print(random_id(loc, gender))
    else:
        print('Usage: ' + __file__ + ' [-c id] or [-g [male/female]]')
        # id_valid = ('A123456789', 'S212305438')
        # for id in id_valid:
            # if check(id) == False:
                # print('fail', id)

        # id_invalid = ('A123456781', 'S212305432')
        # for id in id_invalid:
            # if check(id) == True:
                # print('fail', id)

        # for i in range(26):
            # loc = chr(ord('A') + i)
            # if location_to_number(loc) != mapping[loc]:
                # print('fail', loc)
    
