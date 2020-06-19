validate = lambda zc: str(zc).isdigit() and len(str(zc)) == 5 and not [x for x in range(3) if str(zc)[x+2] == str(zc)[x]] and not [x for x in range(4) if str(zc)[x] == str(zc)[x+1]]

if __name__ == "__main__":
    print(validate(23456))
    print(validate(23556))
    print(validate(25456))
    print(validate("23r56"))
    print(validate(23453456))
    print(validate(236))
    print(validate("04236"))