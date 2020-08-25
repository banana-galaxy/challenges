def solution(s: str):
    j,d=s.split(),{}
    for g in j:d.update({g:j.count(g)})
    return ' '.join(str(list(dict(sorted(d.items(),key=lambda x:x[1],reverse=True)).keys()).index(a)+1)for a in j)