def solution(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    positions = {word: index+1 for index, word in enumerate(sorted(count.keys(), key=lambda x: count[x], reverse=True))}
    return ' '.join([str(positions[word]) for word in words])