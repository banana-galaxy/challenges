def whichExit(m):[v]=[(r.count(1)-r[r.index(0):].count(1)*2)for r in m if 0 in r];return["same",'right','left'][v and(1,2)[v<0]]