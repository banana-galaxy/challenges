x,l,solution="Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split(),lambda u:int(u[:2])+int(u[3:])*30,lambda a,b,c:x[x.index(a.title())-(l(b)-l(c))%7]

if __name__ == '__main__':
    print(solution("Monday", "05/11", "08/11"))