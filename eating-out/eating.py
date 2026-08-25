values = list(map(int, input().split()))
if sum(values[1:]) > 2*values[0]:
    print('impossible')
else:
    print('possible')