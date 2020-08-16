def solution(v,w,V,W,M):
 if w+W<=M:return v+V
 if w<=M and W<=M:return v if v>V else V
 return v if w<=M else V if W<=M else 0