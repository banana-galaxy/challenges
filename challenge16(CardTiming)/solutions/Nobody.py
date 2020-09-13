def solution(lastNumberOfDays):
    if lastNumberOfDays==30 or lastNumberOfDays==28:
        return [31]
    if lastNumberOfDays==31:
        return [28,30,31]