n, s, m = map(int, input().strip().split(' '))
board = [int(x) for x in input().strip().split(' ')]
visited = [False] * n

curr = s
res = (None, None)
h = 0

while True:
    if curr > n: 
        res = ('right', h)
        break

    elif curr < 1:
        res = ('left', h)
        break

    elif board[curr-1] == m:
        res = ('magic', h)
        break

    elif visited[curr-1]:
        res = ('cycle', h)
        break

    visited[curr-1] = True
    curr += board[curr-1]
    h += 1

print(*res, sep='\n')