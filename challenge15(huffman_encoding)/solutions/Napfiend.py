def solution(text):
words = text.split()
encoder = {}
encoded = []

for word in words:
if word in encoder:
encoder[word] = encoder.get(word) + 1
else:
encoder[word] = 1

ordered_encoder = sorted(encoder, key=encoder.get, reverse=True)

for word in words:
encoded.append(ordered_encoder.index(word) + 1)

return ' '.join(map(str, encoded))