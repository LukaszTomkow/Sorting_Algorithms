import json

with open("dataset_0.json", 'r') as f:
    data = json.load(f)
print(data)

for i in range(len(data)):
    if i > i+1 :
        data[i], data[i+1] = data[i+1], data[i]

print(data)


