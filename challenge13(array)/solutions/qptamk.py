def solution(array):
    global a


    global cvalue
    global ocvalue
    a = len(array) - 1
    cvalue = 0
    ocvalue = 0

    for p in range(len(array)):
        for i in range(len(array)):
            for j in range(len(array)):
                if i <= a - j:
                    if array[i] > array[a - j]:
                        continue

                    if array[i] < array[a - j]:
                        temp1 = array[i]
                        temp2 = array[a - j] + 1
                        cvalue = temp2 - temp1
                        ocvalue = ocvalue + cvalue
                        array[i] = array[i] + cvalue

                    if array[i] == array[a - j] and i == a - j:
                        continue
                    if array[i] == array[a - j] and i != a - j:
                        array[i] = array[i] + 1
                        ocvalue = ocvalue + 1
    print(ocvalue)