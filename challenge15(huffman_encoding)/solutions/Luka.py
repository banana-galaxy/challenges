def solution(text):
    amount = []
    words = []
    textnew = []
    textlist = text.split(" ")

    for i in textlist:
        if i not in textnew:
            amount.append(((textlist.count(i), i)))
            textnew.append(i)

    amount.sort(key=lambda tup: tup[0], reverse=True)

    for index, e in enumerate(range(len(amount))):
        amount[e] = (index + 1, amount[e][1])

    text = ""

    for wor in textlist:
        for index, word in amount:
            if wor == word:
                text += str(index) + " "

    return text[:-1]