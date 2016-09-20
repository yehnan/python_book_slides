

li = [0, 1, 2, 3, 4, 5]

for i in range(len(li)):
    if li[i] % 2 == 0:
        del li[i]

print(li)
