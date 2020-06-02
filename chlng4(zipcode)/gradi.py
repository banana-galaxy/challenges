def validate(code):
   code = str(code)
   if len(code) == 5:
       for a in range(5):
        if code[a] > '0' and code[a] < '9':
         if a == 0 and code[a] != code[a - 1]:
             if a == 0 and a == 4 and code[a - 1] == code[a + 1]:
                 return True
        else:
            return False