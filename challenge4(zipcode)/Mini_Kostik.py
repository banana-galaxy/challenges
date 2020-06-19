def validate(postal):
    post = str(postal)
    if len(post) == 5 and post.isnumeric():
        for i in range(0, 4):
            if post[i] == post[i + 1]:
                return False
                break
        for i in range(0, 3):
            if post[i] == post[i + 2]:
                return False
                break
        return True
    else:
        return False