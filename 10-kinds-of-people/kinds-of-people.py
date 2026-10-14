from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = map(int, input().strip().split()) # keep in mind that r and c are 1-indexed

board = []
for _ in range(r):
    row = input().strip()
    row = [int(x) for x in row]
    board.append(row)

r, c = len(board), len(board[0])
groups = [[-1]*c for _ in range(r)]
curr_group = 0

for i in range(r):
    for j in range(c):
        if groups[i][j] != -1:
            continue
        queue = deque([(i, j)])
        groups[i][j] = curr_group
        while queue:
            s = queue.popleft()
            for dr, dc in dirs:
                nr, nc = s[0] + dr, s[1] + dc
                if 0 <= nr < r and 0 <= nc < c and groups[nr][nc] == -1 and board[nr][nc] == board[s[0]][s[1]]:
                    queue.append((nr, nc))
                    groups[nr][nc] = curr_group
        curr_group += 1

n = int(input().strip())
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().strip().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    if groups[r1][c1] == groups[r2][c2]:
        if board[r1][c1] == 1:
            print("decimal")
        else:
            print("binary")
    else:
        print("neither")