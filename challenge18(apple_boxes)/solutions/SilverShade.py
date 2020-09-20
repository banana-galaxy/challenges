def solution(k,o=[0,0]):
    for a in range(k+1):o[a%2==0]+=a*a
    return o[1]-o[0]