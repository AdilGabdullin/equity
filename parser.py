import re
import numpy as np

ranks = tuple('23456789TJQKA')
starters = []
for i in range(13):
    for j in range(13):
        suffix = '' if i == j else 's' if i > j else 'o'
        hand = ranks[max(i, j)] + ranks[min(i, j)]
        starters.append(hand + suffix)

equities = np.zeros((169, 169), np.float32)
lines = iter(open('output.txt'))
for i in range(168):
    for j in range(i + 1, 169):
        line1 = next(lines)
        line2 = next(lines)
        _ = next(lines)
        groups = re.search(r'has (\S*) %.*\((\S*) (\S*)', line1).groups()
        p, win, tie = map(float, groups)
        lose = float(re.search(r'\((\S*)', line2).group(1))
        eq = (win + tie) / (win + lose + 2 * tie)
        equities[i][j] = eq
        equities[j][i] = 1 - eq

np.save('equity.npy', equities)

# test
for i in range(3):
    a = np.random.randint(169)
    b = np.random.randint(169)
    print(f'{starters[a]} vs {starters[b]}: {equities[a][b]}')
    print(f'{starters[b]} vs {starters[a]}: {equities[b][a]}')
