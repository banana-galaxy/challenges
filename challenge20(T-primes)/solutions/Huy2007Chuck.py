# File: t_primes.py
# By: Huy2007Chuck
#
# Weekly coding challenge in Tech With Tim's Discord server
#
# Takes an integer as input and returns True if the number has only 3 divisors
# otherwise returns False.


def solution(n):
    divisors = []  # Creates a new empty list containing the divisors of n

    for i in range(1, n + 1):  # Loops from 1 to n + 1
        if n % i == 0:  # Checks if i is the divisor of n
            divisors.append(i)  # Append i to the divisors list

    if len(divisors) == 3:  # Checks if n has exactly 3 divisors
        return True
    else:
        return False