def lateRide(n):
    how_much = n - ((n // 60) * 60)
    clock = n // 60

    time = []

    while clock > 0:
        time.insert(0, clock % 10)
        clock = (clock - clock % 10) // 10

    while how_much > 0:
        time.insert(0, how_much % 10)
        how_much = (how_much - how_much % 10) // 10

    answer = 0

    for i in time:
        answer += i

    return answer