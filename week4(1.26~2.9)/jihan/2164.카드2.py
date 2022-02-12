n = int(input())
tmp = 2

while 1:
    if (n-tmp)//tmp<1:
        break
    tmp*=2

if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    if (n-tmp)==0:
        print(n)
    else:
        print((n-tmp)*2)