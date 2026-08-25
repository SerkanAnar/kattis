board = []
for i in range(8):
    board.append(input().strip())

found = False
for i in range(8):
    if '*' not in board[i]:
        found = True
        break
    j = board[i].index('*')
    for row in range(8):
        if row == i:
            continue
        if '*' in board[row] and board[row].index('*') == j:
            found = True
            break
    if board[i].count('*') > 1:
        found = True
    diag_i = i - 1
    diag_j = j - 1
    while diag_i >= 0 and diag_j >= 0:
        if board[diag_i].index('*') == diag_j:
            found = True
            break
        diag_i -= 1
        diag_j -= 1
    diag_i = i+1
    diag_j = j+1
    while diag_i < 8 and diag_j < 8:
        if '*' in board[diag_i] and board[diag_i].index('*') == diag_j:
            found = True
            break
        diag_i += 1
        diag_j += 1
    diag_i = i - 1
    diag_j = j + 1
    while diag_i >= 0 and diag_j < 8:
        if board[diag_i].index('*') == diag_j:
            found = True
            break
        diag_i -= 1
        diag_j += 1
    diag_i = i + 1
    diag_j = j - 1
    while diag_i < 8 and diag_j >= 0:
        if '*' in board[diag_i] and board[diag_i].index('*') == diag_j:
            found = True
            break
        diag_i += 1
        diag_j -= 1
if found:
    print('invalid')
else:
    print('valid')