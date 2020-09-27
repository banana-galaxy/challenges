def solution(k):
    def prime(n):
        if n <= 3:
            return n > 1
        if n % 2 < 1 or n % 3 < 1:
            return 0
        i = 5
        while i * i <= n:
            if n % i < 1 or n % (i + 2) < 1:
                return 0
            i += 6
        return 1

    sqrt = int(k ** 0.5)
    return prime(sqrt) if sqrt * sqrt == k else 0