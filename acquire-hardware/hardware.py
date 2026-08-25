h, w = map(int, input().strip().split())
grid = []
for i in range(h):
    grid.append(list(input().strip()))
dp = [[0 for _ in range(w)] for _ in range(h)]

# initialise upper row values and left column values
for i in range(1, w):
    dp[0][i] = dp[0][i-1]
    if grid[0][i] == 'I':
        dp[0][i] += 1

for i in range(1, h):
    dp[i][0] = dp[i-1][0]
    if grid[i][0] == 'I':
        dp[i][0] += 1

for i in range(1, h):
    for j in range(1, w):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (1 if grid[i][j] == 'I' else 0)

print(dp[-1][-1])