import random

def yearToCentury(year):
    if year % 100 == 0:
        return year // 100
    else:    
        return year // 100 + 1

if __name__ == "__main__":
    for i in range(10):
        num = random.randint(0, 9000)
        print(num, yearToCentury(num))
    print(0, yearToCentury(0))