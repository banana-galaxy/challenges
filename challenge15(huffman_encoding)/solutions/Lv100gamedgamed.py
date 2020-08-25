def solution(x):
    c = dict()
    y = x.split()

    for word in y:
        if word in c:
            c[word] += 1
        else:
            c[word] = 1

    counts_x = sorted(c.items(), key=lambda kv: kv[1], reverse=True)

    for i, k in enumerate(counts_x):
        c[k[0]] = i + 1

    answer = ''
    for word in y:
        answer += str(c[word]) + ' '
    return answer.strip()