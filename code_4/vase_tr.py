


# with open('vase.txt', 'r', encoding='utf-8') as fin:
    # with open('vase_gbk.txt', 'w', encoding='gbk') as fout:
        # for line in fin:
            # fout.write(line)


####

with open('vase_gbk.txt', 'r', encoding='gbk') as fin:
    with open('vase_cp950.txt', 'w', encoding='cp950') as fout:
        for line in fin:
            fout.write(line)
