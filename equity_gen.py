from itertools import combinations
import subprocess

ranks = tuple('23456789TJQKA')
suits = tuple('scdh')

pair_combs = list(combinations(suits, 2))
rev_pair_combs = [(s2, s1) for s1, s2 in pair_combs]

suits_combs = {
    'pair': pair_combs,
    'off_suited': pair_combs + rev_pair_combs,
    'suited': [(s, s) for s in suits]
}

combs_all = []
combs_single = []
for i in range(13):
    for j in range(13):
        hand_type = 'pair' if i == j else 'suited' if i > j else 'off_suited'
        r1 = ranks[i]
        r2 = ranks[j]
        hand_combs = [r1 + s1 + r2 + s2 for s1, s2 in suits_combs[hand_type]]
        combs_all.append(','.join(hand_combs))
        combs_single.append(hand_combs[0])



file = open('output.txt', 'w')
for i in range(168):
    print(i)
    for j in range(i + 1, 169):
        file.write(subprocess.getoutput(f'ps-eval {combs_all[i]} {combs_single[j]}')+'\n\n')
file.close()
