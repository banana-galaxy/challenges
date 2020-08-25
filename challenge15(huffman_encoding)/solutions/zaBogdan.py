def solution(words):
h_words = []
test = {}
maximum = -1
for word in words.split():
h_words.append(word)
test[word] = h_words.count(word)
if
maximum = max(maximum, test[word])
seq = ''
for word in words.split():
freq = (maximum-test[word]+1)
seq = seq + str(freq) + ' '
return seq