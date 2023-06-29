import random
import json



dataset = []
temp_data = []

for i in range(1000):
    temp_data.append(i)

for i in range(len(temp_data)):
    a = random.choice(temp_data)
    temp_data.remove(a)
    dataset.append(a)

with open("dataset_3.json", 'w') as f:
    json.dump(dataset, f)

