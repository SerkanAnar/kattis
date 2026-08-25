from collections import defaultdict
n = int(input().strip())
counts = defaultdict(int)

for i in range(n):
    costume = input().strip()
    counts[costume] += 1

min = float('inf')
for key, value in counts.items():
    if value < min:
        min = value

result = []
for key, value in counts.items():
    if value == min:
        result.append(key)

result.sort()
print(*result, sep='\n')