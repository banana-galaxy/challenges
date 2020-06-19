def validate(number):
  number = [int(i) for i in str(number)]

  if len(number) > 5 or len(number) < 5:
    return False

  else:
    for i in range(5):
      num = float(number[i])
      num_data = num.is_integer()
      if num_data == False:
        return False
      else:

        if number[1] == number[3] or number[2] == number[4] or number[0] == number [2]:
          return False
        else:
          return True