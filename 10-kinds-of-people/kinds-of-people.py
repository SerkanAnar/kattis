from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

r, c = map(int, input().strip().split()) # keep in mind that r and c are 1-indexed

board = []
for _ in range(r):
    row = input().strip()
    row = [int(x) for x in row]
    board.append(row)

h, w = len(board), len(board[0])

n = int(input().strip())
queries = []
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().strip().split())
    queries.append((r1, c1, r2, c2))

types = ('decimal', 'binary')
for query in queries:
    visited = [[False] * w for _ in range(h)]
    result = None
    source = (query[0]-1, query[1]-1)
    target = (query[2]-1, query[3]-1)
    found = False
    for type_ in types:
        visited = [[False] * w for _ in range(h)]
        allowed = 1 if type_ == 'decimal' else 0
        if board[source[0]][source[1]] != allowed:
            continue

        queue = deque([source])
        # queue.append(source)
        visited[source[0]][source[1]] = True

        while queue:
            s = queue.popleft() # (0, 0)
            if s[0] == target[0] and s[1] == target[1]:
                if found == True:
                    result = None
                else:
                    found = True
                    result = type_
                break
            # look in all allowed directions
            # check boundaries
            # check that they are allowed
            # add to queue and mark as visited
            for dr, dc in dirs:
                nr, nc = s[0] + dr, s[1] + dc
                if (0 <= nr < h and 0 <= nc < w and board[nr][nc] == allowed and not visited[nr][nc]):
                    queue.append((nr, nc))
                    visited[nr][nc] = True

    print(result if result else "neither")