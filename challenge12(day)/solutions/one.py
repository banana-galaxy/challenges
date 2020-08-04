def solution(day, date_1, date_2):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    date_a, month_a, date_b, month_b = map(int, date_1.split('/') + date_2.split('/'))
    date_diff, month_diff = date_b - date_a, month_b - month_a
    return days[((days.index(day.lower())) + month_diff * 30 + date_diff) % 7] 