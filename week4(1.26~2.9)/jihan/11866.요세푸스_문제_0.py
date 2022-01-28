import sys

n,k = map(int,sys.stdin.readline().split())
circle = [i for i in range(1,n+1)]
pointer = -1
josephus = []

while(any(circle)):
  pointer+=k
  if pointer>=len(circle):
    pointer = pointer % len(circle)
  josephus.append(str(circle.pop(pointer)))
  pointer-=1

print('<' + ", ".join(josephus) + '>')