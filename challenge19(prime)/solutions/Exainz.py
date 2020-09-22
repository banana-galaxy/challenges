def solution(never_used, p):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(p)
    index = 0
    result = ""
    d = {}
    encrypted_list = [3] * (length + 1)
    for i in range(length - 1):
        if gcd(p[i], p[i + 1]) != p[i]:
            encrypted_list[i + 1] = gcd(p[i], p[i + 1])
    for j in range(length - 1):
        if gcd(p[j], p[j + 1]) != p[j]:
            for k in range(j + 2, len(encrypted_list)):
                encrypted_list[k] = p[k - 1] // encrypted_list[k - 1]
    for l in range(length - 1):
        if gcd(p[l], p[l + 1]) != p[l]:
            for m in range(l, -1, -1):
                encrypted_list[m] = p[m] // encrypted_list[m + 1]
    decrypted_list = list(sorted(set(encrypted_list)))
    for value in decrypted_list:
        d[value] = string[index]
        index += 1
    for encrypted_listement in encrypted_list:
        result += d[encrypted_listement]
    return result