import json

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) - 1]
    pivot_index = len(data) - 1

    i = 0
    for j in range(len(data) - 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[pivot_index] = data[pivot_index], data[i]

    left_partition = quick_sort(data[:i])
    right_partition = quick_sort(data[i + 1:])
    
    return left_partition + [data[i]] + right_partition

with open('dataset_1.json', 'r') as f:
    data = json.load(f)

print(quick_sort(data))
