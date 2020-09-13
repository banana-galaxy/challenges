def solution(days: int):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ret_proto = []
    for i in range(len(months)):
        if months[i] == days:
            if i == len(months):
                ret_proto.append(months[0])
            else:
                ret_proto.append(months[i - 1])
        else:
            print(f"{months[i]} != {days}")
    ret = []
    for i in ret_proto:
        if i not in ret:
            ret.append(i)
    return ret