def t_prime(n):
    if 1 <= n <= 10e12 and n % 2 == 0:
        return True
    else:
        return False

check = t_prime()