from itertools import product

operations = ['*', '+', '-', '//']
prod = product(operations, repeat=3)
op_order = []
for i in prod:
    op_order.append(i)

n = int(input())
for i in range(n):
    target = int(input())

    for (first, second, third) in op_order:
        expression = f'4 {first} 4 {second} 4 {third} 4'
        result = eval(expression)
        if result == target:
            print(f'{expression.replace("//", "/")} = {target}')
            break
    else:
        print('no solution')