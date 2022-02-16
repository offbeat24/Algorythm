n = int(input())

fibo_zero = [1, 0, 1]
fibo_one = [0, 1, 1]
def fibonacci(i) :
    if len(fibo_zero) <= i :
        for i in range(len(fibo_zero), i+1) :
            fibo_zero.append(fibo_zero[i-1] + fibo_zero[i-2])
            fibo_one.append(fibo_one[i-1] + fibo_one[i-2])
    
    print(fibo_zero[i], fibo_one[i], sep = ' ')

for _ in range(n) :
    num = int(input())
    fibonacci(num)
    