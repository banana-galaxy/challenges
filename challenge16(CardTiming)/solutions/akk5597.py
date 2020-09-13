def solution(days):
    return {
        28: [31],
        30: [31],
        31: [28, 30, 31]
    }[days]