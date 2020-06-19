def validate(zip):
  if not isinstance(zip, int) or len(str(zip)) != 5:
    return False
  
  zip_list = [i for i in str(zip)]
  
  for i in range(3):
    if zip_list[i] == zip_list[i+1] or zip_list[i] == zip_list[i+2]:
      return False

  if zip_list[3] == zip_list[4] or zip_list[4] == zip_list[2]:
    return False

  return True