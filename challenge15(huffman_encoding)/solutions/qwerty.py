def solution(s):s=s.split();return' '.join(f'{sorted({}.fromkeys(s),key=s.count,reverse=1).index(i)+1}'for i in s)