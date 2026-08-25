
def look_for_check(grid, king_pos):
    # check for rooks
    i, j = king_pos
    
        
    pass

t = int(input()) # t = test cases
grid = [['' for _ in range(8)] for _ in range(8)]
# dirs = {'r': [(1, 0), (0, 1)], 
#         'n': [(2, 1), (2, -1), (1, -2), (1, 2)],
#         'b': [(1, 1), (1, -1)],
#         'q': [(1, 0), (0, 1), (1, 1), (1, -1)]}
for _ in range(t):
    king_pos = (-1, -1)
    for i in range(8):
        line = input().strip()
        for j in range(8):
            grid[i][j] = line[j]
            if line[j] == 'K': 
                king_pos = (i, j)
    print("Yes") if look_for_check(grid, king_pos) else print("No")
    # print(*grid, sep='\n')

