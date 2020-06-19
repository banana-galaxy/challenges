def validate(code):
  def check_neighbours(list_i):
    cn = [list_i[i]!=list_i[i+1] and list_i[i]!=list_i[i+2] for i in range(3)]
    return all(cn)
  try:
    int(code)
    check1 = True
    list_code = [x for x in str(code)]
    if len(list_code) == 5:
      check2 = True
      check3 = check_neighbours(list_code)
    else:
      check2 = False
      check3 = False
  except ValueError:
    check1 = False
    check2 = False
    check3 = False
  valid = check1, check2, check3  
  return all(valid)