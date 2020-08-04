def solution(day, date1, date2):
    days = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    day_ind = days.index(day.lower())
    d1,m1 = [int(x) for x in date1.split("/")]
    d2,m2 = [int(x) for x in date2.split("/")]
    month_diff = abs(m2-m1)-1
    if m1 < m2:
        d1_diff = 30-d1
        ans = days[(day_ind + (d1_diff+d2) + (month_diff*30)%7)%7]
    else:
        d2_diff = 30-d2
        ans = days[(day_ind - (d2_diff+d1) - (month_diff*30)%7)%7]
    return ans.capitalize()