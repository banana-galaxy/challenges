def solution():
    running = True
    count = 0
    print()
    while running:
        try:
            user_input = int(input("> "))
            for i in range (1 , user_input + 1):
                if user_input % i == 0:
                    count = count + 1
            if count > 3:
                print()
                print("False")
                print()
            elif count == 3:
                print()
                print("True")
                print()
            elif count <=3:
                print()
                print("False")
                print()
            count = 0
        except ValueError:
            print()
            print("This is not a whole number.")
            print()