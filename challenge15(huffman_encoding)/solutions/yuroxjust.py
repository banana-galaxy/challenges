def solution(text):
    return_list = []
    word_list = []
    words = {}
    double_words = {}

    for word in text.split(" "):
        word_list.append(word)
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    sorted_words = sorted(words.values(), reverse=True)

    for w in word_list:
        frequency = words[w]
        return_value = [i + 1 for i, j in enumerate(sorted_words) if j == frequency]
        if len(return_value) == 1:
            return_list.append(str(return_value[0]))
        elif w in double_words:
            return_list.append(str(double_words[w]))
        elif w not in double_words:
            for x in return_value:
                if x not in double_words.values():
                    newvalue = x
                    break
            double_words[w] = newvalue
            return_list.append(str(double_words[w]))

    return " ".join(return_list)