def validate(test_zip) -> bool:
    test_zip = str(test_zip)

    if not test_zip.isdecimal():
        return False

    elif len(test_zip) != 5:
        return False

    else:
        for idx, value in enumerate(test_zip[:-1]):
            if value == test_zip[min(idx + 1, len(test_zip) - 1)]:
                return False

            elif value == test_zip[min(idx + 2, len(test_zip) - 1)]:
                return False

    return True