def lateRide(n):
    h, m = round(n / 60), n % 60
    ans1 = 0 if h == 0 else h % 10 + (int(h / 10))
    ans2 = 0 if m == 0 else m % 10 + (int(m / 10))
    return ans1 + ans2