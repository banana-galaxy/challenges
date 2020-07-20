def lateRide(n):
    hrs, mins = n // 60, n % 60
    return hrs%10 + hrs//10 + mins%10 + mins//10