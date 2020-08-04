def solution(day, current_date, wanted_date):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    current_dd, current_mm = int(current_date.split('/')[0]), int(current_date.split('/')[1])
    wanted_dd, wanted_mm = int(wanted_date.split('/')[0]), int(wanted_date.split('/')[1])

    nb_days_diff = (wanted_dd - current_dd) + 30 * (wanted_mm - current_mm)
    week_days_diff = nb_days_diff % 7

    return week[(week.index(day.lower()) + week_days_diff) % 7]