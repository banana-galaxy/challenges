def whichExit(a):
    z,c={"l":0,"r":0},"l"
    for m in a:
        if 0 in m:
            for i in m:
                if i==0:c="r"
                elif i==1:z[c]+=1
            break
    k="right" if z["l"]>z["r"]else"left"if z["l"]<z["r"]else"same"
    return k