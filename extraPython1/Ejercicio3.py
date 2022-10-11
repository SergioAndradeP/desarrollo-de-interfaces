
def isnum(a):
    try:
        int(a)
    except:
        return False;
    return True;


def length(a):
    i = 0
    if not (isnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif (isnum(a)):
        return (a)
    return (i)