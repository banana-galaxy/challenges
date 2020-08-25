def solution(text):
    word_list = text.split()
    word_count_dict = {word: word_list.count(word) for word in word_list}
    word_sorted = {k: v for k, v in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)}
    words = list(word_sorted.keys())
    output = ""
    for word in word_list:
        output += str(words.index(word) + 1) + " "
    return output.rstrip()