def solution(choices=[]):
    time_=0
    x,y=0,0
    if len(choices)>10:
        return False
    else:
        choice_value=dict(zip(['n','s','e','w'],[5,-5,5,-5]))
        x=(choice_value[ch] for ch in choices if ch=="e" or ch=="w")
        y=(choice_value[ch] for ch in choices if ch=="n" or ch=="s")
        if not sum(x) and not sum(y):
            return True
        else :
            return False 