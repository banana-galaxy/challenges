e={'n':2,'s':-2,'w':-3,'e':3}
solution=lambda d:len(d)<=10 and sum(map(lambda x:e[x],d))==0