def solution(day, date, current):
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    # ensure there's no spelling funny stuff
    day = day.lower()
    offset = days.index(day)

    # parse out the months and days
    date_day, date_month = date.split("/")
    current_day, current_month = current.split("/")

    # convert to ints
    date = int(date_month) * 30 + int(date_day)
    current = int(current_month) * 30 + int(current_day)

    diff = (current - date + offset) % 7

    return days[diff].title()