import json

with open("dataset_0.json", 'r') as f:
    data = json.load(f)
print(data)


for i in range(len(data)):
    min_num = 0
    for j in range(i, len(data)):
        if data[i] > data[j]:
            min_num = data[j]
        print(data[i],data[j])
    print(min_num)
    data[i], data[min_num] = data[min_num], data[i]
    print(data)
    
#    data[i], data[min_id] = data[min_id], data[i]


print(data)




