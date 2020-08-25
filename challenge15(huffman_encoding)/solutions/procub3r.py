def solution(text):
    freq = {k: 0 for k in text.split()}
    for i in text.split():
        freq[i] += 1
    enc = 1
    encoded = freq.copy()
    for i in range(max(list(freq.values())), 0, -1):
        if i not in list(freq.values()):
            continue
        for k, v in freq.items():
            if v == i:
                encoded[k] = enc
        enc += 1
    return ' '.join([str(encoded[i]) for i in text.split()])