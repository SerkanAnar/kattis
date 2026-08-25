input = "2 1"

R, C = map(int, input.split())
diff = R - C

A1 = R ** 2
A2 = diff ** 2

result = A2 / A1 * 100

print(result)