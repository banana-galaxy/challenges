# Takes as input a list(seq) and int(n) and return seq shifted to the right by n
def shift(seq, n):
a = n % len(seq)
return seq[-a:] + seq[:-a]


# Challenge solution
def solution(day, date_d, date_tofind):
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# New week list with day as first element
new_week = shift(week, 7 - week.index(day.lower()))

# Two new lists [0] is string day and [1] is string month
date_d, date_tofind = date_d.split("/"), date_tofind.split("/")

# Transform two dates to days and calculate day difference.
num_of_days_date_d = int(date_d[0]) + 30int(date_d[1])
num_of_days_date_tofind = int(date_tofind[0]) + 30int(date_tofind[1])

dates_diff = abs(num_of_days_date_d - num_of_days_date_tofind)%7

return str(new_week[dates_diff]).capitalize()