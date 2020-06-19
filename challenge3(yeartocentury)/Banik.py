def yearToCentury(user_year: int):
    century = int(user_year - 1)
    real_century =  int(century / 100)
    real_century += 1 

    return real_century