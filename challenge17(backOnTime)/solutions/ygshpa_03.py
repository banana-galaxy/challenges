def solution(path):
    pos={'n':0,'s':0, 'w':0 ,'e':0}
    if len(path) > 10 :
        return 'False'
    else:
        for i in path:
            pos[i] +=1
        if pos['n'] == pos['s'] and pos['e']==pos['w']:
            return 'True'
        else:
            return'False' 