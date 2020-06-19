def validate(postal_code):
    postal_code = str(postal_code)

    if not postal_code.isdigit() or len(postal_code) != 5:
        return False

    for index, num in zip(range(len(postal_code)), postal_code):
        if num in (postal_code[index + 1] if not index + 1 > len(postal_code) - 1 else None,
                   postal_code[index + 2] if not index + 2 > len(postal_code) - 1 else None,
                   postal_code[index - 1] if not index - 1 < 0 else None,
                   postal_code[index - 2] if not index - 2 < 0 else None):
            return False

    return True