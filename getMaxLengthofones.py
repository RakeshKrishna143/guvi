arr='101011111'
def getMaxLengthofones(arr, n):
    count = 0
    result = 0
    for i in range(n):
        if (arr[i] == '0'):
            count = 0
        else:
            count+= 1
        result = max(result, count)
    return result 
if arr.count('1')==0:
    print('-1')
else:
    print(getMaxLengthofones(arr, len(arr))) 
