n = int(input())
if n == 1 or n == 2:
    print(n*2)
else:
    a = n // 2
    b = n - a
    print((a+1) * (b+1))