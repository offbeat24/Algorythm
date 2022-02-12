def isprime(num):
    if num!=1:
        for i in range(2,num):
            if num % i == 0:
                return False
    else:
        return False
    return True

n = int(input())
list = input().split(' ')
cnt = 0

for i in range(0,n):
    if isprime(int(list[i])):
        cnt+=1

print(cnt)