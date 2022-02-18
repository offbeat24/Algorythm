import sys
N,r,c = list(map(int,sys.stdin.readline().split()))

field = [[0,1],[2,3]]

def recursion(N):
  if N == 1:
    return
  leng = len(field)
  
  for i in range(leng):
    field[i]+=list(map(lambda x:x+leng**2, field[i]))
    field.append(list(map(lambda x:x+(leng**2)*2,field[i])))
  
  recursion(N-1)

recursion(N)
print(field[r][c])