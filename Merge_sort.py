import json

with open("dataset_0.json", 'r') as f:
    data = json.load(f)

print(data)

def merge_sort(data):
    if len(data) > 1:
        #cut in half
        print(data)
        merge_sort(data[0,len(data)/2])
    
    else:
        #merge remaning data with other list
        print(data)


merge_sort(data)