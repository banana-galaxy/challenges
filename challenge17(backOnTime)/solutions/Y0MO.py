solution=lambda x:[True, False][0 if x.count('n')==x.count('s')and x.count('e')==x.count('w')and len(x)<11 else 1]