


for i in range(0x20, 0x7e+1):
    print('%2X %c   ' % (i, chr(i)), end='')
    if (i-0x20+1) % 8 == 0:
        print()



