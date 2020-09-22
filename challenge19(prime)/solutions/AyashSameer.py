def solution(x,y) :
   a_list = []
   b_list = []
   c = list(y)
   i = 0
   def sort(y,i) :
      if len(y)==1:
        a_list.append(y[0])
        b_list.append(i)
      else :
        a_list.append(min(y))
        y.remove(min(y))
        b_list.append(i)
        if a_list[len(a_list)-1] == min(y) :
           return sort(y,i)
        else :
           return sort(y,i+1)
   sort(y,i)
   b = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
   r = list(map(lambda x:b[x],b_list))
   for j in range(len(c)) :
     for i in range(len(a_list)) :
        if c[j] == a_list[i] :
           c[j] = r[i]
   return "".join(c)