import json

with open("dataset_3.json", 'r') as f:
    data = json.load(f)
print(data)

for i in range(len(data)):
    for j in range(0, len(data)-1):
        if data[j] > data[j+1] :
            data[j], data[j+1] = data[j+1], data[j]

print(data)


