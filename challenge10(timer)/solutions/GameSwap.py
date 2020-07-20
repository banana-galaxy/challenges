def lateRide(n):
    sum = 0; for (char, number) in [(char, number) for char in str(n % 60) for number in str(int(n / 60))] : sum = sum + int(char) + int(number); return sum