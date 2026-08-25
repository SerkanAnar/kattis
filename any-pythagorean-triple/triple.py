import math

n = int(input())
result = [0, 0, 0]
for a in range(1, n):
    for b in range(1, n):
        c = n - a - b
        if math.sqrt(a**2 + b**2) == c:
            result = sorted([a, b, c])
print(*result)