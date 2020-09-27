def solution(x):
    l = [1] * (x + 1);s = {4}
    for i in range(2, x // 2):
        if l[i]: l[i * i::i] = [0] * int((x / i - i + 1));s.add(i * i)
    return int("01"[int(x) in s::2])