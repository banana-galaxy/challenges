def validate(postal_code):

    if isinstance(postal_code, int):
        if len(str(postal_code)) == 5:
            letters = []

            for letter in str(postal_code):
                if letter not in letters:
                    letters.append(letter)

                else:
                    return False

            return True

    return False