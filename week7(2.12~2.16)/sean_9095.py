t = int(input())


def ott(num) :
    
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    elif num == 3 :
        return 4
    else :
        return ott(num-1) + ott(num-2) + ott(num-3)    

for _ in range(t) :
    n = int(input())
    print(ott(n))
    