n = int(input().strip())
reduced = n % 100
result = -1

if n < 100:
    result = 99
elif reduced >= 49: 
    rest = 100 - reduced
    result = n + rest - 1
else:
    result = n - reduced - 1

print(result)