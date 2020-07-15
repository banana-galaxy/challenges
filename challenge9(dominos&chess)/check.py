def fill(matrix):
    black = 0
    white = 0
    for y, dy in enumerate(matrix):
        for x, dx in enumerate(dy):
            if y%2==0:
                if x%2==0:
                    black+=not dx
                else:
                    white+=not dx
            else:
                if x%2==0:
                    white+=not dx
                else:
                    black+=not dx

    if black==white:
        return True
    else:
        return False

def fill2(matrix):
    a,r,l = [],[],[]
    for i, row in enumerate(matrix):
        for u, square in enumerate(row):
            if square == 0:
                if square not in [matrix[i][u + 1] if square != row[-1] else 1,
                                  matrix[i][u - 1] if u != 0 else 1,
                                  matrix[i + 1][u] if row != matrix[-1] else 1,
                                  matrix[i - 1][u] if i != 0 else 1]:
                    l.append(0)
                a.append((u + i) % 2)
            r.append(square)
    if r.count(0) % 2:return False
    if r.count(1) == 0:return True
    if l:return False
    return a.count(0) == a.count(1) and bool(a)

# def fill(m):
#     z=[(u+i)%2for i,x in enumerate(m)for u,a in enumerate(x)if a<1]
#     return z.count(0)==z.count(1)and bool(z)