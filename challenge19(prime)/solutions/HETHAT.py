g=lambda a,b:a*(b<1)or g(b,a%b);solution=lambda _,t:(e:=[x for x in range(len(t)-1)if t[x]!=t[x+1]][0],s:=[g(t[e],t[e+1])],[s.append(t[z-1]/s[-1])for z in range(e+2,len(t)+1)],[s.insert(0,t[z]/s[0])for z in range(e,-1,-1)],"".join(chr(sorted(set(s)).index(a)+65)for a in s))[-1]