import json


def quick_sort(data):
    print(data)
    if len(data) > 1:
        p = data[len(data)-1]      #pivot
        print(f'p: {p}')
        lsubarray = data[:data.index(p)]
        rsubarray = data[data.index(p)+1:]

        k = len(data)-2
        for i in range(len(data) -1):
            print(f'i: {i}')
            print(f'k: {k}')
            print(f'data[i]: {data[i]}')
            if i == k:
                if data[i] > p:
                    print('hwdp')
                    data[i], data[data.index(p)] = data[data.index(p)], data[i]
                break

            if data[i] > p:
                for j in range(len(data)-1):
                    if data[k] < p:
                        print(f'data[k]: {data[k]}')
                        data[i], data[k] = data[k], data[i]
                        k -= 1
                        print(data)
                        break
        print(data)
        print('_________________________________________')
        quick_sort(lsubarray)
        quick_sort(rsubarray)
        
    return data



with open('dataset_0.json', 'r') as f:
    data = json.load(f)

print(quick_sort(data))

