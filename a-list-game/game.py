import math
X = int(input())

num = X
k = 0
current_num = 2
while current_num <= int(math.sqrt(X)):
    if num % current_num == 0:
        num /= current_num
        k += 1
    else:
        current_num += 1
if num > int(math.sqrt(X)):
    k += 1
print(k)