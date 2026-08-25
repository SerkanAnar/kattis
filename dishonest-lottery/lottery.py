from collections import defaultdict

n = int(input().strip())
counts = defaultdict(int)

for i in range(10*n):
    values = list(map(int, input().strip().split()))
    for value in values:
        counts[value] += 1

result = []
for key, value in counts.items():
    if value > 2*n:
        result.append(key)
result.sort()
print(*result, sep=' ') if len(result) != 0 else print(-1)