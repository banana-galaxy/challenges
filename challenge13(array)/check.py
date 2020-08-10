def solution(m):
 a,b=0,m[0]
 for x in m[1:]:a+=max(b-x+1,0);b=max(b+1,x)
 return a

if __name__ == '__main__':
    print(solution([-1000, 0, -2, 0]))