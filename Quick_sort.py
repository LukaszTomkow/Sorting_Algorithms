import json


def quick_sort(data):
    print(data)
    if len(data) > 1:
        p = data[len(data)-1]      #pivot
        print(f'p: {p}')
        lsubarray = data[:data.index(p)-1]
        rsubarray = data[p:]
        print(f"l: {lsubarray}")
        print(f"r: {rsubarray}")
        k = data[len(data)-2]
        for i in range(len(data) -1):
            if i == k:
                if data[i] > p:
                    data[i], data[data.index(p)] = data[data.index(p)], data[i]
                pass

            if data[i] > p:
                lswap = data[i]
                for j in range(len(data)-1):
                    if data[k] < p:
                        rswap = data[k]
                        data[i], data[k] = rswap, lswap
                        k -= 1
        print(data)
        print('')
        quick_sort(lsubarray)
        quick_sort(rsubarray)
        
    return data



with open('dataset_0.json', 'r') as f:
    data = json.load(f)

print(quick_sort(data))

