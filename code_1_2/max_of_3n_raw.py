

a, b, c = 3, 5, 7; x = None
if a < b:        # 縮排零層
    if b < c:        # 縮排一層
        x = c            # 縮排二層
    else:            # 縮排一層
        x = b            # 縮排二層
else:            # 縮排零層
    if a < c:        # 縮排一層
        x = c            # 縮排二層
    else:            # 縮排一層
        x = a            # 縮排二層
# 最後x會是a、b、c中最大的
print(x)
