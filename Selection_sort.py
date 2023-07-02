import json

with open("dataset_3.json", 'r') as f:
    data = json.load(f)
print(data)

for i in range(len(data)):
    min_num = data[i]
    for j in range(i, len(data)):
        if min_num > data[j]:
            min_num = data[j]
            min_num_idx = j
    data[i], data[min_num_idx] = data[min_num_idx], data[i]

print(data)




