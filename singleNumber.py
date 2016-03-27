arr = [1,1,2,2,3,4,4]

def singleNumber(arr):
    counter = {}
    if len(arr) < 1:
        print(arr)
    for i in arr:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for key, value in counter.items():
        if value == 1:
            print(key)


singleNumber(arr)
