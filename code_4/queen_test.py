

import queen_hettingers as het
import queen_howell as how
import queen_basic as ba
import queen_hettingers_gf as het_gf

n = 8

het_answers = het.queen(n)
print(len(het_answers))
print(het_answers)

how_answers = how.queen(n)
# for answer in answers:
    # print(list(enumerate(answer, start=1)))
    #print(answer)

print(len(how_answers))
print(how_answers)

ba_answers = ba.queen(n)
print(len(ba_answers))
print(ba_answers)

ba_gf_answers = tuple(ba.queen_gf(n))

queen_het_g = het_gf.queen_gf(n)
het_g_answers = [x for x in queen_het_g]

print('')

#if set(iter(het_answers)) == set(iter(how_answers)):
if (set(het_answers) == set(how_answers) == set(ba_answers) == set(het_g_answers)
    == set(ba_gf_answers)):
    print('---yes---')
else:
    print('---no---')

