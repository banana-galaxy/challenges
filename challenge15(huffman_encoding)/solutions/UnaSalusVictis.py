def solution(text: str) -> str:
    split_text = text.split()

    uniq_words = []
    for x in split_text:
        if x not in [x[0] for x in uniq_words]:
            uniq_words.append((x, split_text.count(x)))

    uniq_words.sort(key=lambda x: x[1], reverse=True)

    output = [[x[0] for x in uniq_words].index(word) + 1 for word in split_text]

    return " ".join(map(str, output))