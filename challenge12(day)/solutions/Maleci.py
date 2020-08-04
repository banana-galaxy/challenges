def solution(day, day_date, date):
    day = day.upper()
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    day_dates = {}
    day_index = days.index(day)
    day_date = day_date.split("/")[0]
    day_date = int(day_date[1] if day_date[0] == "0" else day_date)
    date = date.split("/")[0]
    date = int(date[1] if date[0] == "0" else date)
    for day in days:
        day_dates[day] = days.index(day) + day_date - day_index
    incorrect_values = [0, -1, -2, -3, -4, -5, 31, 32, 33, 34, 35, 36]
    replaced_values = [30, 29, 28, 27, 26, 25, 1, 2, 3, 4, 5, 6]
    def correct_values():
        for key in day_dates:
            if day_dates[key] in incorrect_values:
                day_dates[key] = replaced_values[incorrect_values.index(day_dates[key])]
    correct_values()
    for key in day_dates:
        if day_dates[key] + 7*(date//7) == date:
            return key.capitalize()
    return day_dates