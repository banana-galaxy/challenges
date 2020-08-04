def solution(d, dm, m):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    d = d.lower()
    dm = dm.split("/")
    m = m.split("/")
    mdif = int(m[1]) - int(dm[1])
    ddif = int(m[0]) - int(dm[0])
    return days[(days.index(d) + (mdif * 30 + ddif)) % 7]