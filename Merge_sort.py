import json

def merge_sort(data):
    if len(data) > 1:
        #cut in half
        data_r = data[len(data)//2:]
        data_l = data[:len(data)//2]

        merge_sort(data_l)
        merge_sort(data_r)

        #merge
        k = 0
        for i in range(len(data_l) + len(data_r)):
            if data_l !=[] and data_r !=[]:
                if data_l[0] < data_r[0] :
                    data[k] = (data_l[0])
                    data_l.pop(0)
                    
                else:
                    data[k] = (data_r[0])
                    data_r.pop(0)
            elif data_l ==[]:
                data[k] = (data_r[0])
                data_r.pop(0)
            else:
                data[k] = (data_l[0])
                data_l.pop(0)
            k += 1
    return data

        
with open("dataset_3.json", 'r') as f:
    data = json.load(f)

print(data)

print(merge_sort(data))