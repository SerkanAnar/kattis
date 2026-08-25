import math
from itertools import permutations

n = input()
line = input()
ages = list(map(int, line.split()))
perm = list(permutations(ages))
ans = None

for permutation in perm:
    found = True
    for i in range(len(permutation)-1):
        if math.gcd(permutation[i], permutation[i+1]) == 1:
            found = False
            break
    if found:
        ans = permutation
        break
if ans:
    print(*ans)
else:
    print('Neibb')