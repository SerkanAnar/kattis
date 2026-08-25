input_values = list(map(int, input().strip().split()))

# For each target value, find boxes that sum to that value

targets = input_values[6:]
inputs = input_values[:6]

sorted_inputs = sorted(inputs, reverse=True)

# after sorting, we know that the first element is at the bottom, and last element is on top of some tower

bottom = sorted_inputs[0]
for i in range(1, len(sorted_inputs)):
    broken = False
    for j in range(i+1, len(sorted_inputs)):
        next_sum = sorted_inputs[i] + sorted_inputs[j]
        if next_sum + bottom in targets:
            result = sorted([bottom, sorted_inputs[i], sorted_inputs[j]], reverse=True)
            values_to_remove = [0, i, j]
            broken = True
            break
    if broken:
        break

sorted_inputs = [box for i, box in enumerate(sorted_inputs) if i not in values_to_remove]

if sum(result) == targets[0]:
    result = result + sorted_inputs
else:
    result = sorted_inputs + result
print(*result)