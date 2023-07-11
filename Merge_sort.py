import json

with open("dataset_0.json", 'r') as f:
    data = json.load(f)

print(data)


def merge_sort(data):
    if len(data) > 1:
        #cut in half
        data_r = data[len(data)//2:]
        data_l = data[:len(data)//2]


        merge_sort(data_l)
        merge_sort(data_r)

        #merge
        print(f"data_l: {data_l}")
        print(f"data_r: {data_r}")
        result = []
        for i in range(len(data_l) + len(data_r)):
            if data_l !=[] and data_r !=[]:
                if data_l[0] < data_r[0] :
                    result.append(data_l[0])
                    data_l.pop(0)
                else:
                    result.append(data_r[0])
                    data_r.pop(0)
            elif data_l ==[]:
                result.append(data_r[0])
                data_r.pop(0)
            else:
                result.append(data_l[0])
                data_l.pop(0)
        print(f"result: {result}")
        print('')


print(merge_sort(data))