def validate(zip):
    zip=str(zip)
    if len(zip)==5:
        for e,i in enumerate(zip):
            try:
                int(i)
            except:
                return False
            if len(zip)-1>e+1:
                if zip[e+1]==i:
                    return False
            if len(zip)-1>e+2:
                if zip[e+2]==i:
                    return False
    else:
        return False
    return True