def solution(st):
    arr = st.split(" ")
    dic = {'hello' : 0}
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    temp = 1
    for a in sort_dic:
        dic[a[0]] = temp
        temp += 1
    temp = 1
    huffed = ""
    for a in arr:
        if not temp:
            huffed += " "
        huffed += str(dic[a])
        temp = 0
    return huffed