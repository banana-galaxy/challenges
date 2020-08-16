def solution(value1,weight1,value2,weight2,maxWeight):
    items = [[value1,weight1],[value2,weight2]]

    items_weight = sorted(items, key = lambda x: x[1], reverse=False)
    items_value = sorted(items, key = lambda x: x[0], reverse=True)

    totalWeight = 0
    max1 = 0
    for item in items_weight:
        totalWeight+=item[1]
        if totalWeight>maxWeight:
            break
        max1+=item[0]

    totalWeight = 0
    max2 = 0
    for item in items_value:
        totalWeight+=item[1]
        if totalWeight>maxWeight:
            break
        max2+=item[0]

    return max(max1,max2)