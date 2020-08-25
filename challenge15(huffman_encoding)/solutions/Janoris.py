# Huffman challenge
class huff_value:
    def __init__(self, v, f):
        self.value = v
        self.freq = f
        self.key = 0

    def set_key(self, k):
        self.key = k


def count_and_delete(dic, value):
    temp = []
    freq = 0
    for i in dic:
        if i == value:
            freq += 1
        else:
            temp.append(i)
    return temp, freq


def solution(values):
    dic = []

    current = ''
    for i in range(len(values)):
        if values[i] != ' ':
            current += values[i]
        else:
            dic.append(current)
            current = ''

    dic.append(current)
    copy = dic
    huff_values = []

    while len(dic) > 0:
        current_value = dic[0]
        new_dic = count_and_delete(dic, current_value)
        temp = huff_value(current_value, new_dic[1])
        huff_values.append(temp)
        dic = new_dic[0]

    sorte = sorted(huff_values, key=lambda x: x.freq, reverse=True)

    key = 0
    for i in sorte:
        key += 1
        i.set_key(key)

    decoded = ''

    for i in copy:
        for x in sorte:
            if x.value == i:
        decoded += str(x.key)
        decoded += ' '
        break

    return decoded