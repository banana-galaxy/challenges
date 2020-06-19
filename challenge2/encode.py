def encode(user):
    result = ""
    preChar = ''
    count = 1
    for index, char in enumerate(user):
        if index == 0:
            preChar = char
            continue

        if preChar == char:
            count += 1
            if index == len(user)-1:
                result += f"{count}{preChar}"
        else:
            if index != len(user)-1:
                result += f"{count}{preChar}"
                count = 1
            else:
                result += f"{count}{preChar}1{char}"

        if count >= 10:
            result += f"9{preChar}"
            count -= 9

        preChar = char
    return result

def decode(user):
    result = ""
    user = list(user)
    amounts = []
    chars = []
    for char in user[::2]:
        if char != None:
            amounts.append(char)
    for char in user[1::2]:
        if char != None:
            chars.append(char)
    for index, amount in enumerate(amounts):
        for i in range(int(amount)):
            result += chars[index]
    
    return result

if __name__ == "__main__":
    print(encode("yiiiiiihaaaaaa"))