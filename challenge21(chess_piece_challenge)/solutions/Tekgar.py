def solution(a,b,n):
    if n<=0:return a==b
    o,ab=ord,abs
    return (o(a[0]) % 2 == o(a[1]) % 2) == (o(b[0]) % 2 == o(b[1]) % 2) and (n >= 2 or ab(o(a[0]) - o(b[0])) == ab(o(a[1]) - o(b[1])))