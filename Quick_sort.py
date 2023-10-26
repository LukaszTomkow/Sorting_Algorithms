import json


def quick_sort(data):
    print(data)
    if len(data) > 1:
        p = data[len(data)-1]      #pivot
        pindex = len(data)-1       #pivot index
        print(f'p: {p}')


        k = len(data)-2
        for i in range(len(data) -1):
            print(f'i: {i}')
            print(f'k: {k}')
            print(f'data[i]: {data[i]}')
            if i == k:
                if data[i] > p:
                    data[i], data[pindex] = data[pindex], data[i]
                    print(data)
                    break

            if data[i] > p:
                for k in range(len(data)-2,0,-1):
                    if data[k] < p:
                        print(f'data[k]: {data[k]}')
                        data[i], data[k] = data[k], data[i]
                        print(data)
                        break
        lsubarray = data[:data.index(p)]
        rsubarray = data[data.index(p)+1:]
        print(data)
        print('_________________________________________')
        quick_sort(lsubarray)
        quick_sort(rsubarray)
        
    return data



with open('dataset_0.json', 'r') as f:
    data = json.load(f)

print(quick_sort(data))

