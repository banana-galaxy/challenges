def solution(days):
    # longest solution yayayayayya
    # slowest solution ever yayayayayaa
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = [i for i, day in enumerate(year) if day == days]
    next = [(month + 1) if month < 11 else 0 for month in months]
    next_month = [year[month] for month in next]
    return list(set(next_month))