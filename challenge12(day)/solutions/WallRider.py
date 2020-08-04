def solution(day, start, end):
    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday']
    day = day.title()
    s_d, s_m = map(int, start.split('/'))
    e_d, e_m = map(int, end.split('/'))
    idx = (weeks.index(day) + (e_d - s_d + (30 * (e_m-s_m))))%7
    return weeks[idx]