def solution(day, daydate, date):
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    day = day.lower()

    if day not in week:
        raise TypeError(f"{day} isn't a valid day of the week.")

    daydate = daydate.split('/')
    date = date.split('/')

    updown = 'down' if int(daydate[1]) - int(date[1]) < 0 else 'up' if int(daydate[1]) - int(date[1]) > 0 else 'down' if int(daydate[0]) - int(date[0]) < 0 else 'up' if int(daydate[0]) - int(date[0]) > 0 else None

    if updown == 'up':
        daydate = int(daydate[0]) + int(daydate[1]) * 30
        date = int(date[0]) + int(date[1]) * 30

        up = date - daydate
        return week[(week.index(day) + up) % 7]
    elif updown == 'down':
        daydate = int(daydate[0]) + int(daydate[1]) * 30
        date = int(date[0]) + int(date[1]) * 30

        down = daydate - date
        return week[(week.index(day) - down) % 7]
    else:
        return day