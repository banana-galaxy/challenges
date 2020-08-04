def soultion(day_of_week,date,other_date):
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    diff_month = int(date.split("/")[1])-int(other_date.split("/")[1])
    diff_days = int(date.split("/")[0])-int(other_date.split("/")[0])
    diff_days = diff_days + diff_month * 30
    diff_days_week = diff_days % len(weekDays)
    return(weekDays[weekDays.index(day_of_week.title())-diff_days_week])