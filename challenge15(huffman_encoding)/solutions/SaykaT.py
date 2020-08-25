def solution(words):
    words = words.split()
    single_words = []
    for word in words:
        if word not in single_words:
            single_words.append(word)
    count = {}
    for word in single_words:
        count[word] = words.count(word)

    sorted_dict = {key: value for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True)}

    ans_dict = {}
    i = 1
    for key in sorted_dict:
        ans_dict[key] = i
        i += 1

    ans_list = []
    for word in words:
        ans_list.append(str(ans_dict[word]))
    ans = " ".join(ans_list)
    return ans